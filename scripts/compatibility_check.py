"""Read-only cross-repository and installed-package compatibility gate."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DMR = {
    "SKILL.md": ("Evidence Contract v1", "Run Contract v1"),
    "references/parameter-card-schema.md": ("Evidence Contract v1",),
    "references/run-contract.md": ("Run Contract v1",),
    "references/data-sources.md": ("Evidence Contract v1",),
    "scripts/evidence_contract.py": ("def evidence_errors(",),
    "scripts/validate_param_card.py": ("--require-evidence",),
    "scripts/run_contract.py": ("class BudgetLedger", "def validate_run("),
    "scripts/evaluate_search_benchmark.py": ("def preflight_request(", "def verify_snapshot("),
}


def version(value):
    if not re.fullmatch(r"\d+\.\d+\.\d+", value):
        raise ValueError("invalid semantic version")
    return tuple(map(int, value.split(".")))


def check_dmr(dmr, source=ROOT):
    manifest = json.loads((source / ".codebuddy-plugin/plugin.json").read_text(encoding="utf-8"))
    pin = manifest["requires"]["deep-market-research"]
    match = re.fullmatch(r">=(\d+\.\d+\.\d+)\s+<(\d+)", pin)
    if not match:
        raise ValueError("invalid DMR pin")
    skill = (dmr / "SKILL.md").read_text(encoding="utf-8-sig")
    marker = re.search(r'^version:\s*"?([\d.]+)"?\s*$', skill, re.M)
    if not marker:
        raise ValueError("DMR version missing")
    installed = version(marker.group(1))
    if not version(match.group(1)) <= installed < (int(match.group(2)), 0, 0):
        raise ValueError(f"DMR {marker.group(1)} outside required range {pin}")
    for path, markers in REQUIRED_DMR.items():
        text = (dmr / path).read_text(encoding="utf-8-sig")
        if not all(item in text for item in markers):
            raise ValueError(f"DMR contract marker missing: {path}")


def same_file(source, installed):
    if not installed.is_file() or hashlib.sha256(source.read_bytes()).digest() != hashlib.sha256(installed.read_bytes()).digest():
        raise ValueError(f"missing or drifted installed file: {installed.name}")


def check_team_package(package, source=ROOT):
    manifest = json.loads((source / ".codebuddy-plugin/plugin.json").read_text(encoding="utf-8"))
    required = [".codebuddy-plugin/plugin.json", "orchestration/contract.md", "portable/SKILL.md", "settings.json"]
    required += [item.removeprefix("./") for item in manifest["agents"]]
    for name in required:
        same_file(source / name, package / name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dmr", type=Path, required=True)
    parser.add_argument("--package", type=Path)
    parser.add_argument("--annex", type=Path)
    args = parser.parse_args()
    try:
        check_dmr(args.dmr)
        if args.package:
            check_team_package(args.package)
        if args.annex:
            same_file(ROOT / "portable/SKILL.md", args.annex)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"COMPATIBILITY FAIL: {exc}")
        return 1
    print("COMPATIBILITY PASS (version, contract artifacts and requested package hashes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
