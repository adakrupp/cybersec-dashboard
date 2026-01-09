"""
Seed script to populate the database with initial cybersecurity data
Run this with: python manage.py shell < scripts/seed_data.py
Or create a management command
"""

import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.resources.models import Category, Certification, Resource
from apps.tools.models import ToolCategory, Tool
from apps.news.models import NewsSource


def seed_news_sources():
    """Create initial news sources"""
    print("Seeding news sources...")

    sources = [
        {
            'name': 'Krebs on Security',
            'source_type': 'RSS',
            'url': 'https://krebsonsecurity.com/feed/',
            'is_active': True,
        },
        {
            'name': 'BleepingComputer',
            'source_type': 'RSS',
            'url': 'https://www.bleepingcomputer.com/feed/',
            'is_active': True,
        },
        {
            'name': 'The Hacker News',
            'source_type': 'RSS',
            'url': 'https://feeds.feedburner.com/TheHackersNews',
            'is_active': True,
        },
        {
            'name': 'Dark Reading',
            'source_type': 'RSS',
            'url': 'https://www.darkreading.com/rss.xml',
            'is_active': True,
        },
        {
            'name': 'r/netsec',
            'source_type': 'REDDIT',
            'url': 'https://reddit.com/r/netsec',
            'is_active': False,  # Enable after configuring Reddit API credentials
        },
        {
            'name': 'r/cybersecurity',
            'source_type': 'REDDIT',
            'url': 'https://reddit.com/r/cybersecurity',
            'is_active': False,  # Enable after configuring Reddit API credentials
        },
    ]

    for source_data in sources:
        source, created = NewsSource.objects.get_or_create(
            name=source_data['name'],
            defaults=source_data
        )
        if created:
            print(f"  Created: {source.name}")

    print(f"✓ News sources seeded ({NewsSource.objects.count()} total)\n")


def seed_resource_categories():
    """Create resource categories"""
    print("Seeding resource categories...")

    categories = [
        {
            'name': 'Certifications',
            'slug': 'certifications',
            'description': 'Industry-recognized cybersecurity certifications',
            'icon': 'fa-certificate',
        },
        {
            'name': 'Courses',
            'slug': 'courses',
            'description': 'Online courses and training programs',
            'icon': 'fa-graduation-cap',
        },
        {
            'name': 'Practice Labs',
            'slug': 'labs',
            'description': 'Hands-on cybersecurity labs and challenges',
            'icon': 'fa-flask',
        },
        {
            'name': 'Documentation',
            'slug': 'documentation',
            'description': 'Technical documentation and guides',
            'icon': 'fa-book',
        },
        {
            'name': 'Books',
            'slug': 'books',
            'description': 'Recommended cybersecurity books',
            'icon': 'fa-book-open',
        },
    ]

    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults=cat_data
        )
        if created:
            print(f"  Created: {category.name}")

    print(f"✓ Categories seeded ({Category.objects.count()} total)\n")


