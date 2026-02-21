import os
import requests
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        # For OpenRouter, you should specify the model in "provider/model" format or just model name if it's unique
        # Example: "openai/gpt-3.5-turbo" or "meta-llama/llama-3.2-3b-instruct:free"
        self.model = os.getenv("LLM_MODEL", "openai/gpt-3.5-turbo")

    def ask_question(self, context):
        if not self.api_key:
            return "Error: OPENROUTER_API_KEY not found in .env"
            
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "X-Title": "AI Interviewer"             # Optional for OpenRouter
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a senior software engineer interviewer."},
                {"role": "user", "content": f"Based on this context, ask one technical interview question:\n{context}"}
            ],
            "temperature": 0.7
        }

        try:
            res = requests.post(url, headers=headers, json=payload)
            res.raise_for_status()
            return res.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error calling LLM: {str(e)}"
