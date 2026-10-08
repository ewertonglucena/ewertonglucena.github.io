from html.parser import HTMLParser
import html

TRANSLATIONS = {
    'Ewerton Gomes de Lucena | Cybersecurity & Microsoft Security': 'Ewerton Gomes de Lucena | Cibersegurança e Microsoft Security',
    'Ewerton Gomes de Lucena — Cybersecurity Consultant, Microsoft Security. Cloud security architecture, identity, data protection, and AI security.': 'Ewerton Gomes de Lucena — Consultor de Cibersegurança, Microsoft Security. Arquitetura de segurança em nuvem, identidade, proteção de dados e segurança de IA.',
    'Skip to resume content': 'Ir para o conteúdo do currículo',
    'Ewerton Lucena, back to top': 'Ewerton Lucena, voltar ao início',
    'CYBERSECURITY / CV 2026': 'CIBERSEGURANÇA / CV 2026',
    'Resume sections': 'Seções do currículo',
    'Resume language': 'Idioma do currículo',
    'Profile': 'Perfil', 'Experience': 'Experiência', 'Education': 'Formação',
    'Expertise': 'Competências', 'Credentials': 'Certificados',
    'Switch to light theme': 'Ativar tema claro', 'Switch to dark theme': 'Ativar tema escuro',
    'Print or save the full resume as PDF': 'Imprimir ou salvar o currículo completo como PDF',
    'Print / PDF': 'Imprimir / PDF', 'Print or save resume as PDF': 'Imprimir ou salvar currículo como PDF',
    'Cloud. Identity. Data.': 'Nuvem. Identidade. Dados.',
    'Cybersecurity Consultant': 'Consultor de Cibersegurança',
    'Specialist in cyber defense technologies, with a focus on cloud security architecture, identity, and data protection.': 'Especialista em tecnologias de defesa cibernética, com foco em arquitetura de segurança em nuvem, identidade e proteção de dados.',
    'Areas of focus': 'Áreas de atuação',
    'DATA & AI PROTECTION': 'PROTEÇÃO DE DADOS E IA',
    'Contact details': 'Informações de contato',
    'Portrait of Ewerton Gomes de Lucena': 'Foto de Ewerton Gomes de Lucena',
    'IDENTITY': 'IDENTIDADE', 'CLOUD': 'NUVEM', 'DATA': 'DADOS',
    'SECURITY BY DESIGN': 'SECURITY BY DESIGN',
    'Career Objective': 'Objetivo Profissional',
    'Cybersecurity consultant focused on': 'Consultor de cibersegurança com foco em',
    'cloud security, identity, and data protection': 'segurança em nuvem, identidade e proteção de dados',
    'in the Microsoft ecosystem. My objective is to help organizations translate business and regulatory requirements into scalable security architectures, strengthen Zero Trust adoption, and protect sensitive data and AI workloads.': 'no ecossistema Microsoft. Meu objetivo é ajudar organizações a traduzir requisitos de negócio e regulatórios em arquiteturas de segurança escaláveis, fortalecer a adoção de Zero Trust e proteger dados sensíveis e cargas de trabalho de IA.',
    'Work Experience': 'Experiência Profissional', '2014 — PRESENT': '2014 — ATUAL',
    'From IT infrastructure to cloud and data security.': 'Da infraestrutura de TI à segurança em nuvem e à proteção de dados.',
    'Collapse responsibilities': 'Recolher responsabilidades', 'Expand responsibilities': 'Expandir responsabilidades',
    'Responsibilities': 'Responsabilidades', 'Current role': 'Cargo atual',
    'Senior Security Consultant': 'Consultor de Segurança Sênior',
    'Microsoft · Cloud Security Architect (Contractor)': 'Microsoft · Arquiteto de Segurança em Nuvem (Terceirizado)',
    'March 2026 — Present': 'Março de 2026 — Atual',
    'Architect and implement cloud security, identity, data protection, and compliance solutions within the Microsoft ecosystem.': 'Desenvolvo arquiteturas e implemento soluções de segurança em nuvem, identidade, proteção de dados e conformidade no ecossistema Microsoft.',
    'Work with Microsoft Entra on Identity and Access Management (IAM), Conditional Access, multifactor authentication (MFA), Identity Governance, and identity protection, aligned with Zero Trust principles.': 'Atuo com Microsoft Entra em gestão de identidades e acessos (IAM), Acesso Condicional, autenticação multifator (MFA), governança e proteção de identidades, em alinhamento com os princípios de Zero Trust.',
    'Implement and enhance Microsoft Purview solutions, including Data Security Posture Management (DSPM), DSPM for AI, Information Protection, and Data Loss Prevention (DLP).': 'Implemento e aprimoro soluções Microsoft Purview, incluindo gestão da postura de segurança de dados (DSPM), DSPM for AI, Information Protection e prevenção de perda de dados (DLP).',
    'Define strategies for classifying, labeling, protecting, and governing sensitive data in Microsoft 365, cloud applications, and AI workloads.': 'Defino estratégias de classificação, rotulagem, proteção e governança de dados sensíveis no Microsoft 365, em aplicações em nuvem e em cargas de trabalho de IA.',
    'Support enterprise clients in identifying and reducing risks related to data, identities, access, and AI use.': 'Apoio clientes corporativos na identificação e redução de riscos relacionados a dados, identidades, acessos e uso de IA.',
    'Translate technical, regulatory, and business requirements into scalable security architectures aligned with Microsoft best practices.': 'Traduzo requisitos técnicos, regulatórios e de negócio em arquiteturas de segurança escaláveis, alinhadas às melhores práticas Microsoft.',
    'Advise clients on adopting security controls, compliance measures, and secure digital transformation.': 'Oriento clientes na adoção de controles de segurança, medidas de conformidade e transformação digital segura.',
    'Information Security Analyst II': 'Analista de Segurança da Informação II',
    'September 2024 — March 2026': 'Setembro de 2024 — Março de 2026',
    'Defined, implemented, and enhanced security controls to protect sensitive data, enterprise environments, and AI solutions.': 'Defini, implementei e aprimorei controles de segurança para proteger dados sensíveis, ambientes corporativos e soluções de IA.',
    'Worked on risk management, regulatory compliance, Brazil’s General Data Protection Law (LGPD), and security throughout the Artificial Intelligence lifecycle.': 'Atuei com gestão de riscos, conformidade regulatória, Lei Geral de Proteção de Dados (LGPD) e segurança ao longo do ciclo de vida da inteligência artificial.',
    'Applied Security by Design principles, including threat modeling, risk assessments, and security requirements definition.': 'Apliquei princípios de Security by Design, incluindo modelagem de ameaças, avaliações de risco e definição de requisitos de segurança.',
    'Implemented and administered DSPM, Cloud Access Security Broker (CASB), and Data Loss Prevention solutions.': 'Implementei e administrei soluções de DSPM, Cloud Access Security Broker (CASB) e prevenção de perda de dados.',
    'Managed information classification and protection, tokenization, and data masking.': 'Gerenciei a classificação e proteção da informação, a tokenização e o mascaramento de dados.',
    'Continuously monitored security posture across Microsoft 365, Azure, and SaaS applications.': 'Monitorei continuamente a postura de segurança no Microsoft 365, no Azure e em aplicações SaaS.',
    'Used Microsoft Purview and Netskope to strengthen governance, compliance, and data protection.': 'Utilizei Microsoft Purview e Netskope para fortalecer a governança, a conformidade e a proteção de dados.',
    'Collaborated with engineering, data science, and architecture teams on strategic initiatives and audits.': 'Colaborei com equipes de engenharia, ciência de dados e arquitetura em iniciativas estratégicas e auditorias.',
    'Security Operations Analyst L2': 'Analista de Operações de Segurança N2',
    'November 2023 — September 2024': 'Novembro de 2023 — Setembro de 2024',
    'Information Security Operations Analyst L1': 'Analista de Operações de Segurança da Informação N1',
    'June 2022 — November 2023': 'Junho de 2022 — Novembro de 2023',
    'Provided cybersecurity consulting and developed security plans.': 'Prestei consultoria em cibersegurança e desenvolvi planos de segurança.',
    'Monitored security events and responded to incidents.': 'Monitorei eventos de segurança e respondi a incidentes.',
    'Developed security reports and action plans aligned with CIS, NIST, CISA, and ISO 27k.': 'Desenvolvi relatórios de segurança e planos de ação alinhados a CIS, NIST, CISA e ISO 27k.',
    'Managed vulnerabilities and applied security best practices in Microsoft Azure.': 'Gerenciei vulnerabilidades e apliquei boas práticas de segurança no Microsoft Azure.',
    'Managed assets and secured on-premises devices, including firewalls, Active Directory, AD FS, and WAF.': 'Gerenciei ativos e a segurança de dispositivos locais, incluindo firewalls, Active Directory, AD FS e WAF.',
    'Worked with Microsoft Azure technologies, including Sentinel, Entra ID, and Azure WAF.': 'Atuei com tecnologias Microsoft Azure, incluindo Sentinel, Entra ID e Azure WAF.',
    'Used Infrastructure as Code tools, including Ansible and Terraform, for infrastructure and cloud security.': 'Utilizei ferramentas de infraestrutura como código, incluindo Ansible e Terraform, para segurança de infraestrutura e nuvem.',
    'Infrastructure Analyst — Supervisor I': 'Analista de Infraestrutura — Supervisor I',
    'April 2021 — June 2022': 'Abril de 2021 — Junho de 2022',
    'Supervised the helpdesk team.': 'Supervisionei a equipe de helpdesk.',
    'Administered cloud and on-premises servers with Windows Server 2008, 2012, and 2016 across Azure and AWS.': 'Administrei servidores em nuvem e locais com Windows Server 2008, 2012 e 2016 em ambientes Azure e AWS.',
    'Administered Kaspersky Endpoint Detection and Response (EDR), including reports, tasks, and incident response.': 'Administrei a solução Kaspersky de detecção e resposta em endpoints (EDR), incluindo relatórios, tarefas e resposta a incidentes.',
    'Used shell scripting with PowerShell, Cisco CLI, and Unix.': 'Utilizei scripts de shell com PowerShell, Cisco CLI e Unix.',
    'IT Technician': 'Técnico de TI',
    'September 2015 — April 2021': 'Setembro de 2015 — Abril de 2021',
    'Supported IT infrastructure and provided management and technical support for the call centers of UVA and Unijorge universities.': 'Prestei suporte à infraestrutura de TI e realizei a gestão e o suporte técnico aos call centers das universidades UVA e Unijorge.',
    'Worked with Azure Cloud and administered Active Directory and Windows Server 2008, 2012, and 2016.': 'Atuei com Azure Cloud e administrei Active Directory e Windows Server 2008, 2012 e 2016.',
    'Supported Cisco local area networks (LAN) and Fortinet solutions: FortiGate, FortiAP, and FortiAnalyzer.': 'Prestei suporte a redes locais (LAN) Cisco e a soluções Fortinet: FortiGate, FortiAP e FortiAnalyzer.',
    'Computer Lab Technician': 'Laboratorista de Informática',
    'August 2015 — September 2015': 'Agosto de 2015 — Setembro de 2015',
    'Supported and advised the academic community on information technology matters.': 'Atendi e assessorei a comunidade acadêmica em assuntos relacionados à tecnologia da informação.',
    'Performed scheduled maintenance and occasional computer repairs.': 'Realizei manutenções programadas e reparos ocasionais em computadores.',
    'IT Infrastructure Intern': 'Estagiário de Infraestrutura de TI',
    'August 2014 — August 2015': 'Agosto de 2014 — Agosto de 2015',
    'Provided helpdesk services and Level 1 support.': 'Prestei atendimento de helpdesk e suporte de nível 1.',
    'Postgraduate Program in Cybersecurity for Business in the Digital Era': 'Pós-graduação em Cibersegurança para Negócios na Era Digital',
    'Extension Course: AI LAB I': 'Curso de Extensão: AI LAB I',
    'Bachelor’s Degree in Computer Science': 'Bacharelado em Ciência da Computação',
    'Cloud Computing Architect Bootcamp': 'Bootcamp de Arquitetura de Computação em Nuvem',
    'Technical Diploma in Computer Networking': 'Técnico em Redes de Computadores',
    'Skills & Expertise': 'Habilidades e Competências',
    'Security architecture, technical delivery, and advisory across cloud, identity, and data.': 'Arquitetura de segurança, implementação técnica e consultoria em nuvem, identidade e dados.',
    'Cloud Security Architecture & Strategy': 'Arquitetura e Estratégia de Segurança em Nuvem',
    'Benchmarks & NIST Cybersecurity Framework': 'Benchmarks e NIST Cybersecurity Framework',
    'Identity & Access Security (IAM)': 'Segurança de Identidades e Acessos (IAM)',
    'Data Security & Microsoft Purview': 'Segurança de Dados e Microsoft Purview',
    'Data Security Posture Management (DSPM)': 'Gestão da Postura de Segurança de Dados (DSPM)',
    'Cloud Security Posture & Vulnerability Management': 'Gestão da Postura de Segurança em Nuvem e de Vulnerabilidades',
    'Security Governance, Risk & Compliance': 'Governança, Riscos e Conformidade em Segurança',
    'Network & Cloud Infrastructure Security': 'Segurança de Redes e de Infraestrutura em Nuvem',
    'Security Monitoring & Incident Response': 'Monitoramento de Segurança e Resposta a Incidentes',
    'AI & Data Protection': 'IA e Proteção de Dados',
    'Security Advisory & Stakeholder Management': 'Consultoria de Segurança e Gestão de Partes Interessadas',
    'Continuous Learning & Technical Leadership': 'Aprendizado Contínuo e Liderança Técnica',
    'Technology focus': 'Tecnologias',
    'Certificates & Training': 'Certificados e Cursos',
    'Search certificates by title, provider, or date': 'Buscar certificados por título, instituição ou data',
    'Search title, provider, or date…': 'Buscar título, instituição ou data…',
    'Filter certificates by provider': 'Filtrar certificados por instituição',
    'All': 'Todos', 'Other providers': 'Outras instituições',
    '22 of 22 certificates and training entries': '22 de 22 certificados e cursos',
    'No certificates match your search.': 'Nenhum certificado corresponde à sua busca.',
    'Clear search and filters': 'Limpar busca e filtros',
    'Microsoft Azure Security Technologies: Microsoft Entra': 'Tecnologias de Segurança do Microsoft Azure: Microsoft Entra',
    'Sell with confidence: Position Microsoft Purview to Secure customer data in the age of AI — Proficient': 'Venda com confiança: posicione o Microsoft Purview para proteger os dados dos clientes na era da IA — Proficiente',
    'Microsoft Certified: Information Security Administrator Associate (SC-401)': 'Microsoft Certified: Administrador Associado de Segurança da Informação (SC-401)',
    'Implement, Govern and Scale Data Security with Microsoft Purview in the era of AI — Skilled': 'Implemente, governe e amplie a segurança de dados com o Microsoft Purview na era da IA — Habilitado',
    'NCCSA — Netskope One Administrator': 'NCCSA — Administrador Netskope One',
    'Microsoft Security Immersion Workshop: On The Brink': 'Microsoft Security Immersion Workshop: On The Brink',
    'Navigating Threats: Advanced Strategies in Threat Modeling': 'Navegando por Ameaças: Estratégias Avançadas de Modelagem de Ameaças',
    'Microsoft Certified: Azure AI Fundamentals (AI-900)': 'Microsoft Certified: Fundamentos de IA do Azure (AI-900)',
    'SoD — Segregation of Duties': 'SoD — Segregação de Funções',
    '[C] CompTIA Security+ 601': '[C] CompTIA Security+ 601',
    'Cloud Security Course': 'Curso de Segurança em Nuvem',
    'Identity and Access Governance': 'Governança de Identidades e Acessos',
    'Microsoft Certified: Security Operations Analyst Associate (SC-200)': 'Microsoft Certified: Analista Associado de Operações de Segurança (SC-200)',
    'Cybersecurity': 'Cibersegurança',
    'Microsoft Certified: Security, Compliance, and Identity Fundamentals (SC-900)': 'Microsoft Certified: Fundamentos de Segurança, Conformidade e Identidade (SC-900)',
    'Network Forensics': 'Forense de Redes',
    'Foundations of Operationalizing MITRE ATT&CK': 'Fundamentos da Operacionalização do MITRE ATT&CK',
    'Kibana Fundamentals': 'Fundamentos de Kibana',
    'Understanding Zero Trust': 'Compreendendo Zero Trust',
    'NSE 3 Network Security Associate': 'NSE 3 — Associado em Segurança de Redes',
    'Cybersecurity Essentials': 'Fundamentos de Cibersegurança',
    'Introduction to LGPD': 'Introdução à LGPD',
    'Languages': 'Idiomas', 'English': 'Inglês', 'Advanced': 'Avançado',
    'Spanish': 'Espanhol', 'Intermediate': 'Intermediário', 'Portuguese (Brazil)': 'Português (Brasil)', 'Native': 'Nativo',
    'Beyond Work': 'Além do Trabalho',
    'Gym & weight training': 'Academia e musculação', 'Forró dancing': 'Dança: forró',
    'Science fiction books': 'Livros de ficção científica', 'TV series': 'Séries de TV',
    'Video games & online cooperative games': 'Videogames e jogos cooperativos online',
    'Cult, horror, crime & sci-fi films': 'Filmes cult, de terror, policiais e de ficção científica',
    'Crime, horror & science fiction books': 'Livros policiais, de terror e de ficção científica',
    'English CV · 2026': 'Currículo em português · 2026',
    'Back to top ↑': 'Voltar ao início ↑',
}

