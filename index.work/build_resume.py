from pathlib import Path
import html, json, base64
from localize_resume import localize, TRANSLATIONS

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / '.work'
WORK.mkdir(exist_ok=True)

jobs = [
    dict(title='Senior Security Consultant', company='Avanade', assignment='Microsoft · Cloud Security Architect (Contractor)', dates='March 2026 — Present', current=True, bullets=[
        'Architect and implement cloud security, identity, data protection, and compliance solutions within the Microsoft ecosystem.',
        'Work with Microsoft Entra on Identity and Access Management (IAM), Conditional Access, multifactor authentication (MFA), Identity Governance, and identity protection, aligned with Zero Trust principles.',
        'Implement and enhance Microsoft Purview solutions, including Data Security Posture Management (DSPM), DSPM for AI, Information Protection, and Data Loss Prevention (DLP).',
        'Define strategies for classifying, labeling, protecting, and governing sensitive data in Microsoft 365, cloud applications, and AI workloads.',
        'Support enterprise clients in identifying and reducing risks related to data, identities, access, and AI use.',
        'Translate technical, regulatory, and business requirements into scalable security architectures aligned with Microsoft best practices.',
        'Advise clients on adopting security controls, compliance measures, and secure digital transformation.'
    ]),
    dict(title='Information Security Analyst II', company='ZAMP', dates='September 2024 — March 2026', bullets=[
        'Defined, implemented, and enhanced security controls to protect sensitive data, enterprise environments, and AI solutions.',
        'Worked on risk management, regulatory compliance, Brazil’s General Data Protection Law (LGPD), and security throughout the Artificial Intelligence lifecycle.',
        'Applied Security by Design principles, including threat modeling, risk assessments, and security requirements definition.',
        'Implemented and administered DSPM, Cloud Access Security Broker (CASB), and Data Loss Prevention solutions.',
        'Managed information classification and protection, tokenization, and data masking.',
        'Continuously monitored security posture across Microsoft 365, Azure, and SaaS applications.',
        'Used Microsoft Purview and Netskope to strengthen governance, compliance, and data protection.',
        'Collaborated with engineering, data science, and architecture teams on strategic initiatives and audits.'
    ]),
    dict(title='Security Operations Analyst L2', company='Clavis Segurança da Informação', dates='November 2023 — September 2024', bullets=[]),
    dict(title='Information Security Operations Analyst L1', company='Clavis Segurança da Informação', dates='June 2022 — November 2023', bullets=[
        'Provided cybersecurity consulting and developed security plans.',
        'Monitored security events and responded to incidents.',
        'Developed security reports and action plans aligned with CIS, NIST, CISA, and ISO 27k.',
        'Managed vulnerabilities and applied security best practices in Microsoft Azure.',
        'Managed assets and secured on-premises devices, including firewalls, Active Directory, AD FS, and WAF.',
        'Worked with Microsoft Azure technologies, including Sentinel, Entra ID, and Azure WAF.',
        'Used Infrastructure as Code tools, including Ansible and Terraform, for infrastructure and cloud security.'
    ]),
    dict(title='Infrastructure Analyst — Supervisor I', company='Universidade Veiga de Almeida', dates='April 2021 — June 2022', bullets=[
        'Supervised the helpdesk team.',
        'Administered cloud and on-premises servers with Windows Server 2008, 2012, and 2016 across Azure and AWS.',
        'Administered Kaspersky Endpoint Detection and Response (EDR), including reports, tasks, and incident response.',
        'Used shell scripting with PowerShell, Cisco CLI, and Unix.'
    ]),
    dict(title='IT Technician', company='Ilumno', dates='September 2015 — April 2021', bullets=[
        'Supported IT infrastructure and provided management and technical support for the call centers of UVA and Unijorge universities.',
        'Worked with Azure Cloud and administered Active Directory and Windows Server 2008, 2012, and 2016.',
        'Supported Cisco local area networks (LAN) and Fortinet solutions: FortiGate, FortiAP, and FortiAnalyzer.'
    ]),
    dict(title='Computer Lab Technician', company='Universidade Veiga de Almeida', dates='August 2015 — September 2015', bullets=[
        'Supported and advised the academic community on information technology matters.',
        'Performed scheduled maintenance and occasional computer repairs.'
    ]),
    dict(title='IT Infrastructure Intern', company='Universidade Veiga de Almeida', dates='August 2014 — August 2015', bullets=[
        'Provided helpdesk services and Level 1 support.'
    ])
]
education = [
    ('Postgraduate Program in Cybersecurity for Business in the Digital Era', 'FIA Business School', '2027'),
    ('Extension Course: AI LAB I', 'PUC-RIO', '2025'),
    ("Bachelor’s Degree in Computer Science", 'Universidade Cruzeiro do Sul', '2023'),
    ('Cloud Computing Architect Bootcamp', 'IGTI (XP Educação)', '2021'),
    ('Technical Diploma in Computer Networking', 'Senai, Firjan RJ', '2016')
]
skills = [
    'Cloud Security Architecture & Strategy', 'Benchmarks & NIST Cybersecurity Framework',
    'Identity & Access Security (IAM)', 'Data Security & Microsoft Purview',
    'Data Security Posture Management (DSPM)', 'Cloud Security Posture & Vulnerability Management',
    'Security Governance, Risk & Compliance', 'Network & Cloud Infrastructure Security',
    'Security Monitoring & Incident Response', 'AI & Data Protection',
    'Security Advisory & Stakeholder Management', 'Continuous Learning & Technical Leadership'
]
certificates = [
    ('Microsoft Azure Security Technologies: Microsoft Entra', 'Skillsoft', 'August 2026'),
    ('Sell with confidence: Position Microsoft Purview to Secure customer data in the age of AI — Proficient', 'Microsoft', 'August 2026'),
    ('Microsoft Certified: Information Security Administrator Associate (SC-401)', 'Microsoft', 'March 2026'),
    ('Implement, Govern and Scale Data Security with Microsoft Purview in the era of AI — Skilled', 'Microsoft', 'March 2026'),
    ('NCCSA — Netskope One Administrator', 'Netskope', 'October 2025'),
    ('Microsoft Security Immersion Workshop: On The Brink', 'Microsoft', 'September 2024'),
    ('Navigating Threats: Advanced Strategies in Threat Modeling', 'Udemy', 'June 2024'),
    ('Microsoft Certified: Azure AI Fundamentals (AI-900)', 'Microsoft', 'June 2024'),
    ('SoD — Segregation of Duties', 'IAM Tech Day', 'January 2024'),
    ('[C] CompTIA Security+ 601', 'Clavis Academy', 'January 2024'),
    ('Cloud Security Course', 'SegInfoBrasil', 'September 2023'),
    ('Identity and Access Governance', 'IAM Tech Day', 'September 2023'),
    ('Microsoft Certified: Security Operations Analyst Associate (SC-200)', 'Microsoft', 'February 2023'),
    ('Cybersecurity', 'FIAP', 'January 2023'),
    ('Microsoft Certified: Security, Compliance, and Identity Fundamentals (SC-900)', 'Microsoft', 'November 2022'),
    ('Network Forensics', 'Clavis Academy', 'September 2022'),
    ('Foundations of Operationalizing MITRE ATT&CK', 'AttackIQ', 'September 2022'),
    ('Kibana Fundamentals', 'Elastic', 'June 2022'),
    ('Understanding Zero Trust', 'LinkedIn', 'June 2022'),
    ('NSE 3 Network Security Associate', 'Fortinet', 'January 2022'),
    ('Cybersecurity Essentials', 'Cisco', 'December 2021'),
    ('Introduction to LGPD', 'Protegon', 'July 2021')
]
e = html.escape

