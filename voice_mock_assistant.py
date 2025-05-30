import streamlit as st
import openai
import json
import speech_recognition as sr

# --- Configuration ---
openai.api_base = "https://openrouter.ai/api/v1"
from config import OPENROUTER_API_KEY
openai.api_key = OPENROUTER_API_KEY


# Load product knowledge base
with open("expanded_product_info.json", "r") as f:
    product_info = json.load(f)

# --- Streamlit UI ---
st.set_page_config(page_title="GroMo AI Assistant", layout="centered")
st.title("🤖 GroMo AI Assistant for GPs ")

# Select Product Type and Company
product_type = st.selectbox("Select Product Type", list(product_info.keys()))
company = st.selectbox("Select Company", list(product_info[product_type].keys()))
language = st.selectbox("Reply Language", ["English", "Hindi"])

# Voice Input
recognizer = sr.Recognizer()
message = ""

if st.button("🎙 Start Listening"):
    with sr.Microphone() as source:
        st.info("Listening... Please speak your customer's message")
        try:
            audio = recognizer.listen(source, timeout=5)
            message = recognizer.recognize_google(audio, language="hi-IN" if language == "Hindi" else "en-IN")
            st.session_state["captured_message"] = message
            st.success(f"Customer said: {message}")
        except Exception as e:
            st.error("Couldn't capture audio. Try again.")

# OR allow manual input
message = st.text_input("Or type the customer's message manually:", value=st.session_state.get("captured_message", ""))

# Call LLM
if st.button("💬 Get AI Suggestion") and message:
    # Inject product facts
    facts = product_info[product_type][company]
    fact_lines = "\n".join([f"- {k.replace('_', ' ').capitalize()}: {v}" for k, v in facts.items()])

    # Build prompt
    prompt = f"""
You are a helpful assistant supporting a GroMo Partner during a customer conversation.
The partner is selling a {product_type} from {company}.

Here are the known facts about this product:
{fact_lines}

Customer said: "{message}"

Reply in {language}. Format:
Pitch: <short convincing pitch line>
Objection Handling: <line to handle doubt/confusion>
If the question is not answerable with the facts, say: 'Please check with the provider for exact terms.'
"""

    try:
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",  # You can switch to another supported model
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response["choices"][0]["message"]["content"]
        st.markdown("### 🤖 AI Assistant Reply")
        st.markdown(reply)
    except Exception as e:
        st.error(f"Error calling LLM: {e}")

