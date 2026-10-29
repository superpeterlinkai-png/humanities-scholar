"""Maintain self-contained humanities bundles from humanities-research.

Default is read-only. --write copies modules/ and resources/ into the two sibling
bundles; it never deletes files or changes entrypoints. Invoke only as an
authorized maintenance operation. Local modifications in destinations are shown
by default before a write is chosen. External publication is outside this tool.
"""
from pathlib import Path
import argparse, hashlib, json, shutil, sys

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',action='store_true')
    args=ap.parse_args()
    source=Path(__file__).resolve().parent.parent
    targets=[source.parent/n for n in ('humanities-writing','humanities-review')]
    if any(not (p/'SKILL.md').is_file() for p in targets):
        raise SystemExit('Expected both sibling humanities bundles; nothing changed.')
    files=sorted(p for folder in ('modules','resources') for p in (source/folder).rglob('*') if p.is_file())
    changes=[]
    for src in files:
        rel=src.relative_to(source)
        for target in targets:
            dst=target/rel
            if not dst.is_file() or digest(dst)!=digest(src):
                changes.append(str(dst.relative_to(source.parent)))
                if args.write:
                    dst.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copy2(src,dst)
                    if digest(dst)!=digest(src): raise RuntimeError('Readback mismatch: '+str(dst))
    report={'source':str(source),'shared_files':len(files),'differences':changes,'written':args.write}
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 1 if changes and not args.write else 0

if __name__=='__main__': sys.exit(main())