def seed_certifications():
    """Create popular certifications"""
    print("Seeding certifications...")

    certs = [
        {
            'name': 'CompTIA Security+',
            'provider': 'CompTIA',
            'difficulty': 'BEGINNER',
            'cost_range': '$370-$400',
            'description': 'Entry-level certification covering essential security concepts, threats, and best practices.',
            'official_url': 'https://www.comptia.org/certifications/security',
        },
        {
            'name': 'Certified Ethical Hacker (CEH)',
            'provider': 'EC-Council',
            'difficulty': 'INTERMEDIATE',
            'cost_range': '$1,199',
            'description': 'Learn ethical hacking techniques and penetration testing methodologies.',
            'official_url': 'https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/',
        },
        {
            'name': 'CISSP',
            'provider': 'ISC2',
            'difficulty': 'ADVANCED',
            'cost_range': '$749',
            'description': 'Advanced security certification for experienced professionals covering 8 security domains.',
            'official_url': 'https://www.isc2.org/Certifications/CISSP',
        },
        {
            'name': 'OSCP',
            'provider': 'Offensive Security',
            'difficulty': 'ADVANCED',
            'cost_range': '$1,499',
            'description': 'Hands-on penetration testing certification requiring real-world exploitation skills.',
            'official_url': 'https://www.offensive-security.com/pwk-oscp/',
        },
        {
            'name': 'GIAC Security Essentials (GSEC)',
            'provider': 'GIAC',
            'difficulty': 'INTERMEDIATE',
            'cost_range': '$2,499',
            'description': 'Demonstrates knowledge of information security beyond basic terminology and concepts.',
            'official_url': 'https://www.giac.org/certifications/security-essentials-gsec/',
        },
    ]

    for cert_data in certs:
        cert, created = Certification.objects.get_or_create(
            name=cert_data['name'],
            defaults=cert_data
        )
        if created:
            print(f"  Created: {cert.name}")

    print(f"✓ Certifications seeded ({Certification.objects.count()} total)\n")


def seed_resources():
    """Create learning resources"""
    print("Seeding learning resources...")

    # Get categories
    courses_cat = Category.objects.get(slug='courses')
    labs_cat = Category.objects.get(slug='labs')
    docs_cat = Category.objects.get(slug='documentation')

    resources_data = [
        # Courses
        {
            'title': 'Cybrary - Free Cybersecurity Training',
            'category': courses_cat,
            'resource_type': 'COURSE',
            'url': 'https://www.cybrary.it/',
            'description': 'Free online cybersecurity training platform with courses on various security topics.',
            'provider': 'Cybrary',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['free', 'courses', 'beginner-friendly'],
        },
        {
            'title': 'TryHackMe',
            'category': labs_cat,
            'resource_type': 'LAB',
            'url': 'https://tryhackme.com/',
            'description': 'Gamified platform for learning cybersecurity through hands-on challenges and labs.',
            'provider': 'TryHackMe',
            'is_free': False,
            'difficulty': 'BEGINNER',
            'tags': ['labs', 'ctf', 'hands-on'],
        },
        {
            'title': 'HackTheBox',
            'category': labs_cat,
            'resource_type': 'LAB',
            'url': 'https://www.hackthebox.com/',
            'description': 'Platform offering penetration testing labs and realistic hacking scenarios.',
            'provider': 'HackTheBox',
            'is_free': False,
            'difficulty': 'INTERMEDIATE',
            'tags': ['pentesting', 'ctf', 'labs'],
        },
        {
            'title': 'OverTheWire Wargames',
            'category': labs_cat,
            'resource_type': 'LAB',
            'url': 'https://overthewire.org/wargames/',
            'description': 'Free wargames to learn and practice security concepts through fun challenges.',
            'provider': 'OverTheWire',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['free', 'wargames', 'linux'],
        },
        {
            'title': 'OWASP Top 10',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://owasp.org/www-project-top-ten/',
            'description': 'Standard awareness document for web application security risks.',
            'provider': 'OWASP',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['web-security', 'owasp', 'documentation'],
        },
        {
            'title': 'NIST Cybersecurity Framework',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://www.nist.gov/cyberframework',
            'description': 'Framework for improving critical infrastructure cybersecurity.',
            'provider': 'NIST',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['framework', 'compliance', 'nist'],
        },
        {
            'title': 'Professor Messer - Security+ Course',
            'category': courses_cat,
            'resource_type': 'VIDEO',
            'url': 'https://www.professormesser.com/security-plus/sy0-601/sy0-601-video/sy0-601-comptia-security-plus-course/',
            'description': 'Free video course covering CompTIA Security+ certification material.',
            'provider': 'Professor Messer',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['security+', 'video', 'certification-prep'],
        },
        {
            'title': 'PentesterLab',
            'category': labs_cat,
            'resource_type': 'LAB',
            'url': 'https://pentesterlab.com/',
            'description': 'Learn penetration testing through hands-on exercises and challenges.',
            'provider': 'PentesterLab',
            'is_free': False,
            'difficulty': 'INTERMEDIATE',
            'tags': ['pentesting', 'web-security', 'labs'],
        },
    ]

    for resource_data in resources_data:
        resource, created = Resource.objects.get_or_create(
            title=resource_data['title'],
            defaults=resource_data
        )
        if created:
            print(f"  Created: {resource.title}")

    print(f"✓ Resources seeded ({Resource.objects.count()} total)\n")


