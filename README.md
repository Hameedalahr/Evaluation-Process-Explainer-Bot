#  Academic Exam Assistant

A professional AI-powered chatbot designed to assist students with academic examination guidance, grading systems, and institutional regulations. Built with Streamlit and Google Gemini AI.

---

##  Features

- **Professional Chat Interface** - Clean, modern UI with intuitive message layout
- **Real-time Responses** - Instant answers powered by Google Gemini AI
- **Academic Expertise** - Specialized knowledge about:
  - Examination patterns and schedules
  - Grading systems and evaluation criteria
  - Revaluation and supplementary exam processes
  - Academic regulations and policies
- **Safety-First Design** - Prevents misuse by refusing to:
  - Predict grades or marks
  - Answer exam questions directly
  - Solve numerical or theoretical problems
  - Make unverified claims about outcomes
- **Conversation History** - Maintains chat context throughout the session
- **Student-Friendly** - Neutral, formal, and accessible explanations

---

### Interacting with the Chatbot

1. Type your question in the input field at the bottom
2. Press Enter or click the send button
3. The assistant will provide accurate, policy-based responses
4. View your chat history as you continue the conversation

### Example Questions

- "What is the grading scale used in our institution?"
- "How does the revaluation process work?"
- "What are the eligibility criteria for supplementary exams?"
- "Explain the academic regulations regarding attendance"

---

## 📁 Project Structure

```
aignite/
├── app.py                 # Main Streamlit application
├── gemini_client.py       # Google Gemini API integration
├── system_prompt.py       # AI system prompt and constraints
├── requirements.txt       # Python dependencies
├── backup.py              # Backup utilities
├── .env                   # Environment variables (create this)
├── __pycache__/           # Python cache files
├── virtualvenv/           # Virtual environment folder
└── README.md              # This file
```

---

## 🔐 System Prompt & Safety

The chatbot operates under a strict system prompt (`system_prompt.py`) that ensures:

**What it CAN do:**

- ✅ Explain examination patterns and schedules
- ✅ Clarify grading systems and evaluation methods
- ✅ Describe revaluation and supplementary processes
- ✅ Provide institutional policy information
- ✅ Maintain academic integrity

**What it CANNOT do:**

- ❌ Predict grades or marks
- ❌ Answer or solve exam questions
- ❌ Solve numerical problems
- ❌ Make guaranteed predictions about outcomes
- ❌ Bypass academic policies

When users ask for prohibited content, the assistant politely refuses and redirects to legitimate academic guidance.

---