def job_html(job, i):
    bullets = ''.join(f'<li>{e(b)}</li>' for b in job['bullets'])
    detail = f'<details open class="responsibilities"><summary>Responsibilities <span class="disclosure-icon" aria-hidden="true">−</span></summary><ul>{bullets}</ul></details>' if bullets else ''
    assignment = f'<p class="assignment">{e(job["assignment"])}</p>' if job.get('assignment') else ''
    current = '<span class="current-label">Current role</span>' if job.get('current') else ''
    return f'''<article class="job {'job-current' if job.get('current') else ''}">
      <div class="job-header"><div><p class="company">{e(job['company'])} {current}</p><h3>{e(job['title'])}</h3>{assignment}</div><p class="dates">{e(job['dates'])}</p></div>{detail}
    </article>'''

education_html = ''.join(f'<article class="education-item"><div><h3>{e(title)}</h3><p>{e(school)}</p></div><span class="year">{year}</span></article>' for title, school, year in education)
skills_html = ''.join(f'<li>{e(s)}</li>' for s in skills)
certs_html = ''.join(f'<li class="certificate" data-provider="{e(provider)}"><span class="cert-icon" aria-hidden="true">◇</span><div><h3>{e(title)}</h3><p>{e(provider)} <span aria-hidden="true">/</span> <span>{date}</span></p></div></li>' for title, provider, date in certificates)

template = (ROOT / '.work' / 'resume-template.html').read_text(encoding='utf-8')
portrait=Path('C:/Users/ewert/OneDrive/backup/a_clean_cutout_portrait_on_a_transparent_backgroun.png').read_bytes()
photo='data:image/png;base64,'+base64.b64encode(portrait).decode('ascii')
for key, value in {'PHOTO':photo,'TRANSLATIONS':json.dumps(TRANSLATIONS,ensure_ascii=False).replace('</','<\\/'),'JOBS':''.join(job_html(j,i) for i,j in enumerate(jobs)), 'EDUCATION':education_html, 'SKILLS':skills_html, 'CERTIFICATES':certs_html}.items():
    template = template.replace('@@'+key+'@@', value)

# Fonts remain local platform fonts: no third-party request is needed to open this file.
# Bahnschrift and Trebuchet MS are available on Windows; explicit fallbacks keep the file portable.
destination = ROOT / '[EN] CV - Ewerton Gomes de Lucena 2026 - Interactive.html'
destination.write_text(localize(template,'en-US'), encoding='utf-8')
bilingual=ROOT / 'CV - Ewerton Gomes de Lucena 2026 - PT-BR EN-US.html'
bilingual.write_text(localize(template,'pt-BR'), encoding='utf-8')
(WORK / 'resume-content.json').write_text(json.dumps({'jobs':jobs, 'education':education, 'skills':skills, 'certificates':certificates}, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'html':str(bilingual),'english_html':str(destination), 'bytes':bilingual.stat().st_size, 'jobs':len(jobs),'education':len(education),'skills':len(skills),'certificates':len(certificates)}))
