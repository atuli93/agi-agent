# AGI Agent (Flask + OpenAI)

A modular AGI (Artificial General Intelligence) agent built with **Flask** that takes user prompts and returns AI-generated responses. Designed for easy experimentation, remixing, and deployment.

---

## 🚀 Features

- Web interface using Flask
- AI-powered responses via OpenAI API
- Modular architecture for extensions
- Ready for local development or deployment

---

## 📦 Project Structure

```bash
agi-agent/
│
├─ app.py # Main Flask application
├─ requirements.txt # Python dependencies
├─ templates/ # HTML templates
│ └─ index.html
├─ static/ # CSS / JS files
│ └─ style.css
├─ .venv/ # Virtual environment (ignored by git)
└─ README.md
```

---

## 🛠️ Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/atulchief/agi-agent.git
cd agi-agent
```

---

### 2️⃣ Create a virtual environment (recommended)

```bash
python3 -m venv .venv
```

---

# Activate it:

## Linux / WSL / macOS

```bash
source .venv/bin/activate
```

## Windows (CMD / PowerShell)

```bash
.venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set up OpenAI API Key

## Create a .env file (or set environment variable) with your OpenAI key:

```OPENAI_API_KEY=your_openai_api_key_here```

---

### 5️⃣ Run the app

```bash
python app.py
```

**Open your browser at: http://127.0.0.1:5000**

---

### 📝 Usage

**Enter a prompt in the web interface**
**Click Submit**
**Receive AI-generated responses in real-time**
**Customize responses or add new modules by editing ```app.py```

---

### ⚙️ Development Notes

Do not commit .venv/ or API keys
Flask auto-reloads during development
Add new HTML templates in templates/ and CSS in static/
Keep dependencies updated in requirements.txt

---

### 📜 License

This project is licensed under the MIT License. See LICENSE
 for details.

---

### 💡 Tips

**Test your API key before pushing to production**
**Use .gitignore to exclude sensitive files:**

```bash
.venv/
__pycache__/
*.pyc
.env
```

**Keep your project modular for easy extensions and experimentation**
