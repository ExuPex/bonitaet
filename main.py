from fastapi import FastAPI

app = FastAPI()

# TOOL 1: Bonität prüfen
@app.get("/check")
def check_credit(name: str):
    first_letter = name.strip()[0].upper()
    score = 0.85 if first_letter < 'N' else 0.42
    return {
        "customer": name,
        "credit_score": score,
        "decision": "ACCEPT" if score > 0.5 else "REJECT"
    }

# TOOL 2: Bestellung ausführen
@app.get("/execute")
def execute_order(order_id: str, action: str):
    # action ist entweder 'deliver' oder 'cancel'
    status = "ERFOLGREICH" if action.lower() == "deliver" else "STORNIERT"
    return {
        "order_id": order_id,
        "status": status,
        "message": f"Die Bestellung wurde {status}."
    }
