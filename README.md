GroMo AI Assistant 🧑‍💻

An AI-powered assistant that helps GroMo Partners pitch financial products confidently during live customer conversations. This tool combines voice recognition, LLM reasoning, and product-specific context to generate personalized sales pitches and objection-handling messages in real time.

🌐 Live Demo Features

🔊 Voice-to-text input (via mic)

🤖 Real-time LLM integration using OpenRouter

📂 Smart prompts with product + company context

🔄 JSON-powered product knowledge base

🌐 Hindi / English response options

✅ Brand-safe replies with guardrails

💡 How It Works

The GroMo Partner selects a product and company

Speaks or types the customer’s question

The app fetches product facts from a JSON file

These facts + the question are sent to a language model

The LLM returns a confident pitch and objection response

🔧 Installation

# Clone the repo
https://github.com/AnushaMittal1234/GROMO-AI-Assistant-by-Bitmask.git
cd gromo-ai-assistant

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

🔍 Project Structure

gromo-ai-assistant/
├── app/
│   └── gromo_ai_assistant.py
├── data/
│   ├── expanded_product_info.json
│   └── config_sample.py
├── docs/
│   └── README.md
├── .gitignore
├── requirements.txt

🔑 API Key Setup

Create a file config.py in the /data folder with your OpenRouter API key:

# config.py
OPENROUTER_API_KEY = "your-api-key-here"

Never upload your real config.py to GitHub. Use .gitignore to exclude it.

🎓 Technologies Used

Python

Streamlit

OpenRouter API (for LLM)

Google Speech Recognition

📚 Use Cases

Helps GroMo Partners pitch products more confidently

Assists with objection handling during real customer calls

Works across categories like Credit Cards, Loans, Savings A/c

🚀 Future Improvements

Integrate real-time call transcript APIs

Add support for retrieval-based answers from docs

Voice reply (TTS)

Auto-detection of product from query

🙏 Built With Love By

Team Bitmask — FinArva AI Hackathon 2025
