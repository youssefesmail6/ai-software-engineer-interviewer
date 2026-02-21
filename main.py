import streamlit as st
import os
from app.services.interview_service import InterviewService
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Technical AI Interviewer",
    page_icon="🤖",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
    }
    .stTextArea>div>div>textarea {
        border-radius: 10px;
    }
    .header {
        color: #2c3e50;
        text-align: center;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Service
@st.cache_resource
def get_service():
    return InterviewService()

interviewer = get_service()

# --- HEADER ---
st.markdown("<h1 class='header'>🤖 Technical AI Interviewer</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- SESSION STATE ---
if 'question' not in st.session_state:
    st.session_state.question = None
if 'feedback' not in st.session_state:
    st.session_state.feedback = None

# --- MAIN INTERFACE ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Interview Panel")
    
    if st.button("Generate Random Question"):
        with st.spinner("Thinking of a question..."):
            st.session_state.question = interviewer.generate_question()
            st.session_state.feedback = None

    if st.session_state.question:
        st.info(f"**Question:** {st.session_state.question}")
        
        user_answer = st.text_area("Your Answer:", placeholder="Type your technical explanation here...", height=200)
        
        if st.button("Submit Answer"):
            if user_answer.strip():
                with st.spinner("Evaluating your response..."):
                    st.session_state.feedback = interviewer.evaluate_answer(st.session_state.question, user_answer)
            else:
                st.warning("Please provide an answer first!")

with col2:
    st.subheader("📊 Feedback & Results")
    if st.session_state.feedback:
        st.markdown(st.session_state.feedback)
    else:
        st.write("Results and detailed evaluation will appear here after submission.")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Settings & Info")
    st.write("This AI Interviewer uses **RAG (Retrieval-Augmented Generation)** to fetch context from a knowledge base and evaluate your answers.")
    
    st.divider()
    
    api_status_gemini = "✅ Configured" if os.getenv("GOOGLE_API_KEY") else "❌ Missing"
    api_status_openrouter = "✅ Configured" if os.getenv("OPENROUTER_API_KEY") else "❌ Missing"
    
    st.write(f"**Gemini API:** {api_status_gemini}")
    st.write(f"**OpenRouter API:** {api_status_openrouter}")
    
    if st.button("Clear Session"):
        st.session_state.question = None
        st.session_state.feedback = None
        st.rerun()

    st.divider()
    st.caption("v1.0.0 | RAG-based AI Interviewer")
