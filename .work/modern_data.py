"""Confirmed additions from the user's questionnaire and public LinkedIn profile."""
from localize_resume import TRANSLATIONS
import html

def tr(en, pt):
    TRANSLATIONS[en] = pt
    return en

TITLE = tr('Senior Cybersecurity Consultant | Identity & Access Security | Microsoft Security', 'Consultor Sênior de Cibersegurança | Identity & Access Security | Microsoft Security')
INTRO = tr('I connect identity and access security with cloud architecture and data protection. My background spans IT infrastructure, security operations and consulting, with hands-on work in Microsoft Entra ID, authentication and identity governance. I translate business requirements into security controls aligned with Zero Trust.', 'Conecto segurança de identidades e acessos à arquitetura de nuvem e à proteção de dados. Minha trajetória reúne infraestrutura de TI, operações de segurança e consultoria, com atuação prática em Microsoft Entra ID, autenticação e governança de identidades. Traduzo requisitos de negócio em controles de segurança alinhados a Zero Trust.')
OBJECTIVE = tr('I am pursuing architect or specialist opportunities in Identity & Access Security. I bring experience in Microsoft Entra ID, Conditional Access, multifactor authentication and identity governance, supported by a background in infrastructure, cloud security and Microsoft Purview. My focus is to design access controls that support business needs and protect sensitive data.', 'Busco oportunidades como arquiteto ou especialista em Identity & Access Security. Reúno experiência em Microsoft Entra ID, Acesso Condicional, autenticação multifator e governança de identidades, apoiada pela trajetória em infraestrutura, segurança em nuvem e Microsoft Purview. Meu foco é desenvolver controles de acesso que atendam ao negócio e protejam dados sensíveis.')
META_TITLE = tr('Ewerton Gomes de Lucena | Identity & Access Security', 'Ewerton Gomes de Lucena | Segurança de Identidades e Acessos')
META_DESCRIPTION = tr('Senior cybersecurity consultant focused on Identity & Access Security, Microsoft Entra ID and Zero Trust, with experience in cloud architecture and data protection.', 'Consultor sênior de cibersegurança com foco em Identity & Access Security, Microsoft Entra ID e Zero Trust, com experiência em arquitetura de nuvem e proteção de dados.')

