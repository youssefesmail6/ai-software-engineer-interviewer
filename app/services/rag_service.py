from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import json
import os

class RAGService:
    def __init__(self):
        # Using a reliable model for local embeddings
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = None
        self.index_path = os.path.join(os.getcwd(), "faiss_index")

    def load_data(self):
        # Ensure path is relative to project root
        data_path = os.path.join(os.getcwd(), "data", "questions.json")
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # We embed the Question + Answer pair for better context retrieval
        texts = [f"Question: {q['question']}\nAnswer: {q['answer']}" for q in data]
        metadatas = [{"id": q.get("id"), "category": q.get("category")} for q in data]

        # Check if the FAISS index file actually exists inside the directory
        index_file = os.path.join(self.index_path, "index.faiss")
        
        if os.path.exists(index_file):
            try:
                self.db = FAISS.load_local(
                    self.index_path, 
                    self.embeddings, 
                    allow_dangerous_deserialization=True
                )
            except Exception as e:
                print(f"Error loading FAISS index: {e}. Rebuilding...")
                self._build_and_save(texts, metadatas)
        else:
            self._build_and_save(texts, metadatas)

    def _build_and_save(self, texts, metadatas):
        # Create FAISS index from scratch
        self.db = FAISS.from_texts(
            texts,
            embedding=self.embeddings,
            metadatas=metadatas
        )
        # Save it locally so we don't have to re-embed every time
        self.db.save_local(self.index_path)

    def retrieve(self, query, k=2):
        if not self.db:
            self.load_data()
        return self.db.similarity_search(query, k=k)
