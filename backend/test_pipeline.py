from agent.reasoning import get_ai_response
from agent.tools import execute_tool


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

print("\nAI RESPONSE:\n")

print(ai_response)

# STEP 2: TOOL EXECUTION
tool_response = execute_tool(
    ai_response
)

print("\nTOOL RESPONSE:\n")

print(tool_response)