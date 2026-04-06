# 🎓 Multi-Agent Education System

An AI-powered **Multi-Agent Education System** that automatically generates structured learning content using multiple intelligent agents working together.

The system takes a **topic as input** and produces:

* 📘 Concept explanation
* 🧠 Structured educational content
* 🖼️ AI-generated diagrams/images
* 📑 Well-formatted learning material

---

# 🚀 Features

* 🤖 **Multi-Agent Architecture**
* 📚 Generates structured educational content
* 🖼️ Automatic diagram/image generation
* ⚡ Fast and intelligent workflow
* 🧩 Modular and scalable design
* 🖥️ Simple Streamlit interface
* 🔑 Secure API key handling using `.env`

---

# 🧠 System Overview

The system uses multiple AI agents coordinated by a central controller:

### Agents in the system:

* **Research Agent** → Collects topic information
* **Writer Agent** → Converts information into structured explanation
* **Image Agent** → Generates diagrams or visuals
* **Orchestrator (Crew Manager)** → Manages communication between agents

All agents collaborate to generate high-quality educational material automatically.

---

# 🏗️ Architecture

```
User Input
     ↓
Orchestrator Agent
     ↓
 ┌──────────────┬──────────────┬──────────────┐
 Research Agent   Writer Agent   Image Agent
     ↓               ↓              ↓
     └────────── Combined Output ──────────┘
                        ↓
                 Final Educational Content
```

---

# ⚙️ Tech Stack

* Python 🐍
* Streamlit 🎨
* LLM (Gemini / OpenAI compatible) 🤖
* Multi-Agent workflow ⚡
* Environment variables (.env) 🔐

---

# 📂 Project Structure

```
multi_agent_education_system
│── app.py                 # Streamlit interface
│── agents.py              # AI agents logic
│── crew.py                # orchestrator logic
│── tasks.py               # task definitions
│── image_generator.py     # diagram generation
│── requirements.txt       # dependencies
│── README.md              # project documentation
│── .gitignore             # ignored files
```

---

# ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/bhawsararya/Muti-Agent-Education-System.git
cd Muti-Agent-Education-System
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Create .env file

Create `.env` file and add your API key:

```
API_KEY=your_api_key_here
```

---

### 4. Run the application

```
streamlit run app.py
```

---

# 📊 Workflow

1. User enters topic
2. Orchestrator assigns tasks to agents
3. Research agent gathers information
4. Writer agent formats structured content
5. Image agent generates diagrams
6. System displays final educational output

---

# 🔒 Security

Sensitive files are protected using `.gitignore`:

```
.env
__pycache__/
```

---

# 🌟 Use Cases

* Students learning new topics
* Teachers generating study material
* AI-based education platforms
* Automated content creation
* Concept explanation with diagrams

---

# 📌 Future Improvements

* Add quiz generation
* PDF export feature
* Voice explanation support
* Multi-language support
* Vector database integration
* Advanced diagram generation

---

# ⭐ If you like this project

Give it a star on GitHub ⭐