for en, pt in {
    'Projects':'Projetos', 'Key Projects & Achievements':'Projetos e Realizações',
    'Explore by specialization':'Explore por especialização', 'Identity & Access Security':'Identity & Access Security',
    'Cloud & Data Security':'Cloud & Data Security', 'Career at a glance':'Trajetória em números',
    'IT experience':'Experiência em TI', 'Cybersecurity experience':'Experiência em cibersegurança',
    'Current Identity Security role':'Atuação atual em Identity Security',
    'Professional certifications recorded':'Certificações profissionais registradas', 'Projects presented':'Projetos apresentados',
    'Since August 2014':'Desde agosto de 2014', 'Since June 2022':'Desde junho de 2022',
    'Since March 2026; earlier IAM periods are not quantified':'Desde março de 2026; períodos anteriores em IAM não quantificados',
    'Issued credentials; current validity is not assumed':'Credenciais emitidas; validade atual não presumida',
    'Based on recorded month/year dates; overlapping periods are counted once.':'Com base nas datas registradas em mês/ano; períodos simultâneos são contados uma vez.',
    'View experience':'Ver experiência', 'View projects':'Ver projetos',
    'From infrastructure and security operations to consulting and identity architecture.':'Da infraestrutura e das operações de segurança à consultoria e à arquitetura de identidades.',
    'Relevant to this focus':'Relacionado a este foco', 'Role progression: L1 → L2':'Progressão de cargo: N1 → N2',
    'Hands-on experience':'Experiência prática', 'Studies; no production experience reported':'Estudos; sem experiência em produção informada',
    'Identity governance':'Governança de identidades', 'Access reviews':'Revisões de acesso',
    'User lifecycle':'Ciclo de vida de usuários', 'Privileged Identity Management (PIM)':'Privileged Identity Management (PIM)',
    'Conditional Access':'Acesso Condicional', 'Multifactor authentication (MFA)':'Autenticação multifator (MFA)',
    'Entitlement Management':'Gerenciamento de Direitos', 'Lifecycle Workflows':'Fluxos de Trabalho do Ciclo de Vida',
    'Cloud Security':'Segurança em Nuvem', 'Data Security':'Segurança de Dados',
    'Data Loss Prevention (DLP)':'Prevenção de Perda de Dados (DLP)', 'Sensitivity labels':'Rótulos de sensibilidade',
    'Context & challenge':'Contexto e desafio', 'My contribution':'Minha contribuição',
    'Implementation':'Implementação', 'Documented outcome':'Resultado documentado',
    'Advisory contribution':'Contribuição consultiva', 'Data Security Maturity':'Data Security Maturity',
    'User Lifecycle':'Ciclo de Vida de Usuários', 'Identity & data governance':'Governança de identidades e dados',
    'Professional certifications':'Certificações profissionais', 'Courses & learning badges':'Cursos e badges de aprendizagem',
    'Workshops & training':'Workshops e treinamentos', 'Credential category':'Categoria da credencial',
    'All categories':'Todas as categorias', 'Credential ID':'Identificador da credencial', 'Credential ID:':'Identificador da credencial:',
    'Recorded on LinkedIn ↗':'Registro no LinkedIn ↗', 'Official certification details ↗':'Informações oficiais da certificação ↗',
    'Expired January 2024':'Expirada em janeiro de 2024', 'Expired December 2022':'Expirada em dezembro de 2022',
    'Learning badge':'Badge de aprendizagem', 'Training issued by Clavis Academy':'Treinamento emitido pela Clavis Academy',
    'Identity. Cloud. Data.':'Identidade. Nuvem. Dados.', 'Additional expertise':'Competências complementares',
    'Certification history is separate from courses and learning badges. Official program links describe the certification; they do not verify individual issuance or renewal.':'O histórico de certificações está separado de cursos e badges. Links dos programas oficiais descrevem a certificação; não comprovam emissão individual nem renovação.',
    'Introduction to Cybersecurity':'Introdução à Cibersegurança',
    'Protecting Non-Human Identities':'Proteção de Identidades Não Humanas',
    '2025 — 2027 · Program period listed on LinkedIn':'2025 — 2027 · Período do curso informado no LinkedIn',
    'Security operations and incident response. Progressed from L1 to L2 within Clavis.':'Operações de segurança e resposta a incidentes. Evoluí de N1 para N2 na Clavis.',
    'Infrastructure support for academic and call-center environments.':'Suporte à infraestrutura de ambientes acadêmicos e call centers.',
    'IT infrastructure, service support and team supervision.':'Infraestrutura de TI, suporte a serviços e supervisão de equipe.',
    'Technical support for academic users and computer labs.':'Suporte técnico a usuários acadêmicos e laboratórios de informática.',
    'Helpdesk and first-line infrastructure support.':'Helpdesk e suporte inicial à infraestrutura.',
    'Design cloud, identity and data protection controls in the Microsoft ecosystem.':'Desenvolvo controles de nuvem, identidade e proteção de dados no ecossistema Microsoft.',
    'Data protection, security posture and governance across Microsoft 365 and cloud services.':'Proteção de dados, postura de segurança e governança no Microsoft 365 e em serviços de nuvem.',
}.items(): tr(en, pt)

PROJECTS = [
    dict(id='lifecycle', focus='identity', title='User Lifecycle', context='ZAMP', label='Advisory contribution', fields=[
        ('Context & challenge', tr('The lack of a defined user lifecycle affected the rollout of confidentiality labels in the Data Security Maturity initiative.', 'A ausência de um ciclo de vida definido para os usuários afetava a implantação de rótulos de confidencialidade no projeto Data Security Maturity.')),
        ('My contribution', tr('Provided the Identity Management team with insights on user lifecycle requirements and their relationship to data governance.', 'Levei à equipe de Gestão de Identidade insights sobre requisitos do ciclo de vida dos usuários e sua relação com a governança dos dados.')),
    ], technologies=['User lifecycle', 'Identity & data governance', 'draw.io']),
    dict(id='data-maturity', focus='cloud-data', title='Data Security Maturity', context='ZAMP', label='Data Security', fields=[
        ('Context & challenge', tr('A phased security maturity program was needed in an environment with limited visibility of users across different management areas.', 'O ambiente precisava de um programa de maturidade em segurança por fases, com baixa visibilidade dos usuários distribuídos entre diferentes gerências.')),
        ('My contribution', tr('Conducted proofs of concept and studied organizational processes, departments and data governance requirements as the analyst dedicated to the initiative.', 'Conduzi provas de conceito e estudos dos processos organizacionais, departamentos e requisitos de governança de dados como analista dedicado à iniciativa.')),
        ('Implementation', tr('Implemented Microsoft Information Protection and Purview DSPM reporting, alongside license management and an on-premises AdminDroid deployment.', 'Implementei Microsoft Information Protection e relatórios do Purview DSPM, com gestão de licenças e implantação local do AdminDroid.')),
        ('Documented outcome', tr('Started data labeling and policy adoption for Marketing, Communications, Product Quality, Information Security and IT departments.', 'Iniciei a rotulagem de dados e a aplicação de políticas nas áreas de Marketing, Comunicação, Qualidade de Produto, Segurança da Informação e Tecnologia da Informação.')),
    ], technologies=['Microsoft Purview', 'Information Protection', 'DSPM', 'AdminDroid', 'draw.io']),
]

