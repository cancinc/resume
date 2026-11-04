"""Build the review PDF directly from preview/index.html to keep wording aligned.
Requires reportlab, lxml, fonttools; optionally pymupdf for review images.
Run from the repository root. Font files are cached under tmp/pdfs.
"""
from pathlib import Path
from xml.sax.saxutils import escape
from urllib.request import urlretrieve
from lxml import html
from fontTools.ttLib import TTFont as SourceFont
from fontTools.varLib.instancer import instantiateVariableFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.enums import TA_LEFT

ROOT=Path(__file__).resolve().parents[1]
cache=ROOT/'tmp/pdfs'; cache.mkdir(parents=True,exist_ok=True)
variable=cache/'DM-Sans-variable.ttf'
if not variable.exists(): urlretrieve('https://raw.githubusercontent.com/google/fonts/main/ofl/dmsans/DMSans%5Bopsz,wght%5D.ttf',variable)
for weight,name in [(400,'Regular'),(700,'Bold')]:
 path=cache/f'DM-Sans-{name}.ttf'
 if not path.exists():
  font=SourceFont(variable)
  instantiateVariableFont(font,{'opsz':12,'wght':weight},inplace=True)
  for record in font['name'].names:
   if record.nameID in (1,4,6): record.string=('DMSansResume'+name).encode(record.getEncoding())
  font.save(path)
 pdfmetrics.registerFont(TTFont('DM'+name,str(path)))
pdfmetrics.registerFontFamily('DMRegular',normal='DMRegular',bold='DMBold',italic='DMRegular',boldItalic='DMBold')
page=html.fromstring((ROOT/'preview/index.html').read_text())
def text(node): return ' '.join(' '.join(node.itertext()).split())
def find(cls,scope=page): return scope.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," '+cls+' ")]')
def clean(s): return escape(s.replace('—','-').replace('–','-').replace('’',"'").replace('·',' | '))
styles={
 'body':ParagraphStyle('body',fontName='DMRegular',fontSize=9.4,leading=13,spaceAfter=5,textColor=HexColor('#12293A')),
 'name':ParagraphStyle('name',fontName='DMBold',fontSize=27,leading=31,spaceAfter=6),
 'section':ParagraphStyle('section',fontName='DMBold',fontSize=10,leading=14,spaceBefore=10,spaceAfter=7,textColor=HexColor('#1F6A97'),keepWithNext=True),
 'role':ParagraphStyle('role',fontName='DMBold',fontSize=10.4,leading=14,spaceBefore=8,spaceAfter=2,keepWithNext=True),
 'meta':ParagraphStyle('meta',fontName='DMRegular',fontSize=8.5,leading=11.5,spaceAfter=5,textColor=HexColor('#4B6272'),keepWithNext=True),
 'bullet':ParagraphStyle('bullet',fontName='DMRegular',fontSize=9.4,leading=13,spaceAfter=4,leftIndent=10,firstLineIndent=-8,textColor=HexColor('#12293A')),
}
story=[]
def add(s,style='body',raw=False): story.append(Paragraph(s if raw else clean(s),styles[style]))
def section(s): add(s.upper(),'section')
def role(n):
 title=text(n.find('.//h3')); org=text(find('org',n)[0]); date=text(find('date',n)[0])
 add(title,'role');add(org+' | '+date,'meta')
 for node in n.xpath('./div[last()]/*'):
  if node.tag=='p' and 'org' not in node.get('class',''): add(text(node))
  if node.tag=='ul':
   for li in node: add('- '+text(li),'bullet')
add('Nicholas King','name')
add(text(find('eyebrow')[0]),'meta')
add('<link href="https://nicking.cv" color="#1F6A97">nicking.cv</link> | <link href="mailto:nmpk_accounts@icloud.com" color="#1F6A97">nmpk_accounts@icloud.com</link> | <link href="https://www.linkedin.com/in/nicholasmpking" color="#1F6A97">LinkedIn</link>','meta',True)
section('Profile');add(text(find('intro')[0]))
section('Leadership experience')
roles=find('role')
for r in roles[:4]: role(r)
story.append(PageBreak())
section('Leadership experience - continued')
for r in roles[4:]: role(r)
section('Leadership capabilities')
for n in find('capability'):
 add('<b>'+clean(text(n.find('h3')))+':</b> '+clean(text(n.find('p'))),raw=True)
section('Education & community leadership')
for n in find('entry'):
 add('<b>'+clean(text(n.find('h3')))+'.</b> '+clean(text(n.find('p'))),raw=True)
section('Selected research')
for n in page.xpath('//*[@id="research"]//article'):
 title=text(n.find('.//h3')); date=text(find('date',n)[0]); link=n.find('.//a').get('href')
 add('<b>'+clean(title)+'.</b> '+clean(date)+'. <link color="#1F6A97" href="'+link+'">Publication</link>',raw=True)
add('<link color="#1F6A97" href="https://www.ncbi.nlm.nih.gov/myncbi/1hCqusxmqdoka/bibliography/public/">Full bibliography</link>',raw=True)
out=ROOT/'output/pdf/Nicholas_King_Resume.pdf';out.parent.mkdir(parents=True,exist_ok=True)
def footer(c,doc):
 c.setFont('DMRegular',8);c.setFillColor(HexColor('#4B6272'));c.drawString(42,25,'Nicholas King | nicking.cv');c.drawRightString(570,25,str(doc.page))
 c.setTitle('Nicholas King - Resume');c.setAuthor('Nicholas King');c.setSubject('Scientific strategy, research leadership, and strategic partnerships')
class ResumeDoc(SimpleDocTemplate):
 def afterPage(self): footer(self.canv,self)
doc=ResumeDoc(str(out),pagesize=(612,792),rightMargin=42,leftMargin=42,topMargin=34,bottomMargin=42)
doc.build(story)
print(out)
try:
 import pymupdf
 pdf=pymupdf.open(out)
 print('Pages:',len(pdf))
 for i,p in enumerate(pdf): p.get_pixmap(matrix=pymupdf.Matrix(1.7,1.7)).save(cache/f'resume-page-{i+1}.png')
except ImportError: pass
