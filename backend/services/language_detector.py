def detect_language(text):

    # Hindi Detection
    hindi_chars = range(0x0900, 0x097F)

    # Tamil Detection
    tamil_chars = range(0x0B80, 0x0BFF)

    for char in text:

        unicode_value = ord(char)

        if unicode_value in hindi_chars:

            return "Hindi"

        if unicode_value in tamil_chars:

            return "Tamil"

    return "English"