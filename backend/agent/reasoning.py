import re


def get_ai_response(user_message):

    message = user_message.lower()

    response = {
        "intent": "",
        "doctor_type": "",
        "slot": "",
        "patient_name": ""
    }

    # Detect Intent
    if (
        "book" in message
        or "appointment" in message
        or "अपॉइंटमेंट" in user_message
        or "மருத்துவர்" in user_message
    ):

        response["intent"] = "book_appointment"

    elif (
        "cancel" in message
        or "रद्द" in user_message
    ):

        response["intent"] = "cancel_appointment"

    elif (
        "reschedule" in message
        or "change" in message
    ):

        response["intent"] = "reschedule_appointment"

    elif (
        "availability" in message
        or "available" in message
    ):

        response["intent"] = "check_availability"

    # Detect Doctor Type
    doctor_types = [
        "cardiologist",
        "dermatologist",
        "neurologist"
    ]

    for doctor in doctor_types:

        if doctor in message:
            response["doctor_type"] = doctor

    # Detect Time Slot
    slot_pattern = r"\d{1,2}:\d{2}\s?(AM|PM|am|pm|a\.m\.|p\.m\.)"

    slot_match = re.search(slot_pattern, user_message)

    if slot_match:
        response["slot"] = slot_match.group()

        response["slot"] = (
        response["slot"]
        .replace("a.m.", "AM")
        .replace("p.m.", "PM")
    )


    # Detect Patient Name
    name_patterns = [
        r"my name is (\w+)",
        r"i am (\w+)"
    ]

    for pattern in name_patterns:

        match = re.search(pattern, message)

        if match:
            response["patient_name"] = match.group(1)

    return response