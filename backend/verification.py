
# Sample compliance requirements for educational demonstration

REQUIRED_FIELDS = [
    ("technical_specs", "Technical specifications provided"),
    ("warranty", "Warranty information provided"),
    ("delivery_period", "Delivery period provided"),
    ("price_quote", "Price quote provided"),
    ("seller_documents", "Seller documents confirmed"),
]


def verify_checks(checked):
    if not isinstance(checked, dict):
        checked = {}

    results = []
    compliant = 0

    for key, label in REQUIRED_FIELDS:
        passed = bool(checked.get(key, False))

        if passed:
            compliant += 1

        results.append({
            "item": label,
            "status": "Compliant" if passed else "Needs review"
        })

    total = len(REQUIRED_FIELDS)
    score = round(compliant / total * 100)

    if score == 100:
        overall = "Ready for human review"
    elif score >= 60:
        overall = "Partially compliant"
    else:
        overall = "Needs more information"

    return {
        "compliance_score": score,
        "overall_status": overall,
        "checks_passed": compliant,
        "checks_total": total,
        "results": results
    }
