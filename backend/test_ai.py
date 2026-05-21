from agent.reasoning import get_ai_response

user_message = """
मुझे कल हृदय रोग विशेषज्ञ से
10 बजे अपॉइंटमेंट चाहिए।
मेरा नाम भावना है।
"""

response = get_ai_response(user_message)

print("\nAI RESPONSE:\n")

print(response)