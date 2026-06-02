"""
Portfolio sample datamart generator.

This script does not use real sales, advertising, customer, product, or
promotion data. It only generates an illustrative schema for portfolio review.
"""

import json
from pathlib import Path

OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "dashboard_data.sample.json"

sample_data = {
    "meta": {
        "project": "Naver Promotion Dashboard Portfolio Sample",
        "period": "2026-05",
        "notice": "This sample uses anonymized and illustrative values only. It does not include real product, sales, advertising, customer, or promotion data.",
        "reliability_policy": [
            "Original source files are not modified.",
            "Official promotion metrics and daily sales metrics are not force-merged when aggregation standards differ.",
            "Unavailable metrics are not fabricated.",
        ],
    },
    "executive_summary": {
        "monthly_sales": 125_000_000,
        "mom_sales_change_rate": 0.18,
        "ad_spend": 8_200_000,
        "purchase_completed_roas": 7.82,
        "new_customers": 1_480,
        "conversion_rate": 0.034,
    },
    "daily_flow": [
        {
            "date": "2026-05-01",
            "sales": 3_600_000,
            "ad_spend": 210_000,
            "visits": 9_800,
            "orders": 310,
            "event_marker": "CRM",
        },
        {
            "date": "2026-05-02",
            "sales": 4_200_000,
            "ad_spend": 260_000,
            "visits": 11_200,
            "orders": 354,
            "event_marker": "Official Promotion",
        },
        {
            "date": "2026-05-03",
            "sales": 5_100_000,
            "ad_spend": 280_000,
            "visits": 12_600,
            "orders": 402,
            "event_marker": "LIVE",
        },
    ],
    "ad_type_performance": [
        {
            "ad_type": "Search Ad",
            "spend": 3_200_000,
            "purchase_completed_sales": 31_500_000,
            "clicks": 18_400,
            "conversions": 920,
            "roas": 7.64,
        },
        {
            "ad_type": "Catalog Ad",
            "spend": 2_100_000,
            "purchase_completed_sales": 17_600_000,
            "clicks": 12_100,
            "conversions": 540,
            "roas": 8.38,
        },
        {
            "ad_type": "ADVoost",
            "spend": 2_900_000,
            "purchase_completed_sales": 27_800_000,
            "clicks": 15_300,
            "conversions": 760,
            "roas": 7.41,
        },
    ],
    "official_promotion": {
        "note": "Official promotion performance is tracked separately from total daily sales because aggregation standards may differ.",
        "items": [
            {
                "promotion_group": "Official Deal A",
                "period": "2026-05-02~2026-05-06",
                "promotion_sales": 18_200_000,
                "orders": 980,
            },
            {
                "promotion_group": "Official Deal B",
                "period": "2026-05-16~2026-05-20",
                "promotion_sales": 16_400_000,
                "orders": 870,
            },
        ],
    },
}

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text(json.dumps(sample_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {OUTPUT_PATH}")
