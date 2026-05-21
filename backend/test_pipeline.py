from agent.reasoning import get_ai_response
from agent.tools import execute_tool
from services.language_detector import (
    detect_language
)

from services.response_generator import (
    generate_response
)
from memory.session_memory import (
    save_session_memory
)

from memory.persistent_memory import (
    save_patient_memory
)

user_message = """
मुझे हृदय रोग विशेषज्ञ के साथ
10:00 AM पर अपॉइंटमेंट चाहिए।
मेरा नाम भवाना है।
"""

language = detect_language(
    user_message
)

# STEP 1: AI REASONING
ai_response = get_ai_response(
    user_message
)
save_session_memory(
    "session_1",
    ai_response
)

print("\nAI RESPONSE:\n")

print(ai_response)

# STEP 2: TOOL EXECUTION
tool_response = execute_tool(
    ai_response
)

final_response = generate_response(
    language,
    tool_response
)

print("\nFINAL VOICE RESPONSE:\n")

print(final_response)

save_patient_memory(
    ai_response["patient_name"],
    {
        "preferred_doctor":
            ai_response["doctor_type"],

        "last_booked_slot":
            ai_response["slot"]
    }
)

print("\nTOOL RESPONSE:\n")

print(tool_response)