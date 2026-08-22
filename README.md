📚 AI Study Assistant (Website:- https://ai-study-assistant-17.streamlit.app/)

An adaptive, AI-powered study planner built with Streamlit. It generates a personalized study schedule from your subjects and available time, ranks subjects by urgency using a weighted priority algorithm, lets you reschedule the plan conversationally when things change, and can push your finalized study sessions straight to Google Calendar.

---

## 🎯 Objective

Studying for multiple subjects at once makes it hard to know what to focus on first — especially when exam dates, difficulty, and syllabus progress are all different for each subject. This project solves that by:

- Automatically calculating which subjects need the most attention using a transparent priority formula.
- Using an LLM to turn that priority data into a concrete, time-boxed study plan.
- Letting the plan adapt in real time through a chat interface when the user's available time or circumstances change (e.g. "I only have 2 hours today" or "my DSA exam is tomorrow").
- Syncing the finalized plan to Google Calendar so it fits into the user's actual schedule.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | [Streamlit](https://streamlit.io/) |
| AI / LLM | [Hugging Face Inference API](https://huggingface.co/docs/huggingface_hub) — `meta-llama/Llama-3.1-8B-Instruct` |
| Calendar Integration | Google Calendar API (`google-api-python-client`, OAuth via `google-auth-oauthlib`) |
| Config / Secrets | `python-dotenv` |
| Language | Python |

---

## ⚙️ Implementation Details

The app is organized into a few focused modules:

- **`app.py`** — Main Streamlit entry point. Handles page layout, session state, the tabbed UI (Setup, Study Plan, Priority, AI Assistant), and wires the other modules together.
- **`priority.py`** — Calculates a priority score per subject from three weighted factors:
  - Exam urgency (**40%**) — based on days remaining until the exam.
  - Difficulty (**30%**) — self-reported as Easy / Medium / Hard.
  - Remaining syllabus (**30%**) — `100 − progress%`.

  The weighted score maps to a **High / Medium / Low** priority label, which drives how much study time each subject gets.
- **`agent.py`** — Talks to the Hugging Face Inference API to generate the initial AI study plan from subjects, priorities, and available hours.
- **`rescheduler.py`** — Handles the conversational "AI Assistant" tab: parses the user's natural-language message (e.g. new time available, an exam moved up), detects situations like an exam crisis, and regenerates the plan accordingly.
- **`dashboard.py`** — Renders the detailed per-subject dashboard: overall progress, priority breakdown, and an editable progress slider per subject that recalculates priority on save.
- **`google_calendar.py`** — Handles Google OAuth (via `credentials.json` / `token.json`) and pushes the generated study sessions to the user's Google Calendar as events.

**Data flow:** Subjects + exam dates + difficulty + progress → `priority.py` scores each subject → `agent.py` sends that context to the LLM to draft a plan → the plan is displayed and optionally adjusted via `rescheduler.py` → confirmed sessions are pushed to Google Calendar via `google_calendar.py`.



## 🖼️ Screenshots

<img width="384" height="756" alt="Screenshot 2026-08-22 at 10 24 51 PM" src="https://github.com/user-attachments/assets/d42786d8-e72e-4158-9705-5e6101d64e8b" />
<img width="360" height="728" alt="Screenshot 2026-08-22 at 10 25 56 PM" src="https://github.com/user-attachments/assets/14bf3371-3c46-4c0c-9c61-5fb9dd09b557" />
<img width="403" height="770" alt="Screenshot 2026-08-22 at 10 26 06 PM" src="https://github.com/user-attachments/assets/48b2134e-5ef6-49eb-ad32-39d8aadd7690" />
<img width="380" height="686" alt="Screenshot 2026-08-22 at 10 27 06 PM" src="https://github.com/user-attachments/assets/acccc3fd-e818-4983-9019-cf10fdc4c88d" />






## 🎯 Task Selection

Within a generated plan, subjects are ordered and allocated time based on their priority score rather than being treated equally:

1. Every subject is scored using the weighted formula above (exam urgency, difficulty, remaining syllabus).
2. Subjects are sorted **highest score first**, so the most urgent/hardest/least-complete subjects surface at the top of both the Priority tab and the generated plan.
3. When the AI builds the schedule, higher-priority subjects are allocated a larger share of the available study hours.
4. If circumstances change (less time available, an exam moved closer), the rescheduler re-evaluates and re-prioritizes tasks rather than just shrinking every subject's time proportionally — e.g. an imminent exam can trigger an "exam crisis" mode that concentrates most of the remaining time on that one subject.

This keeps the plan responsive to what actually matters most at any given moment, rather than splitting time evenly across subjects.
