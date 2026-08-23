import streamlit as st
from datetime import time, date

from agent import generate_study_plan
from priority import calculate_priority
from rescheduler import reschedule_plan
from dashboard import show_dashboard
from google_calendar import add_study_plan_to_calendar


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main content */
    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Main title */
    h1 {
        font-size: 2.6rem;
        font-weight: 800;
    }

    h2 {
        font-weight: 750;
    }

    h3 {
        font-weight: 700;
    }

    /* Small spacing */
    .small-gap {
        margin-top: 8px;
        margin-bottom: 8px;
    }

    /* Hide unnecessary decoration */
    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if "study_plan" not in st.session_state:
    st.session_state["study_plan"] = None

if "study_sessions" not in st.session_state:
    st.session_state["study_sessions"] = None

if "subject_data" not in st.session_state:
    st.session_state["subject_data"] = None

if "rescheduled_plan" not in st.session_state:
    st.session_state["rescheduled_plan"] = None


# ============================================================
# HEADER
# ============================================================

st.title("📚 AI Study Assistant")

st.caption(
    "YOUR PERSONAL AI-POWERED ADAPTIVE STUDY PLANNER"
)

st.write(
    "Create a personalized study plan, understand your priorities, "
    "adapt when plans change, and sync your schedule with Google Calendar."
)


# ============================================================
# QUICK FEATURES
# ============================================================

st.subheader("✨ What your assistant can do")

feature1, feature2, feature3, feature4 = st.columns(4)

with feature1:
    with st.container(border=True):
        st.markdown("### 🤖")
        st.write("**AI Planning**")
        st.caption(
            "Creates a personalized study schedule."
        )

with feature2:
    with st.container(border=True):
        st.markdown("### 🎯")
        st.write("**Smart Priority**")
        st.caption(
            "Ranks subjects using exam urgency and progress."
        )

with feature3:
    with st.container(border=True):
        st.markdown("### 🔄")
        st.write("**Rescheduling**")
        st.caption(
            "Adapts your plan when your time changes."
        )

with feature4:
    with st.container(border=True):
        st.markdown("### 📅")
        st.write("**Google Calendar**")
        st.caption(
            "Adds your study sessions to Calendar."
        )


st.divider()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("📚 Study Assistant")

    st.caption(
        "Adaptive AI learning companion"
    )

    st.divider()

    st.subheader("How it works")

    st.markdown(
        """
        **1.** Add your subjects

        **2.** Enter exam dates

        **3.** Set difficulty

        **4.** Add syllabus progress

        **5.** Choose your study window

        **6.** Generate your plan

        **7.** Reschedule whenever needed
        """
    )

    st.divider()

    st.subheader("🎯 Priority Formula")

    st.write(
        "📅 Exam urgency — **40%**"
    )

    st.write(
        "🎯 Difficulty — **30%**"
    )

    st.write(
        "📚 Remaining syllabus — **30%**"
    )

    st.divider()

    st.caption(
        "Built with Streamlit + Hugging Face"
    )


# ============================================================
# TABS
# ============================================================

setup_tab, plan_tab, priority_tab, ai_tab = st.tabs(
    [
        "⚙️ Setup",
        "📅 Study Plan",
        "🎯 Priority",
        "🤖 AI Assistant"
    ]
)


# ============================================================
# SETUP TAB
# ============================================================

