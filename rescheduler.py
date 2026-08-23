import os
import re
import json

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from agent import format_time


# ============================================
# HUGGING FACE
# ============================================

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN"),
    provider="auto"
)


# ============================================
# EXTRACT USER INTENT USING AI
# ============================================

def extract_user_intent(
    message,
    subject_data
):

    subjects = [
        item["subject"]
        for item in subject_data
    ]

    subject_list = ", ".join(subjects)

    prompt = f"""
You are an intent extraction system for an
AI Study Assistant.

The student said:

"{message}"

Available subjects:
{subject_list}

Determine whether the student is talking about
an upcoming exam or test.

Return ONLY valid JSON in exactly this format:

{{
    "exam_related": true,
    "subject": "DSA",
    "days_until_exam": 1,
    "available_minutes": 180
}}

Rules:

1. exam_related:
   true if the student mentions an exam,
   test, paper, assessment, quiz, midterm,
   final, or similar upcoming academic assessment.

2. subject:
   Identify the subject from the available
   subjects.
   Return null if no subject can be identified.

3. days_until_exam:
   Estimate the number of days until the exam.

   Examples:
   tomorrow = 1
   next day = 1
   day after tomorrow = 2
   in 3 days = 3
   next week = 7

   If no timeframe is given, return null.

4. available_minutes:
   Extract how much study time the student has.

   Examples:
   3 hours = 180
   1.5 hours = 90
   90 minutes = 90

   Return null if no available time is given.

Do not include markdown.
Do not include explanations.
Return JSON only.
"""

    try:

        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            max_tokens=300,

            extra_body={
                "reasoning_effort": "low"
            }
        )


        text = (
            response.choices[0]
            .message
            .content
        )


        if not text:

            return None


        # ------------------------------------
        # CLEAN RESPONSE
        # ------------------------------------

        text = text.strip()

        # Remove markdown JSON fences if model
        # accidentally adds them.

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


        # ------------------------------------
        # PARSE JSON
        # ------------------------------------

        data = json.loads(text)


        return data


    except Exception as e:

        print(
            f"Intent extraction error: {e}"
        )

        return None


# ============================================
# FALLBACK TIME EXTRACTION
# ============================================

def extract_minutes(message):

    message = message.lower()


    hour_match = re.search(
        r"(\d+(?:\.\d+)?)\s*"
        r"(?:hours?|hrs?|hr)",
        message
    )


    if hour_match:

        return int(
            float(
                hour_match.group(1)
            ) * 60
        )


    minute_match = re.search(
        r"(\d+)\s*"
        r"(?:minutes?|mins?|min)",
        message
    )


    if minute_match:

        return int(
            minute_match.group(1)
        )


    return None


# ============================================
# FIND SUBJECT
# ============================================

def find_subject(
    message,
    subject_data
):

    message_lower = message.lower()


    for item in subject_data:

        subject = (
            item["subject"]
            .lower()
        )


        if subject in message_lower:

            return item


    return None


# ============================================
# DETERMINE EXAM URGENCY
# ============================================

def is_exam_crisis(
    intent
):

    if not intent:

        return False


    if not intent.get(
        "exam_related",
        False
    ):

        return False


    days = intent.get(
        "days_until_exam"
    )


    # Exam today/tomorrow/within 2 days

    if days is not None:

        return days <= 2


    # If AI detected an exam but couldn't
    # determine the date, we can still treat
    # it as potentially urgent.

    return True


# ============================================
# MAIN RESCHEDULER
# ============================================

