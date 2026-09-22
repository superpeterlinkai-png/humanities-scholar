import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

package = Path(__file__).resolve().parents[1]
scratch = Path(tempfile.mkdtemp(prefix="humanities-install-test-"))
destination = scratch / "installed"
destination.mkdir()
sentinel = destination / "unrelated-skill.txt"
sentinel.write_text("Preserve existing unrelated files.\n", encoding="utf-8")

def run(script, target):
    return subprocess.run([sys.executable, str(script), "--destination", str(target)], capture_output=True, text=True, encoding="utf-8")

def hashes(folder):
    return {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.rglob("*") if p.is_file()}

success = run(package / "install.py", destination)
assert success.returncode == 0, success.stderr
first = hashes(destination)
repeat = run(package / "install.py", destination)
assert repeat.returncode == 1 and "Refusing to overwrite" in repeat.stderr
assert hashes(destination) == first, "Rejected duplicate install changed existing files"
assert sentinel.read_text(encoding="utf-8") == "Preserve existing unrelated files.\n"

damaged = scratch / "damaged-package"
shutil.copytree(package, damaged)
entry = damaged / "skills" / "humanities-research" / "SKILL.md"
with entry.open("a", encoding="utf-8") as stream:
    stream.write("\nTest-only change.\n")
rejected_target = scratch / "should-not-exist"
tampered = run(damaged / "install.py", rejected_target)
assert tampered.returncode == 1 and "differ from MANIFEST" in tampered.stderr
assert not rejected_target.exists(), "Invalid package caused a destination mutation"

report = {
    "valid_install": {k:v for k,v in json.loads(success.stdout).items() if k != "destination"},
    "duplicate_install": "rejected; existing files byte-identical",
    "unrelated_file": "preserved",
    "tampered_package": "rejected before destination creation",
    "result": "PASS",
}
print(json.dumps(report, ensure_ascii=False))
