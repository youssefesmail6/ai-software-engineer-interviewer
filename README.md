# 🤖 AI Technical Interviewer (RAG-Powered)

Experience a professional technical interview powered by AI. This application uses **Retrieval-Augmented Generation (RAG)** to provide context-aware questions and senior-level evaluations of your answers.

## 🚀 Key Features
- **RAG-Powered Context**: Uses **FAISS** and LangChain for ultra-fast, reliable local vector storage (compatible with Python 3.14).
- **Unified AI Engine**: All power comes from **OpenRouter**, consolidating your API management for both question generation and evaluation.
- **Detailed AI Evaluation**: Provides a senior-level breakdown of your answers, scoring you on correctness, clarity, and completeness.
- **Dynamic Session History**: Track your current interview progress and feedback in real-time.
- **Modern UI**: A premium, responsive web interface built with **Streamlit**.

---

## 🛠️ Project Structure
```text
ai_interviewer/
├── app/
│   ├── services/
│
│   │   ├── eval_service.py      # LLM Evaluation via OpenRouter
│   │   ├── interview_service.py # Core orchestration
│   │   ├── llm_service.py       # Question generation via OpenRouter
│   │   └── rag_service.py       # FAISS & Embedding logic
│   
├── data/
│   └── questions.json           # Your technical Q&A dataset
├── faiss_index/                 # Local vector database (auto-generated)
├── main.py                      # Streamlit App Entry Point
├── requirements.txt             # Project dependencies (optimized for Python 3.14)
└── README.md                    # Documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone & Navigate
```bash
git clone <repository-url>
cd ai_interviewer
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory:
```env
OPENROUTER_API_KEY=your_openrouter_api_key
LLM_MODEL=openai/gpt-3.5-turbo  # Model used for questions & evaluation
```

### 3. Setup Virtual Environment (Python 3.10 - 3.14+)
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run
Launch the application shell:
```bash
streamlit run main.py
```

---

## 📚 Technologies Used
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Vector DB**: [FAISS](https://github.com/facebookresearch/faiss) (Meta)
- **Embeddings**: [HuggingFace (all-MiniLM-L6-v2)](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **Framework**: [LangChain](https://www.langchain.com/)
- **LLM Gateway**: [OpenRouter](https://openrouter.ai/)