GROUPS = [
    ('identity', 'Identity & Access Security', ['Microsoft Entra ID', 'Identity & Access Management (IAM)', 'Conditional Access', 'Multifactor authentication (MFA)', 'Privileged Identity Management (PIM)', 'Access reviews', 'Entitlement Management', 'Lifecycle Workflows', 'Identity governance', 'Zero Trust', 'Active Directory']),
    ('cloud', 'Cloud Security', ['Microsoft Azure', 'Microsoft 365', 'AWS', 'Cloud Security Architecture & Strategy', 'Cloud Security Posture & Vulnerability Management', 'Security Monitoring & Incident Response', 'Microsoft Sentinel', 'Ansible', 'Terraform']),
    ('data', 'Data Security', ['Microsoft Purview', 'Data Loss Prevention (DLP)', 'Data Security Posture Management (DSPM)', 'Cloud Access Security Broker (CASB)', 'Information Protection', 'Sensitivity labels', 'Security Governance, Risk & Compliance', 'AI & Data Protection']),
]

def enrich_jobs(jobs):
    dates=[('2026-03',None),('2024-09','2026-03'),('2023-11','2024-09'),('2022-06','2023-11'),('2021-04','2022-06'),('2015-09','2021-04'),('2015-08','2015-09'),('2014-08','2015-08')]
    summaries=['Design cloud, identity and data protection controls in the Microsoft ecosystem.', 'Data protection, security posture and governance across Microsoft 365 and cloud services.', 'Security operations and incident response. Progressed from L1 to L2 within Clavis.', 'Provided cybersecurity consulting and developed security plans.', 'IT infrastructure, service support and team supervision.', 'Infrastructure support for academic and call-center environments.', 'Technical support for academic users and computer labs.', 'Helpdesk and first-line infrastructure support.']
    technologies=[['Microsoft Entra ID','Conditional Access','MFA','Identity Governance','Microsoft Purview','Microsoft 365'],['Microsoft Purview','DSPM','DLP','Netskope','Microsoft 365','Azure'],[],['Sentinel','Entra ID','Active Directory','AD FS','Azure WAF','Ansible','Terraform'],['Azure','AWS','Windows Server','Kaspersky EDR','PowerShell'],['Active Directory','Azure','Windows Server','Cisco','Fortinet'],[],[]]
    for i, job in enumerate(jobs):
        job.update(start=dates[i][0],end=dates[i][1],summary=summaries[i],technologies=technologies[i],focus=['identity','cloud-data'] if i in (0,3,5) else ['cloud-data'],cybersecurity=i<4,identity=i==0)
    jobs[1]['outcome']=PROJECTS[1]['fields'][-1][1]
    return jobs

