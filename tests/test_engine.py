
"""
VIX Core Engine Tests
Phase 1 - Rule & confidence validation
"""

from vix_core.engine.vix_engine import VIXEngine


def test_low_risk_approval():
    engine = VIXEngine(
        signals_path="signals/signals_v1.yaml",
        rules_path="rules/decision_rules_v1.yaml"
    )

    vehicle_input = {"confidence_score": 0.85}
    decision = engine.evaluate(vehicle_input)

    assert decision == "approve"


def test_medium_risk_manual_review():
    engine = VIXEngine(
        signals_path="signals/signals_v1.yaml",
        rules_path="rules/decision_rules_v1.yaml"
    )

    vehicle_input = {"confidence_score": 0.6}
    decision = engine.evaluate(vehicle_input)

    assert decision == "manual_review"


def test_high_risk_rejection():
    engine = VIXEngine(
        signals_path="signals/signals_v1.yaml",
        rules_path="rules/decision_rules_v1.yaml"
    )

    vehicle_input = {"confidence_score": 0.3}
    decision = engine.evaluate(vehicle_input)

    assert decision == "reject"
