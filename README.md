# 🎓 Academic Exam Assistant

A professional AI-powered chatbot designed to assist students with academic examination guidance, grading systems, and institutional regulations. Built with Streamlit and Google Gemini AI.

---

## ✨ Features

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

## 🚀 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Modern Python web framework
- **AI Engine**: [Google Generative AI (Gemini)](https://ai.google.dev/) - State-of-the-art language model
- **Language**: Python 3.x
- **API**: Google Gemini Flash Latest

---

## 📋 Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher
- A Google Cloud API key for Gemini AI
- pip (Python package manager)

---

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/aignite.git
cd aignite
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv virtualvenv
```

**Activate Virtual Environment:**
- **Windows:**
  ```bash
  virtualvenv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source virtualvenv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

**Getting Your API Key:**
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Get API Key"
3. Create a new API key
4. Copy it to your `.env` file

---

## 🎯 Usage

### Run the Application
```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

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

## 🎨 UI/UX Features

- **Gradient Theme** - Modern purple-blue gradient design
- **Smart Message Layout**:
  - User messages appear on the **right** (purple gradient)
  - Assistant responses appear on the **left** (light gray with accent)
- **Responsive Design** - Works on desktop and tablet devices
- **Smooth Interactions** - Real-time message updates and styling
- **Professional Typography** - Clear, readable text with proper spacing

---

## 📦 Dependencies

Key libraries used (see `requirements.txt` for complete list):
```
streamlit>=1.28.0
google-genai>=0.3.0
python-dotenv>=1.0.0
```

---

## 🐛 Troubleshooting

### Issue: "API key not found" error
- **Solution**: Ensure `.env` file exists in the project root with `GEMINI_API_KEY` set

### Issue: Streamlit app not loading
- **Solution**: Try clearing cache with `streamlit run app.py --logger.level=debug`

### Issue: Slow responses
- **Solution**: Check your internet connection and API quota on Google Cloud Console

### Issue: Virtual environment not activating
- **Solution**: Ensure you're in the project directory and use the correct activation command for your OS

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 💡 Future Enhancements

- [ ] Multi-language support
- [ ] Advanced analytics and logging
- [ ] Database integration for storing FAQs
- [ ] Voice input/output capabilities
- [ ] Integration with institution management systems
- [ ] Mobile app version

---

## 📧 Support

For issues, questions, or suggestions, please:
- Open an issue on GitHub
- Contact the development team
- Check the FAQs in the documentation

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini AI](https://ai.google.dev/)
- Designed for educational institutions

---

**Made with ❤️ for better academic guidance**