def reschedule_plan(
    subject_data,
    user_message,
    original_start
):

    # ----------------------------------------
    # ASK AI TO UNDERSTAND USER
    # ----------------------------------------

    intent = extract_user_intent(

        user_message,

        subject_data

    )


    # ----------------------------------------
    # GET AVAILABLE TIME
    # ----------------------------------------

    new_minutes = None


    if intent:

        new_minutes = intent.get(
            "available_minutes"
        )


    # Fallback if AI misses the time

    if not new_minutes:

        new_minutes = extract_minutes(
            user_message
        )


    if not new_minutes:

        return (
            "⚠️ I couldn't determine "
            "how much study time you have.\n\n"
            "Try something like:\n\n"
            "\"I have my DSA exam tomorrow "
            "and only 3 hours to study.\""
        )


    # ----------------------------------------
    # FIND EXAM SUBJECT
    # ----------------------------------------

    exam_subject = None


    if intent:

        detected_subject = (
            intent.get("subject")
        )


        if detected_subject:

            for item in subject_data:

                if (
                    item["subject"].lower()
                    ==
                    detected_subject.lower()
                ):

                    exam_subject = item

                    break


    # Fallback to direct subject matching

    if not exam_subject:

        exam_subject = find_subject(
            user_message,
            subject_data
        )


    # ----------------------------------------
    # CHECK EXAM CRISIS
    # ----------------------------------------

    crisis = is_exam_crisis(
        intent
    )


    if crisis and exam_subject:

        return create_exam_crisis_plan(

            exam_subject,

            subject_data,

            new_minutes,

            original_start,

            user_message,

            intent

        )


    # ----------------------------------------
    # NORMAL RESCHEDULING
    # ----------------------------------------

    return create_normal_reschedule(

        subject_data,

        new_minutes,

        original_start,

        user_message

    )


# ============================================
# EXAM CRISIS PLAN
# ============================================

def create_exam_crisis_plan(

    exam_subject,

    subject_data,

    new_minutes,

    original_start,

    user_message,

    intent

):

    # ========================================
    # DETERMINE EXAM URGENCY
    # ========================================

    days = intent.get(
        "days_until_exam"
    )


    if days == 0:

        urgency_text = "TODAY"

    elif days == 1:

        urgency_text = "TOMORROW"

    elif days is not None:

        urgency_text = (
            f"IN {days} DAYS"
        )

    else:

        urgency_text = (
            "UPCOMING"
        )


    # ========================================
    # GIVE 80% TO EXAM SUBJECT
    # ========================================

    exam_time = int(
        new_minutes * 0.80
    )


    remaining_time = (
        new_minutes
        - exam_time
    )


    # ========================================
    # FIND OTHER SUBJECTS
    # ========================================

    other_subjects = [

        item

        for item in subject_data

        if item["subject"]
        != exam_subject["subject"]

    ]


    other_subjects.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    # ========================================
    # CREATE SESSIONS
    # ========================================

    sessions = []


    # Main exam subject

    sessions.append({

        "subject":
            exam_subject["subject"],

        "topic":
            exam_subject.get(
                "topic",
                "High-yield exam revision"
            ),

        "duration":
            exam_time,

        "priority":
            "EXAM CRITICAL"

    })


    # Remaining time

    if (
        remaining_time >= 10
        and other_subjects
    ):

        sessions.append({

            "subject":
                other_subjects[0]["subject"],

            "topic":
                other_subjects[0].get(
                    "topic",
                    "Quick revision"
                ),

            "duration":
                remaining_time,

            "priority":
                other_subjects[0]["priority"]

        })


    # ========================================
    # BUILD SCHEDULE
    # ========================================

    current_minutes = (

        original_start.hour * 60

        + original_start.minute

    )


    plan = []


    for session in sessions:

        start = current_minutes


        end = (
            current_minutes
            + session["duration"]
        )


        plan.append({

            "start":
                format_time(start),

            "end":
                format_time(end),

            "subject":
                session["subject"],

            "topic":
                session["topic"],

            "duration":
                session["duration"],

            "priority":
                session["priority"]

        })


        current_minutes = end


    # ========================================
    # OUTPUT
    # ========================================

    output = (
        "## 🚨 EXAM CRISIS MODE\n\n"
    )


    output += (
        f"**Exam:** "
        f"{exam_subject['subject']}\n\n"
    )


    output += (
        f"**Exam timing:** "
        f"{urgency_text}\n\n"
    )


    output += (
        "The plan has been optimized around "
        "your upcoming exam.\n\n"
    )


    output += (
        "| Time | Subject | Topic | "
        "Duration | Priority |\n"
    )


    output += (
        "|------|---------|-------|"
        "----------|----------|\n"
    )


    for item in plan:

        output += (

            f"| {item['start']} - "
            f"{item['end']} "

            f"| {item['subject']} "

            f"| {item['topic']} "

            f"| {item['duration']} min "

            f"| {item['priority']} |\n"

        )


    actual_total = sum(

        item["duration"]

        for item in plan

    )


    output += (

        f"\n**⏱️ Total Study Time: "

        f"{actual_total // 60} hours "

        f"{actual_total % 60} minutes**"

    )


    # ========================================
    # DEFERRED SUBJECTS
    # ========================================

    deferred = [

        item

        for item in subject_data

        if item["subject"]
        != exam_subject["subject"]

    ]


    if deferred:

        output += (
            "\n\n## ⏸️ DEFERRED SUBJECTS\n\n"
        )


        output += (
            "These subjects were deferred "
            "because of the urgent exam:\n\n"
        )


        for item in deferred:

            output += (

                f"- **{item['subject']}** "
                f"— {item['priority']} "
                f"({item['score']}/100)\n"

            )


    output += (

        "\n\n🚨 **Recommendation:** "

        "Focus on high-yield revision, "

        "weak areas, and practice questions "

        "for the upcoming exam."

    )


    return output