LINKEDIN='https://www.linkedin.com/in/ewertonlucena/'
def enrich_certificates(original):
    certs=[]
    for title, provider, date in original:
        category='professional' if 'Microsoft Certified:' in title or title.startswith(('NCCSA','NSE 3')) else 'workshop' if provider=='IAM Tech Day' or 'Workshop' in title else 'course'
        certs.append(dict(title=title,provider=provider,date=date,category=category,focus='identity' if any(x in title for x in ('Entra','Identity','Zero Trust','SC-900')) else 'cloud-data'))
    certs.extend([
        dict(title='Protecting Non-Human Identities',provider='Okta',date='',category='course',focus='identity',note='Learning badge',source=LINKEDIN),
        dict(title='Introduction to Cybersecurity',provider='Cisco',date='December 2021',category='course',focus='cloud-data',source=LINKEDIN),
        dict(title='Scrum Foundation Professional Certificate (SFPC)',provider='CertiProf',date='July 2020',category='professional',focus='general',credential_id='TLSZHZSGHH-MHWMRTST-RPFLHLKHPS',source=LINKEDIN),
        dict(title='NSE 1 Network Security Associate',provider='Fortinet',date='December 2020',category='professional',focus='cloud-data',credential_id='3SbZyta6gl',note='Expired December 2022',source=LINKEDIN),
        dict(title='NSE 2 Network Security Associate',provider='Fortinet',date='December 2020',category='professional',focus='cloud-data',credential_id='Y21L3VDppu',note='Expired December 2022',source=LINKEDIN),
    ])
    metadata={
        'SC-401':dict(official='https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-401/'),
        'SC-200':dict(official='https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/'),
        'SC-900':dict(official='https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/'),
        'AI-900':dict(official='https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/'),
        'Kibana Fundamentals':dict(credential_id='C77710',source=LINKEDIN),
        'Understanding Zero Trust':dict(credential_id='AXou4TE4DniTSJXJyCSTfwZY1y4S',source=LINKEDIN),
        'NSE 3':dict(credential_id='kxr2YS6aaU',note='Expired January 2024',source=LINKEDIN),
        '[C] CompTIA':dict(note='Training issued by Clavis Academy'),
        'Foundations of Operationalizing':dict(source=LINKEDIN),
        'Cybersecurity Essentials':dict(source=LINKEDIN),
        'Introduction to LGPD':dict(source=LINKEDIN),
    }
    for cert in certs:
        for key, values in metadata.items():
            if key in cert['title']: cert.update(values)
    return certs

e=html.escape
def projects_html():
    result=[]
    for project in PROJECTS:
        fields=''.join(f'<div><dt>{e(label)}</dt><dd>{e(text)}</dd></div>' for label,text in project['fields'])
        tags=''.join(f'<li>{e(tag)}</li>' for tag in project['technologies'])
        result.append(f'<article class="project-card" data-focus="{project["focus"]}"><p class="project-kicker">{e(project["context"])} / <span>{e(project["label"])}</span></p><h3>{e(project["title"])}</h3><dl>{fields}</dl><ul class="project-tags" aria-label="Technology focus">{tags}</ul></article>')
    return ''.join(result)

def groups_html():
    result=[]
    for key,title,skills in GROUPS:
        tags=''.join(f'<li>{e(skill)}</li>' for skill in skills)
        studies='<div class="study-note"><p>Studies; no production experience reported</p><ul class="project-tags"><li>Okta</li><li>CyberArk</li><li>SailPoint</li></ul></div>' if key=='identity' else ''
        result.append(f'<article class="skill-group" id="group-{key}" data-skill-group="{key}"><h3>{e(title)}</h3><p class="small-note">Hands-on experience</p><ul class="skill-tags">{tags}</ul>{studies}</article>')
    return ''.join(result)

def certificates_html(certs):
    result=[]
    labels={'professional':'Professional certifications','course':'Courses & learning badges','workshop':'Workshops & training'}
    for category,label in labels.items():
        items=[]
        for cert in certs:
            if cert['category']!=category: continue
            date=f' / <span>{e(cert["date"])}</span>' if cert['date'] else ''
            note=f'<p class="cert-note">{e(cert["note"])}</p>' if cert.get('note') else ''
            cid=f'<p class="credential-id">Credential ID: <span>{e(cert["credential_id"])}</span></p>' if cert.get('credential_id') else ''
            links=''.join(f'<a href="{e(cert[key])}" target="_blank" rel="noopener noreferrer">{text}</a>' for key,text in [('official','Official certification details ↗'),('source','Recorded on LinkedIn ↗')] if cert.get(key))
            items.append(f'<li class="certificate" data-provider="{e(cert["provider"])}" data-category="{category}" data-focus="{cert["focus"]}"><span class="cert-icon" aria-hidden="true">◇</span><div><h3>{e(cert["title"])}</h3><p>{e(cert["provider"])}{date}</p>{note}{cid}<div class="cert-links">{links}</div></div></li>')
        result.append(f'<div class="credential-category" data-category="{category}"><h3 class="category-heading">{label}</h3><ul class="certificate-list">{"".join(items)}</ul></div>')
    return ''.join(result)
