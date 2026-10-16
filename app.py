import os
import streamlit as st
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.warning("Set OPENAI_API_KEY environment variable (or use a secrets manager).")
else:
    openai.api_key = OPENAI_API_KEY

st.set_page_config(page_title="AI Productivity Assistant MVP", layout="wide")
st.title("AI Productivity Assistant — MVP")

tab = st.sidebar.radio("Feature", ["Email Generator", "Meeting Summarizer", "Task Planner", "Chatbot"])


def call_model(prompt, max_tokens=300):
    try:
        resp = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.2,
        )
        return resp.choices[0].text.strip()
    except Exception as e:
        return f"Error calling model: {e}"

if tab == "Email Generator":
    st.header("Email Generator")
    tone = st.selectbox("Tone", ["Professional", "Casual", "Concise", "Persuasive"])
    recipient = st.text_input("Recipient name / role")
    subject = st.text_input("Subject")
    context = st.text_area("Context / Key points (what should be included)")
    if st.button("Generate Email"):
        prompt = f"""Write an email with subject: \"{subject}\". Tone: {tone}. Recipient: {recipient}. Include these points: {context}.
Write full email body and a 1-line subject suggestion."""
        with st.spinner("Generating..."):
            out = call_model(prompt)
        st.subheader("Output")
        st.text_area("Email", value=out, height=300)

elif tab == "Meeting Summarizer":
    st.header("Meeting Summarizer")
    transcript = st.text_area("Paste meeting transcript (or notes)", height=300)
    if st.button("Summarize Meeting"):
        prompt = f"""You are a meeting summarization assistant. Produce:
- 3–5 bullet quick summary
- Key decisions
- Action items with owners (if present)
- 1-line meeting gist

Transcript:
{transcript}
"""
        with st.spinner("Summarizing..."):
            out = call_model(prompt, max_tokens=400)
        st.subheader("Summary")
        st.text_area("Summary", value=out, height=300)

elif tab == "Task Planner":
    st.header("Task Planner")
    goal = st.text_area("Describe the goal or project")
    constraints = st.text_area("Constraints or timeline (optional)")
    if st.button("Create Task Plan"):
        prompt = f"""Given the goal: {goal}
Constraints: {constraints}
Return:
1) High-level plan (3–6 steps)
2) Break down each step into tasks with estimated times and suggested owner roles
3) Suggested next 3 immediate actions
"""
        with st.spinner("Creating plan..."):
            out = call_model(prompt, max_tokens=500)
        st.subheader("Task Plan")
        st.text_area("Plan", value=out, height=400)

else:  # Chatbot
    st.header("Chatbot (prototype)")
    if 'history' not in st.session_state:
        st.session_state['history'] = ""
    user_input = st.text_input("You:", key="chat")
    if st.button("Send"):
        history = st.session_state.get('history', '')
        prompt = f"Conversation so far:\n{history}\nUser: {user_input}\nAssistant:"
        with st.spinner("Thinking..."):
            out = call_model(prompt, max_tokens=200)
        st.session_state.history = history + f"\nUser: {user_input}\nAssistant: {out}"
    st.text_area("Conversation", value=st.session_state.get("history", ""), height=300)
