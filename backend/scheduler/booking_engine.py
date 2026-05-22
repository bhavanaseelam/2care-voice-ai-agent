from scheduler.mock_data import doctors_data

appointments = []

# Stores booked appointments
booked_appointments = []


# Check available slots
def check_availability(doctor_type):

    if doctor_type not in doctors_data:

        return {
            "status": "error",
            "message": "Doctor type not found"
        }

    return {
        "status": "success",
        "doctor": doctors_data[doctor_type]["doctor_name"],
        "available_slots":
            doctors_data[doctor_type]["available_slots"]
    }


# Book appointment
def book_appointment(patient_name, doctor_type, slot):

    # Check doctor exists
    if doctor_type not in doctors_data:

        return {
            "status": "error",
            "message": "Doctor not available"
        }

    # Check slot exists
    available_slots = doctors_data[doctor_type]["available_slots"]

    if slot not in available_slots:

        return {
            "status": "error",
            "message": "Selected slot unavailable"
        }

    # Prevent double booking
    for appointment in booked_appointments:

        if (
            appointment["doctor_type"] == doctor_type
            and appointment["slot"] == slot
        ):

            return {
                "status": "conflict",
                "message": "Slot already booked",
                "alternative_slots": available_slots
            }

    # Save appointment
    appointment = {
        "patient_name": patient_name,
        "doctor_type": doctor_type,
        "doctor_name":
            doctors_data[doctor_type]["doctor_name"],
        "slot": slot,
        "status": "confirmed"
    }

    booked_appointments.append(appointment)

    appointments.append(appointment)

    return {
        "status": "success",
        "message": "Appointment booked successfully",
        "appointment": appointment
    }


# Cancel appointment
def cancel_appointment(patient_name):

    for appointment in booked_appointments:

        if appointment["patient_name"] == patient_name:

            booked_appointments.remove(appointment)

            return {
                "status": "success",
                "message": "Appointment cancelled"
            }

    return {
        "status": "error",
        "message": "No appointment found"
    }


# Reschedule appointment
def reschedule_appointment(
    patient_name,
    new_slot
):

    for appointment in booked_appointments:

        if appointment["patient_name"] == patient_name:

            appointment["slot"] = new_slot

            return {
                "status": "success",
                "message": "Appointment rescheduled",
                "updated_appointment": appointment
            }

    return {
        "status": "error",
        "message": "Appointment not found"
    }


# View all bookings
def get_all_appointments():

    return booked_appointments