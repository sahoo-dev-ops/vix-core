from fastapi import FastAPI
from engine.vix_engine import VIXEngine

app = FastAPI(
    title="VIX API",
    version="2.0",
    description="Vehicle Intelligence X - Risk Decision API"
)

# Load engine once (important)
engine = VIXEngine(
    signals_path="signals/signals_v1.yaml",
    rules_path="rules/decision_rules_v1.yaml"
)

@app.get("/")
def health_check():
    return {"status": "VIX API is running"}

@app.post("/evaluate")
def evaluate_vehicle(vehicle_input: dict):
    decision = engine.evaluate(vehicle_input)
    return {
        "decision": decision,
        "input": vehicle_input
    }
