"""Check case integrity and obvious private identifiers without a personal blacklist."""
from pathlib import Path
import hashlib,json,re

root=Path(__file__).resolve().parents[1]
cases=root/'examples/longform'
metrics=json.loads((cases/'metrics.json').read_text(encoding='utf-8'))
assert len(metrics)==14
seen=set();paragraph_count=0
for row in metrics:
    key=(row['case'],row['version'])
    assert key not in seen
    seen.add(key)
    article=cases/row['case']/(row['version']+'.md')
    text=article.read_text(encoding='utf-8')
    assert hashlib.sha256(article.read_bytes()).hexdigest()==row['sha256'], str(article)
    assert text.count('<!-- BODY_START -->')==text.count('<!-- BODY_END -->')==1
    body=text.split('<!-- BODY_START -->')[1].split('<!-- BODY_END -->')[0]
    body=re.sub(r'^\s*#{1,6}.*$','',body,flags=re.M)
    assert len(re.findall(r'[\u3400-\u4dbf\u4e00-\u9fff]',body))==row['public_body_han']
    assert 20000<=row['original_body_han']<=21000
    paras=json.loads((cases/row['case']/(row['version']+'-paragraphs.json')).read_text(encoding='utf-8'))
    for para in paras:
        assert para['text'] in text, f'Paragraph mismatch: {key} {para.get("id")}'
    paragraph_count+=len(paras)
assert paragraph_count==1287
assert sum(r['original_body_han'] for r in metrics)==284340

patterns=[
    re.compile(r'[A-Za-z]:[\\/]Users[\\/](?!Public\b|Default\b)[^\s<>/\\]+'),
    re.compile(r'/(?:home|Users)/[a-zA-Z0-9_.-]+/'),
    re.compile(r'\b(?:RELS|THEO)\s*\d{4}\b'),
    re.compile(r'(?<![\w.])[\w.+-]+@(?:gmail|outlook|hotmail)\.[a-z.]+',re.I),
]
files=0
for folder in [root/'skills',cases]:
    for p in folder.rglob('*'):
        if not p.is_file() or p.suffix not in ('.md','.txt','.json','.yaml','.py'):continue
        text=p.read_text(encoding='utf-8');files+=1
        assert not any(pattern.search(text) for pattern in patterns), f'Potential private identifier: {p.relative_to(root)}'
for core in ['humanities-research','humanities-writing','humanities-review']:
    p=root/'skills'/core/'resources/humanities-author-voice/references/initial-preferences.md'
    assert '没有预填任何个人声音或思想档案' in p.read_text(encoding='utf-8')
print(json.dumps({'articles':len(metrics),'paragraphs':paragraph_count,'scanned_text_files':files,'result':'PASS'}))
