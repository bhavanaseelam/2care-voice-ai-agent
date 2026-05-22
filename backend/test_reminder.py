from scheduler.booking_engine import book_appointment
from scheduler.reminder_engine import send_reminders


book_appointment(
    patient_name="Bhavana",
    doctor_type="cardiologist",
    slot="10:00 AM"
)

book_appointment(
    patient_name="Rahul",
    doctor_type="dermatologist",
    slot="2:00 PM"
)

send_reminders()