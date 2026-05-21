from services.tts import (
    speak_text
)

message = """
Your appointment has been booked successfully.
"""

print(message)

speak_text(message)