for en, pt in {
    'August': 'Agosto', 'March': 'Março', 'October': 'Outubro', 'September': 'Setembro',
    'June': 'Junho', 'January': 'Janeiro', 'February': 'Fevereiro', 'November': 'Novembro',
    'December': 'Dezembro', 'July': 'Julho'
}.items():
    for year in range(2021, 2027):
        TRANSLATIONS[f'{en} {year}'] = f'{pt} de {year}'


class Localizer(HTMLParser):
    """Keep semantic HTML intact; annotate translatable text nodes and attributes."""
    def __init__(self, locale):
        super().__init__(convert_charrefs=True)
        self.locale = locale
        self.parts = []
        self.raw_tag = None
        self.in_title = False

    def translated(self, value):
        return TRANSLATIONS.get(value, value) if self.locale == 'pt-BR' else value

    def start(self, tag, attrs, close='>'):
        entries = dict(attrs)
        if tag == 'html':
            entries['lang'] = self.locale
        if 'data-lang' in entries:
            entries['aria-pressed'] = str(entries['data-lang'] == self.locale).lower()
        for key in ('aria-label', 'title', 'placeholder', 'alt', 'content'):
            value = entries.get(key)
            if value in TRANSLATIONS:
                entries[f'data-i18n-{key}'] = value
                entries[key] = self.translated(value)
        rendered = ''.join(' '+key if value is None else f' {key}="{html.escape(value,quote=True)}"' for key, value in entries.items())
        self.parts.append(f'<{tag}{rendered}{close}')

    def handle_starttag(self, tag, attrs):
        self.start(tag, attrs)
        if tag in ('script', 'style'):
            self.raw_tag = tag
        if tag == 'title':
            self.in_title = True

    def handle_startendtag(self, tag, attrs):
        self.start(tag, attrs, '/>')

    def handle_endtag(self, tag):
        self.parts.append(f'</{tag}>')
        if tag == self.raw_tag:
            self.raw_tag = None
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.raw_tag:
            self.parts.append(data)
            return
        key = data.strip()
        if self.in_title:
            self.parts.append(html.escape(self.translated(data)))
        elif key in TRANSLATIONS:
            prefix = data[:len(data)-len(data.lstrip())]
            suffix = data[len(data.rstrip()):]
            self.parts.append(f'{prefix}<span data-i18n="{html.escape(key,quote=True)}">{html.escape(self.translated(key))}</span>{suffix}')
        else:
            self.parts.append(html.escape(data))

    def handle_decl(self, decl):
        self.parts.append(f'<!{decl}>')

    def handle_comment(self, data):
        self.parts.append(f'<!--{data}-->')


def localize(document, locale):
    parser = Localizer(locale)
    parser.feed(document)
    parser.close()
    return ''.join(parser.parts)
