from scheduler.booking_engine import (
    check_availability,
    book_appointment,
    cancel_appointment,
    reschedule_appointment
)


def execute_tool(ai_response):

    intent = ai_response.get("intent")

    doctor_type = ai_response.get("doctor_type")

    slot = ai_response.get("slot")

    patient_name = ai_response.get("patient_name")

    # BOOK APPOINTMENT
    if intent == "book_appointment":

        return book_appointment(
            patient_name,
            doctor_type,
            slot
        )

    # CHECK AVAILABILITY
    elif intent == "check_availability":

        return check_availability(
            doctor_type
        )

    # CANCEL APPOINTMENT
    elif intent == "cancel_appointment":

        return cancel_appointment(
            patient_name
        )

    # RESCHEDULE APPOINTMENT
    elif intent == "reschedule_appointment":

        return reschedule_appointment(
            patient_name,
            slot
        )

    return {
        "status": "error",
        "message": "Unknown intent"
    }