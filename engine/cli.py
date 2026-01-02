import argparse
from engine.vix_engine import VIXEngine


def main():
    parser = argparse.ArgumentParser(description="VIX Engine CLI")
    parser.add_argument(
        "--confidence-score",
        type=float,
        required=True,
        help="Confidence score between 0 and 1"
    )

    args = parser.parse_args()

    engine = VIXEngine(
        signals_path="signals/signals_v1.yaml",
        rules_path="rules/decision_rules_v1.yaml",
    )

    decision = engine.evaluate({
        "confidence_score": args.confidence_score
    })

    print(f"VIX Decision: {decision}")


if __name__ == "__main__":
    main()
