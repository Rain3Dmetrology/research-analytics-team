"""Compatibility negative matrix; synthetic artifacts, no network."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from compatibility_check import ROOT, REQUIRED_DMR, check_dmr, check_team_package


class CompatibilityTest(unittest.TestCase):
    def test_version_and_contract_matrix(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d)
            for rel, markers in REQUIRED_DMR.items():
                file = target / rel
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text("\n".join(markers), encoding="utf-8")
            skill = target / "SKILL.md"
            markers = "\n".join(REQUIRED_DMR["SKILL.md"])
            for version, passed in (("2.9.0", False), ("2.9.1", True), ("3.0.0", False)):
                skill.write_text(f'version: "{version}"\n{markers}', encoding="utf-8")
                if passed:
                    check_dmr(target)
                else:
                    with self.assertRaises(ValueError):
                        check_dmr(target)
            skill.write_text(f'version: "2.9.1"\n{markers}', encoding="utf-8")
            (target / "scripts/run_contract.py").write_text("stale", encoding="utf-8")
            with self.assertRaises(ValueError):
                check_dmr(target)
            (target / "scripts/run_contract.py").unlink()
            with self.assertRaises(OSError):
                check_dmr(target)

    def test_same_version_stale_package_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d)
            manifest = json.loads((ROOT / ".codebuddy-plugin/plugin.json").read_text(encoding="utf-8"))
            files = [".codebuddy-plugin/plugin.json", "orchestration/contract.md", "portable/SKILL.md", "settings.json"]
            files += [x.removeprefix("./") for x in manifest["agents"]]
            for rel in files:
                dest = target / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / rel, dest)
            check_team_package(target)
            with (target / "orchestration/contract.md").open("a", encoding="utf-8") as f:
                f.write("\nstale fixture\n")
            with self.assertRaises(ValueError):
                check_team_package(target)


if __name__ == "__main__":
    unittest.main()
