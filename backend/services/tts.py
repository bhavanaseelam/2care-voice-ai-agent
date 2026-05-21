import pyttsx3


engine = pyttsx3.init()


# Voice Speed
engine.setProperty(
    "rate",
    165
)

# Volume
engine.setProperty(
    "volume",
    1
)


def speak_text(text):

    print("\nAI Speaking...\n")

    engine.say(text)

    engine.runAndWait()