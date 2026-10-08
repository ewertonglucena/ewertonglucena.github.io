from pathlib import Path
from pypdf import PdfReader
from localize_resume import TRANSLATIONS
import json, re, unicodedata, urllib.request

data = json.loads(Path('.work/resume-content.json').read_text(encoding='utf-8'))
def normalize(text):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', text).lower())

texts = [text for job in data['jobs'] for text in [job['title'], job['company'], job['dates']] + job['bullets']]
texts += [certificate[0] for certificate in data['certificates']]
texts += [education[0] for education in data['education']]
texts += data['skills']
report = {}
for locale in ['pt-BR', 'en-US']:
    reader = PdfReader(f'.work/print-bilingual-{locale}.pdf')
    printed = normalize(' '.join(page.extract_text() for page in reader.pages))
    missing = [text for text in texts if normalize(TRANSLATIONS.get(text, text) if locale == 'pt-BR' else text) not in printed]
    report[locale] = {'pages':len(reader.pages), 'content_checks':len(texts), 'missing':missing, 'portrait_in_print':len(reader.pages[0].images)>0}
    assert not missing, missing
response = urllib.request.urlopen('http://127.0.0.1:8876/?lang=pt-BR', timeout=5)
content = response.read().decode('utf-8')
report['preview'] = {'status':response.status, 'bilingual_html':('data-lang="pt-BR"' in content and 'data-lang="en-US"' in content)}
assert report['preview']['bilingual_html']
Path('.work/print-verification-bilingual.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
