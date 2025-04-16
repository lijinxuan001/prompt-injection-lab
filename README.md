
# 🧠 Prompt Injection Lab

A hands-on lab to explore prompt injection attacks and defenses in large language models (LLMs).  
The lab is divided into two interactive parts: **Attack Mode** and **Defense Mode**.

---

## 🎯 Modes

### Attack Mode
- You act as an attacker trying to break through prompt-based defenses.
- Each level increases in difficulty with stronger model protections.

### Defense Mode
- You act as the LLM system designer.
- Your goal is to block adversarial prompts using strategies like:
  - Input filtering
  - Output filtering
  - Behavioral detection
  - Multi-LLM validation (future level)
- Includes "Evolution Defense" mode: iteratively improve until an attack is blocked.

---

## 🚀 Getting Started

1. Make sure [Ollama](https://ollama.com) is installed and a model is running, e.g.:
```bash
ollama run llama3
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the lab:
```bash
python main.py
```

---

## 📂 Project Structure

```
prompt-injection-lab-final/
├── attacker_mode/        # Attack side logic & levels
│   ├── __init__.py
│   └── play.py
│   └── levels/
│       └── level_1.json
├── defender_mode/        # Defense side logic & scenarios
│   ├── __init__.py
│   └── evolve.py
│   └── scenarios/
│       └── scenario_1.json
├── engine/               # Shared model & scoring engine
│   ├── __init__.py
│   ├── llm.py
│   └── score.py
├── main.py               # Entry point
└── requirements.txt      # Dependencies
```
