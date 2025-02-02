import requests
import os 
from dotenv import load_dotenv 
import json

load_dotenv()

# Retrieve API key from environment variables
API_KEY = os.getenv("GEMINI_API_KEY")

def test_gemini():
    # Example endpoint and API key
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "contents": [{
        "parts":[{"text": "Which of the following is written by Miranda?\nA) Hamilton\nB) The Perfect Stranger\nC) Pride and Prejudice"}]
    }],
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            response_data = json.loads(response.text)
            text_response = response_data['candidates'][0]['content']['parts'][0]['text']
            print("Gemini Response:")
            print(text_response)  # Print the API's response
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_gemini()