with setup_tab:

    st.header("👨‍🎓 Student Setup")

    st.caption(
        "Enter your subjects and tell the assistant how much time you have."
    )


    # --------------------------------------------------------
    # BASIC INFORMATION
    # --------------------------------------------------------

    col1, col2 = st.columns(
        [1, 2]
    )


    with col1:

        name = st.text_input(
            "Your Name",
            placeholder="Enter your name"
        )


    with col2:

        subjects_input = st.text_input(
            "Subjects",
            placeholder="Enter your subjects"
        )


    # --------------------------------------------------------
    # SUBJECT LIST
    # --------------------------------------------------------

    subject_names = [

        subject.strip()

        for subject in subjects_input.split(",")

        if subject.strip()

    ]


    # --------------------------------------------------------
    # SUBJECT INFORMATION
    # --------------------------------------------------------

    if subject_names:

        st.subheader("📚 Subject Information")

        st.caption(
            "These details help calculate the priority of each subject."
        )


        subject_data = []


        for subject in subject_names:

            with st.container(
                border=True
            ):

                st.markdown(
                    f"### 📖 {subject}"
                )


                col1, col2, col3 = st.columns(3)


                with col1:

                    exam_date = st.date_input(
                        "Exam Date",
                        value=date.today(),
                        key=f"exam_{subject}"
                    )


                with col2:

                    difficulty = st.selectbox(
                        "Difficulty",
                        [
                            "Easy",
                            "Medium",
                            "Hard"
                        ],
                        index=1,
                        key=f"difficulty_{subject}"
                    )


                with col3:

                    progress = st.slider(
                        "Syllabus Completed",
                        min_value=0,
                        max_value=100,
                        value=50,
                        step=5,
                        key=f"progress_{subject}"
                    )


                # --------------------------------------------
                # CALCULATE PRIORITY
                # --------------------------------------------

                priority_info = calculate_priority(

                    exam_date,

                    difficulty,

                    progress

                )


                subject_data.append({

                    "subject":
                        subject,

                    "exam_date":
                        exam_date,

                    "difficulty":
                        difficulty,

                    "progress":
                        progress,

                    "score":
                        priority_info["score"],

                    "priority":
                        priority_info["priority"],

                    "exam_score":
                        priority_info["exam_score"],

                    "difficulty_score":
                        priority_info["difficulty_score"],

                    "remaining_score":
                        priority_info["remaining_score"]

                })


                # --------------------------------------------
                # PRIORITY DISPLAY
                # --------------------------------------------

                p1, p2 = st.columns(2)


                with p1:

                    st.metric(
                        "Priority Score",
                        f"{priority_info['score']} / 100"
                    )


                with p2:

                    st.metric(
                        "Priority",
                        priority_info["priority"]
                    )


                st.progress(
                    priority_info["score"] / 100
                )


    # ========================================================
    # STUDY WINDOW
    # ========================================================

    st.divider()

    st.header("⏰ Your Study Window")

    st.caption(
        "Choose exactly when you are available to study."
    )


    time_col1, time_col2 = st.columns(2)


    with time_col1:

        start_time = st.time_input(
            "Start Time",
            value=time(18, 0)
        )


    with time_col2:

        end_time = st.time_input(
            "End Time",
            value=time(23, 0)
        )


    start_minutes = (

        start_time.hour * 60
        + start_time.minute

    )


    end_minutes = (

        end_time.hour * 60
        + end_time.minute

    )


    if end_minutes > start_minutes:

        available_minutes = (

            end_minutes
            - start_minutes

        )


        available_hours = (

            available_minutes / 60

        )


        st.success(

            f"⏱️ You have **{available_hours:.1f} hours** "
            "available for studying."

        )


    else:

        available_minutes = 0

        st.error(
            "⚠️ End time must be after start time."
        )


    # ========================================================
    # GENERATE PLAN
    # ========================================================

    st.write("")


    generate_button = st.button(
        "✨ Generate My Study Plan",
        type="primary",
        use_container_width=True
    )


    if generate_button:

        if not name:

            st.warning(
                "👤 Please enter your name."
            )


        elif not subject_names:

            st.warning(
                "📚 Please enter at least one subject."
            )


        elif available_minutes <= 0:

            st.error(
                "⏰ Please select a valid study window."
            )


        else:

            with st.spinner(
                "🧠 AI is creating your personalized study plan..."
            ):

                plan = generate_study_plan(

                    subject_data,

                    start_time,

                    end_time

                )


            # --------------------------------------------
            # SAVE PLAN
            # --------------------------------------------

            st.session_state[
                "study_plan"
            ] = plan["markdown"]


            st.session_state[
                "study_sessions"
            ] = plan["sessions"]


            st.session_state[
                "subject_data"
            ] = subject_data


            st.session_state[
                "name"
            ] = name


            st.session_state[
                "start_time"
            ] = start_time


            st.session_state[
                "end_time"
            ] = end_time


            st.session_state[
                "available_minutes"
            ] = available_minutes


            # --------------------------------------------
            # RESET OLD RESCHEDULED PLAN
            # --------------------------------------------

            st.session_state[
                "rescheduled_plan"
            ] = None


            st.session_state[
                "chat_history"
            ] = []


            st.success(
                "🎉 Your personalized study plan is ready!"
            )


