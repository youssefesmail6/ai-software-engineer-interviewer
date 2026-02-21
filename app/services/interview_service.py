from .rag_service import RAGService
from .llm_service import LLMService
from .eval_service import EvalService

class InterviewService:
    def __init__(self):
        self.rag = RAGService()
        self.llm = LLMService()
        self.eval = EvalService()
        self.rag.load_data()

    def generate_question(self, topic="software engineering interview"):
        docs = self.rag.retrieve(topic)
        if docs:
            context = docs[0].page_content
            return self.llm.ask_question(context)
        return "No relevant context found to generate a question."

    def evaluate_answer(self, question, answer):
        return self.eval.evaluate(question, answer)
