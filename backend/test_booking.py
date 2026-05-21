from scheduler.booking_engine import (
    check_availability,
    book_appointment,
    cancel_appointment,
    reschedule_appointment,
    get_all_appointments
)

print("\nChecking Availability\n")

print(
    check_availability("cardiologist")
)

print("\nBooking Appointment\n")

print(
    book_appointment(
        "Bhavana",
        "cardiologist",
        "10:00 AM"
    )
)

print("\nTrying Double Booking\n")

print(
    book_appointment(
        "Rahul",
        "cardiologist",
        "10:00 AM"
    )
)

print("\nRescheduling Appointment\n")

print(
    reschedule_appointment(
        "Bhavana",
        "11:00 AM"
    )
)

print("\nAll Appointments\n")

print(
    get_all_appointments()
)

print("\nCancelling Appointment\n")

print(
    cancel_appointment("Bhavana")
)

print("\nFinal Appointments\n")

print(
    get_all_appointments()
)