# Curriculum vitae — Ewerton Gomes de Lucena

Currículo estático bilíngue, com foco inicial em Identity & Access Security.
Arquivo para GitHub Pages: `index.html`. Não exige npm, framework, servidor de aplicação ou build no serviço de hospedagem.

## Visualização

Abra o HTML diretamente no navegador, ou execute `python .work/serve_preview.py` e acesse `http://127.0.0.1:8876/`.

Links de especialização:

- `?mode=identity` (padrão)
- `?mode=cloud-data`
- `?mode=identity&lang=pt-BR`
- `?mode=cloud-data&lang=en-US`

O idioma segue as preferências do navegador, com prioridade para um idioma explícito na URL ou uma escolha manual anterior. O modo altera destaques e a ordem dos projetos e credenciais, preservando a cronologia das experiências.

## Atualização dos dados

- `.work/build_resume.py`: experiências, formação e registros herdados do currículo original.
- `.work/modern_data.py`: datas estruturadas, competências, projetos, classificação de credenciais e traduções dos novos textos.
- `.work/localize_resume.py`: traduções anteriores e renderização das versões estáticas.
- `.work/resume-template.html`: estrutura semântica, visual original e interações já existentes.
- `.work/modern-resume.css` e `.work/modern-resume.js`: novos estilos, modos e cálculo de durações.
- `.work/portrait.png`: cópia local, sem alterações, da foto anexada.
- `.work/resume-content.json`: dados estruturados gerados, também incorporados ao HTML.

Para regenerar os arquivos: `python .work/build_resume.py`.
O HTML inclui CSS, scripts, traduções e foto. O conteúdo principal funciona offline e permanece legível sem JavaScript.

## Indicadores

As durações usam limites em mês/ano e a data atual em America/Sao_Paulo. Períodos em andamento são atualizados ao abrir ou retornar à página. Intervalos simultâneos são unidos antes da soma.

TI inclui os vínculos registrados desde agosto de 2014. Cibersegurança considera os cargos de segurança desde junho de 2022. O indicador de Identity Security representa apenas a atuação atual documentada, desde março de 2026; não atribui automaticamente o período da ZAMP à experiência específica em IAM.

A contagem de certificações representa o histórico registrado, incluindo credenciais Fortinet com expiração informada. Cursos, badges e workshops têm categorias próprias. Não se presume validade atual sem evidência de renovação.

## Impressão e testes

O botão Imprimir / PDF inclui todos os grupos de competências, certificados e responsabilidades, mesmo com filtros ativos e detalhes recolhidos. O estado da tela é restaurado depois da impressão. Os PDFs completos têm texto selecionável e links.

Testes locais (dependências de navegador já disponíveis no ambiente):

- `node .work/verify_bilingual.cjs`
- `node .work/verify_modernization.cjs`
- `node .work/verify_language_detection.cjs`
- `node .work/check_horizontal_labels.cjs`
- `python .work/inspect_bilingual_print.py`

## Publicação

O `index.html` e o arquivo `.nojekyll` estão preparados para GitHub Pages. A publicação e o push dependem de autorização explícita do proprietário; nenhuma alteração remota foi feita neste trabalho.
