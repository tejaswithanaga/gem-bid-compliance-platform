from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Educational demo only: these are sample checks, not official GeM rules.
REQUIRED_FIELDS = [
    ("technical_specs", "Technical specifications provided"),
    ("warranty", "Warranty information provided"),
    ("delivery_period", "Delivery period provided"),
    ("price_quote", "Price quote provided"),
    ("seller_documents", "Seller documents confirmed"),
]

@app.get("/api/health")
def health():
    return jsonify({
        "status": "running",
        "service": "Demo Bid Compliance API",
        "note": "Educational rule-based demonstration only"
    })

@app.post("/api/verify")
def verify_bid():
    data = request.get_json(silent=True) or {}
    tender_title = str(data.get("tender_title", "")).strip()
    checked = data.get("checks", {})
    if not tender_title:
        return jsonify({"error": "Please enter a tender or bid title."}), 400

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

    return jsonify({
        "tender_title": tender_title,
        "compliance_score": score,
        "overall_status": overall,
        "checks_passed": compliant,
        "checks_total": total,
        "results": results,
        "disclaimer": "Demo only. This is not an official GeM verification and does not replace expert review."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
