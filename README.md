
# 🧠 Prompt Injection Lab

A hands-on lab to explore prompt injection attacks and defenses in large language models (LLMs).  
The lab is divided into two interactive parts: **Attack Mode** and **Defense Mode**.

---

## 🎯 Modes

### Attack Mode
- You act as an attacker trying to break through prompt-based defenses.
- Each level increases in difficulty with stronger model protections.
  - level 1: Zero Protection
  - level 2: Input filtering
  - level 3: Output filtering
  - level 4: Input filtering & Output filtering 
  - level 5: LLM-based Injection Detection

### Defense Mode
- You act as the LLM system designer.
- Your goal is to block adversarial prompts using strategies like:
  - Zero Protection
  - Input filtering
  - Input filtering & Output filtering
  - Input filtering & Output filtering & Behavioral detection
  - Input filtering & Output filtering & Behavioral detection & Multi-LLM validation (future level)
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

4. quit the lab:
```bash
Your attack prompt: /quit
```

5. guess the result :
```bash
Your attack prompt: /guess
```
---

## 📂 Project Structure

```
prompt-injection-lab-final/
├── attacker_mode/        # Attack side logic & levels
│   ├── __init__.py
│   ├── playdirect.py
│   ├── playindirect.py
│   └── levels/
│       ├── level_*.json
│       └── secret.json
├── defender_mode/        # Defense side logic & scenarios
│   ├── __init__.py
│   ├── evolve.py
│   ├── indirect.py
│   ├── files/
│   └── scenarios/
│       └── scenario_1.json
├── engine/               # Shared model & scoring engine
│   ├── __init__.py
│   ├── llm.py
│   ├── password.py
│   ├── llmdetector.py
│   ├── scored.py
│   └── runner.py
├── main.py               # Entry point
└── requirements.txt      # Dependencies
```
