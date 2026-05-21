from memory.session_memory import (
    save_session_memory,
    get_session_memory
)

from memory.persistent_memory import (
    save_patient_memory,
    get_patient_memory
)

print("\nSESSION MEMORY TEST\n")

save_session_memory(
    "session_1",
    {
        "intent": "book_appointment",
        "doctor": "cardiologist"
    }
)

session_data = get_session_memory(
    "session_1"
)

print(session_data)

print("\nPERSISTENT MEMORY TEST\n")

save_patient_memory(
    "bhavana",
    {
        "preferred_language": "Hindi",
        "preferred_doctor": "cardiologist"
    }
)

patient_data = get_patient_memory(
    "bhavana"
)

print(patient_data)