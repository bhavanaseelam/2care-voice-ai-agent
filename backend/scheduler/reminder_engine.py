from scheduler.booking_engine import appointments
from services.response_generator import generate_response


def send_reminders():

    print("\nOUTBOUND AI REMINDER SYSTEM\n")

    if not appointments:
        print("No appointments found")
        return

    for appointment in appointments:

        patient_name = appointment["patient_name"]
        doctor_name = appointment["doctor_name"]
        slot = appointment["slot"]

        reminder_message = (
            f"Hello {patient_name}, "
            f"this is a reminder for your appointment with "
            f"{doctor_name} at {slot}."
        )

        final_message = generate_response(
            "English",
            {
                "status": "success",
                "message": reminder_message
            }
        )

        print(final_message)