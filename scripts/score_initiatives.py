#!/usr/bin/env python3
"""Score product initiatives with RICE.

CSV columns: name, reach, impact, confidence, effort
Impact can be numeric or one of: massive, high, medium, low, minimal.
Confidence can be numeric 0-1, percentage, or one of: high, medium, low.
Effort is person-months or one of: xs, s, m, l, xl.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

IMPACT = {"massive": 3.0, "high": 2.0, "medium": 1.0, "low": 0.5, "minimal": 0.25}
CONFIDENCE = {"high": 1.0, "medium": 0.8, "low": 0.5}
EFFORT = {"xs": 0.25, "s": 0.5, "m": 1.0, "l": 2.0, "xl": 4.0}


def parse_value(raw: str, mapping: dict[str, float]) -> float:
    value = str(raw).strip().lower()
    if value in mapping:
        return mapping[value]
    if value.endswith("%"):
        return float(value[:-1]) / 100
    return float(value)


def score(row: dict[str, str]) -> float:
    reach = float(row["reach"])
    impact = parse_value(row["impact"], IMPACT)
    confidence = parse_value(row["confidence"], CONFIDENCE)
    effort = parse_value(row["effort"], EFFORT)
    if effort <= 0:
        raise ValueError(f"effort must be greater than zero for {row.get('name', '<unnamed>')}")
    return (reach * impact * confidence) / effort


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: score_initiatives.py initiatives.csv", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    required = {"name", "reach", "impact", "confidence", "effort"}
    if not rows or not required.issubset(rows[0].keys()):
        print("CSV must include: name, reach, impact, confidence, effort", file=sys.stderr)
        return 2

    ranked = sorted(((score(row), row) for row in rows), reverse=True, key=lambda item: item[0])
    print("| Rank | Initiative | RICE Score | Reach | Impact | Confidence | Effort |")
    print("| ---: | --- | ---: | ---: | --- | --- | --- |")
    for rank, (rice, row) in enumerate(ranked, start=1):
        print(
            f"| {rank} | {row['name']} | {rice:.2f} | {row['reach']} | "
            f"{row['impact']} | {row['confidence']} | {row['effort']} |"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
