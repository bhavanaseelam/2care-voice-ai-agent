from services.language_detector import (
    detect_language
)

from services.response_generator import (
    generate_response
)

# TEST INPUTS
english_text = "I want to book appointment"

hindi_text = "मुझे अपॉइंटमेंट बुक करना है"

tamil_text = "எனக்கு நேர்முகம் பதிவு செய்ய வேண்டும்"

# DETECT LANGUAGES
print("\nENGLISH DETECTION\n")

english_language = detect_language(
    english_text
)

print(english_language)

print("\nHINDI DETECTION\n")

hindi_language = detect_language(
    hindi_text
)

print(hindi_language)

print("\nTAMIL DETECTION\n")

tamil_language = detect_language(
    tamil_text
)

print(tamil_language)

# RESPONSE TEST
mock_response = {
    "status": "success"
}

print("\nHINDI RESPONSE\n")

print(
    generate_response(
        "Hindi",
        mock_response
    )
)

print("\nTAMIL RESPONSE\n")

print(
    generate_response(
        "Tamil",
        mock_response
    )
)