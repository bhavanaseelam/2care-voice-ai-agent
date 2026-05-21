import speech_recognition as sr

recognizer = sr.Recognizer()

recognizer.pause_threshold = 2


def speech_to_text():

    with sr.Microphone() as source:

        print("\nListening...\n")

        recognizer.adjust_for_ambient_noise(
            source
        )

        audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=15
        )

    try:

        text = recognizer.recognize_google(
            audio
        )

        print("\nYou Said:\n")

        print(text)

        return text

    except Exception as e:

        print("\nSpeech Recognition Error\n")

        print(e)

        return ""