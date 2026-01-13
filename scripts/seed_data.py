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
from apps.learning_paths.models import LearningPath, SkillNode


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
            'name': 'SecurityWeek',
            'source_type': 'RSS',
            'url': 'https://www.securityweek.com/feed/',
            'is_active': True,
        },
        {
            'name': 'Naked Security by Sophos',
            'source_type': 'RSS',
            'url': 'https://nakedsecurity.sophos.com/feed/',
            'is_active': True,
        },
        {
            'name': 'Graham Cluley',
            'source_type': 'RSS',
            'url': 'https://grahamcluley.com/feed/',
            'is_active': True,
        },
        {
            'name': 'Threatpost',
            'source_type': 'RSS',
            'url': 'https://threatpost.com/feed/',
            'is_active': True,
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
        {
            'name': 'Reverse Engineering',
            'slug': 'reverse-engineering',
            'description': 'Tools for reverse engineering binaries and malware analysis',
        },
        {
            'name': 'Vulnerability Scanning',
            'slug': 'vulnerability-scanning',
            'description': 'Tools for automated vulnerability detection and assessment',
        },
        {
            'name': 'Online Security Analysis',
            'slug': 'online-security-analysis',
            'description': 'Web-based tools for malware analysis, URL scanning, and threat intelligence',
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
    reverse_cat = ToolCategory.objects.get(slug='reverse-engineering')
    vuln_cat = ToolCategory.objects.get(slug='vulnerability-scanning')
    online_cat = ToolCategory.objects.get(slug='online-security-analysis')

    tools_data = [
        # Network Analysis
        {
            'name': 'Wireshark',
            'category': network_cat,
            'description': 'The world\'s most popular network protocol analyzer for deep inspection of network traffic.',
            'use_case': 'Capture and analyze network packets, troubleshoot network issues, detect security problems.',
            'url': 'https://www.wireshark.org/',
            'github_url': 'https://github.com/wireshark/wireshark',
            'tutorial_url': 'https://www.wireshark.org/docs/',
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
            'tutorial_url': 'https://nmap.org/book/man.html',
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
            'tutorial_url': 'https://docs.metasploit.com/',
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
            'tutorial_url': 'https://portswigger.net/burp/documentation',
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
            'tutorial_url': 'https://www.zaproxy.org/getting-started/',
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
            'tutorial_url': 'https://www.openwall.com/john/doc/',
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
            'tutorial_url': 'https://hashcat.net/wiki/',
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
            'tutorial_url': 'https://www.autopsy.com/support/',
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
            'tutorial_url': 'https://github.com/laramies/theHarvester#readme',
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
            'tutorial_url': 'https://www.maltego.com/maltego-essentials/',
            'is_open_source': False,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['osint', 'data-mining', 'visualization'],
        },

        # === NEW NETWORK ANALYSIS TOOLS (8) ===
        {
            'name': 'tcpdump',
            'category': network_cat,
            'description': 'Powerful command-line packet analyzer for capturing and analyzing network traffic.',
            'use_case': 'Packet capture, network troubleshooting, protocol analysis.',
            'url': 'https://www.tcpdump.org/',
            'github_url': 'https://github.com/the-tcpdump-group/tcpdump',
            'tutorial_url': 'https://danielmiessler.com/study/tcpdump/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['packet-capture', 'cli', 'network-analysis'],
        },
        {
            'name': 'Netcat',
            'category': network_cat,
            'description': 'TCP/UDP networking utility for reading and writing data across network connections.',
            'use_case': 'Port scanning, banner grabbing, file transfers, backdoors.',
            'url': 'http://netcat.sourceforge.net/',
            'github_url': '',
            'tutorial_url': 'https://www.sans.org/security-resources/sec560/netcat_cheat_sheet_v1.pdf',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'BEGINNER',
            'tags': ['networking', 'port-scanning', 'swiss-army-knife'],
        },
        {
            'name': 'Masscan',
            'category': network_cat,
            'description': 'Ultra-fast port scanner capable of scanning the entire Internet in under 6 minutes.',
            'use_case': 'Large-scale network reconnaissance and port scanning.',
            'url': 'https://github.com/robertdavidgraham/masscan',
            'github_url': 'https://github.com/robertdavidgraham/masscan',
            'tutorial_url': 'https://github.com/robertdavidgraham/masscan#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['port-scanner', 'fast', 'reconnaissance'],
        },
        {
            'name': 'Angry IP Scanner',
            'category': network_cat,
            'description': 'Fast and friendly network scanner for IP addresses and ports.',
            'use_case': 'Network discovery, IP scanning, port scanning with GUI.',
            'url': 'https://angryip.org/',
            'github_url': 'https://github.com/angryip/ipscan',
            'tutorial_url': 'https://angryip.org/documentation/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'BEGINNER',
            'tags': ['network-scanner', 'gui', 'port-scanner'],
        },
        {
            'name': 'NetworkMiner',
            'category': network_cat,
            'description': 'Network forensic analysis tool for extracting artifacts from PCAP files.',
            'use_case': 'Network forensics, PCAP analysis, file extraction.',
            'url': 'https://www.netresec.com/?page=NetworkMiner',
            'github_url': '',
            'tutorial_url': 'https://www.netresec.com/?page=NetworkMiner',
            'is_open_source': False,
            'platforms': ['Windows', 'Linux'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['forensics', 'pcap-analysis', 'network-forensics'],
        },
        {
            'name': 'Ettercap',
            'category': network_cat,
            'description': 'Comprehensive suite for man-in-the-middle attacks on LAN.',
            'use_case': 'MITM attacks, network sniffing, ARP poisoning.',
            'url': 'https://www.ettercap-project.org/',
            'github_url': 'https://github.com/Ettercap/ettercap',
            'tutorial_url': 'https://www.ettercap-project.org/ettercap/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'ADVANCED',
            'tags': ['mitm', 'network-attack', 'arp-poisoning'],
        },
        {
            'name': 'Bettercap',
            'category': network_cat,
            'description': 'Powerful framework for network attacks and monitoring.',
            'use_case': 'WiFi monitoring, MITM attacks, network reconnaissance.',
            'url': 'https://www.bettercap.org/',
            'github_url': 'https://github.com/bettercap/bettercap',
            'tutorial_url': 'https://www.bettercap.org/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['network-attack', 'wifi', 'mitm'],
        },
        {
            'name': 'Zeek',
            'category': network_cat,
            'description': 'Powerful network security monitoring framework (formerly Bro).',
            'use_case': 'Network security monitoring, traffic analysis, intrusion detection.',
            'url': 'https://zeek.org/',
            'github_url': 'https://github.com/zeek/zeek',
            'tutorial_url': 'https://docs.zeek.org/en/master/quickstart.html',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['network-monitoring', 'ids', 'traffic-analysis'],
        },

        # === NEW WEB APPLICATION SECURITY TOOLS (10) ===
        {
            'name': 'SQLmap',
            'category': web_cat,
            'description': 'Automatic SQL injection and database takeover tool.',
            'use_case': 'Detecting and exploiting SQL injection vulnerabilities.',
            'url': 'https://sqlmap.org/',
            'github_url': 'https://github.com/sqlmapproject/sqlmap',
            'tutorial_url': 'https://github.com/sqlmapproject/sqlmap/wiki/Usage',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['sql-injection', 'web-security', 'exploitation'],
        },
        {
            'name': 'Nikto',
            'category': web_cat,
            'description': 'Web server scanner that performs comprehensive tests.',
            'use_case': 'Web server vulnerability scanning and enumeration.',
            'url': 'https://cirt.net/Nikto2',
            'github_url': 'https://github.com/sullo/nikto',
            'tutorial_url': 'https://cirt.net/Nikto2',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'BEGINNER',
            'tags': ['web-scanner', 'vulnerability-scanner', 'enumeration'],
        },
        {
            'name': 'Gobuster',
            'category': web_cat,
            'description': 'Fast directory and DNS brute-forcing tool written in Go.',
            'use_case': 'Directory enumeration, DNS subdomain discovery.',
            'url': 'https://github.com/OJ/gobuster',
            'github_url': 'https://github.com/OJ/gobuster',
            'tutorial_url': 'https://github.com/OJ/gobuster#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'BEGINNER',
            'tags': ['brute-force', 'directory-enumeration', 'dns'],
        },
        {
            'name': 'ffuf',
            'category': web_cat,
            'description': 'Fast web fuzzer written in Go for discovering hidden content.',
            'use_case': 'Web fuzzing, parameter discovery, directory brute forcing.',
            'url': 'https://github.com/ffuf/ffuf',
            'github_url': 'https://github.com/ffuf/ffuf',
            'tutorial_url': 'https://github.com/ffuf/ffuf#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['fuzzing', 'web-security', 'brute-force'],
        },
        {
            'name': 'Wapiti',
            'category': web_cat,
            'description': 'Web application vulnerability scanner that audits security.',
            'use_case': 'Black-box web vulnerability scanning and testing.',
            'url': 'https://wapiti-scanner.github.io/',
            'github_url': 'https://github.com/wapiti-scanner/wapiti',
            'tutorial_url': 'https://wapiti-scanner.github.io/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['vulnerability-scanner', 'web-security', 'black-box'],
        },
        {
            'name': 'Commix',
            'category': web_cat,
            'description': 'Automated tool for detecting and exploiting command injection vulnerabilities.',
            'use_case': 'Command injection testing and exploitation.',
            'url': 'https://github.com/commixproject/commix',
            'github_url': 'https://github.com/commixproject/commix',
            'tutorial_url': 'https://github.com/commixproject/commix/wiki',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['command-injection', 'exploitation', 'web-security'],
        },
        {
            'name': 'XSStrike',
            'category': web_cat,
            'description': 'Advanced XSS detection and exploitation suite.',
            'use_case': 'Detecting and exploiting XSS vulnerabilities.',
            'url': 'https://github.com/s0md3v/XSStrike',
            'github_url': 'https://github.com/s0md3v/XSStrike',
            'tutorial_url': 'https://github.com/s0md3v/XSStrike#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['xss', 'web-security', 'exploitation'],
        },
        {
            'name': 'WPScan',
            'category': web_cat,
            'description': 'WordPress security scanner for vulnerabilities and misconfigurations.',
            'use_case': 'WordPress vulnerability scanning and enumeration.',
            'url': 'https://wpscan.com/',
            'github_url': 'https://github.com/wpscanteam/wpscan',
            'tutorial_url': 'https://github.com/wpscanteam/wpscan#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'BEGINNER',
            'tags': ['wordpress', 'cms-scanner', 'vulnerability-scanner'],
        },
        {
            'name': 'Nuclei',
            'category': web_cat,
            'description': 'Fast and customizable vulnerability scanner based on templates.',
            'use_case': 'Automated vulnerability detection with custom templates.',
            'url': 'https://nuclei.projectdiscovery.io/',
            'github_url': 'https://github.com/projectdiscovery/nuclei',
            'tutorial_url': 'https://nuclei.projectdiscovery.io/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['vulnerability-scanner', 'automation', 'templates'],
        },
        {
            'name': 'dirb',
            'category': web_cat,
            'description': 'Web content scanner for finding hidden directories and files.',
            'use_case': 'Directory brute forcing and content discovery.',
            'url': 'http://dirb.sourceforge.net/',
            'github_url': '',
            'tutorial_url': 'https://www.kali.org/tools/dirb/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS'],
            'difficulty': 'BEGINNER',
            'tags': ['brute-force', 'directory-enumeration', 'content-discovery'],
        },

        # === NEW PENETRATION TESTING TOOLS (14) ===
        {
            'name': 'Cobalt Strike',
            'category': pentest_cat,
            'description': 'Commercial adversary simulation and red team operations platform.',
            'use_case': 'Advanced persistent threat simulation and red team exercises.',
            'url': 'https://www.cobaltstrike.com/',
            'github_url': '',
            'tutorial_url': 'https://www.cobaltstrike.com/help',
            'is_open_source': False,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['red-team', 'c2', 'adversary-simulation'],
        },
        {
            'name': 'Empire',
            'category': pentest_cat,
            'description': 'Post-exploitation framework built on PowerShell and Python.',
            'use_case': 'Post-exploitation, lateral movement, persistence.',
            'url': 'https://github.com/EmpireProject/Empire',
            'github_url': 'https://github.com/EmpireProject/Empire',
            'tutorial_url': 'https://github.com/EmpireProject/Empire/wiki',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['post-exploitation', 'powershell', 'c2'],
        },
        {
            'name': 'BeEF',
            'category': pentest_cat,
            'description': 'Browser Exploitation Framework for testing web browser security.',
            'use_case': 'Client-side attacks and browser exploitation.',
            'url': 'https://beefproject.com/',
            'github_url': 'https://github.com/beefproject/beef',
            'tutorial_url': 'https://github.com/beefproject/beef/wiki',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'ADVANCED',
            'tags': ['browser-exploitation', 'xss', 'client-side'],
        },
        {
            'name': 'Social-Engineer Toolkit',
            'category': pentest_cat,
            'description': 'Framework for social engineering attacks and phishing.',
            'use_case': 'Social engineering, phishing campaigns, credential harvesting.',
            'url': 'https://github.com/trustedsec/social-engineer-toolkit',
            'github_url': 'https://github.com/trustedsec/social-engineer-toolkit',
            'tutorial_url': 'https://github.com/trustedsec/social-engineer-toolkit#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['social-engineering', 'phishing', 'credential-harvesting'],
        },
        {
            'name': 'Aircrack-ng',
            'category': pentest_cat,
            'description': 'Complete suite for WiFi network security auditing.',
            'use_case': 'WiFi password cracking, WEP/WPA/WPA2 attacks.',
            'url': 'https://www.aircrack-ng.org/',
            'github_url': 'https://github.com/aircrack-ng/aircrack-ng',
            'tutorial_url': 'https://www.aircrack-ng.org/doku.php?id=getting_started',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['wifi', 'wireless', 'password-cracking'],
        },
        {
            'name': 'Reaver',
            'category': pentest_cat,
            'description': 'Brute force attack tool against WiFi Protected Setup (WPS).',
            'use_case': 'WPS PIN attacks and WiFi password recovery.',
            'url': 'https://github.com/t6x/reaver-wps-fork-t6x',
            'github_url': 'https://github.com/t6x/reaver-wps-fork-t6x',
            'tutorial_url': 'https://github.com/t6x/reaver-wps-fork-t6x#readme',
            'is_open_source': True,
            'platforms': ['Linux'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['wifi', 'wps', 'brute-force'],
        },
        {
            'name': 'Hydra',
            'category': pentest_cat,
            'description': 'Fast and flexible network login brute forcer.',
            'use_case': 'Password brute forcing for network services (SSH, FTP, HTTP, etc.).',
            'url': 'https://github.com/vanhauser-thc/thc-hydra',
            'github_url': 'https://github.com/vanhauser-thc/thc-hydra',
            'tutorial_url': 'https://github.com/vanhauser-thc/thc-hydra#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'BEGINNER',
            'tags': ['brute-force', 'password-cracking', 'network'],
        },
        {
            'name': 'Medusa',
            'category': pentest_cat,
            'description': 'Speedy, parallel, and modular login brute forcer.',
            'use_case': 'Fast parallel password attacks on network services.',
            'url': 'http://foofus.net/goons/jmk/medusa/medusa.html',
            'github_url': '',
            'tutorial_url': 'http://foofus.net/goons/jmk/medusa/medusa.html',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['brute-force', 'password-cracking', 'parallel'],
        },
        {
            'name': 'CrackMapExec',
            'category': pentest_cat,
            'description': 'Swiss army knife for pentesting Windows/Active Directory networks.',
            'use_case': 'Active Directory enumeration, lateral movement, password spraying.',
            'url': 'https://github.com/byt3bl33d3r/CrackMapExec',
            'github_url': 'https://github.com/byt3bl33d3r/CrackMapExec',
            'tutorial_url': 'https://www.crackmapexec.wiki/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'ADVANCED',
            'tags': ['active-directory', 'lateral-movement', 'windows'],
        },
        {
            'name': 'Impacket',
            'category': pentest_cat,
            'description': 'Collection of Python classes for working with network protocols.',
            'use_case': 'Windows protocol manipulation, pass-the-hash attacks, SMB relay.',
            'url': 'https://github.com/fortra/impacket',
            'github_url': 'https://github.com/fortra/impacket',
            'tutorial_url': 'https://github.com/fortra/impacket#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'ADVANCED',
            'tags': ['windows', 'protocols', 'active-directory'],
        },
        {
            'name': 'Responder',
            'category': pentest_cat,
            'description': 'LLMNR, NBT-NS and MDNS poisoner for credential theft.',
            'use_case': 'Network poisoning attacks and credential harvesting.',
            'url': 'https://github.com/lgandx/Responder',
            'github_url': 'https://github.com/lgandx/Responder',
            'tutorial_url': 'https://github.com/lgandx/Responder#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['network-poisoning', 'credential-harvesting', 'mitm'],
        },
        {
            'name': 'mimikatz',
            'category': pentest_cat,
            'description': 'Windows credential extraction and manipulation tool.',
            'use_case': 'Extracting passwords, hashes, and Kerberos tickets from Windows.',
            'url': 'https://github.com/gentilkiwi/mimikatz',
            'github_url': 'https://github.com/gentilkiwi/mimikatz',
            'tutorial_url': 'https://github.com/gentilkiwi/mimikatz/wiki',
            'is_open_source': True,
            'platforms': ['Windows'],
            'difficulty': 'ADVANCED',
            'tags': ['windows', 'credential-dumping', 'post-exploitation'],
        },
        {
            'name': 'PowerSploit',
            'category': pentest_cat,
            'description': 'PowerShell post-exploitation framework.',
            'use_case': 'Windows post-exploitation, privilege escalation, lateral movement.',
            'url': 'https://github.com/PowerShellMafia/PowerSploit',
            'github_url': 'https://github.com/PowerShellMafia/PowerSploit',
            'tutorial_url': 'https://github.com/PowerShellMafia/PowerSploit#readme',
            'is_open_source': True,
            'platforms': ['Windows'],
            'difficulty': 'ADVANCED',
            'tags': ['powershell', 'post-exploitation', 'windows'],
        },
        {
            'name': 'Covenant',
            'category': pentest_cat,
            'description': '.NET command and control framework for red team operations.',
            'use_case': 'C2 operations, post-exploitation, red team exercises.',
            'url': 'https://github.com/cobbr/Covenant',
            'github_url': 'https://github.com/cobbr/Covenant',
            'tutorial_url': 'https://github.com/cobbr/Covenant/wiki',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['c2', 'red-team', 'dotnet'],
        },

        # === NEW FORENSICS TOOLS (8) ===
        {
            'name': 'Volatility',
            'category': forensics_cat,
            'description': 'Advanced memory forensics framework for incident response.',
            'use_case': 'Memory dump analysis, malware detection, incident response.',
            'url': 'https://www.volatilityfoundation.org/',
            'github_url': 'https://github.com/volatilityfoundation/volatility',
            'tutorial_url': 'https://github.com/volatilityfoundation/volatility/wiki',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'ADVANCED',
            'tags': ['memory-forensics', 'incident-response', 'malware-analysis'],
        },
        {
            'name': 'FTK Imager',
            'category': forensics_cat,
            'description': 'Data preview and imaging tool for forensic investigations.',
            'use_case': 'Creating forensic images, data preview, file extraction.',
            'url': 'https://www.exterro.com/ftk-imager',
            'github_url': '',
            'tutorial_url': 'https://www.exterro.com/ftk-imager',
            'is_open_source': False,
            'platforms': ['Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['disk-imaging', 'forensics', 'data-preview'],
        },
        {
            'name': 'Sleuth Kit',
            'category': forensics_cat,
            'description': 'Collection of command-line tools for file system forensic analysis.',
            'use_case': 'File system analysis, deleted file recovery, timeline creation.',
            'url': 'https://www.sleuthkit.org/',
            'github_url': 'https://github.com/sleuthkit/sleuthkit',
            'tutorial_url': 'https://www.sleuthkit.org/sleuthkit/docs.php',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['file-system-analysis', 'forensics', 'cli'],
        },
        {
            'name': 'Binwalk',
            'category': forensics_cat,
            'description': 'Tool for analyzing, reverse engineering, and extracting firmware images.',
            'use_case': 'Firmware analysis, file extraction, reverse engineering.',
            'url': 'https://github.com/ReFirmLabs/binwalk',
            'github_url': 'https://github.com/ReFirmLabs/binwalk',
            'tutorial_url': 'https://github.com/ReFirmLabs/binwalk/wiki',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['firmware-analysis', 'reverse-engineering', 'iot'],
        },
        {
            'name': 'Rekall',
            'category': forensics_cat,
            'description': 'Advanced memory analysis framework for incident response.',
            'use_case': 'Memory forensics, malware analysis, live system analysis.',
            'url': 'http://www.rekall-forensic.com/',
            'github_url': 'https://github.com/google/rekall',
            'tutorial_url': 'http://www.rekall-forensic.com/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'ADVANCED',
            'tags': ['memory-forensics', 'incident-response', 'live-analysis'],
        },
        {
            'name': 'Scalpel',
            'category': forensics_cat,
            'description': 'Fast file carving tool for recovering deleted files.',
            'use_case': 'File recovery, deleted file carving, forensic investigation.',
            'url': 'https://github.com/sleuthkit/scalpel',
            'github_url': 'https://github.com/sleuthkit/scalpel',
            'tutorial_url': 'https://github.com/sleuthkit/scalpel#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['file-carving', 'data-recovery', 'forensics'],
        },
        {
            'name': 'Foremost',
            'category': forensics_cat,
            'description': 'Console program to recover files based on headers and footers.',
            'use_case': 'File recovery, data carving from disk images.',
            'url': 'http://foremost.sourceforge.net/',
            'github_url': '',
            'tutorial_url': 'http://foremost.sourceforge.net/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS'],
            'difficulty': 'BEGINNER',
            'tags': ['file-recovery', 'data-carving', 'forensics'],
        },
        {
            'name': 'Bulk Extractor',
            'category': forensics_cat,
            'description': 'Extracts useful information from disk images without parsing file system.',
            'use_case': 'Email extraction, credit card number recovery, URL extraction.',
            'url': 'https://github.com/simsong/bulk_extractor',
            'github_url': 'https://github.com/simsong/bulk_extractor',
            'tutorial_url': 'https://github.com/simsong/bulk_extractor#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['data-extraction', 'forensics', 'information-recovery'],
        },

        # === NEW OSINT TOOLS (6) ===
        {
            'name': 'Shodan',
            'category': osint_cat,
            'description': 'Search engine for Internet-connected devices and services.',
            'use_case': 'Finding exposed devices, services, and vulnerabilities.',
            'url': 'https://www.shodan.io/',
            'github_url': '',
            'tutorial_url': 'https://help.shodan.io/the-basics/what-is-shodan',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'BEGINNER',
            'tags': ['search-engine', 'reconnaissance', 'exposure-detection'],
        },
        {
            'name': 'Recon-ng',
            'category': osint_cat,
            'description': 'Full-featured web reconnaissance framework written in Python.',
            'use_case': 'OSINT gathering, subdomain enumeration, information collection.',
            'url': 'https://github.com/lanmaster53/recon-ng',
            'github_url': 'https://github.com/lanmaster53/recon-ng',
            'tutorial_url': 'https://github.com/lanmaster53/recon-ng/wiki',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['osint', 'reconnaissance', 'framework'],
        },
        {
            'name': 'SpiderFoot',
            'category': osint_cat,
            'description': 'Automated OSINT tool for reconnaissance and threat intelligence.',
            'use_case': 'Automated OSINT collection, threat intelligence gathering.',
            'url': 'https://www.spiderfoot.net/',
            'github_url': 'https://github.com/smicallef/spiderfoot',
            'tutorial_url': 'https://www.spiderfoot.net/documentation/',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['osint', 'automation', 'threat-intelligence'],
        },
        {
            'name': 'Metagoofil',
            'category': osint_cat,
            'description': 'Tool for extracting metadata from public documents.',
            'use_case': 'Metadata extraction, information leakage detection.',
            'url': 'https://github.com/laramies/metagoofil',
            'github_url': 'https://github.com/laramies/metagoofil',
            'tutorial_url': 'https://github.com/laramies/metagoofil#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'BEGINNER',
            'tags': ['metadata', 'document-analysis', 'information-gathering'],
        },
        {
            'name': 'FOCA',
            'category': osint_cat,
            'description': 'Tool for finding metadata and hidden information in documents.',
            'use_case': 'Metadata analysis, information leakage detection.',
            'url': 'https://github.com/ElevenPaths/FOCA',
            'github_url': 'https://github.com/ElevenPaths/FOCA',
            'tutorial_url': 'https://github.com/ElevenPaths/FOCA#readme',
            'is_open_source': True,
            'platforms': ['Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['metadata', 'document-analysis', 'osint'],
        },
        {
            'name': 'Sherlock',
            'category': osint_cat,
            'description': 'Hunt down social media accounts by username across platforms.',
            'use_case': 'Username OSINT, social media reconnaissance.',
            'url': 'https://github.com/sherlock-project/sherlock',
            'github_url': 'https://github.com/sherlock-project/sherlock',
            'tutorial_url': 'https://github.com/sherlock-project/sherlock#readme',
            'is_open_source': True,
            'platforms': ['Linux', 'macOS', 'Windows'],
            'difficulty': 'BEGINNER',
            'tags': ['osint', 'social-media', 'username-search'],
        },

        # === NEW PASSWORD CRACKING TOOLS (3) ===
        {
            'name': 'Ophcrack',
            'category': password_cat,
            'description': 'Windows password cracker based on rainbow tables.',
            'use_case': 'Windows password recovery using rainbow tables.',
            'url': 'https://ophcrack.sourceforge.io/',
            'github_url': '',
            'tutorial_url': 'https://ophcrack.sourceforge.io/',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'BEGINNER',
            'tags': ['password-cracking', 'windows', 'rainbow-tables'],
        },
        {
            'name': 'RainbowCrack',
            'category': password_cat,
            'description': 'Password cracker using time-memory tradeoff algorithm.',
            'use_case': 'Fast password cracking with precomputed rainbow tables.',
            'url': 'http://project-rainbowcrack.com/',
            'github_url': '',
            'tutorial_url': 'http://project-rainbowcrack.com/',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['rainbow-tables', 'password-cracking', 'hash-cracking'],
        },
        {
            'name': 'L0phtCrack',
            'category': password_cat,
            'description': 'Password auditing and recovery application for Windows.',
            'use_case': 'Windows password auditing and security assessment.',
            'url': 'https://www.l0phtcrack.com/',
            'github_url': '',
            'tutorial_url': 'https://www.l0phtcrack.com/',
            'is_open_source': False,
            'platforms': ['Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['password-auditing', 'windows', 'security-assessment'],
        },

        # === NEW REVERSE ENGINEERING TOOLS (8) ===
        {
            'name': 'Ghidra',
            'category': reverse_cat,
            'description': 'NSA\'s software reverse engineering suite.',
            'use_case': 'Binary analysis, decompilation, malware reverse engineering.',
            'url': 'https://ghidra-sre.org/',
            'github_url': 'https://github.com/NationalSecurityAgency/ghidra',
            'tutorial_url': 'https://ghidra-sre.org/CheatSheet.html',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['reverse-engineering', 'decompiler', 'binary-analysis'],
        },
        {
            'name': 'IDA Pro',
            'category': reverse_cat,
            'description': 'Industry-standard interactive disassembler and debugger.',
            'use_case': 'Professional reverse engineering, malware analysis, vulnerability research.',
            'url': 'https://hex-rays.com/ida-pro/',
            'github_url': '',
            'tutorial_url': 'https://hex-rays.com/ida-pro/',
            'is_open_source': False,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['disassembler', 'debugger', 'professional'],
        },
        {
            'name': 'Radare2',
            'category': reverse_cat,
            'description': 'Open-source reverse engineering framework.',
            'use_case': 'Binary analysis, debugging, disassembly, exploitation.',
            'url': 'https://rada.re/',
            'github_url': 'https://github.com/radareorg/radare2',
            'tutorial_url': 'https://book.rada.re/',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['reverse-engineering', 'framework', 'binary-analysis'],
        },
        {
            'name': 'OllyDbg',
            'category': reverse_cat,
            'description': '32-bit assembler level debugger for Windows.',
            'use_case': 'Windows binary debugging, malware analysis, reverse engineering.',
            'url': 'http://www.ollydbg.de/',
            'github_url': '',
            'tutorial_url': 'http://www.ollydbg.de/',
            'is_open_source': False,
            'platforms': ['Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['debugger', 'windows', 'assembly'],
        },
        {
            'name': 'x64dbg',
            'category': reverse_cat,
            'description': 'Open-source x64/x32 debugger for Windows.',
            'use_case': 'Windows binary debugging, reverse engineering, malware analysis.',
            'url': 'https://x64dbg.com/',
            'github_url': 'https://github.com/x64dbg/x64dbg',
            'tutorial_url': 'https://x64dbg.com/',
            'is_open_source': True,
            'platforms': ['Windows'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['debugger', 'windows', 'open-source'],
        },
        {
            'name': 'Binary Ninja',
            'category': reverse_cat,
            'description': 'Binary analysis platform with modern UI and collaboration features.',
            'use_case': 'Binary analysis, vulnerability research, exploit development.',
            'url': 'https://binary.ninja/',
            'github_url': '',
            'tutorial_url': 'https://docs.binary.ninja/',
            'is_open_source': False,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'ADVANCED',
            'tags': ['binary-analysis', 'modern-ui', 'collaboration'],
        },
        {
            'name': 'Hopper',
            'category': reverse_cat,
            'description': 'Reverse engineering tool for macOS and Linux.',
            'use_case': 'macOS/Linux binary analysis and disassembly.',
            'url': 'https://www.hopperapp.com/',
            'github_url': '',
            'tutorial_url': 'https://www.hopperapp.com/tutorial.html',
            'is_open_source': False,
            'platforms': ['macOS', 'Linux'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['disassembler', 'macos', 'linux'],
        },
        {
            'name': 'Cutter',
            'category': reverse_cat,
            'description': 'Free and open-source GUI for Radare2.',
            'use_case': 'Reverse engineering with graphical interface.',
            'url': 'https://cutter.re/',
            'github_url': 'https://github.com/rizinorg/cutter',
            'tutorial_url': 'https://cutter.re/docs/',
            'is_open_source': True,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['gui', 'radare2', 'reverse-engineering'],
        },

        # === NEW VULNERABILITY SCANNING TOOLS (5) ===
        {
            'name': 'Nessus',
            'category': vuln_cat,
            'description': 'Comprehensive vulnerability scanner from Tenable.',
            'use_case': 'Enterprise vulnerability scanning, compliance auditing.',
            'url': 'https://www.tenable.com/products/nessus',
            'github_url': '',
            'tutorial_url': 'https://docs.tenable.com/nessus/',
            'is_open_source': False,
            'platforms': ['Windows', 'Linux', 'macOS'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['vulnerability-scanner', 'enterprise', 'compliance'],
        },
        {
            'name': 'OpenVAS',
            'category': vuln_cat,
            'description': 'Open-source vulnerability scanner and manager.',
            'use_case': 'Network vulnerability scanning, security assessment.',
            'url': 'https://www.openvas.org/',
            'github_url': 'https://github.com/greenbone/openvas-scanner',
            'tutorial_url': 'https://www.openvas.org/',
            'is_open_source': True,
            'platforms': ['Linux'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['vulnerability-scanner', 'open-source', 'network-security'],
        },
        {
            'name': 'Nexpose',
            'category': vuln_cat,
            'description': 'Vulnerability management solution from Rapid7.',
            'use_case': 'Vulnerability management, risk prioritization, remediation tracking.',
            'url': 'https://www.rapid7.com/products/nexpose/',
            'github_url': '',
            'tutorial_url': 'https://www.rapid7.com/products/nexpose/',
            'is_open_source': False,
            'platforms': ['Windows', 'Linux'],
            'difficulty': 'ADVANCED',
            'tags': ['vulnerability-management', 'enterprise', 'risk-management'],
        },
        {
            'name': 'Qualys',
            'category': vuln_cat,
            'description': 'Cloud-based vulnerability management and compliance platform.',
            'use_case': 'Cloud vulnerability scanning, compliance monitoring, asset management.',
            'url': 'https://www.qualys.com/',
            'github_url': '',
            'tutorial_url': 'https://www.qualys.com/docs/',
            'is_open_source': False,
            'platforms': ['Cloud'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['cloud-based', 'vulnerability-management', 'compliance'],
        },
        {
            'name': 'Acunetix',
            'category': vuln_cat,
            'description': 'Automated web application security testing solution.',
            'use_case': 'Web application vulnerability scanning, security testing.',
            'url': 'https://www.acunetix.com/',
            'github_url': '',
            'tutorial_url': 'https://www.acunetix.com/support/docs/',
            'is_open_source': False,
            'platforms': ['Windows', 'Linux'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['web-scanner', 'automated', 'application-security'],
        },
        # Online Security Analysis
        {
            'name': 'VirusTotal',
            'category': online_cat,
            'description': 'Free online service that analyzes files and URLs for viruses, worms, trojans and other malicious content using 70+ antivirus engines.',
            'use_case': 'Analyze suspicious files, URLs, domains, and IP addresses for malware and security threats.',
            'url': 'https://www.virustotal.com/',
            'github_url': '',
            'tutorial_url': 'https://support.virustotal.com/hc/en-us',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'BEGINNER',
            'tags': ['malware-analysis', 'file-scanning', 'url-scanning', 'threat-intelligence'],
        },
        {
            'name': 'Cisco Talos Intelligence',
            'category': online_cat,
            'description': 'Comprehensive threat intelligence platform providing real-time information about security threats, vulnerabilities, and malicious actors.',
            'use_case': 'Research threat intelligence, check IP/domain reputation, analyze malware samples.',
            'url': 'https://talosintelligence.com/',
            'github_url': '',
            'tutorial_url': 'https://talosintelligence.com/reputation_center',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['threat-intelligence', 'reputation', 'malware-analysis'],
        },
        {
            'name': 'URLhaus',
            'category': online_cat,
            'description': 'Project from abuse.ch to share malicious URLs that are being used for malware distribution.',
            'use_case': 'Check if a URL is known to distribute malware, research malware campaigns.',
            'url': 'https://urlhaus.abuse.ch/',
            'github_url': '',
            'tutorial_url': 'https://urlhaus.abuse.ch/api/',
            'is_open_source': True,
            'platforms': ['Web'],
            'difficulty': 'BEGINNER',
            'tags': ['malware-urls', 'threat-intelligence', 'malware-distribution'],
        },
        {
            'name': 'Hybrid Analysis',
            'category': online_cat,
            'description': 'Free malware analysis service powered by Falcon Sandbox that detects and analyzes unknown threats using advanced analysis technology.',
            'use_case': 'Submit suspicious files for automated malware analysis in a sandbox environment.',
            'url': 'https://www.hybrid-analysis.com/',
            'github_url': '',
            'tutorial_url': 'https://www.hybrid-analysis.com/docs/api/v2',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['sandbox', 'malware-analysis', 'automated-analysis'],
        },
        {
            'name': 'AbuseIPDB',
            'category': online_cat,
            'description': 'Database of reported malicious IP addresses involved in hacking attempts, spam, and other abusive behavior.',
            'use_case': 'Check IP address reputation, report malicious IPs, investigate suspicious connections.',
            'url': 'https://www.abuseipdb.com/',
            'github_url': '',
            'tutorial_url': 'https://www.abuseipdb.com/api.html',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'BEGINNER',
            'tags': ['ip-reputation', 'abuse-reporting', 'threat-intelligence'],
        },
        {
            'name': 'AlienVault OTX',
            'category': online_cat,
            'description': 'Open Threat Exchange - collaborative threat intelligence platform where security professionals share threat data.',
            'use_case': 'Access global threat intelligence, share IoCs, research emerging threats.',
            'url': 'https://otx.alienvault.com/',
            'github_url': '',
            'tutorial_url': 'https://otx.alienvault.com/api',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['threat-intelligence', 'ioc', 'collaboration'],
        },
        {
            'name': 'Shodan',
            'category': online_cat,
            'description': 'Search engine for Internet-connected devices. Discover exposed servers, IoT devices, and security vulnerabilities.',
            'use_case': 'Reconnaissance, identify exposed services, discover vulnerable devices, security research.',
            'url': 'https://www.shodan.io/',
            'github_url': '',
            'tutorial_url': 'https://help.shodan.io/',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['reconnaissance', 'iot', 'exposed-services', 'osint'],
        },
        {
            'name': 'Have I Been Pwned',
            'category': online_cat,
            'description': 'Check if your email or phone has been compromised in a data breach. Largest breach database with billions of records.',
            'use_case': 'Verify if credentials have been leaked, monitor for account compromises.',
            'url': 'https://haveibeenpwned.com/',
            'github_url': '',
            'tutorial_url': 'https://haveibeenpwned.com/API/v3',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'BEGINNER',
            'tags': ['breach-detection', 'credential-leak', 'data-breach'],
        },
        {
            'name': 'MX Toolbox',
            'category': online_cat,
            'description': 'Comprehensive suite of network diagnostic and lookup tools for DNS, email, and network troubleshooting.',
            'use_case': 'DNS lookup, email security checks, blacklist monitoring, network diagnostics.',
            'url': 'https://mxtoolbox.com/',
            'github_url': '',
            'tutorial_url': 'https://mxtoolbox.com/SuperTool.aspx',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'BEGINNER',
            'tags': ['dns', 'email-security', 'network-tools', 'diagnostics'],
        },
        {
            'name': 'SSL Labs',
            'category': online_cat,
            'description': 'Free SSL/TLS server testing tool by Qualys that analyzes HTTPS configurations and identifies security issues.',
            'use_case': 'Test SSL/TLS configuration, identify certificate issues, verify HTTPS security.',
            'url': 'https://www.ssllabs.com/ssltest/',
            'github_url': '',
            'tutorial_url': 'https://github.com/ssllabs/research/wiki/SSL-Server-Rating-Guide',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'BEGINNER',
            'tags': ['ssl', 'tls', 'certificate-testing', 'https'],
        },
        {
            'name': 'URLScan.io',
            'category': online_cat,
            'description': 'Website scanner that takes screenshots, analyzes DOM, and detects malicious content and phishing attempts.',
            'use_case': 'Scan suspicious URLs, analyze website behavior, detect phishing sites.',
            'url': 'https://urlscan.io/',
            'github_url': '',
            'tutorial_url': 'https://urlscan.io/about-api/',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'BEGINNER',
            'tags': ['url-scanning', 'phishing-detection', 'website-analysis'],
        },
        {
            'name': 'ANY.RUN',
            'category': online_cat,
            'description': 'Interactive online malware analysis sandbox. Analyze malware in real-time with full control.',
            'use_case': 'Interactive malware analysis, observe malware behavior, generate IoCs.',
            'url': 'https://any.run/',
            'github_url': '',
            'tutorial_url': 'https://any.run/api-documentation/',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'INTERMEDIATE',
            'tags': ['sandbox', 'malware-analysis', 'interactive'],
        },
        {
            'name': 'PhishTank',
            'category': online_cat,
            'description': 'Community-driven anti-phishing site where users submit, verify, and track phishing sites.',
            'use_case': 'Verify if a URL is a known phishing site, report phishing URLs.',
            'url': 'https://www.phishtank.com/',
            'github_url': '',
            'tutorial_url': 'https://www.phishtank.com/api_info.php',
            'is_open_source': False,
            'platforms': ['Web'],
            'difficulty': 'BEGINNER',
            'tags': ['phishing', 'url-verification', 'community'],
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


def seed_learning_paths():
    """Create learning paths and skill nodes"""
    print("Seeding learning paths...")

    # Create "Web Security Fundamentals" Learning Path
    web_path, created = LearningPath.objects.get_or_create(
        slug='web-security-fundamentals',
        defaults={
            'name': 'Web Security Fundamentals',
            'description': 'Master the fundamentals of web application security from basic concepts to advanced penetration testing techniques.',
            'icon': 'fas fa-shield-halved',
            'difficulty': 'INTERMEDIATE',
            'estimated_hours': 220,
            'is_published': True,
            'order': 1,
        }
    )
    if created:
        print(f"  Created: {web_path.name}")

    # Create skill nodes for Web Security path
    skill_nodes_data = [
        # Level 1: Foundations
        {
            'learning_path': web_path,
            'slug': 'linux-basics',
            'title': 'Linux Basics',
            'description': 'Learn Linux command line, file systems, permissions, and basic system administration.',
            'difficulty': 'BEGINNER',
            'estimated_hours': 20,
            'order': 1,
            'prerequisites': [],
            'resources': ['Professor Messer Security+'],
            'tools': ['Wireshark', 'Nmap'],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'Linux Journey',
                    'url': 'https://linuxjourney.com/',
                    'type': 'course',
                    'description': 'Free interactive guide to learning Linux from beginner to advanced'
                },
                {
                    'title': 'Linux Command Line Basics (Udacity)',
                    'url': 'https://www.udacity.com/course/linux-command-line-basics--ud595',
                    'type': 'course',
                    'description': 'Free course covering essential Linux command line skills'
                },
                {
                    'title': 'The Linux Command Handbook',
                    'url': 'https://www.freecodecamp.org/news/the-linux-commands-handbook/',
                    'type': 'article',
                    'description': 'Comprehensive reference guide to Linux commands'
                }
            ]
        },
        {
            'learning_path': web_path,
            'slug': 'networking-fundamentals',
            'title': 'Networking Fundamentals',
            'description': 'Understand TCP/IP, DNS, HTTP, and network protocols essential for security testing.',
            'difficulty': 'BEGINNER',
            'estimated_hours': 25,
            'order': 2,
            'prerequisites': [],
            'resources': ['Professor Messer Security+', 'NIST Cybersecurity Framework'],
            'tools': ['Wireshark', 'tcpdump', 'Nmap'],
            'certifications': ['CompTIA Security+'],
            'learning_resources': [
                {
                    'title': 'Networking Fundamentals (Cisco)',
                    'url': 'https://www.netacad.com/courses/networking/networking-basics',
                    'type': 'course',
                    'description': 'Free Cisco course covering networking fundamentals'
                },
                {
                    'title': 'Computer Networking: A Top-Down Approach',
                    'url': 'https://gaia.cs.umass.edu/kurose_ross/online_lectures.htm',
                    'type': 'video',
                    'description': 'Free video lectures from the popular networking textbook'
                },
                {
                    'title': 'TCP/IP Guide',
                    'url': 'http://www.tcpipguide.com/',
                    'type': 'documentation',
                    'description': 'Comprehensive online reference for TCP/IP protocols'
                }
            ]
        },
        {
            'learning_path': web_path,
            'slug': 'programming-python',
            'title': 'Programming Basics (Python)',
            'description': 'Learn Python programming for security automation and scripting.',
            'difficulty': 'BEGINNER',
            'estimated_hours': 30,
            'order': 3,
            'prerequisites': [],
            'resources': ['Cybrary'],
            'tools': [],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'Python for Everybody (Coursera)',
                    'url': 'https://www.py4e.com/',
                    'type': 'course',
                    'description': 'Free Python course with videos, exercises, and examples'
                },
                {
                    'title': 'Automate the Boring Stuff with Python',
                    'url': 'https://automatetheboringstuff.com/',
                    'type': 'book',
                    'description': 'Free online book teaching Python through practical automation tasks'
                },
                {
                    'title': 'Python Tutorial (Official)',
                    'url': 'https://docs.python.org/3/tutorial/',
                    'type': 'documentation',
                    'description': 'Official Python tutorial from python.org'
                }
            ]
        },
        # Level 2: Web Technologies
        {
            'learning_path': web_path,
            'slug': 'http-https-protocol',
            'title': 'HTTP/HTTPS Protocol',
            'description': 'Deep dive into HTTP methods, headers, cookies, and HTTPS encryption.',
            'difficulty': 'BEGINNER',
            'estimated_hours': 15,
            'order': 4,
            'prerequisites': ['networking-fundamentals'],
            'resources': ['OWASP Top 10', 'OWASP Cheat Sheet Series'],
            'tools': ['Burp Suite', 'OWASP ZAP'],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'HTTP Protocol Fundamentals',
                    'url': 'https://developer.mozilla.org/en-US/docs/Web/HTTP',
                    'type': 'documentation',
                    'description': 'MDN Web Docs comprehensive HTTP guide'
                },
                {
                    'title': 'HTTP: The Definitive Guide',
                    'url': 'https://www.oreilly.com/library/view/http-the-definitive/1565925092/',
                    'type': 'book',
                    'description': 'Comprehensive book covering HTTP in detail'
                },
                {
                    'title': 'How HTTPS Works (Comic)',
                    'url': 'https://howhttps.works/',
                    'type': 'article',
                    'description': 'Fun illustrated guide to understanding HTTPS'
                }
            ]
        },
        {
            'learning_path': web_path,
            'slug': 'html-css-javascript',
            'title': 'HTML/CSS/JavaScript',
            'description': 'Learn web development fundamentals to understand client-side vulnerabilities.',
            'difficulty': 'BEGINNER',
            'estimated_hours': 20,
            'order': 5,
            'prerequisites': ['programming-python'],
            'resources': [],
            'tools': [],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'freeCodeCamp Responsive Web Design',
                    'url': 'https://www.freecodecamp.org/learn/2022/responsive-web-design/',
                    'type': 'course',
                    'description': 'Free interactive HTML/CSS course with projects'
                },
                {
                    'title': 'JavaScript.info - The Modern JavaScript Tutorial',
                    'url': 'https://javascript.info/',
                    'type': 'tutorial',
                    'description': 'Comprehensive modern JavaScript guide from basics to advanced'
                },
                {
                    'title': 'MDN Web Development Tutorials',
                    'url': 'https://developer.mozilla.org/en-US/docs/Learn',
                    'type': 'documentation',
                    'description': 'Mozilla Developer Network web development learning resources'
                }
            ]
        },
        {
            'learning_path': web_path,
            'slug': 'sql-databases',
            'title': 'SQL Databases',
            'description': 'Understand database fundamentals and SQL queries for injection testing.',
            'difficulty': 'BEGINNER',
            'estimated_hours': 15,
            'order': 6,
            'prerequisites': ['programming-python'],
            'resources': [],
            'tools': ['SQLMap'],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'SQL Tutorial (W3Schools)',
                    'url': 'https://www.w3schools.com/sql/',
                    'type': 'tutorial',
                    'description': 'Interactive SQL tutorial with examples and exercises'
                },
                {
                    'title': 'SQLBolt - Learn SQL Interactively',
                    'url': 'https://sqlbolt.com/',
                    'type': 'tutorial',
                    'description': 'Interactive lessons and exercises for learning SQL'
                },
                {
                    'title': 'Database Design Basics',
                    'url': 'https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5',
                    'type': 'article',
                    'description': 'Microsoft guide to database fundamentals'
                }
            ]
        },
        # Level 3: Security Concepts
        {
            'learning_path': web_path,
            'slug': 'owasp-top-10',
            'title': 'OWASP Top 10',
            'description': 'Master the most critical web application security risks.',
            'difficulty': 'INTERMEDIATE',
            'estimated_hours': 20,
            'order': 7,
            'prerequisites': ['http-https-protocol', 'html-css-javascript', 'sql-databases'],
            'resources': ['OWASP Top 10', 'OWASP Testing Guide', 'PortSwigger Web Security Academy'],
            'tools': ['Burp Suite', 'OWASP ZAP'],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'OWASP Top 10 2021',
                    'url': 'https://owasp.org/www-project-top-ten/',
                    'type': 'documentation',
                    'description': 'Official OWASP Top 10 documentation with examples'
                },
                {
                    'title': 'PortSwigger Web Security Academy',
                    'url': 'https://portswigger.net/web-security',
                    'type': 'course',
                    'description': 'Free online training covering all OWASP Top 10 vulnerabilities with labs'
                },
                {
                    'title': 'OWASP Top 10 Learning Path (TryHackMe)',
                    'url': 'https://tryhackme.com/path/outline/owasp',
                    'type': 'course',
                    'description': 'Hands-on learning path with practical exercises'
                }
            ]
        },
        {
            'learning_path': web_path,
            'slug': 'burp-suite-basics',
            'title': 'Burp Suite Basics',
            'description': 'Learn to use Burp Suite for intercepting and manipulating HTTP traffic.',
            'difficulty': 'INTERMEDIATE',
            'estimated_hours': 15,
            'order': 8,
            'prerequisites': ['http-https-protocol', 'owasp-top-10'],
            'resources': ['PortSwigger Web Security Academy'],
            'tools': ['Burp Suite'],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'Burp Suite Official Documentation',
                    'url': 'https://portswigger.net/burp/documentation',
                    'type': 'documentation',
                    'description': 'Comprehensive official documentation for Burp Suite'
                },
                {
                    'title': 'Burp Suite Tutorial for Beginners',
                    'url': 'https://www.youtube.com/watch?v=G3hpAeoZ4ek',
                    'type': 'video',
                    'description': 'Video tutorial covering Burp Suite basics'
                },
                {
                    'title': 'Burp Suite Certified Practitioner',
                    'url': 'https://portswigger.net/web-security/certification',
                    'type': 'course',
                    'description': 'Free training materials for Burp Suite certification'
                }
            ]
        },
        {
            'learning_path': web_path,
            'slug': 'xss-csrf',
            'title': 'XSS & CSRF Attacks',
            'description': 'Understand and exploit cross-site scripting and cross-site request forgery vulnerabilities.',
            'difficulty': 'INTERMEDIATE',
            'estimated_hours': 15,
            'order': 9,
            'prerequisites': ['owasp-top-10', 'html-css-javascript'],
            'resources': ['OWASP Top 10', 'PortSwigger Web Security Academy'],
            'tools': ['Burp Suite', 'OWASP ZAP'],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'XSS Tutorial (PortSwigger)',
                    'url': 'https://portswigger.net/web-security/cross-site-scripting',
                    'type': 'tutorial',
                    'description': 'Comprehensive guide to XSS attacks with interactive labs'
                },
                {
                    'title': 'CSRF Tutorial (PortSwigger)',
                    'url': 'https://portswigger.net/web-security/csrf',
                    'type': 'tutorial',
                    'description': 'Complete guide to CSRF vulnerabilities and exploitation'
                },
                {
                    'title': 'XSS Game by Google',
                    'url': 'https://xss-game.appspot.com/',
                    'type': 'course',
                    'description': 'Hands-on XSS challenges from Google'
                }
            ]
        },
        # Level 4: Advanced Attacks
        {
            'learning_path': web_path,
            'slug': 'sql-injection',
            'title': 'SQL Injection',
            'description': 'Master SQL injection techniques including blind SQLi and advanced exploitation.',
            'difficulty': 'INTERMEDIATE',
            'estimated_hours': 20,
            'order': 10,
            'prerequisites': ['sql-databases', 'owasp-top-10'],
            'resources': ['OWASP Top 10', 'PortSwigger Web Security Academy'],
            'tools': ['SQLMap', 'Burp Suite'],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'SQL Injection (PortSwigger)',
                    'url': 'https://portswigger.net/web-security/sql-injection',
                    'type': 'tutorial',
                    'description': 'Complete SQL injection guide with labs from basic to advanced'
                },
                {
                    'title': 'SQL Injection Cheat Sheet',
                    'url': 'https://portswigger.net/web-security/sql-injection/cheat-sheet',
                    'type': 'documentation',
                    'description': 'Comprehensive SQLi payloads and techniques reference'
                },
                {
                    'title': 'SQLi Labs by Audi-1',
                    'url': 'https://github.com/Audi-1/sqli-labs',
                    'type': 'tutorial',
                    'description': 'Hands-on SQL injection practice environment'
                }
            ]
        },
        {
            'learning_path': web_path,
            'slug': 'auth-session-management',
            'title': 'Authentication & Session Management',
            'description': 'Learn to identify and exploit authentication and session management flaws.',
            'difficulty': 'INTERMEDIATE',
            'estimated_hours': 15,
            'order': 11,
            'prerequisites': ['http-https-protocol'],
            'resources': ['OWASP Top 10'],
            'tools': ['Burp Suite', 'John the Ripper'],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'Authentication Vulnerabilities (PortSwigger)',
                    'url': 'https://portswigger.net/web-security/authentication',
                    'type': 'tutorial',
                    'description': 'Guide to authentication bypass and exploitation'
                },
                {
                    'title': 'Session Management Cheat Sheet (OWASP)',
                    'url': 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html',
                    'type': 'documentation',
                    'description': 'Best practices and attack vectors for sessions'
                },
                {
                    'title': 'JWT Security Best Practices',
                    'url': 'https://curity.io/resources/learn/jwt-best-practices/',
                    'type': 'article',
                    'description': 'Understanding JWT vulnerabilities and secure implementation'
                }
            ]
        },
        {
            'learning_path': web_path,
            'slug': 'api-security',
            'title': 'API Security',
            'description': 'Test REST and GraphQL APIs for security vulnerabilities.',
            'difficulty': 'INTERMEDIATE',
            'estimated_hours': 15,
            'order': 12,
            'prerequisites': ['http-https-protocol', 'programming-python'],
            'resources': ['OWASP API Security Top 10'],
            'tools': ['Burp Suite', 'Postman'],
            'certifications': [],
            'learning_resources': [
                {
                    'title': 'OWASP API Security Top 10',
                    'url': 'https://owasp.org/www-project-api-security/',
                    'type': 'documentation',
                    'description': 'Official OWASP API security risks documentation'
                },
                {
                    'title': 'API Security Testing (PortSwigger)',
                    'url': 'https://portswigger.net/web-security/api-testing',
                    'type': 'tutorial',
                    'description': 'Practical guide to API security testing'
                },
                {
                    'title': 'REST API Security Essentials',
                    'url': 'https://restfulapi.net/security-essentials/',
                    'type': 'article',
                    'description': 'Essential REST API security concepts'
                }
            ]
        },
        # Level 5: Mastery
        {
            'learning_path': web_path,
            'slug': 'web-penetration-testing',
            'title': 'Web Penetration Testing',
            'description': 'Comprehensive web application penetration testing methodology and reporting.',
            'difficulty': 'ADVANCED',
            'estimated_hours': 40,
            'order': 13,
            'prerequisites': ['owasp-top-10', 'burp-suite-basics', 'xss-csrf', 'sql-injection', 'auth-session-management', 'api-security'],
            'resources': ['OWASP Testing Guide'],
            'tools': ['Burp Suite', 'OWASP ZAP', 'SQLMap', 'Nikto'],
            'certifications': ['Certified Ethical Hacker (CEH)', 'Offensive Security Certified Professional (OSCP)'],
            'learning_resources': [
                {
                    'title': 'OWASP Web Security Testing Guide',
                    'url': 'https://owasp.org/www-project-web-security-testing-guide/',
                    'type': 'documentation',
                    'description': 'Comprehensive methodology for web application security testing'
                },
                {
                    'title': 'The Web Application Hackers Handbook',
                    'url': 'https://www.amazon.com/Web-Application-Hackers-Handbook-Exploiting/dp/1118026470',
                    'type': 'book',
                    'description': 'Classic book on web application security testing (paid)'
                },
                {
                    'title': 'PentesterLab Web Challenges',
                    'url': 'https://pentesterlab.com/',
                    'type': 'course',
                    'description': 'Hands-on web pentesting exercises and vulnerable applications'
                },
                {
                    'title': 'HackTheBox Web Challenges',
                    'url': 'https://www.hackthebox.com/',
                    'type': 'course',
                    'description': 'Real-world web application pentesting challenges'
                }
            ]
        },
    ]

    # Create skill nodes
    node_objects = {}  # Store created nodes for linking prerequisites
    for node_data in skill_nodes_data:
        prereq_slugs = node_data['prerequisites']
        resource_names = node_data['resources']
        tool_names = node_data['tools']
        cert_names = node_data['certifications']
        learning_resources = node_data.get('learning_resources', [])

        # Create node with basic fields
        node_defaults = {
            'title': node_data['title'],
            'description': node_data['description'],
            'difficulty': node_data['difficulty'],
            'estimated_hours': node_data['estimated_hours'],
            'order': node_data['order'],
            'learning_resources': learning_resources,
        }

        node, created = SkillNode.objects.get_or_create(
            learning_path=node_data['learning_path'],
            slug=node_data['slug'],
            defaults=node_defaults
        )
        if created:
            print(f"    Created skill: {node.title}")
        else:
            # Update existing node with learning_resources if it doesn't have them
            if not node.learning_resources:
                node.learning_resources = learning_resources
                node.save()

        node_objects[node_data['slug']] = node

        # Link resources
        for resource_name in resource_names:
            try:
                resource = Resource.objects.get(title=resource_name)
                node.resources.add(resource)
            except Resource.DoesNotExist:
                pass

        # Link tools
        for tool_name in tool_names:
            try:
                tool = Tool.objects.get(name=tool_name)
                node.tools.add(tool)
            except Tool.DoesNotExist:
                pass

        # Link certifications
        for cert_name in cert_names:
            try:
                cert = Certification.objects.get(name=cert_name)
                node.certifications.add(cert)
            except Certification.DoesNotExist:
                pass

    # Now link prerequisites
    for node_data in skill_nodes_data:
        node = node_objects[node_data['slug']]
        for prereq_slug in node_data['prerequisites']:
            if prereq_slug in node_objects:
                prereq_node = node_objects[prereq_slug]
                node.prerequisites.add(prereq_node)

    print(f"✓ Learning paths seeded ({LearningPath.objects.count()} paths, {SkillNode.objects.count()} skills)\n")


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
        seed_learning_paths()

        print("="*50)
        print("✓ ALL DATA SEEDED SUCCESSFULLY!")
        print("="*50 + "\n")

    except Exception as e:
        print(f"\n✗ Error during seeding: {str(e)}\n")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
