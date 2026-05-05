# 🎓 AI Study Coach

> **Zero-Prompt AI That Just Works — A Personal Study Mentor That Thinks For You**

---

## 🚨 Problem: AI is Powerful, But Not Usable

Modern AI tools are powerful, but they come with a hidden barrier:

> **They require users to think like engineers.**

Students preparing for exams like JEE/NEET:

* Don’t know how to write good prompts
* Provide vague inputs → get poor results
* Lose trust in AI tools

This creates a critical gap:

> ❌ AI exists
> ❌ But users can’t *use it effectively*

---

## 💡 Solution: Zero-Prompt AI Study Coach

**AI Study Coach eliminates prompting completely.**

Instead of asking users to “tell the AI what to do”, the system:

* Guides users through **structured inputs** (forms, sliders, selections)
* Accepts **file uploads (PDF/images)** for automatic analysis
* Infers intent using **context + behavior + inputs**
* Generates **highly personalized outputs without any prompt writing**

👉 The experience feels like:

> Using Google Search or a smart app — not talking to an AI model.

---

## 🧠 How It Solves “Zero-Prompt AI”

This project directly implements the hackathon’s vision:

| Requirement           | Implementation                            |
| --------------------- | ----------------------------------------- |
| ❌ No prompt writing   | ✅ Fully guided UI (no text prompt needed) |
| 📊 Structured inputs  | ✅ Sliders, dropdowns, step-by-step flow   |
| 📄 File understanding | ✅ Upload marks/test data → AI analysis    |
| 🧭 Context awareness  | ✅ Uses user profile + progress updates    |
| 🔁 Adaptive behavior  | ✅ Updates plan based on daily progress    |
| 🎯 Natural UX         | ✅ Feels like an app, not a chatbot        |

---

### 🧠 Zero-Prompt in Action

User does NOT write:
❌ "Give me a study plan for JEE"

Instead, the app asks:
✔ What is your goal?
✔ How many hours do you study?
✔ Upload your test data

And automatically generates:
✔ Analysis
✔ Strategy
✔ Daily plan
✔ Immediate next action

👉 No prompts. No confusion. Just results.

---

## ✨ Key Features

### 🎯 Zero-Prompt Guided Experience

Users never type prompts. The system extracts intent through structured interaction.

---

### 📄 File-Based Intelligence

Upload test results or study material → AI automatically interprets performance.

---

### 🧠 Deep AI Analysis

* Identifies weak subjects & root causes
* Detects patterns (low confidence, time imbalance)
* Provides strategic insights

---

### 📊 Subject-Wise Breakdown

Physics, Chemistry, Mathematics:

* Weak topics
* Mistake patterns
* Targeted improvements

---

### 🔍 Explain My Weakness

Interactive feature:

> “Why am I weak in Physics?”

AI responds with:

* Conceptual gaps
* Behavioral mistakes
* Fix strategy

---

### 📈 Adaptive Progress Tracking

User updates:

* Hours studied
* Subject focus
* Difficulties

AI dynamically:

* Re-adjusts plan
* Corrects mistakes
* Updates priorities

---

### ⚡ Instant Action Mode (Key Differentiator)

> “What should I do RIGHT NOW?”

AI gives:

* Exact task
* Time-bound goal
* Immediate execution plan

👉 Eliminates decision fatigue completely.

---

## 🛠️ How It Works

1. **Select Goal** → (Crack JEE / Improve / Revise)
2. **Upload Context** → (optional file input)
3. **Set Baseline** → (hours, confidence, exam)
4. **AI Analysis** → personalized strategy
5. **Drill Down** → weakness explanation
6. **Adapt** → update daily progress
7. **Execute** → instant action mode

---

## 💻 Tech Stack

* **Frontend:** Streamlit (Python)
* **AI Engine:** Google Gemini (2.5 Flash / Pro via `google-genai`)
* **State Management:** Streamlit `session_state`
* **Environment:** python-dotenv

---

## 🔥 Why This Stands Out

Most AI tools:

> Require users to *figure out what to ask*

**AI Study Coach:**

> Figures out what the user *needs* — automatically

---

### 🚀 Core Differentiation

* No prompt engineering required
* Context-aware + adaptive
* Action-oriented (not just informative)
* Designed for **non-technical users**

---

## 🧪 Real-World Impact

A student can:

* Upload marks
* Click a few options
* Instantly get:

  * Strategy
  * Plan
  * Weakness insights
  * Next action

👉 Without writing a single prompt

---

## 🚀 Future Improvements

* 📊 Performance dashboards & analytics
* 📚 RAG-based textbook recommendations
* 🔔 Smart reminders (WhatsApp/Telegram)
* 👤 User accounts + long-term tracking

---

## 🏁 Demo Instructions

```bash
git clone <your-repo-url>
cd AI-STUDY-COACH/ai-study-coach
pip install -r requirements.txt
```

Create `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Run:

```bash
streamlit run app.py
```

---

## 💡 Final Thought

> **This AI doesn’t wait for prompts — it understands you.**

That’s what Zero-Prompt AI should feel like.
