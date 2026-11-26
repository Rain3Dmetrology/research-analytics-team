"""Native installer smoke: isolated home, no credentials or network."""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_smoke(dmr):
    with tempfile.TemporaryDirectory(prefix="rat-install-") as temp:
        home = Path(temp)
        base = home / ".workbuddy" / "skills"
        base.mkdir(parents=True)
        pkg = home / ".workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team"
        pkg.mkdir(parents=True)
        for name in (".codebuddy-plugin", "agents", "orchestration", "portable", "settings.json"):
            src = ROOT / name
            if src.is_dir():
                shutil.copytree(src, pkg / name)
            else:
                shutil.copy2(src, pkg / name)
        env = dict(os.environ, HOME=temp, USERPROFILE=temp, PYTHONUTF8="1")
        def run(repo, check, expected):
            if os.name == "nt":
                cmd = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(repo / "install.ps1")]
                flag = "-Check"
            else:
                cmd = ["bash", str(repo / "install.sh")]
                flag = "--check"
            result = subprocess.run(cmd + ([flag] if check else []), env=env,
                                    capture_output=True, text=True, encoding="utf-8",
                                    errors="replace", timeout=90)
            if result.returncode != expected:
                raise RuntimeError(f"expected exit {expected}, got {result.returncode}: {result.stdout}{result.stderr}")
        run(dmr, False, 0)
        run(dmr, True, 0)
        run(ROOT, False, 0)
        run(ROOT, True, 0)
        annex = base / "research-orchestrator/SKILL.md"
        original = annex.read_bytes()
        annex.write_bytes(original + b"\n# synthetic drift\n")
        run(ROOT, True, 1)
        annex.write_bytes(original)
        skill = base / "deep-market-research/SKILL.md"
        skill.write_text(skill.read_text(encoding="utf-8").replace("2.9.1", "3.0.0"), encoding="utf-8")
        run(ROOT, True, 1)


if __name__ == "__main__":
    run_smoke(Path(sys.argv[1]).resolve())
    print("NATIVE INSTALL SMOKE PASS")
