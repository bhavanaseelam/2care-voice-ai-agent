from agent.reasoning import get_ai_response
from agent.tools import execute_tool
from memory.session_memory import (
    save_session_memory
)

from memory.persistent_memory import (
    save_patient_memory
)

user_message = """
I want to book an appointment
with a cardiologist
at 10:00 AM.
My name is Bhavana.
"""

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