from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import subprocess, shutil, re
root=Path(__file__).resolve().parent.parent
work=root/'.work'
poppler=Path('C:/Users/ewert/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
subprocess.run([str(poppler),'-r','90','-png',str(work/'print-bilingual-pt-BR.pdf'),str(work/'modern-print')],check=True)
pages=sorted(page for page in work.glob('modern-print-*.png') if re.fullmatch(r'modern-print-\d+\.png', page.name))
sheet=Image.new('RGB',(4*400,2*605),'#d9e2e6')
draw=ImageDraw.Draw(sheet)
for i,page in enumerate(pages):
    preview=Image.open(page).convert('RGB')
    preview.thumbnail((380,565))
    x=(i%4)*400+10;y=(i//4)*605+28
    sheet.paste(preview,(x,y))
    draw.text((x, y-19),f'Page {i+1}',fill='#173440')
sheet.save(work/'modern-print-contact-sheet.png')
for locale in ['pt-BR','en-US']:
    shutil.copyfile(work/f'print-bilingual-{locale}.pdf',root/f'Curriculum vitae - Ewerton Gomes de Lucena - {locale}.pdf')
print({'rendered_pages':len(pages),'contact_sheet':str(work/'modern-print-contact-sheet.png')})
