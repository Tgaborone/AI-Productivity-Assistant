# AI-Powered Productivity Assistant

Fast MVP: AI-powered workplace productivity assistant demonstrating:

- Email generation
- Meeting summarization (from pasted transcript)
- Task planning (generate actionable tasks from goals)
- Basic chatbot prototype

Tech stack
- Python 3.10+
- Streamlit for quick UI
- OpenAI-compatible API (set OPENAI_API_KEY or other provider key)

Quick start
1. Clone this repo
2. Create virtualenv: `python -m venv .venv && source .venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Set your API key in environment: `export OPENAI_API_KEY="sk-..."` or use a secrets manager
5. Run: `streamlit run app.py`
6. Open the displayed URL.

Responsible AI
- Only paste meeting transcripts for which you have consent.
- Do not store private PII in public repos.
- Validate outputs before sending emails or tasks.

Contents
- app.py — Streamlit app (MVP)
- prompts.md — curated prompts and examples
- samples/ — example transcript and generated outputs

License
- MIT
