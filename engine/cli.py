from engine.vix_engine import VIXEngine

def main():
    engine = VIXEngine(
        signals_path="signals/signals_v1.yaml",
        rules_path="rules/decision_rules_v1.yaml"
    )

    sample_vehicle = {
        "confidence_score": 0.72
    }

    decision = engine.evaluate(sample_vehicle)
    print("VIX Decision:", decision)

if __name__ == "__main__":
    main()
