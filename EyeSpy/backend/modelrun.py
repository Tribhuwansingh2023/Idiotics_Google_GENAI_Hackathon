import streamlit as st
import joblib
import re

# --- Page Configuration ---
st.set_page_config(
    page_title="EyeSpy Fake News Detector",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Load Model & Vectorizer ---
try:
    vectorizer = joblib.load('vectorizer.jb')
    model = joblib.load('model.jb')
except FileNotFoundError:
    st.error("Model or vectorizer not found. Please ensure 'vectorizer.jb' and 'model.jb' are in the correct directory.")
    st.stop()

# --- Custom CSS for modern UI ---
st.markdown("""
<style>
    /* Core Styles */
    body {
        color: #ffffff;
        background-color: #0a0a0a;
    }
    .stApp {
        background: #0a0a0a;
    }
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Gradient Text */
    .gradient-text {
        background: linear-gradient(135deg, #00d4ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* Hero Section */
    .hero {
        text-align: center;
        padding: 4rem 1rem;
    }
    .hero h1 {
        font-size: clamp(2.5rem, 5vw, 4.5rem);
        line-height: 1.2;
        margin-bottom: 1rem;
    }
    .hero p {
        font-size: clamp(1.1rem, 2.5vw, 1.4rem);
        color: #b0b0b0;
        max-width: 800px;
        margin: 0 auto 2rem auto;
    }

    /* Main Content Area */
    .main-content {
        padding: 2rem 1rem;
        background: #1a1a1a;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        max-width: 900px;
        margin: 2rem auto;
    }
    
    /* Text Area */
    .stTextArea textarea {
        background: #0a0a0a;
        color: #ffffff;
        border: 1px solid #00d4ff;
        border-radius: 10px;
        min-height: 250px;
        font-family: 'Poppins', sans-serif;
    }

    /* Button */
    .stButton button {
        background: linear-gradient(135deg, #00d4ff, #00ff88);
        color: #0a0a0a;
        border: none;
        padding: 15px 35px;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        margin: 1rem auto;
        display: block;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(0, 212, 255, 0.3);
    }

    /* Result Display */
    .result-box {
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
        text-align: center;
        font-size: 1.2rem;
    }
    .result-real {
        background: rgba(0, 255, 136, 0.1);
        border: 1px solid #00ff88;
        color: #00ff88;
    }
    .result-fake {
        background: rgba(255, 107, 53, 0.1);
        border: 1px solid #ff6b35;
        color: #ff6b35;
    }
    .result-warning {
        background: rgba(255, 180, 0, 0.1);
        border: 1px solid #ffb400;
        color: #ffb400;
    }
</style>
""", unsafe_allow_html=True)

# --- UI Sections ---

# Hero Section
with st.container():
    st.markdown("""
    <div class="hero">
        <h1 class="gradient-text">EyeSpy Fake News Detector</h1>
        <p>Combat misinformation with AI. Paste the text of a news article below to check its authenticity.</p>
    </div>
    """, unsafe_allow_html=True)

# Main Analysis Section
with st.container():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.subheader("Analyze News Content")
    news_input = st.text_area(
        "Enter the news article text here:", 
        height=300,
        placeholder="Paste the full text of the news article you want to analyze..."
    )

    if st.button("Analyze with EyeSpy"):
        # Basic input validation
        cleaned_input = re.sub(r'\s+', ' ', news_input).strip()
        
        if len(cleaned_input) < 50: # Check for minimum length
            st.markdown("""
            <div class="result-box result-warning">
                <strong>⚠️ Please enter more text.</strong><br>
                <small>For an accurate analysis, please provide at least 50 characters.</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            # --- Prediction Logic ---
            with st.spinner("Analyzing..."):
                transformed_input = vectorizer.transform([cleaned_input])
                prediction = model.predict(transformed_input)
                prediction_proba = model.predict_proba(transformed_input)

                if prediction[0] == 1: # REAL
                    confidence = prediction_proba[0][1] * 100
                    st.markdown(f"""
                    <div class="result-box result-real">
                        <strong>✅ The news article appears to be REAL</strong><br>
                        Confidence: <strong>{confidence:.2f}%</strong>
                    </div>
                    """, unsafe_allow_html=True)
                else: # FAKE
                    confidence = prediction_proba[0][0] * 100
                    st.markdown(f"""
                    <div class="result-box result-fake">
                        <strong>⚠️ This news article is likely FAKE</strong><br>
                        Confidence: <strong>{confidence:.2f}%</strong>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem 0; color: #b0b0b0;">
    <p>© 2025 EyeSpy | Made By team IDIOTICS ❤️(GEN AI HACKATHON) </p>
</div>
""", unsafe_allow_html=True)
