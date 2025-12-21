"""
VIX Core Engine – Phase 1
Vehicle Intelligence X
Rule-based + signal-driven decision engine
"""

import yaml
from pathlib import Path


class VIXEngine:
    def __init__(self, signals_path, rules_path):
        self.signals = self._load_yaml(signals_path)
        self.rules = self._load_yaml(rules_path)

    def _load_yaml(self, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def evaluate(self, vehicle_input):
        """
        vehicle_input: dict with raw vehicle data
        """
        confidence_score = vehicle_input.get("confidence_score", 0)

        thresholds = self.rules["risk_thresholds"]
        actions = self.rules["actions"]

        if confidence_score < thresholds["high_risk"]["confidence_score_below"]:
            return actions["high_risk"]

        if thresholds["medium_risk"]["confidence_score_between"][0] <= confidence_score <= thresholds["medium_risk"]["confidence_score_between"][1]:
            return actions["medium_risk"]

        if confidence_score > thresholds["low_risk"]["confidence_score_above"]:
            return actions["low_risk"]

        return "manual_review"
