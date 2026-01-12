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
            'source_type': 'RSS',
            'url': 'https://www.reddit.com/r/netsec/.rss',
            'is_active': True,  # Using Reddit's public RSS feed (no API key needed)
        },
        {
            'name': 'r/cybersecurity',
            'source_type': 'RSS',
            'url': 'https://www.reddit.com/r/cybersecurity/.rss',
            'is_active': True,  # Using Reddit's public RSS feed (no API key needed)
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
    books_cat = Category.objects.get(slug='books')

    resources_data = [
        # === EXISTING COURSES (2) ===
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

        # === NEW DOCUMENTATION & FRAMEWORKS (14) ===
        {
            'title': 'MITRE ATT&CK Framework',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://attack.mitre.org/',
            'description': 'Comprehensive knowledge base of adversary tactics and techniques based on real-world observations.',
            'provider': 'MITRE',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['framework', 'threat-intelligence', 'tactics'],
        },
        {
            'title': 'CIS Controls',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://www.cisecurity.org/controls',
            'description': 'Prioritized set of actions to protect against the most pervasive cyber attacks.',
            'provider': 'Center for Internet Security',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['framework', 'best-practices', 'controls'],
        },
        {
            'title': 'OWASP API Security Top 10',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://owasp.org/www-project-api-security/',
            'description': 'Top 10 most critical security risks for APIs.',
            'provider': 'OWASP',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['api-security', 'owasp', 'web-security'],
        },
        {
            'title': 'OWASP Mobile Top 10',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://owasp.org/www-project-mobile-top-10/',
            'description': 'Top 10 mobile application security risks.',
            'provider': 'OWASP',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['mobile-security', 'owasp', 'app-security'],
        },
        {
            'title': 'SANS Top 25 Software Errors',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://www.sans.org/top25-software-errors/',
            'description': 'Most dangerous software weaknesses and how to avoid them.',
            'provider': 'SANS/CWE',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['secure-coding', 'vulnerabilities', 'best-practices'],
        },
        {
            'title': 'PCI DSS',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://www.pcisecuritystandards.org/',
            'description': 'Payment Card Industry Data Security Standard for protecting cardholder data.',
            'provider': 'PCI Security Standards Council',
            'is_free': True,
            'difficulty': 'ADVANCED',
            'tags': ['compliance', 'payment-security', 'standard'],
        },
        {
            'title': 'MITRE CVE',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://cve.mitre.org/',
            'description': 'Common Vulnerabilities and Exposures database of publicly disclosed cybersecurity vulnerabilities.',
            'provider': 'MITRE',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['vulnerabilities', 'cve', 'database'],
        },
        {
            'title': 'NVD (National Vulnerability Database)',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://nvd.nist.gov/',
            'description': 'US government repository of standards-based vulnerability management data.',
            'provider': 'NIST',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['vulnerabilities', 'cvss', 'database'],
        },
        {
            'title': 'Exploit Database',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://www.exploit-db.com/',
            'description': 'Archive of public exploits and corresponding vulnerable software.',
            'provider': 'Offensive Security',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['exploits', 'pentesting', 'vulnerabilities'],
        },
        {
            'title': 'OWASP Cheat Sheet Series',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://cheatsheetseries.owasp.org/',
            'description': 'Concise collection of high-value security information for specific application security topics.',
            'provider': 'OWASP',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['cheat-sheets', 'owasp', 'quick-reference'],
        },
        {
            'title': 'OWASP Testing Guide',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://owasp.org/www-project-web-security-testing-guide/',
            'description': 'Comprehensive guide to testing web application security.',
            'provider': 'OWASP',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['testing', 'owasp', 'web-security'],
        },
        {
            'title': 'NIST SP 800-53',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final',
            'description': 'Security and privacy controls for information systems and organizations.',
            'provider': 'NIST',
            'is_free': True,
            'difficulty': 'ADVANCED',
            'tags': ['controls', 'compliance', 'nist'],
        },
        {
            'title': 'OWASP Secure Coding Practices',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/',
            'description': 'Quick reference guide for secure coding practices.',
            'provider': 'OWASP',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['secure-coding', 'owasp', 'development'],
        },
        {
            'title': 'ATT&CK Navigator',
            'category': docs_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://mitre-attack.github.io/attack-navigator/',
            'description': 'Web-based tool for navigating and annotating ATT&CK matrices.',
            'provider': 'MITRE',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['attack', 'framework', 'tool'],
        },

        # === NEW COURSES & TRAINING (8) ===
        {
            'title': 'SANS Cyber Aces',
            'category': courses_cat,
            'resource_type': 'COURSE',
            'url': 'https://www.cyberaces.org/',
            'description': 'Free tutorials on operating systems, networking, and system administration.',
            'provider': 'SANS',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['free', 'fundamentals', 'networking'],
        },
        {
            'title': 'PortSwigger Web Security Academy',
            'category': courses_cat,
            'resource_type': 'COURSE',
            'url': 'https://portswigger.net/web-security',
            'description': 'Free online web security training with interactive labs.',
            'provider': 'PortSwigger',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['free', 'web-security', 'hands-on'],
        },
        {
            'title': 'Google Cybersecurity Certificate',
            'category': courses_cat,
            'resource_type': 'COURSE',
            'url': 'https://www.coursera.org/google-certificates/cybersecurity-certificate',
            'description': 'Professional certificate program for entry-level cybersecurity careers.',
            'provider': 'Google/Coursera',
            'is_free': False,
            'difficulty': 'BEGINNER',
            'tags': ['certificate', 'career-prep', 'beginner-friendly'],
        },
        {
            'title': 'Cisco Networking Academy - Cybersecurity',
            'category': courses_cat,
            'resource_type': 'COURSE',
            'url': 'https://www.netacad.com/courses/cybersecurity',
            'description': 'Free cybersecurity courses from basic concepts to advanced topics.',
            'provider': 'Cisco',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['free', 'networking', 'cisco'],
        },
        {
            'title': 'CISA Cybersecurity Training',
            'category': courses_cat,
            'resource_type': 'COURSE',
            'url': 'https://www.cisa.gov/cybersecurity-training-exercises',
            'description': 'Free training from US Cybersecurity & Infrastructure Security Agency.',
            'provider': 'CISA',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['free', 'government', 'infrastructure'],
        },
        {
            'title': 'Open Security Training',
            'category': courses_cat,
            'resource_type': 'COURSE',
            'url': 'https://opensecuritytraining.info/',
            'description': 'Free security training courses covering various advanced topics.',
            'provider': 'OpenSecurityTraining2',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['free', 'advanced-topics', 'in-depth'],
        },
        {
            'title': 'Immersive Labs',
            'category': courses_cat,
            'resource_type': 'COURSE',
            'url': 'https://www.immersivelabs.com/',
            'description': 'Gamified cybersecurity training platform with hands-on labs.',
            'provider': 'Immersive Labs',
            'is_free': False,
            'difficulty': 'INTERMEDIATE',
            'tags': ['gamified', 'hands-on', 'labs'],
        },
        {
            'title': 'SANS Reading Room',
            'category': courses_cat,
            'resource_type': 'DOCUMENTATION',
            'url': 'https://www.sans.org/white-papers/',
            'description': 'Collection of research papers and technical whitepapers on security topics.',
            'provider': 'SANS',
            'is_free': True,
            'difficulty': 'ADVANCED',
            'tags': ['research', 'whitepapers', 'advanced'],
        },

        # === NEW PRACTICE LABS (5) ===
        {
            'title': 'picoCTF',
            'category': labs_cat,
            'resource_type': 'LAB',
            'url': 'https://picoctf.org/',
            'description': 'Free cybersecurity competition and practice platform for all skill levels.',
            'provider': 'Carnegie Mellon University',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['free', 'ctf', 'competition'],
        },
        {
            'title': 'VulnHub',
            'category': labs_cat,
            'resource_type': 'LAB',
            'url': 'https://www.vulnhub.com/',
            'description': 'Vulnerable virtual machines for practicing penetration testing skills.',
            'provider': 'VulnHub',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['free', 'virtual-machines', 'pentesting'],
        },
        {
            'title': 'DVWA (Damn Vulnerable Web Application)',
            'category': labs_cat,
            'resource_type': 'LAB',
            'url': 'https://dvwa.co.uk/',
            'description': 'Intentionally vulnerable web application for learning web security.',
            'provider': 'DVWA',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['free', 'web-security', 'vulnerable-app'],
        },
        {
            'title': 'Blue Team Labs Online',
            'category': labs_cat,
            'resource_type': 'LAB',
            'url': 'https://blueteamlabs.online/',
            'description': 'Defensive security training platform with realistic scenarios.',
            'provider': 'Blue Team Labs Online',
            'is_free': False,
            'difficulty': 'INTERMEDIATE',
            'tags': ['blue-team', 'defense', 'soc'],
        },
        {
            'title': 'LetsDefend',
            'category': labs_cat,
            'resource_type': 'LAB',
            'url': 'https://letsdefend.io/',
            'description': 'Blue team training with realistic SOC analyst scenarios.',
            'provider': 'LetsDefend',
            'is_free': False,
            'difficulty': 'INTERMEDIATE',
            'tags': ['blue-team', 'soc', 'incident-response'],
        },

        # === NEW BOOKS (6) ===
        {
            'title': 'The Web Application Hacker\'s Handbook',
            'category': books_cat,
            'resource_type': 'BOOK',
            'url': 'https://www.amazon.com/Web-Application-Hackers-Handbook-Exploiting/dp/1118026470',
            'description': 'Comprehensive guide to discovering and exploiting web application security flaws.',
            'provider': 'Wiley',
            'is_free': False,
            'difficulty': 'INTERMEDIATE',
            'tags': ['web-security', 'pentesting', 'bible'],
        },
        {
            'title': 'Penetration Testing: A Hands-On Introduction to Hacking',
            'category': books_cat,
            'resource_type': 'BOOK',
            'url': 'https://nostarch.com/pentesting',
            'description': 'Beginner-friendly introduction to penetration testing fundamentals.',
            'provider': 'No Starch Press',
            'is_free': False,
            'difficulty': 'BEGINNER',
            'tags': ['pentesting', 'beginner-friendly', 'hands-on'],
        },
        {
            'title': 'Hacking: The Art of Exploitation (2nd Edition)',
            'category': books_cat,
            'resource_type': 'BOOK',
            'url': 'https://nostarch.com/hacking2.htm',
            'description': 'Deep dive into exploitation techniques with C programming and assembly.',
            'provider': 'No Starch Press',
            'is_free': False,
            'difficulty': 'ADVANCED',
            'tags': ['exploitation', 'low-level', 'advanced'],
        },
        {
            'title': 'Security Engineering (Ross Anderson)',
            'category': books_cat,
            'resource_type': 'BOOK',
            'url': 'https://www.cl.cam.ac.uk/~rja14/book.html',
            'description': 'Free comprehensive textbook on building secure systems.',
            'provider': 'Ross Anderson',
            'is_free': True,
            'difficulty': 'ADVANCED',
            'tags': ['free', 'systems', 'engineering'],
        },
        {
            'title': 'The Tangled Web',
            'category': books_cat,
            'resource_type': 'BOOK',
            'url': 'https://nostarch.com/tangledweb',
            'description': 'Comprehensive guide to securing modern web applications.',
            'provider': 'No Starch Press',
            'is_free': False,
            'difficulty': 'INTERMEDIATE',
            'tags': ['web-security', 'browsers', 'http'],
        },
        {
            'title': 'RTFM: Red Team Field Manual',
            'category': books_cat,
            'resource_type': 'BOOK',
            'url': 'https://www.amazon.com/Rtfm-Red-Team-Field-Manual/dp/1494295504',
            'description': 'Quick reference for red team operations and penetration testing commands.',
            'provider': 'Self-published',
            'is_free': False,
            'difficulty': 'INTERMEDIATE',
            'tags': ['reference', 'commands', 'red-team'],
        },

        # === NEW VIDEOS (4) ===
        {
            'title': 'IppSec (YouTube)',
            'category': courses_cat,
            'resource_type': 'VIDEO',
            'url': 'https://www.youtube.com/c/ippsec',
            'description': 'HackTheBox machine walkthroughs and penetration testing tutorials.',
            'provider': 'IppSec',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['free', 'youtube', 'walkthroughs'],
        },
        {
            'title': 'LiveOverflow (YouTube)',
            'category': courses_cat,
            'resource_type': 'VIDEO',
            'url': 'https://www.youtube.com/c/LiveOverflow',
            'description': 'Security research, CTF writeups, and exploitation techniques.',
            'provider': 'LiveOverflow',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['free', 'youtube', 'ctf'],
        },
        {
            'title': 'John Hammond (YouTube)',
            'category': courses_cat,
            'resource_type': 'VIDEO',
            'url': 'https://www.youtube.com/c/JohnHammond010',
            'description': 'Cybersecurity tutorials, malware analysis, and CTF solutions.',
            'provider': 'John Hammond',
            'is_free': True,
            'difficulty': 'BEGINNER',
            'tags': ['free', 'youtube', 'tutorials'],
        },
        {
            'title': 'Security Now Podcast',
            'category': courses_cat,
            'resource_type': 'VIDEO',
            'url': 'https://twit.tv/shows/security-now',
            'description': 'Weekly podcast covering security news and in-depth technical discussions.',
            'provider': 'Steve Gibson',
            'is_free': True,
            'difficulty': 'INTERMEDIATE',
            'tags': ['free', 'podcast', 'news'],
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
