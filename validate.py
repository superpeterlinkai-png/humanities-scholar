"""Validate suite metadata, local links, invocation prompts, and file hashes."""
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from install import checked_sources


def string_scalar(value):
    """Read the single-line string scalars used by the package metadata."""
    if value.startswith('"'):
        result = json.loads(value)
    elif value.startswith("'") and value.endswith("'"):
        result = value[1:-1].replace("''", "'")
    else:
        if not value or value[0] in "'[{&*!|>@`" or ': ' in value or ' #' in value:
            raise ValueError(f"Unsupported metadata scalar: {value}")
        result = value
    if not isinstance(result, str):
        raise ValueError("Metadata field must be a string")
    return result


def main():
    root = Path(__file__).resolve().parent
    names, expected = checked_sources(root)
    links = 0
    for name in names:
        folder = root / "skills" / name
        body = (folder / "SKILL.md").read_text(encoding="utf-8")
        front = re.match(r"\A---\nname: ([a-z-]+)\ndescription: (.+)\n(?:[^\n]*\n)*?---\n", body)
        if not front or front[1] != name:
            raise ValueError(f"Invalid skill frontmatter: {name}")
        description = string_scalar(front[2])
        if not description or len(description) > 1024:
            raise ValueError(f"Invalid description: {name}")
        ui_path = folder / "agents" / "openai.yaml"
        if not ui_path.exists():
            continue
        ui = ui_path.read_text(encoding="utf-8")
        match = re.search(r"^  default_prompt: (.+)$", ui, re.M)
        if not match or "$" + name not in string_scalar(match[1]):
            raise ValueError(f"Missing invocation in prompt: {name}")
        match = re.search(r"^  short_description: (.+)$", ui, re.M)
        if not match or not 25 <= len(string_scalar(match[1])) <= 64:
            raise ValueError(f"Invalid UI description length: {name}")
    for path in (root / "skills").rglob("*.md"):
        content = path.read_text(encoding="utf-8")
        if "[TODO:" in content:
            raise ValueError(f"Unfinished scaffold: {path}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://", "#")):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            if not resolved.is_relative_to(root / "skills") or not resolved.is_file():
                raise ValueError(f"Broken or escaping link in {path}: {target}")
            links += 1
    print(json.dumps({"skills": len(names), "hashed_files": len(expected), "local_links": links, "result": "PASS"}))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
