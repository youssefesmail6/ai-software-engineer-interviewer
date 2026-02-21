import os
import requests
from dotenv import load_dotenv

load_dotenv()

class EvalService:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        # You can use a stronger model for evaluation like Gemini Flash or Pro via OpenRouter
        self.model = os.getenv("LLM_MODEL", "openai/gpt-3.5-turbo")

    def evaluate(self, question, answer):
        if not self.api_key:
            return "Error: OPENROUTER_API_KEY not found in .env"

        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "X-Title": "AI Interviewer Evaluator"
        }

        prompt = f"""
        You are a senior software engineering interviewer.
        
        Evaluate the candidate's answer based on the following:
        
        Question: {question}
        Candidate Answer: {answer}

        Please provide:
        1. Correctness Score (out of 10)
        2. Clarity Score (out of 10)
        3. Completeness Score (out of 10)
        4. Detailed Feedback (Strengths and Weaknesses)
        5. A Model Answer
        
        Format the response clearly with markdown headers.
        """

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a professional technical interviewer providing detailed feedback."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3 # Lower temperature for more consistent evaluation
        }

        try:
            res = requests.post(url, headers=headers, json=payload)
            res.raise_for_status()
            return res.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error calling OpenRouter for evaluation: {str(e)}"
