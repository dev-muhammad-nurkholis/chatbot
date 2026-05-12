import os
from dotenv import load_dotenv
from google import genai

gemini_api_key = os.getenv("GEMINI_API_KEY")
load_dotenv(override=True)

client = genai.Client()

print("Aplikasi Chatbot Sederhana")
print("==================================")
print("Silakan untuk bertanya kepada saya")
print("Ketik 'keluar' untuk keluar.\n")

def send_message(message):
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = message
    )
    return response

while(True):
    input_text = input("Kamu : ")
    if input_text.lower() == "keluar":
        print("Terima kasih telah bertanya kepada saya")
        break   
    
    result = send_message(input_text)
    print("Saya : ", result.text )