# ============================================================
# STUDY PLAN TAB
# ============================================================

with plan_tab:

    if not st.session_state["study_plan"]:

        st.info(
            "👋 Generate a study plan from the "
            "**Setup** tab to see it here."
        )

    else:

        st.header(
            f"📅 {st.session_state['name']}'s Study Plan"
        )


        # ----------------------------------------------------
        # PLAN SUMMARY
        # ----------------------------------------------------

        available_hours = (

            st.session_state[
                "available_minutes"
            ] / 60

        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "⏱️ Study Time",
                f"{available_hours:.1f} hrs"
            )


        with col2:

            st.metric(
                "📚 Subjects",
                len(
                    st.session_state[
                        "subject_data"
                    ]
                )
            )


        with col3:

            st.metric(

                "🕐 Study Window",

                (
                    st.session_state[
                        "start_time"
                    ].strftime("%I:%M %p")

                    + " – "

                    + st.session_state[
                        "end_time"
                    ].strftime("%I:%M %p")
                )
            )


        st.write("")


        # ----------------------------------------------------
        # STUDY PLAN
        # ----------------------------------------------------

        with st.container(
            border=True
        ):

            st.markdown(
                st.session_state[
                    "study_plan"
                ]
            )


        st.divider()


        # ----------------------------------------------------
        # GOOGLE CALENDAR
        # ----------------------------------------------------

        st.header("📅 Google Calendar")

        st.caption(
            "Add your generated study sessions directly to your calendar."
        )


        calendar_date = st.date_input(
            "Study Date",
            value=date.today(),
            key="calendar_date"
        )


        if st.button(
            "📅 Add Study Plan to Google Calendar",
            type="primary",
            use_container_width=True
        ):

            try:

                events = add_study_plan_to_calendar(

                    st.session_state[
                        "study_sessions"
                    ],

                    calendar_date,

                    st.session_state[
                        "start_time"
                    ]

                )


                st.success(

                    f"✅ Added {len(events)} "
                    "study sessions to Google Calendar!"

                )


            except Exception as e:

                st.error(
                    f"❌ Google Calendar error: {e}"
                )


        st.info(
            "💡 Your plan is based on exam urgency, "
            "difficulty and remaining syllabus."
        )


# ============================================================
# PRIORITY TAB
# ============================================================

with priority_tab:

    if not st.session_state["subject_data"]:

        st.info(
            "Generate a study plan first to see your priority analysis."
        )

    else:

        st.header(
            "🎯 Smart Priority Analysis"
        )


        st.caption(
            "The assistant uses three factors to decide which subjects need more attention."
        )


        # ----------------------------------------------------
        # FORMULA
        # ----------------------------------------------------

        c1, c2, c3 = st.columns(3)


        with c1:

            st.metric(
                "📅 Exam Urgency",
                "40%"
            )


        with c2:

            st.metric(
                "🎯 Difficulty",
                "30%"
            )


        with c3:

            st.metric(
                "📚 Remaining Syllabus",
                "30%"
            )


        st.divider()


        # ----------------------------------------------------
        # SORT SUBJECTS
        # ----------------------------------------------------

        sorted_subjects = sorted(

            st.session_state[
                "subject_data"
            ],

            key=lambda x: x["score"],

            reverse=True

        )


        # ----------------------------------------------------
        # SUBJECT CARDS
        # ----------------------------------------------------

        number_of_columns = min(
            len(sorted_subjects),
            3
        )


        priority_columns = st.columns(
            number_of_columns
        )


        for index, item in enumerate(
            sorted_subjects
        ):

            with priority_columns[
                index % number_of_columns
            ]:

                with st.container(
                    border=True
                ):

                    st.subheader(
                        f"📚 {item['subject']}"
                    )


                    st.metric(
                        "Priority Score",
                        f"{item['score']}/100"
                    )


                    st.write(
                        f"**{item['priority']} Priority**"
                    )


                    st.progress(
                        item["score"] / 100
                    )


        st.divider()


        # ----------------------------------------------------
        # DETAILED BREAKDOWN
        # ----------------------------------------------------

        st.subheader(
            "🔍 Detailed Breakdown"
        )


        for item in sorted_subjects:

            with st.expander(

                f"📖 {item['subject']} — "
                f"{item['priority']} — "
                f"{item['score']}/100"

            ):

                col1, col2 = st.columns(2)


                with col1:

                    st.write(
                        f"📅 **Exam Date:** "
                        f"{item['exam_date']}"
                    )

                    st.write(
                        f"🎯 **Difficulty:** "
                        f"{item['difficulty']}"
                    )

                    st.write(
                        f"📊 **Syllabus Completed:** "
                        f"{item['progress']}%"
                    )

                    st.progress(
                        item["progress"] / 100
                    )


                with col2:

                    st.write(
                        f"📅 **Exam Urgency Score:** "
                        f"{item['exam_score']}"
                    )

                    st.write(
                        f"🎯 **Difficulty Score:** "
                        f"{item['difficulty_score']}"
                    )

                    st.write(
                        f"📚 **Remaining Syllabus Score:** "
                        f"{item['remaining_score']}"
                    )


        st.success(
            "💡 Higher-priority subjects receive more attention "
            "when your study time is limited."
        )


