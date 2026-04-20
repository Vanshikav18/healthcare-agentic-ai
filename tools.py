import json

def load_knowledge():
    with open("knowledge_base.json") as f:
        return json.load(f)

def detect_disease(user_input):
    data = load_knowledge()
    user_input = user_input.lower()

    for disease in data:
        if disease in user_input:
            return disease, data[disease]

    return None, None