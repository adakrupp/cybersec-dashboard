"""
NVD (National Vulnerability Database) API integration
API Documentation: https://nvd.nist.gov/developers/vulnerabilities
"""

import requests
import time
from datetime import datetime, timezone, timedelta
from django.utils import timezone as django_timezone
from .models import CVE
import logging

logger = logging.getLogger(__name__)


class NVDAPIClient:
    """Client for interacting with the NVD API"""

    BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    RATE_LIMIT_DELAY = 6  # Seconds between requests (free tier: max 5 requests per 30 seconds)

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'CybersecDashboard/1.0',
        })
        self.last_request_time = 0

    def _rate_limit(self):
        """Ensure we don't exceed rate limits"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.RATE_LIMIT_DELAY:
            time.sleep(self.RATE_LIMIT_DELAY - elapsed)
        self.last_request_time = time.time()

    def search_cve_by_id(self, cve_id):
        """Search for a specific CVE by ID"""
        self._rate_limit()

        try:
            params = {'cveId': cve_id}
            response = self.session.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data.get('totalResults', 0) == 0:
                return None

            return self._parse_cve_data(data['vulnerabilities'][0])

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching CVE {cve_id}: {str(e)}")
            return None

    def search_cve_by_keyword(self, keyword, max_results=20):
        """Search CVEs by keyword"""
        self._rate_limit()

        try:
            params = {
                'keywordSearch': keyword,
                'resultsPerPage': min(max_results, 100),  # API max is 2000
            }
            response = self.session.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            vulnerabilities = data.get('vulnerabilities', [])

            return [self._parse_cve_data(vuln) for vuln in vulnerabilities[:max_results]]

        except requests.exceptions.RequestException as e:
            logger.error(f"Error searching CVEs with keyword '{keyword}': {str(e)}")
            return []

    def fetch_recent_cves(self, days=30, max_results=50):
        """Fetch recent CVEs from the last N days"""
        self._rate_limit()

        try:
            # Calculate date range
            end_date = datetime.now(timezone.utc)
            start_date = end_date - timedelta(days=days)

            params = {
                'pubStartDate': start_date.strftime('%Y-%m-%dT%H:%M:%S.000'),
                'pubEndDate': end_date.strftime('%Y-%m-%dT%H:%M:%S.000'),
                'resultsPerPage': min(max_results, 100),
            }

            response = self.session.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            vulnerabilities = data.get('vulnerabilities', [])

            return [self._parse_cve_data(vuln) for vuln in vulnerabilities[:max_results]]

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching recent CVEs: {str(e)}")
            return []

    def _parse_cve_data(self, vuln_data):
        """Parse CVE data from NVD API response"""
        try:
            cve = vuln_data.get('cve', {})

            cve_id = cve.get('id', '')
            description = self._extract_description(cve)
            published_date = self._parse_date(cve.get('published'))
            last_modified = self._parse_date(cve.get('lastModified'))

            # Extract CVSS score and severity
            cvss_score = None
            severity = None
            metrics = cve.get('metrics', {})

            # Try CVSS v3.1 first
            if 'cvssMetricV31' in metrics and metrics['cvssMetricV31']:
                cvss_data = metrics['cvssMetricV31'][0]['cvssData']
                cvss_score = cvss_data.get('baseScore')
                severity = cvss_data.get('baseSeverity', '').upper()
            # Fallback to CVSS v3.0
            elif 'cvssMetricV30' in metrics and metrics['cvssMetricV30']:
                cvss_data = metrics['cvssMetricV30'][0]['cvssData']
                cvss_score = cvss_data.get('baseScore')
                severity = cvss_data.get('baseSeverity', '').upper()
            # Fallback to CVSS v2
            elif 'cvssMetricV2' in metrics and metrics['cvssMetricV2']:
                cvss_score = metrics['cvssMetricV2'][0]['cvssData'].get('baseScore')
                # Map v2 score to severity
                if cvss_score:
                    if cvss_score >= 9.0:
                        severity = 'CRITICAL'
                    elif cvss_score >= 7.0:
                        severity = 'HIGH'
                    elif cvss_score >= 4.0:
                        severity = 'MEDIUM'
                    else:
                        severity = 'LOW'

            # Extract affected products
            affected_products = []
            configurations = cve.get('configurations', [])
            for config in configurations:
                for node in config.get('nodes', []):
                    for cpe_match in node.get('cpeMatch', []):
                        criteria = cpe_match.get('criteria', '')
                        if criteria:
                            # Extract vendor and product from CPE string
                            parts = criteria.split(':')
                            if len(parts) >= 5:
                                vendor = parts[3]
                                product = parts[4]
                                affected_products.append(f"{vendor} {product}")

            # Extract references
            references = []
            for ref in cve.get('references', [])[:5]:  # Limit to 5 references
                url = ref.get('url')
                if url:
                    references.append(url)

            return {
                'cve_id': cve_id,
                'description': description,
                'published_date': published_date,
                'last_modified': last_modified,
                'cvss_score': cvss_score,
                'severity': severity,
                'affected_products': list(set(affected_products[:10])),  # Unique, max 10
                'references': references,
            }

        except Exception as e:
            logger.error(f"Error parsing CVE data: {str(e)}")
            return None

    def _extract_description(self, cve):
        """Extract English description from CVE data"""
        descriptions = cve.get('descriptions', [])
        for desc in descriptions:
            if desc.get('lang') == 'en':
                return desc.get('value', '')
        # Fallback to first description
        if descriptions:
            return descriptions[0].get('value', '')
        return ''

    def _parse_date(self, date_string):
        """Parse ISO date string to datetime"""
        if not date_string:
            return django_timezone.now()
        try:
            # Remove timezone info if present and parse
            date_string = date_string.replace('Z', '+00:00')
            return datetime.fromisoformat(date_string)
        except Exception:
            return django_timezone.now()


def cache_cve(cve_data):
    """Cache CVE data in database"""
    if not cve_data:
        return None

    try:
        cve, created = CVE.objects.update_or_create(
            cve_id=cve_data['cve_id'],
            defaults=cve_data
        )
        return cve
    except Exception as e:
        logger.error(f"Error caching CVE {cve_data.get('cve_id')}: {str(e)}")
        return None


def search_cve(query):
    """
    Search for CVEs by ID or keyword
    First checks cache, then queries NVD API if needed
    """
    client = NVDAPIClient()

    # Check if query is a CVE ID format
    if query.upper().startswith('CVE-'):
        # Check cache first
        try:
            cve = CVE.objects.get(cve_id=query.upper())
            # Refresh if older than 7 days
            if (django_timezone.now() - cve.cached_at).days < 7:
                return [cve]
        except CVE.DoesNotExist:
            pass

        # Fetch from API
        cve_data = client.search_cve_by_id(query.upper())
        if cve_data:
            cve = cache_cve(cve_data)
            return [cve] if cve else []
        return []

    else:
        # Keyword search - check cache first
        cached_cves = CVE.objects.filter(description__icontains=query)[:20]
        if cached_cves.exists():
            return list(cached_cves)

        # Fetch from API
        cve_data_list = client.search_cve_by_keyword(query, max_results=20)
        cves = []
        for cve_data in cve_data_list:
            cve = cache_cve(cve_data)
            if cve:
                cves.append(cve)
        return cves


def fetch_recent_cves(days=30):
    """Fetch and cache recent CVEs"""
    client = NVDAPIClient()
    cve_data_list = client.fetch_recent_cves(days=days, max_results=50)

    cves = []
    for cve_data in cve_data_list:
        cve = cache_cve(cve_data)
        if cve:
            cves.append(cve)

    logger.info(f"Fetched and cached {len(cves)} recent CVEs")
    return cves
