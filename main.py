from fastapi import FastAPI
import uuid

app = FastAPI()

# TOOL 1: Bonität prüfen
@app.get("/check")
def check_credit(name: str):
    # Einfache Logik für den PoC: Namen A-M bekommen ACCEPT, N-Z bekommen REJECT
    first_letter = name.strip()[0].upper()
    score = 0.85 if first_letter < 'N' else 0.12
    return {
        "customer": name,
        "credit_score": score,
        "decision": "ACCEPT" if score > 0.5 else "REJECT"
    }

# TOOL 2: Order Processor
@app.get("/execute")
def execute_order(customer: str, status: str, total_price: float):
    """
    Verarbeitet die Bestellung und liefert rein technische Variablen zurück.
    Der Agent nutzt diese Daten, um die finale Antwort zu formulieren.
    """
    if status == "BESTELLUNG":
        # Generiert eine zufällige ID, z.B. ORD-A1B2C3
        random_id = f"ORD-{uuid.uuid4().hex[:6].upper()}"
        
        return {
            "success": True,
            "order_id": random_id,
            "logistics_status": "READY_FOR_SHIPPING",
            "estimated_delivery": "2-3 Werktage",
            "total_price_billed": total_price
        }
    
    elif status == "OPPORTUNITY":
        return {
            "success": False,
            "reason": "INSUFFICIENT_STOCK",
            "reserved_quantity": 5, 
            "next_step": "SALES_FOLLOW_UP",
            "info": "Bestand zu niedrig für Sofortversand."
        }
    
    return {
        "success": False, 
        "reason": "UNKNOWN_STATUS",
        "info": "Der übermittelte Status konnte nicht verarbeitet werden."
    }