# ============================================================
# AI ASSISTANT TAB
# ============================================================

with ai_tab:

    if not st.session_state["study_plan"]:

        st.info(
            "Generate a study plan first. "
            "Then you can ask the AI to adapt it."
        )

    else:

        st.header(
            "🤖 AI Rescheduling Assistant"
        )


        st.caption(
            "Tell the AI what changed and it will adapt your plan."
        )


        # ----------------------------------------------------
        # EXAMPLES
        # ----------------------------------------------------

        with st.container(
            border=True
        ):

            st.subheader(
                "💬 Example requests"
            )


            st.write(
                "⏱️ **I only have 2 hours today.**"
            )

            st.write(
                "🚨 **I have my DSA exam tomorrow "
                "and only 3 hours to study.**"
            )

            st.write(
                "📚 **My DSA paper is the next morning "
                "and I've got 2 hours.**"
            )

            st.write(
                "📅 **I have a DSA test in 2 days "
                "and 4 hours available.**"
            )


        st.write("")


        # ----------------------------------------------------
        # CHAT HISTORY
        # ----------------------------------------------------

        for message in st.session_state[
            "chat_history"
        ]:

            with st.chat_message(
                message["role"]
            ):

                st.markdown(
                    message["content"]
                )


        # ----------------------------------------------------
        # CHAT INPUT
        # ----------------------------------------------------

        user_message = st.chat_input(
            "Tell me what changed..."
        )


        if user_message:

            # -----------------------------------------------
            # SAVE USER MESSAGE
            # -----------------------------------------------

            st.session_state[
                "chat_history"
            ].append({

                "role":
                    "user",

                "content":
                    user_message

            })


            with st.chat_message(
                "user"
            ):

                st.markdown(
                    user_message
                )


            # -----------------------------------------------
            # AI RESPONSE
            # -----------------------------------------------

            with st.chat_message(
                "assistant"
            ):

                with st.spinner(
                    "🧠 Understanding your request..."
                ):

                    new_plan = reschedule_plan(

                        st.session_state[
                            "subject_data"
                        ],

                        user_message,

                        st.session_state[
                            "start_time"
                        ]

                    )


                st.markdown(
                    "✅ I've adapted your study plan."
                )


            # -----------------------------------------------
            # SAVE NEW PLAN
            # -----------------------------------------------

            st.session_state[
                "rescheduled_plan"
            ] = new_plan


            st.session_state[
                "chat_history"
            ].append({

                "role":
                    "assistant",

                "content":
                    "✅ I've adapted your study plan."

            })


            st.rerun()


        # ----------------------------------------------------
        # UPDATED PLAN
        # ----------------------------------------------------

        if st.session_state[
            "rescheduled_plan"
        ]:

            st.divider()


            st.header(
                "🔄 Your Updated Plan"
            )


            with st.container(
                border=True
            ):

                st.markdown(
                    st.session_state[
                        "rescheduled_plan"
                    ]
                )


            st.success(
                "Your original plan is still available "
                "in the Study Plan tab."
            )


# ============================================================
# DETAILED DASHBOARD
# ============================================================

if st.session_state["subject_data"]:

    st.divider()


    with st.expander(
        "📊 Open Detailed Dashboard"
    ):

        show_dashboard(

            st.session_state[
                "subject_data"
            ]

        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "📚 AI Study Assistant  •  "
    "Built with Streamlit + Hugging Face  •  "
    "Adaptive AI Study Planning"
)
