from datetime import datetime, timedelta
import json

def load_knowledge():
    with open("knowledge_base.json") as f:
        return json.load(f)

def get_disease_data(disease):
    data = load_knowledge()
    return data.get(disease.lower(), {})

def validate_treatment(treatment):
    valid = ["Insulin therapy", "Paracetamol", "Exercise", "Diet control"]
    return treatment in valid

def validate_resources():
    return {
        "doctor_available": True,
        "medicine_available": True,
        "time_slot_available": True
    }

def generate_schedule(steps):
    schedule = []
    start = datetime.now()

    for i, step in enumerate(steps):
        schedule.append({
            "step": step,
            "time": (start + timedelta(hours=i)).strftime("%Y-%m-%d %H:%M")
        })

    return schedule