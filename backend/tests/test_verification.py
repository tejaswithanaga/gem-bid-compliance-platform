
from verification import verify_checks


def test_all_documents_compliant():
    checks = {
        "technical_specs": True,
        "warranty": True,
        "delivery_period": True,
        "price_quote": True,
        "seller_documents": True
    }

    result = verify_checks(checks)

    assert result["compliance_score"] == 100
    assert result["checks_passed"] == 5
    assert result["overall_status"] == "Ready for human review"


def test_partially_compliant():
    checks = {
        "technical_specs": True,
        "warranty": True,
        "delivery_period": True,
        "price_quote": True,
        "seller_documents": False
    }

    result = verify_checks(checks)

    assert result["compliance_score"] == 80
    assert result["checks_passed"] == 4
    assert result["overall_status"] == "Partially compliant"


def test_no_documents_compliant():
    checks = {
        "technical_specs": False,
        "warranty": False,
        "delivery_period": False,
        "price_quote": False,
        "seller_documents": False
    }

    result = verify_checks(checks)

    assert result["compliance_score"] == 0
    assert result["checks_passed"] == 0
    assert result["overall_status"] == "Needs more information"


def test_missing_checklist():
    result = verify_checks({})

    assert result["compliance_score"] == 0
    assert result["checks_passed"] == 0


def test_invalid_checklist():
    result = verify_checks(None)

    assert result["compliance_score"] == 0
    assert result["checks_passed"] == 0
