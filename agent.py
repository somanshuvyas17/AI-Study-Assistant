import os
import json
import re
import streamlit as st

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# GET HUGGING FACE TOKEN
# ============================================================

HF_TOKEN = os.getenv("HF_TOKEN")

# Streamlit Cloud fallback
if not HF_TOKEN:
    try:
        HF_TOKEN = st.secrets["HF_TOKEN"]
    except Exception:
        HF_TOKEN = None


# ============================================================
# CHECK TOKEN
# ============================================================

if not HF_TOKEN:
    st.error(
        "❌ Hugging Face API token not found.\n\n"
        "For local use, add HF_TOKEN to your .env file.\n"
        "For Streamlit Cloud, add HF_TOKEN to Secrets."
    )
    st.stop()


# ============================================================
# HUGGING FACE CLIENT
# ============================================================

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)


# ============================================================
# MODEL
# ============================================================

MODEL = "meta-llama/Llama-3.1-8B-Instruct"


# ============================================================
# FORMAT TIME
# ============================================================

def format_time(total_minutes):

    hour = (total_minutes // 60) % 24
    minute = total_minutes % 60

    period = "AM" if hour < 12 else "PM"

    display_hour = hour % 12

    if display_hour == 0:
        display_hour = 12

    return f"{display_hour}:{minute:02d} {period}"


# ============================================================
# EXTRACT JSON
# ============================================================

def extract_json(text):

    if not text:
        return None

    text = text.strip()

    # Remove markdown code fences
    text = re.sub(
        r"```json",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"```",
        "",
        text
    )

    text = text.strip()

    # Find JSON object
    start = text.find("{")
    end = text.rfind("}")

    if start != -1 and end != -1:

        json_text = text[
            start:end + 1
        ]

        try:
            return json.loads(json_text)

        except json.JSONDecodeError:
            pass

    return None


# ============================================================
# GENERATE STUDY PLAN
# ============================================================

def generate_study_plan(
    subject_data,
    start_time,
    end_time
):

    # --------------------------------------------------------
    # CALCULATE AVAILABLE TIME
    # --------------------------------------------------------

    start_minutes = (
        start_time.hour * 60
        + start_time.minute
    )

    end_minutes = (
        end_time.hour * 60
        + end_time.minute
    )

    available_minutes = (
        end_minutes
        - start_minutes
    )

    if available_minutes <= 0:

        return {
            "markdown":
                "❌ Invalid study time.",

            "sessions": []
        }


    # --------------------------------------------------------
    # SUBJECT INFORMATION
    # --------------------------------------------------------

    subject_text = ""

    for item in subject_data:

        subject_text += f"""

Subject: {item['subject']}
Exam Date: {item['exam_date']}
Difficulty: {item['difficulty']}
Syllabus Completed: {item['progress']}%
Priority Score: {item['score']}/100
Priority Level: {item['priority']}
Exam Urgency Score: {item['exam_score']}
Difficulty Score: {item['difficulty_score']}
Remaining Syllabus Score: {item['remaining_score']}

"""


    # --------------------------------------------------------
    # AI PROMPT
    # --------------------------------------------------------

    prompt = f"""
You are an intelligent AI Study Planner.

Create a realistic study plan for a student.

The student has exactly:

{available_minutes} minutes

available between:

{start_time.strftime('%I:%M %p')}

and:

{end_time.strftime('%I:%M %p')}

SUBJECT INFORMATION:

{subject_text}

IMPORTANT RULES:

1. Use the ENTIRE available study time.

2. Do not create a plan shorter than the available time.

3. Allocate more time to higher-priority subjects.

4. Consider exam urgency.

5. Consider subject difficulty.

6. Consider remaining syllabus.

7. Subjects do NOT need equal time.

8. Include short breaks when appropriate.

9. The total duration of all sessions and breaks
   must equal exactly {available_minutes} minutes.

10. Do not schedule anything outside the given
    study window.

11. Create realistic and specific topics.

12. If an exam is very close, prioritize revision,
    important concepts and practice questions.

13. Avoid vague activities such as:
    "Study DSA"

14. Instead use specific activities such as:
    "Practice binary search problems"

15. Return ONLY valid JSON.

Return exactly this structure:

{{
    "sessions": [
        {{
            "subject": "DSA",
            "topic": "Binary Search",
            "duration": 45,
            "type": "Study"
        }},
        {{
            "subject": "BREAK",
            "topic": "Short Break",
            "duration": 10,
            "type": "Break"
        }}
    ]
}}

The duration values must be integers.

The total duration of ALL sessions must equal:

{available_minutes}

Do not include any text outside the JSON.
"""


    # --------------------------------------------------------
    # CALL HUGGING FACE
    # --------------------------------------------------------

    try:

        response = client.chat.completions.create(

            model=MODEL,

            messages=[

                {
                    "role": "system",
                    "content":
                        "You are an expert academic "
                        "study planner. Return only "
                        "valid JSON when requested."
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            max_tokens=1800,

            temperature=0.3

        )

        output = (
            response.choices[0]
            .message.content
        )

    except Exception as e:

        return {

            "markdown":
                f"❌ Hugging Face error: {e}",

            "sessions": []
        }


    # --------------------------------------------------------
    # PARSE JSON
    # --------------------------------------------------------

    parsed = extract_json(output)

    if not parsed:

        return {

            "markdown":
                "⚠️ The AI did not return "
                "a valid study plan. "
                "Please try again.",

            "sessions": []
        }


    sessions = parsed.get(
        "sessions",
        []
    )


    if not sessions:

        return {

            "markdown":
                "⚠️ No study sessions "
                "were generated.",

            "sessions": []
        }


    # --------------------------------------------------------
    # CLEAN SESSIONS
    # --------------------------------------------------------

    cleaned_sessions = []

    for session in sessions:

        try:

            subject = str(
                session.get(
                    "subject",
                    "Study"
                )
            )

            topic = str(
                session.get(
                    "topic",
                    "Study Session"
                )
            )

            duration = int(
                session.get(
                    "duration",
                    0
                )
            )

            session_type = str(
                session.get(
                    "type",
                    "Study"
                )
            )


            if duration <= 0:
                continue


            cleaned_sessions.append({

                "subject":
                    subject,

                "topic":
                    topic,

                "duration":
                    duration,

                "type":
                    session_type

            })

        except Exception:

            continue


    # --------------------------------------------------------
    # IF AI RETURNED NOTHING
    # --------------------------------------------------------

    if not cleaned_sessions:

        return {

            "markdown":
                "⚠️ No valid study sessions "
                "were generated.",

            "sessions": []
        }


    # --------------------------------------------------------
    # VALIDATE TOTAL TIME
    # --------------------------------------------------------

    total_duration = sum(

        session["duration"]

        for session in cleaned_sessions

    )


    difference = (
        available_minutes
        - total_duration
    )


    # --------------------------------------------------------
    # FIX SMALL TIME DIFFERENCE
    # --------------------------------------------------------

    if difference != 0:

        cleaned_sessions[-1][
            "duration"
        ] += difference


    # --------------------------------------------------------
    # SAFETY CHECK
    # --------------------------------------------------------

    final_total = sum(

        session["duration"]

        for session in cleaned_sessions

    )


    if final_total != available_minutes:

        return {

            "markdown":
                "⚠️ The AI generated an "
                "invalid time allocation. "
                "Please try again.",

            "sessions": []
        }


    # --------------------------------------------------------
    # CREATE MARKDOWN
    # --------------------------------------------------------

    markdown = create_markdown_plan(

        cleaned_sessions,

        start_time,

        available_minutes

    )


    return {

        "markdown":
            markdown,

        "sessions":
            cleaned_sessions

    }


# ============================================================
# CREATE MARKDOWN PLAN
# ============================================================

def create_markdown_plan(
    sessions,
    start_time,
    available_minutes
):

    current_minutes = (

        start_time.hour * 60
        + start_time.minute

    )


    markdown = ""

    markdown += (
        "## 📅 Today's Study Plan\n\n"
    )


    markdown += (

        f"**Total Study Window:** "
        f"{available_minutes // 60}h "
        f"{available_minutes % 60}m\n\n"

    )


    markdown += (
        "| Time | Activity | Duration |\n"
    )

    markdown += (
        "|---|---|---|\n"
    )


    for session in sessions:

        start_string = format_time(
            current_minutes
        )


        end_minutes = (

            current_minutes
            + session["duration"]

        )


        end_string = format_time(
            end_minutes
        )


        if (
            session["type"]
            .lower()
            == "break"
        ):

            activity = (

                f"☕ **Break** — "
                f"{session['topic']}"

            )

        else:

            activity = (

                f"📚 **{session['subject']}** — "
                f"{session['topic']}"

            )


        markdown += (

            f"| {start_string} – {end_string} "
            f"| {activity} "
            f"| {session['duration']} min |\n"

        )


        current_minutes = end_minutes


    markdown += "\n"


    markdown += (
        "### 💡 Study Tip\n\n"
        "Stay focused during each session and "
        "avoid switching subjects unnecessarily. "
        "Your plan prioritizes subjects based on "
        "exam urgency, difficulty and remaining syllabus."
    )


    return markdown
