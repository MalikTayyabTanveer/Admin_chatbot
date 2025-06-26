# Admin Chatbot with LLM

## 📌 Project Overview

This project is an **Admin Management Chatbot** powered by a **Large Language Model (LLM)** (LLaMA 3 via Groq) and a **local SQLite database**. It allows an administrator to manage users through natural language commands such as:

- `Add the user john@abc.com with phone +923001234567 and city Lahore.`
- `Remove user john@abc.com`
- `Update john@abc.com with name John Doe and city Paris`

The LLM extracts intent and user attributes (email, name, phone, city), and updates the SQLite database accordingly. The frontend is built using **Streamlit**.

---

## ⚙️ Installation

### ✅ Prerequisites

- Python 3.9+
- [Groq API Key](https://console.groq.com/) (for LLaMA 3)
- `.env` file to store your API key

### 📦 Steps to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/admin-chatbot-llm.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd admin-chatbot-llm
   ```

3. **(Optional) Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file and add your Groq API key**:
   ```bash
   echo "GROQ_API_KEY=your_groq_api_key" > .env
   ```

---

## 🚀 Usage

### ▶️ Running the Chatbot

Launch the chatbot UI with Streamlit:

```bash
streamlit run main_chatbot_llm.py
```

You’ll see a simple chat interface in your browser.

---

### 💬 Example Commands

Try typing any of the following:

```
Add ali.khan@example.com with name Ali Khan, phone +923331234567, and city Karachi.
Remove user john.smith@xyz.com
Update user jane@abc.com with phone +923001111111 and city Dubai
```

The chatbot will process the command, update the database, and respond accordingly.

---

## 📁 Project Structure

```
├── main_chatbot_llm.py        # Streamlit frontend
├── llm_parser.py              # LangChain LLM & parser logic
├── init_db_llm.py             # SQLite DB setup
├── .env                       # API keys
├── requirements.txt           # Python dependencies
```

---

## 🧑‍💻 Contact

For questions, suggestions, or collaborations:

- 📇 LinkedIn: [Tayyab Tanveer](https://www.linkedin.com/in/tayyab-tanveer-b000282b3/)
- 📧 Email: adamjosaph@gmail.com

---

*Built with 💡 using LangChain, Streamlit, and Groq.*
