def doctor_response(user_text):
    """
    Core medical logic (English).
    This can later be replaced with an LLM.
    """
    user_text = user_text.lower()

    if "fever" in user_text:
        return "You may have a mild infection. Drink plenty of fluids and consult a doctor if fever persists."
    elif "headache" in user_text:
        return "Headaches can occur due to stress or dehydration. Rest well and stay hydrated."
    elif "cold" in user_text or "cough" in user_text:
        return "Common cold symptoms usually resolve in a few days. Warm fluids may help."
    else:
        return "I recommend consulting a healthcare professional for accurate diagnosis."


