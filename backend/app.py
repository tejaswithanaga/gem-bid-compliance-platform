
from flask import Flask, request, jsonify
from flask_cors import CORS

from verification import verify_checks

app = Flask(__name__)
CORS(app)


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

    if not isinstance(data, dict):
        data = {}

    tender_title = str(data.get("tender_title", "")).strip()
    checked = data.get("checks", {})

    if not tender_title:
        return jsonify({
            "error": "Please enter a tender or bid title."
        }), 400

    verification_result = verify_checks(checked)

    response = {
        "tender_title": tender_title,
        **verification_result,
        "disclaimer": (
            "Demo only. This is not an official GeM verification "
            "and does not replace expert review."
        )
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
