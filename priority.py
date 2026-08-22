from datetime import date


# ============================================
# EXAM URGENCY
# ============================================

def calculate_exam_urgency(exam_date):

    today = date.today()

    days_left = (
        exam_date - today
    ).days

    if days_left <= 2:
        return 100

    elif days_left <= 7:
        return 85

    elif days_left <= 14:
        return 70

    elif days_left <= 30:
        return 50

    else:
        return 30


# ============================================
# DIFFICULTY SCORE
# ============================================

def calculate_difficulty(difficulty):

    difficulty = difficulty.lower()

    if difficulty == "hard":
        return 100

    elif difficulty == "medium":
        return 60

    else:
        return 30


# ============================================
# PRIORITY SCORE
# ============================================

def calculate_priority(
    exam_date,
    difficulty,
    progress
):

    exam_score = calculate_exam_urgency(
        exam_date
    )

    difficulty_score = calculate_difficulty(
        difficulty
    )

    # If progress = 40%,
    # remaining syllabus = 60%
    remaining_score = 100 - progress


    # Weighted score

    final_score = (
        (exam_score * 0.40)
        +
        (difficulty_score * 0.30)
        +
        (remaining_score * 0.30)
    )


    # Priority label

    if final_score >= 70:

        priority = "High"

    elif final_score >= 45:

        priority = "Medium"

    else:

        priority = "Low"


    return {
        "score": round(final_score, 1),
        "priority": priority,
        "exam_score": exam_score,
        "difficulty_score": difficulty_score,
        "remaining_score": remaining_score
    }