def seed_tool_categories():
    """Create tool categories"""
    print("Seeding tool categories...")

    categories = [
        {
            'name': 'Network Analysis',
            'slug': 'network-analysis',
            'description': 'Tools for analyzing network traffic and protocols',
        },
        {
            'name': 'Penetration Testing',
            'slug': 'pentesting',
            'description': 'Tools for security testing and exploitation',
        },
        {
            'name': 'Password Cracking',
            'slug': 'password-cracking',
            'description': 'Tools for password recovery and cracking',
        },
        {
            'name': 'Web Application Security',
            'slug': 'web-security',
            'description': 'Tools for testing web application security',
        },
        {
            'name': 'Forensics',
            'slug': 'forensics',
            'description': 'Digital forensics and incident response tools',
        },
        {
            'name': 'OSINT',
            'slug': 'osint',
            'description': 'Open Source Intelligence gathering tools',
        },
    ]

    for cat_data in categories:
        category, created = ToolCategory.objects.get_or_create(
            slug=cat_data['slug'],
            defaults=cat_data
        )
        if created:
            print(f"  Created: {category.name}")

    print(f"✓ Tool categories seeded ({ToolCategory.objects.count()} total)\n")


def seed_tools():
    """Create security tools"""
    print("Seeding security tools...")

    # Get categories
    network_cat = ToolCategory.objects.get(slug='network-analysis')
    pentest_cat = ToolCategory.objects.get(slug='pentesting')
    password_cat = ToolCategory.objects.get(slug='password-cracking')
    web_cat = ToolCategory.objects.get(slug='web-security')
    forensics_cat = ToolCategory.objects.get(slug='forensics')
    osint_cat = ToolCategory.objects.get(slug='osint')

    tools_data = [
        # Network Analysis
        {
            'name': 'Wireshark',
            'category': network_cat,
            'description': 'The world\'s most popular network protocol analyzer for deep inspection of network traffic.',
            'use_case': 'Capture and analyze network packets, troubleshoot network issues, detect security problems.',
            'url': 'https://www.wireshark.org/',
            'github_url': 'https://github.com/wireshark/wireshark',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['packet-analyzer', 'network', 'traffic-analysis'],
        },
        {
            'name': 'Nmap',
            'category': network_cat,
            'description': 'Network scanner for discovering hosts and services on a computer network.',
            'use_case': 'Port scanning, network discovery, security auditing, and vulnerability detection.',
            'url': 'https://nmap.org/',
            'github_url': 'https://github.com/nmap/nmap',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'BEGINNER',
            'tags': ['port-scanner', 'network-discovery', 'reconnaissance'],
        },
        # Pentesting
        {
            'name': 'Metasploit Framework',
            'category': pentest_cat,
            'description': 'Comprehensive penetration testing platform with thousands of exploits and payloads.',
            'use_case': 'Exploit development, vulnerability testing, penetration testing, and security research.',
            'url': 'https://www.metasploit.com/',
            'github_url': 'https://github.com/rapid7/metasploit-framework',
            'is_open_source': True,
            'platforms': ['Linux', 'Windows', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['exploitation', 'pentesting', 'framework'],
        },
        {
            'name': 'Burp Suite',
            'category': web_cat,
            'description': 'Integrated platform for web application security testing.',
            'use_case': 'Web vulnerability scanning, manual testing, intercepting proxy, and attack automation.',
            'url': 'https://portswigger.net/burp',
            'github_url': '',
            'is_open_source': False,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['web-proxy', 'vulnerability-scanner', 'web-testing'],
        },
        {
            'name': 'OWASP ZAP',
            'category': web_cat,
            'description': 'Free open-source web application security scanner.',
            'use_case': 'Finding vulnerabilities in web applications during development and testing.',
            'url': 'https://www.zaproxy.org/',
            'github_url': 'https://github.com/zaproxy/zaproxy',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'BEGINNER',
            'tags': ['web-scanner', 'owasp', 'security-testing'],
        },
        # Password Cracking
        {
            'name': 'John the Ripper',
            'category': password_cat,
            'description': 'Fast password cracker supporting hundreds of hash and cipher types.',
            'use_case': 'Password auditing, hash cracking, and security testing.',
            'url': 'https://www.openwall.com/john/',
            'github_url': 'https://github.com/openwall/john',
            'is_open_source': True,
            'platforms': ['Linux', 'Windows', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['password-cracking', 'hash-cracking', 'security-audit'],
        },
        {
            'name': 'Hashcat',
            'category': password_cat,
            'description': 'Advanced password recovery tool using GPU acceleration.',
            'use_case': 'High-speed password cracking with support for over 300 hash types.',
            'url': 'https://hashcat.net/hashcat/',
            'github_url': 'https://github.com/hashcat/hashcat',
            'is_open_source': True,
            'platforms': ['Linux', 'Windows', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['gpu-cracking', 'password-recovery', 'hash-cracking'],
        },
        # Forensics
        {
            'name': 'Autopsy',
            'category': forensics_cat,
            'description': 'Digital forensics platform for analyzing hard drives and smartphones.',
            'use_case': 'Digital investigations, file recovery, and forensic analysis.',
            'url': 'https://www.autopsy.com/',
            'github_url': 'https://github.com/sleuthkit/autopsy',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['forensics', 'disk-analysis', 'investigations'],
        },
        # OSINT
        {
            'name': 'theHarvester',
            'category': osint_cat,
            'description': 'OSINT tool for gathering emails, subdomains, hosts, and more.',
            'use_case': 'Reconnaissance and information gathering from public sources.',
            'url': 'https://github.com/laramies/theHarvester',
            'github_url': 'https://github.com/laramies/theHarvester',
            'is_open_source': True,
            'platforms': ['Linux', 'Windows', 'macOS'],
            'difficulty': 'BEGINNER',
            'tags': ['osint', 'reconnaissance', 'information-gathering'],
        },
        {
            'name': 'Maltego',
            'category': osint_cat,
            'description': 'Interactive data mining tool for link analysis and intelligence gathering.',
            'use_case': 'OSINT investigations, network analysis, and visualizing relationships.',
            'url': 'https://www.maltego.com/',
            'github_url': '',
            'is_open_source': False,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['osint', 'data-mining', 'visualization'],
        },
    ]

    for tool_data in tools_data:
        tool, created = Tool.objects.get_or_create(
            name=tool_data['name'],
            defaults=tool_data
        )
        if created:
            print(f"  Created: {tool.name}")

    print(f"✓ Tools seeded ({Tool.objects.count()} total)\n")


def main():
    """Run all seed functions"""
    print("\n" + "="*50)
    print("SEEDING CYBERSEC DASHBOARD DATABASE")
    print("="*50 + "\n")

    try:
        seed_news_sources()
        seed_resource_categories()
        seed_certifications()
        seed_resources()
        seed_tool_categories()
        seed_tools()

        print("="*50)
        print("✓ ALL DATA SEEDED SUCCESSFULLY!")
        print("="*50 + "\n")

    except Exception as e:
        print(f"\n✗ Error during seeding: {str(e)}\n")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
