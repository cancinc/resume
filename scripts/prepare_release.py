"""Build the synchronized PDF and stage only the intended deployment assets."""
from pathlib import Path
import subprocess,sys,shutil
root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(root/'scripts/build_resume_pdf.py')],check=True)
preview=root/'preview'
shutil.copy2(root/'output/pdf/Nicholas_King_Resume.pdf',preview/'Nicholas_King_Resume.pdf')
release=root/'output/site';release.mkdir(exist_ok=True)
source=(preview/'index.html').read_text().replace('<div class="review">DESIGN DRAFT · November 2026 · For review</div>','')
(release/'index.html').write_text(source)
shutil.copy2(root/'output/pdf/Nicholas_King_Resume.pdf',release/'Nicholas_King_Resume.pdf')
result=subprocess.run([sys.executable,str(root/'scripts/check_release.py')],check=True,capture_output=True,text=True)
(root/'output/release-checks.json').write_text(result.stdout)
print(result.stdout)
