"""Check public artifacts, exact scoped edits, provenance, and skill identities."""
from pathlib import Path
import hashlib,json,re

root=Path(__file__).resolve().parents[1]
examples=root/'examples';cases=examples/'defensive-generation'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not (examples/'longform').exists()
ids=['01-philosophical-reading','02-literary-religious-experience','03-aesthetics-essay','04-negative-argument-review','05-selected-local-revision','06-interdisciplinary-religion']
for name in ids:
    for file in ['source.md','task.md']:
        assert (cases/'cases'/name/file).read_text(encoding='utf-8').strip()
    assert (cases/'results/candidate'/(name+'.md')).is_file()
for name in ids[:3]:
    assert (cases/'results/baseline'/(name+'.md')).is_file()
for file in ['reviews/blind-comparison.md','reviews/controls.md']:
    assert (cases/file).is_file(),file

artifact_files=json.loads((cases/'artifact-manifest.json').read_text(encoding='utf-8'))
for rel,digest in artifact_files.items():
    p=(root/rel).resolve()
    assert p.is_relative_to(examples),rel
    assert sha(p)==digest,rel
actual={p.relative_to(root).as_posix() for p in examples.rglob('*') if p.is_file() and p.name!='artifact-manifest.json'}
assert actual==set(artifact_files), 'Artifact manifest does not cover the complete example collection'

source=(cases/'cases'/ids[4]/'source.md').read_text(encoding='utf-8')
expected=source[source.index('## 门口的告示'):].rstrip()
task=(cases/'cases'/ids[4]/'task.md').read_text(encoding='utf-8')
for number in [2,5]:
    section=task.split(f'### {number}\n',1)[1].split('\n### ',1)[0]
    old=re.search(r'^原句：(.+)$',section,re.M)[1]
    new=re.search(r'^拟改句：(.+)$',section,re.M)[1]
    assert expected.count(old)==1
    expected=expected.replace(old,new)
actual=(cases/'results/candidate'/f'{ids[4]}.md').read_text(encoding='utf-8').rstrip()
assert actual==expected+'\n\n本轮仅落实第 2 项和第 5 项。', 'Scoped edit changed unselected text'

revisions=examples/'revisions'
sources=json.loads((revisions/'source-manifest.json').read_text(encoding='utf-8'))
for entry in sources:assert sha(revisions/entry['snapshot_path'])==entry['sha256']
retained=json.loads((revisions/'retained-source-manifest.json').read_text(encoding='utf-8'))
for entry in retained:assert sha(revisions/entry['snapshot_path'])==entry['sha256']
for folder in sorted((revisions/'retained-validation').iterdir()):
    assert (folder/'review.md').is_file() and (folder/'revision.md').is_file()
    receipt=json.loads((folder/'loads.json').read_text(encoding='utf-8'))
    for entry in receipt['files']:
        assert sha(root/'skills'/entry['path'].removeprefix('skills/'))==entry['sha256']
loads=json.loads((revisions/'skill-read-manifest.json').read_text(encoding='utf-8'))['entries']
for entry in loads:assert sha(root/entry['path'])==entry['sha256']
package_hashes=json.loads((cases/'package-hashes.json').read_text(encoding='utf-8'))
for entry in package_hashes:
    if entry['path'].startswith('candidate/'):
        assert sha(root/entry['path'].removeprefix('candidate/'))==entry['sha256']
baseline=json.loads((cases/'baseline-instructions.json').read_text(encoding='utf-8'))
old_hashes={e['path'].removeprefix('baseline/'):e['sha256'] for e in package_hashes if e['path'].startswith('baseline/')}
assert {e['path']:e['sha256'] for e in baseline}==old_hashes
for entry in baseline:
    assert hashlib.sha256(entry['content'].encode('utf-8')).hexdigest()==entry['sha256'],entry['path']

patterns=[
    re.compile(r'[A-Za-z]:[\\/]Users[\\/](?!Public\b|Default\b)[^\s<>/\\]+'),
    re.compile(r'/(?:home|Users)/[a-zA-Z0-9_.-]+/'),
    re.compile(r'\b(?:RELS|THEO)\s*\d{4}\b'),
    re.compile(r'(?<![\w.])[\w.+-]+@(?:gmail|outlook|hotmail)\.[a-z.]+',re.I),
]
files=0
for folder in [root/'skills',examples,root/'validation']:
    for p in folder.rglob('*'):
        if not p.is_file() or p.suffix not in ('.md','.txt','.json','.yaml','.py'):continue
        text=p.read_text(encoding='utf-8');files+=1
        assert not any(pattern.search(text) for pattern in patterns), f'Potential private identifier: {p.relative_to(root)}'
for core in ['humanities-research','humanities-writing','humanities-review']:
    p=root/'skills'/core/'resources/humanities-author-voice/references/initial-preferences.md'
    assert '没有预填任何个人声音或思想档案' in p.read_text(encoding='utf-8')
print(json.dumps({'new_tasks':len(ids),'paired_tasks':3,'existing_case_source_snapshots':len(sources),'artifact_files':len(artifact_files),'scoped_edit':'exact match','scanned_text_files':files,'result':'PASS'}))
