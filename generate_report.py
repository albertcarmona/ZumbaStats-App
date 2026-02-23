import json
from pathlib import Path


def generate_report(data: dict, report_name: str):
    report_path = Path("data") / "zumba4" / f"{report_name}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        print(f"Report generated successfully at {report_path}")