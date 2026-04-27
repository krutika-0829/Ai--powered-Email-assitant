import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def req_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json = {
            "model" : "mistral",
            "prompt" : prompt,
            "stream" : False
        }
    )


    return response.json()["response"]

def summarize(email):
    clean_text = " ".join(email.split())
    prompt = f""" 
    You are an AI email assistant.
    Summarize  email into 2 to 3 lines in simple words .
    Return JSON format only :
    {{
     "Summary" : "..."
    }}
    \"\"\"{clean_text}\"\"\"
    """
    return req_llm(prompt)

def tone_detect(email):
    clean_text = " ".join(email.split())
    prompt = f"""
     You are an AI email assistant.
     Classify the tone of the email.

    Definitions:
    - Formal: Professional, structured, official language
    - Informal: Casual, friendly, conversational language
    - Angry: Contains frustration, complaints, or strong negative emotion
    - Polite: Respectful and courteous language with formal tone
    - Neutral: No strong emotional tone

    Choose ONLY one tone from:
    Formal, Informal, Angry, Polite, Neutral
    YOU MUST RETURN JSON FORMAT ONLY:
    {{
    "Tone" : "..."
    }}
    \"\"\"{clean_text}\"\"\"
    """
    return  req_llm(prompt)

def get_tone(email):
    result = tone_detect(email)
    try:
        return json.loads(result)["Tone"]
    except:
        return "Neutral"

def generate_reply(email,tone):
    clean_text = " ".join(email.split())
    prompt = f"""
    You are an AI email assistant.

Write a reply to the email.

Detected tone: {tone}

Instructions:
- Match the reply tone with the detected tone
- If Informal → casual, friendly reply
- If Formal → professional reply
- If Angry → calm and polite reply
- If Polite → respectful reply
- If Neutral → balanced reply

Include:
1. Subject line
2. Greeting
3. Clear and concise body

Return ONLY valid JSON:
{{
  "subject": "...",
  "reply": "..."
}}

Rules:
- No extra text
- Only JSON output

    Email:
    \"\"\"{clean_text}\"\"\"
    """
    return req_llm(prompt)