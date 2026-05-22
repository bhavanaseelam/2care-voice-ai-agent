from fastapi import FastAPI
from pydantic import BaseModel

from agent.reasoning import (
    get_ai_response
)

from agent.tools import (
    execute_tool
)

from services.response_generator import (
    generate_response
)

from services.language_detector import (
    detect_language
)

from memory.persistent_memory import (
    save_patient_memory
)

from scheduler.booking_engine import (
    get_all_appointments
)

from services.tts import (
    speak_text
)


app = FastAPI()


# REQUEST MODEL

class VoiceRequest(BaseModel):

    message: str


@app.get("/")
def home():

    return {
        "message": "2Care Voice AI Agent Running Successfully"
    }


# MAIN VOICE AI ENDPOINT

@app.post("/voice-agent")
def voice_agent(request: VoiceRequest):

    user_message = request.message

    # Language Detection
    language = detect_language(
        user_message
    )

    # AI Reasoning
    ai_response = get_ai_response(
        user_message
    )

    # Tool Execution
    tool_response = execute_tool(
        ai_response
    )

    # Final Response
    final_response = generate_response(
        language,
        tool_response
    )

    # Voice Output
    # speak_text(final_response)

    # Save Memory
    save_patient_memory(
        ai_response["patient_name"],
        {
            "preferred_doctor":
            ai_response["doctor_type"],

            "last_booked_slot":
            ai_response["slot"]
        }
    )

    return {
        "language": language,
        "ai_response": ai_response,
        "tool_response": tool_response,
        "final_response": final_response
    }


# GET APPOINTMENTS

@app.get("/appointments")
def appointments():

    return {
        "appointments":
        get_all_appointments()
    }