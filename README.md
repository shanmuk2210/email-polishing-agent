# EmailCraft AI

EmailCraft AI is an AI-powered email rewriting assistant that transforms rough, informal, or poorly structured emails into clear, professional, natural-sounding messages.

The application preserves the original intent and facts while improving grammar, structure, clarity, readability, and tone.

## Features

- ✨ **Professionally rewrites rough emails**
- 🎯 **Preserves the original intent and facts**
- 🤝 **Produces natural, human-sounding emails**
- 📝 **Improves grammar, spelling, punctuation, and sentence structure**
- 📧 **Maintains the author's original voice**
- 🚫 **Avoids unnecessary corporate jargon and exaggerated formality**
- ⬇️ **Downloads polished emails as `.txt` files**
- 📋 **Copies polished emails to the clipboard**
- ⚙️ **Supports configurable AI model and temperature**
- 🖥️ **Provides a clean Streamlit-based user interface**

## How It Works

1. Enter or paste a rough email.
2. EmailCraft AI analyzes the intended message.
3. The AI improves the email's grammar, structure, clarity, and tone.
4. The polished email is displayed alongside the original.
5. Copy the polished email or download it as a `.txt` file.

## Architecture

The project uses:

- **Streamlit** — Web interface
- **CrewAI** — AI agent and task orchestration
- **Gemini** — LLM runtime
- **Python** — Application development

## Project Structure

```text
email-assistant/
│
├── app.py
├── main.py
│
├── agents/
│   └── email_agent.py
│
├── tasks/
│   └── email_task.py
│
└── config/
    └── settings.py


---
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/msangeeth28/crewai-email-assistant.git

cd crewai-email-assistant
```
---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Google Gemini

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace:

```text
your_api_key_here
```

with your Google Gemini API key.

Keep the API key private and never commit the `.env` file to GitHub.

---


# ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---
