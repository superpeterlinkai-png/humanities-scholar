"""Install this complete skill suite without overwriting existing directories."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys


def checked_sources(root):
    manifest = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
    names = manifest["skills"]
    if not names or len(names) != len(set(names)):
        raise ValueError("Manifest has no skills or duplicate skills")
    if any(not re.fullmatch(r"humanities-[a-z-]+", name) for name in names):
        raise ValueError("Unsafe skill name")
    skills_root = (root / "skills").resolve()
    expected = manifest["files"]
    actual = {}
    for name in names:
        folder = skills_root / name
        if not folder.is_dir() or folder.is_symlink():
            raise ValueError(f"Missing or linked skill: {name}")
        for path in folder.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"Symlink not supported: {path}")
            if path.is_file():
                resolved = path.resolve()
                if not resolved.is_relative_to(skills_root):
                    raise ValueError("Source escapes skills root")
                actual[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    if set(p.name for p in skills_root.iterdir() if p.is_dir()) != set(names):
        raise ValueError("Unexpected or missing skill directories")
    if actual != expected:
        raise ValueError("Skill files differ from MANIFEST.json; installation stopped")
    return names, expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    names, expected = checked_sources(root)
    destination = args.destination.expanduser().resolve()
    if destination == root or destination.is_relative_to(root):
        raise ValueError("Install destination must be outside this package")
    if destination.exists() and not destination.is_dir():
        raise ValueError("Destination is not a directory")
    collisions = [str(destination / name) for name in names if (destination / name).exists()]
    if collisions:
        raise ValueError("Refusing to overwrite existing directories: " + ", ".join(collisions))
    # All hashes and destination collisions are checked before any mutation.
    destination.mkdir(parents=True, exist_ok=True)
    for name in names:
        target = destination / name
        if not target.resolve().is_relative_to(destination):
            raise ValueError("Destination escapes installation root")
        shutil.copytree(root / "skills" / name, target)
    for relative, digest in expected.items():
        target = destination.joinpath(*Path(relative).parts[1:])
        if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            raise ValueError(f"Verification failed: {target}")
    print(json.dumps({"installed": len(names), "verified_files": len(expected), "destination": str(destination)}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
