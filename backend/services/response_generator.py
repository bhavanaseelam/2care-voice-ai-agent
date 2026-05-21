def generate_response(
    language,
    tool_response
):

    status = tool_response.get(
        "status"
    )

    # ENGLISH
    if language == "English":

        if status == "success":

            return "Your appointment has been booked successfully."

        return "Sorry, something went wrong."

    # HINDI
    elif language == "Hindi":

        if status == "success":

            return "आपकी अपॉइंटमेंट सफलतापूर्वक बुक हो गई है।"

        return "माफ़ कीजिए, कुछ गलत हो गया।"

    # TAMIL
    elif language == "Tamil":

        if status == "success":

            return "உங்கள் நேர்முகம் வெற்றிகரமாக பதிவு செய்யப்பட்டது."

        return "மன்னிக்கவும், ஏதோ தவறு நடந்தது."

    return "Response unavailable."