# ============================================
# NORMAL RESCHEDULING
# ============================================

def create_normal_reschedule(

    subject_data,

    new_minutes,

    original_start,

    user_message

):

    subject_data = sorted(

        subject_data,

        key=lambda x: x["score"],

        reverse=True

    )


    minimum_time = 20


    selected_subjects = []

    deferred_subjects = []


    remaining_time = new_minutes


    # ----------------------------------------
    # SELECT SUBJECTS
    # ----------------------------------------

    for item in subject_data:

        if remaining_time >= minimum_time:

            selected_subjects.append(
                item
            )

            remaining_time -= (
                minimum_time
            )

        else:

            deferred_subjects.append(
                item
            )


    if (
        not selected_subjects
        and subject_data
    ):

        selected_subjects.append(
            subject_data[0]
        )

        deferred_subjects = (
            subject_data[1:]
        )


    # ----------------------------------------
    # ALLOCATE TIME
    # ----------------------------------------

    total_score = sum(

        item["score"]

        for item in selected_subjects

    )


    if total_score <= 0:

        total_score = len(
            selected_subjects
        )


    minimum_total = (

        len(selected_subjects)

        * minimum_time

    )


    extra_time = (

        new_minutes

        - minimum_total

    )


    for item in selected_subjects:

        item["duration"] = (
            minimum_time
        )


        share = (

            item["score"]

            / total_score

        )


        additional = int(

            extra_time * share

        )


        item["duration"] += (
            additional
        )


    # ----------------------------------------
    # FIX ROUNDING
    # ----------------------------------------

    allocated = sum(

        item["duration"]

        for item in selected_subjects

    )


    difference = (

        new_minutes

        - allocated

    )


    if selected_subjects:

        selected_subjects[0][
            "duration"
        ] += difference


    # ----------------------------------------
    # BUILD SCHEDULE
    # ----------------------------------------

    current_minutes = (

        original_start.hour * 60

        + original_start.minute

    )


    plan = []


    for item in selected_subjects:

        duration = item["duration"]


        start = current_minutes


        end = (

            current_minutes

            + duration

        )


        plan.append({

            "start":
                format_time(start),

            "end":
                format_time(end),

            "subject":
                item["subject"],

            "topic":
                item.get(
                    "topic",
                    "Revision"
                ),

            "duration":
                duration,

            "priority":
                item["priority"]

        })


        current_minutes = end


    # ----------------------------------------
    # OUTPUT
    # ----------------------------------------

    output = (
        "## 🔄 RESCHEDULED STUDY PLAN\n\n"
    )


    output += (

        "| Time | Subject | Topic | "

        "Duration | Priority |\n"

    )


    output += (

        "|------|---------|-------|"

        "----------|----------|\n"

    )


    for item in plan:

        output += (

            f"| {item['start']} - "
            f"{item['end']} "

            f"| {item['subject']} "

            f"| {item['topic']} "

            f"| {item['duration']} min "

            f"| {item['priority']} |\n"

        )


    actual_total = sum(

        item["duration"]

        for item in plan

    )


    output += (

        f"\n**⏱️ New Study Time: "

        f"{actual_total // 60} hours "

        f"{actual_total % 60} minutes**"

    )


    if deferred_subjects:

        output += (
            "\n\n## ⏸️ DEFERRED SUBJECTS\n\n"
        )


        output += (

            "These subjects were deferred "

            "because of limited available time:\n\n"

        )


        for item in deferred_subjects:

            output += (

                f"- **{item['subject']}** "

                f"— {item['priority']} "

                f"({item['score']}/100)\n"

            )


    output += (

        f"\n\n**🔄 Reason:** "

        f"{user_message}"

    )


    return output
