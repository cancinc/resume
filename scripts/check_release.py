"""Read-only checks for the prepared site/PDF release. Run from any directory."""
from pathlib import Path
from lxml import html
from pypdf import PdfReader
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
folder=ROOT/'output/site'
pdf=PdfReader(folder/'Nicholas_King_Resume.pdf')
page=html.fromstring((folder/'index.html').read_text())
def norm(t):return re.sub(r'\s+',' ',t.replace('’',"'").replace('—','-').replace('–','-')).strip()
text=norm(' '.join(p.extract_text() for p in pdf.pages))
checks={}
checks['two_page_pdf']=len(pdf.pages)==2
checks['experience_bullets_synchronized']=all(norm(' '.join(n.itertext())) in text for n in page.xpath('//*[@id="experience"]//li'))
checks['no_doctoral_or_annual_claims']=not any(t in text.lower() for t in ['ph.d','doctorate','annually','global budget'])
checks['confirmed_current_title']='Director, New Approach Methods' in text
checks['confirmed_transition_dates']='Sep 2026 - Present' in text and 'Nov 2021 - Sep 2026' in text
checks['confirmed_senior_pm_dates']='Sep 2014 - Jul 2019' in text
checks['local_links_resolve']=all((folder/a.get('href')).is_file() for a in page.xpath('//a[@href]') if not a.get('href').startswith(('#','http','mailto:')))
checks['section_anchors_resolve']=all(page.xpath('//*[@id=$id]',id=a.get('href')[1:]) for a in page.xpath('//a[starts-with(@href,"#")]'))
checks['only_release_assets']=sorted(p.name for p in folder.iterdir())==['Nicholas_King_Resume.pdf','index.html']
checks['pdf_identical_to_reviewed_output']=(folder/'Nicholas_King_Resume.pdf').read_bytes()==(ROOT/'output/pdf/Nicholas_King_Resume.pdf').read_bytes()
checks['no_stale_pdf_note']='update is pending' not in (folder/'index.html').read_text()
checks['sans_serif_only']='DM+Serif' not in (folder/'index.html').read_text() and 'JetBrains' not in (folder/'index.html').read_text()
result={'checks':checks,'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(folder.iterdir())}}
print(json.dumps(result,indent=2))
if not all(checks.values()):raise SystemExit(1)
