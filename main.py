from fastapi import FastAPI
from typing import Optional

app = FastAPI(title="CreditScore-API", description="Simuliert eine Bonitätsprüfung")

@app.get("/check")
def check_credit(name: str):
    """Prüft die Bonität basierend auf dem Namen."""
    first_letter = name.strip()[0].upper()
    score = 0.85 if first_letter < 'N' else 0.42
    return {
        "customer": name,
        "credit_score": score,
        "decision": "ACCEPT" if score > 0.5 else "REJECT"
    }