# # # # # # # # import streamlit as st

# # # # # # # # st.set_page_config(
# # # # # # # #     page_title="AI Study Assistant",
# # # # # # # #     page_icon="📚"
# # # # # # # # )

# # # # # # # # st.title("📚 AI Study Assistant")
# # # # # # # # st.write("Your personal AI-powered study planner")

# # # # # # # # st.header("Student Information")

# # # # # # # # name = st.text_input("Your Name")

# # # # # # # # subjects = st.text_input(
# # # # # # # #     "Subjects",
# # # # # # # #     placeholder="DSA, Java, Maths"
# # # # # # # # )

# # # # # # # # hours = st.number_input(
# # # # # # # #     "Available study hours today",
# # # # # # # #     min_value=1,
# # # # # # # #     max_value=12,
# # # # # # # #     value=3
# # # # # # # # )

# # # # # # # # if st.button("Generate Study Plan"):

# # # # # # # #     if name and subjects:

# # # # # # # #         st.success("Study plan will be generated!")

# # # # # # # #         st.write("### 📅 Your Information")
# # # # # # # #         st.write(f"**Name:** {name}")
# # # # # # # #         st.write(f"**Subjects:** {subjects}")
# # # # # # # #         st.write(f"**Available Hours:** {hours}")

# # # # # # # #     else:
# # # # # # # #         st.warning("Please enter your name and subjects.")



# # # # # # # # import streamlit as st
# # # # # # # # from agent import generate_study_plan


# # # # # # # # st.set_page_config(
# # # # # # # #     page_title="AI Study Assistant",
# # # # # # # #     page_icon="📚"
# # # # # # # # )

# # # # # # # # st.title("📚 AI Study Assistant")
# # # # # # # # st.write("Your personal AI-powered study planner")

# # # # # # # # st.header("Student Information")

# # # # # # # # name = st.text_input("Your Name")

# # # # # # # # subjects = st.text_input(
# # # # # # # #     "Subjects",
# # # # # # # #     placeholder="DSA, Java, Maths"
# # # # # # # # )

# # # # # # # # hours = st.number_input(
# # # # # # # #     "Available study hours today",
# # # # # # # #     min_value=1,
# # # # # # # #     max_value=12,
# # # # # # # #     value=3
# # # # # # # # )

# # # # # # # # if st.button("Generate Study Plan"):

# # # # # # # #     if name and subjects:

# # # # # # # #         with st.spinner("🧠 AI is creating your study plan..."):

# # # # # # # #             plan = generate_study_plan(
# # # # # # # #                 subjects,
# # # # # # # #                 hours
# # # # # # # #             )

# # # # # # # #         st.success("Study plan generated!")

# # # # # # # #         st.subheader(f"📅 {name}'s Study Plan")

# # # # # # # #         st.markdown(plan)

# # # # # # # #     else:

# # # # # # # #         st.warning(
# # # # # # # #             "Please enter your name and subjects."
# # # # # # # #         )




# # # # # # # import streamlit as st
# # # # # # # from agent import generate_study_plan
# # # # # # # from rescheduler import reschedule_plan


# # # # # # # st.set_page_config(
# # # # # # #     page_title="AI Study Assistant",
# # # # # # #     page_icon="📚"
# # # # # # # )

# # # # # # # st.title("📚 AI Study Assistant")
# # # # # # # st.write("Your personal AI-powered study planner")


# # # # # # # # -----------------------------
# # # # # # # # STUDENT INFORMATION
# # # # # # # # -----------------------------

# # # # # # # st.header("👨‍🎓 Student Information")

# # # # # # # name = st.text_input("Your Name")

# # # # # # # subjects = st.text_input(
# # # # # # #     "Subjects",
# # # # # # #     placeholder="DSA, Java, Maths"
# # # # # # # )

# # # # # # # hours = st.number_input(
# # # # # # #     "Available study hours today",
# # # # # # #     min_value=1,
# # # # # # #     max_value=12,
# # # # # # #     value=3
# # # # # # # )


# # # # # # # # -----------------------------
# # # # # # # # GENERATE PLAN
# # # # # # # # -----------------------------

# # # # # # # if st.button("📚 Generate Study Plan"):

# # # # # # #     if name and subjects:

# # # # # # #         with st.spinner("🧠 Creating your study plan..."):

# # # # # # #             plan = generate_study_plan(
# # # # # # #                 subjects,
# # # # # # #                 hours
# # # # # # #             )

# # # # # # #         st.session_state["study_plan"] = plan
# # # # # # #         st.session_state["original_hours"] = hours

# # # # # # #     else:

# # # # # # #         st.warning("Please enter your name and subjects.")


# # # # # # # # -----------------------------
# # # # # # # # DISPLAY ORIGINAL PLAN
# # # # # # # # -----------------------------

# # # # # # # if "study_plan" in st.session_state:

# # # # # # #     st.success("Study plan generated!")

# # # # # # #     st.subheader(f"📅 {name}'s Study Plan")

# # # # # # #     st.markdown(
# # # # # # #         st.session_state["study_plan"]
# # # # # # #     )


# # # # # # #     # -----------------------------
# # # # # # #     # RESCHEDULER
# # # # # # #     # -----------------------------

# # # # # # #     st.divider()

# # # # # # #     st.header("🔄 Reschedule Your Plan")

# # # # # # #     st.write(
# # # # # # #         "Something came up? Tell the AI how much time you have now."
# # # # # # #     )

# # # # # # #     new_hours = st.number_input(
# # # # # # #         "How many hours do you have now?",
# # # # # # #         min_value=1,
# # # # # # #         max_value=12,
# # # # # # #         value=2
# # # # # # #     )

# # # # # # #     reason = st.text_area(
# # # # # # #         "What changed?",
# # # # # # #         placeholder="I only have 2 hours today."
# # # # # # #     )

# # # # # # #     if st.button("🔄 Reschedule Plan"):

# # # # # # #         if reason:

# # # # # # #             with st.spinner(
# # # # # # #                 "🧠 Rescheduling your study plan..."
# # # # # # #             ):

# # # # # # #                 new_plan = reschedule_plan(
# # # # # # #                     st.session_state["study_plan"],
# # # # # # #                     new_hours,
# # # # # # #                     reason
# # # # # # #                 )

# # # # # # #             st.session_state["rescheduled_plan"] = new_plan

# # # # # # #         else:

# # # # # # #             st.warning("Please explain why you need to reschedule.")


# # # # # # # # -----------------------------
# # # # # # # # DISPLAY NEW PLAN
# # # # # # # # -----------------------------

# # # # # # # if "rescheduled_plan" in st.session_state:

# # # # # # #     st.success("Plan successfully rescheduled!")

# # # # # # #     st.subheader("🔄 Your New Study Plan")

# # # # # # #     st.markdown(
# # # # # # #         st.session_state["rescheduled_plan"]
# # # # # # #     )





# # # # # # import streamlit as st

# # # # # # from agent import generate_study_plan
# # # # # # from rescheduler import reschedule_plan


# # # # # # # -----------------------------
# # # # # # # PAGE CONFIG
# # # # # # # -----------------------------

# # # # # # st.set_page_config(
# # # # # #     page_title="AI Study Assistant",
# # # # # #     page_icon="📚"
# # # # # # )


# # # # # # # -----------------------------
# # # # # # # TITLE
# # # # # # # -----------------------------

# # # # # # st.title("📚 AI Study Assistant")

# # # # # # st.write(
# # # # # #     "Your personal AI-powered study planner"
# # # # # # )


# # # # # # # -----------------------------
# # # # # # # STUDENT INFORMATION
# # # # # # # -----------------------------

# # # # # # st.header("👨‍🎓 Student Information")

# # # # # # name = st.text_input(
# # # # # #     "Your Name"
# # # # # # )

# # # # # # subjects = st.text_input(
# # # # # #     "Subjects",
# # # # # #     placeholder="DSA, Java, Maths"
# # # # # # )

# # # # # # hours = st.number_input(
# # # # # #     "Available study hours today",
# # # # # #     min_value=1,
# # # # # #     max_value=12,
# # # # # #     value=3
# # # # # # )


# # # # # # # -----------------------------
# # # # # # # GENERATE ORIGINAL PLAN
# # # # # # # -----------------------------

# # # # # # if st.button("📚 Generate Study Plan"):

# # # # # #     if name and subjects:

# # # # # #         with st.spinner(
# # # # # #             "🧠 AI is creating your study plan..."
# # # # # #         ):

# # # # # #             plan = generate_study_plan(
# # # # # #                 subjects,
# # # # # #                 hours
# # # # # #             )

# # # # # #         # Save the plan
# # # # # #         st.session_state["study_plan"] = plan
# # # # # #         st.session_state["original_hours"] = hours
# # # # # #         st.session_state["name"] = name

# # # # # #         # Remove old rescheduled plan
# # # # # #         if "rescheduled_plan" in st.session_state:
# # # # # #             del st.session_state["rescheduled_plan"]

# # # # # #     else:

# # # # # #         st.warning(
# # # # # #             "Please enter your name and subjects."
# # # # # #         )


# # # # # # # -----------------------------
# # # # # # # ORIGINAL STUDY PLAN
# # # # # # # -----------------------------

# # # # # # if "study_plan" in st.session_state:

# # # # # #     st.success("Study plan generated!")

# # # # # #     st.header(
# # # # # #         f"📅 {st.session_state['name']}'s Study Plan"
# # # # # #     )

# # # # # #     st.caption(
# # # # # #         f"Original available time: "
# # # # # #         f"{st.session_state['original_hours']} hours"
# # # # # #     )

# # # # # #     st.markdown(
# # # # # #         st.session_state["study_plan"]
# # # # # #     )


# # # # # #     # -----------------------------
# # # # # #     # AI CHAT
# # # # # #     # -----------------------------

# # # # # #     st.divider()

# # # # # #     st.header("🤖 AI Rescheduling Assistant")

# # # # # #     st.write(
# # # # # #         "Something changed? Tell the AI what happened."
# # # # # #     )

# # # # # #     st.info(
# # # # # #         "Example: "
# # # # # #         "\"I only have 2 hours today because I have an appointment.\""
# # # # # #     )


# # # # # #     # Chat history
# # # # # #     if "chat_history" not in st.session_state:
# # # # # #         st.session_state["chat_history"] = []


# # # # # #     # Display previous messages
# # # # # #     for message in st.session_state["chat_history"]:

# # # # # #         with st.chat_message(message["role"]):

# # # # # #             st.markdown(message["content"])


# # # # # #     # Chat input
# # # # # #     user_message = st.chat_input(
# # # # # #         "Tell me what changed..."
# # # # # #     )


# # # # # #     if user_message:

# # # # # #         # Show user message
# # # # # #         st.session_state["chat_history"].append(
# # # # # #             {
# # # # # #                 "role": "user",
# # # # # #                 "content": user_message
# # # # # #             }
# # # # # #         )

# # # # # #         with st.chat_message("user"):
# # # # # #             st.markdown(user_message)


# # # # # #         # Generate new plan
# # # # # #         with st.spinner(
# # # # # #             "🧠 AI is rescheduling your plan..."
# # # # # #         ):

# # # # # #             new_plan = reschedule_plan(
# # # # # #                 st.session_state["study_plan"],
# # # # # #                 user_message
# # # # # #             )


# # # # # #         # Save response
# # # # # #         st.session_state["rescheduled_plan"] = new_plan

# # # # # #         st.session_state["chat_history"].append(
# # # # # #             {
# # # # # #                 "role": "assistant",
# # # # # #                 "content": new_plan
# # # # # #             }
# # # # # #         )

# # # # # #         # Rerun to display everything properly
# # # # # #         st.rerun()


# # # # # # # -----------------------------
# # # # # # # RESCHEDULED PLAN
# # # # # # # -----------------------------

# # # # # # if "rescheduled_plan" in st.session_state:

# # # # # #     st.divider()

# # # # # #     st.header("🔄 Your Rescheduled Plan")

# # # # # #     st.markdown(
# # # # # #         st.session_state["rescheduled_plan"]
# # # # # #     )





# # # # # import streamlit as st
# # # # # from datetime import time

# # # # # from agent import generate_study_plan
# # # # # from rescheduler import reschedule_plan


# # # # # # ============================================
# # # # # # PAGE CONFIG
# # # # # # ============================================

# # # # # st.set_page_config(
# # # # #     page_title="AI Study Assistant",
# # # # #     page_icon="📚",
# # # # #     layout="centered"
# # # # # )


# # # # # # ============================================
# # # # # # TITLE
# # # # # # ============================================

# # # # # st.title("📚 AI Study Assistant")

# # # # # st.write(
# # # # #     "Your personal AI-powered study planner"
# # # # # )


# # # # # # ============================================
# # # # # # STUDENT INFORMATION
# # # # # # ============================================

# # # # # st.header("👨‍🎓 Student Information")


# # # # # name = st.text_input(
# # # # #     "Your Name"
# # # # # )


# # # # # subjects = st.text_input(
# # # # #     "Subjects",
# # # # #     placeholder="DSA, Java, Maths"
# # # # # )


# # # # # # ============================================
# # # # # # TIME SLOT
# # # # # # ============================================

# # # # # st.subheader("📅 Choose Your Study Time")


# # # # # start_time = st.time_input(
# # # # #     "Start Time",
# # # # #     value=time(18, 0)
# # # # # )


# # # # # end_time = st.time_input(
# # # # #     "End Time",
# # # # #     value=time(23, 0)
# # # # # )


# # # # # # Calculate available time

# # # # # start_minutes = (
# # # # #     start_time.hour * 60
# # # # #     + start_time.minute
# # # # # )


# # # # # end_minutes = (
# # # # #     end_time.hour * 60
# # # # #     + end_time.minute
# # # # # )


# # # # # if end_minutes > start_minutes:

# # # # #     available_minutes = (
# # # # #         end_minutes - start_minutes
# # # # #     )

# # # # #     available_hours = (
# # # # #         available_minutes / 60
# # # # #     )


# # # # #     st.info(
# # # # #         f"⏱️ Available study time: "
# # # # #         f"**{available_hours:.1f} hours**"
# # # # #     )


# # # # # else:

# # # # #     available_minutes = 0

# # # # #     st.error(
# # # # #         "⚠️ End time must be after start time."
# # # # #     )


# # # # # # ============================================
# # # # # # GENERATE PLAN
# # # # # # ============================================

# # # # # if st.button(
# # # # #     "📚 Generate Study Plan",
# # # # #     use_container_width=True
# # # # # ):

# # # # #     if not name or not subjects:

# # # # #         st.warning(
# # # # #             "Please enter your name and subjects."
# # # # #         )

# # # # #     elif available_minutes <= 0:

# # # # #         st.error(
# # # # #             "Please select a valid study time."
# # # # #         )

# # # # #     else:

# # # # #         with st.spinner(
# # # # #             "🧠 AI is creating your study plan..."
# # # # #         ):

# # # # #             plan = generate_study_plan(
# # # # #                 subjects,
# # # # #                 start_time,
# # # # #                 end_time
# # # # #             )


# # # # #         # Save information

# # # # #         st.session_state["study_plan"] = plan

# # # # #         st.session_state["name"] = name

# # # # #         st.session_state["subjects"] = subjects

# # # # #         st.session_state["start_time"] = start_time

# # # # #         st.session_state["end_time"] = end_time

# # # # #         st.session_state[
# # # # #             "available_minutes"
# # # # #         ] = available_minutes


# # # # #         # Clear previous rescheduling

# # # # #         if "rescheduled_plan" in st.session_state:

# # # # #             del st.session_state[
# # # # #                 "rescheduled_plan"
# # # # #             ]


# # # # #         if "chat_history" in st.session_state:

# # # # #             st.session_state[
# # # # #                 "chat_history"
# # # # #             ] = []


# # # # # # ============================================
# # # # # # ORIGINAL STUDY PLAN
# # # # # # ============================================

# # # # # if "study_plan" in st.session_state:

# # # # #     st.divider()


# # # # #     st.header(
# # # # #         f"📅 {st.session_state['name']}'s Study Plan"
# # # # #     )


# # # # #     original_hours = (
# # # # #         st.session_state[
# # # # #             "available_minutes"
# # # # #         ] / 60
# # # # #     )


# # # # #     st.caption(
# # # # #         f"🕐 Study Slot: "
# # # # #         f"{st.session_state['start_time'].strftime('%I:%M %p')}"
# # # # #         f" – "
# # # # #         f"{st.session_state['end_time'].strftime('%I:%M %p')}"
# # # # #     )


# # # # #     st.caption(
# # # # #         f"⏱️ Available Study Time: "
# # # # #         f"{original_hours:.1f} hours"
# # # # #     )


# # # # #     st.markdown(
# # # # #         st.session_state["study_plan"]
# # # # #     )


# # # # # # ============================================
# # # # # # AI RESCHEDULING ASSISTANT
# # # # # # ============================================

# # # # # if "study_plan" in st.session_state:

# # # # #     st.divider()


# # # # #     st.header(
# # # # #         "🤖 AI Rescheduling Assistant"
# # # # #     )


# # # # #     st.write(
# # # # #         "Something changed? "
# # # # #         "Tell the AI what happened."
# # # # #     )


# # # # #     st.info(
# # # # #         "Example: "
# # # # #         "\"I only have 2 hours today because "
# # # # #         "I have an appointment.\""
# # # # #     )


# # # # #     # Initialize chat history

# # # # #     if "chat_history" not in st.session_state:

# # # # #         st.session_state[
# # # # #             "chat_history"
# # # # #         ] = []


# # # # #     # Display previous messages

# # # # #     for message in st.session_state[
# # # # #         "chat_history"
# # # # #     ]:

# # # # #         with st.chat_message(
# # # # #             message["role"]
# # # # #         ):

# # # # #             st.markdown(
# # # # #                 message["content"]
# # # # #             )


# # # # #     # Chat input

# # # # #     user_message = st.chat_input(
# # # # #         "Tell me what changed..."
# # # # #     )


# # # # #     if user_message:

# # # # #         # Display user message

# # # # #         st.session_state[
# # # # #             "chat_history"
# # # # #         ].append({

# # # # #             "role": "user",

# # # # #             "content": user_message

# # # # #         })


# # # # #         with st.chat_message("user"):

# # # # #             st.markdown(
# # # # #                 user_message
# # # # #             )


# # # # #         # Generate new plan

# # # # #         with st.spinner(
# # # # #             "🧠 AI is rescheduling your plan..."
# # # # #         ):

# # # # #             new_plan = reschedule_plan(

# # # # #                 st.session_state[
# # # # #                     "study_plan"
# # # # #                 ],

# # # # #                 user_message,

# # # # #                 st.session_state[
# # # # #                     "start_time"
# # # # #                 ],

# # # # #                 st.session_state[
# # # # #                     "end_time"
# # # # #                 ]

# # # # #             )


# # # # #         # Save new plan

# # # # #         st.session_state[
# # # # #             "rescheduled_plan"
# # # # #         ] = new_plan


# # # # #         # Add AI response

# # # # #         st.session_state[
# # # # #             "chat_history"
# # # # #         ].append({

# # # # #             "role": "assistant",

# # # # #             "content": new_plan

# # # # #         })


# # # # #         st.rerun()


# # # # # # ============================================
# # # # # # RESCHEDULED PLAN
# # # # # # ============================================

# # # # # if "rescheduled_plan" in st.session_state:

# # # # #     st.divider()


# # # # #     st.header(
# # # # #         "🔄 Your Rescheduled Plan"
# # # # #     )


# # # # #     st.markdown(
# # # # #         st.session_state[
# # # # #             "rescheduled_plan"
# # # # #         ]
# # # # #     )





# # # # import streamlit as st
# # # # from datetime import time

# # # # from agent import generate_study_plan
# # # # from rescheduler import reschedule_plan


# # # # # ============================================
# # # # # PAGE CONFIG
# # # # # ============================================

# # # # st.set_page_config(
# # # #     page_title="AI Study Assistant",
# # # #     page_icon="📚",
# # # #     layout="centered"
# # # # )


# # # # # ============================================
# # # # # TITLE
# # # # # ============================================

# # # # st.title("📚 AI Study Assistant")

# # # # st.write(
# # # #     "Your personal AI-powered study planner"
# # # # )


# # # # # ============================================
# # # # # STUDENT INFORMATION
# # # # # ============================================

# # # # st.header("👨‍🎓 Student Information")

# # # # name = st.text_input(
# # # #     "Your Name"
# # # # )

# # # # subjects = st.text_input(
# # # #     "Subjects",
# # # #     placeholder="DSA, Java, Maths"
# # # # )


# # # # # ============================================
# # # # # TIME SLOT
# # # # # ============================================

# # # # st.subheader("📅 Choose Your Study Time")

# # # # start_time = st.time_input(
# # # #     "Start Time",
# # # #     value=time(18, 0)
# # # # )

# # # # end_time = st.time_input(
# # # #     "End Time",
# # # #     value=time(23, 0)
# # # # )


# # # # # Calculate available time

# # # # start_minutes = (
# # # #     start_time.hour * 60
# # # #     + start_time.minute
# # # # )

# # # # end_minutes = (
# # # #     end_time.hour * 60
# # # #     + end_time.minute
# # # # )


# # # # if end_minutes > start_minutes:

# # # #     available_minutes = (
# # # #         end_minutes - start_minutes
# # # #     )

# # # #     available_hours = (
# # # #         available_minutes / 60
# # # #     )

# # # #     st.info(
# # # #         f"⏱️ Available study time: "
# # # #         f"**{available_hours:.1f} hours**"
# # # #     )

# # # # else:

# # # #     available_minutes = 0

# # # #     st.error(
# # # #         "⚠️ End time must be after start time."
# # # #     )


# # # # # ============================================
# # # # # GENERATE STUDY PLAN
# # # # # ============================================

# # # # if st.button(
# # # #     "📚 Generate Study Plan",
# # # #     use_container_width=True
# # # # ):

# # # #     if not name or not subjects:

# # # #         st.warning(
# # # #             "Please enter your name and subjects."
# # # #         )

# # # #     elif available_minutes <= 0:

# # # #         st.error(
# # # #             "Please select a valid study time."
# # # #         )

# # # #     else:

# # # #         with st.spinner(
# # # #             "🧠 AI is creating your study plan..."
# # # #         ):

# # # #             plan = generate_study_plan(
# # # #                 subjects,
# # # #                 start_time,
# # # #                 end_time
# # # #             )


# # # #         # Save information

# # # #         st.session_state["study_plan"] = plan

# # # #         st.session_state["name"] = name

# # # #         st.session_state["subjects"] = subjects

# # # #         st.session_state["start_time"] = start_time

# # # #         st.session_state["end_time"] = end_time

# # # #         st.session_state[
# # # #             "available_minutes"
# # # #         ] = available_minutes


# # # #         # Clear previous rescheduled plan

# # # #         if "rescheduled_plan" in st.session_state:

# # # #             del st.session_state[
# # # #                 "rescheduled_plan"
# # # #             ]


# # # #         # Clear previous chat

# # # #         st.session_state[
# # # #             "chat_history"
# # # #         ] = []


# # # # # ============================================
# # # # # ORIGINAL STUDY PLAN
# # # # # ============================================

# # # # if "study_plan" in st.session_state:

# # # #     st.divider()

# # # #     st.header(
# # # #         f"📅 {st.session_state['name']}'s Study Plan"
# # # #     )


# # # #     original_hours = (
# # # #         st.session_state[
# # # #             "available_minutes"
# # # #         ] / 60
# # # #     )


# # # #     st.caption(
# # # #         f"🕐 Study Slot: "
# # # #         f"{st.session_state['start_time'].strftime('%I:%M %p')}"
# # # #         f" – "
# # # #         f"{st.session_state['end_time'].strftime('%I:%M %p')}"
# # # #     )


# # # #     st.caption(
# # # #         f"⏱️ Available Study Time: "
# # # #         f"{original_hours:.1f} hours"
# # # #     )


# # # #     # Display original plan

# # # #     st.markdown(
# # # #         st.session_state["study_plan"]
# # # #     )


# # # # # ============================================
# # # # # AI RESCHEDULING ASSISTANT
# # # # # ============================================

# # # # if "study_plan" in st.session_state:

# # # #     st.divider()

# # # #     st.header(
# # # #         "🤖 AI Rescheduling Assistant"
# # # #     )

# # # #     st.write(
# # # #         "Something changed? "
# # # #         "Tell the AI what happened."
# # # #     )


# # # #     st.info(
# # # #         "Example: "
# # # #         "\"I only have 2 hours today because "
# # # #         "I have an appointment.\""
# # # #     )


# # # #     # Initialize chat history

# # # #     if "chat_history" not in st.session_state:

# # # #         st.session_state[
# # # #             "chat_history"
# # # #         ] = []


# # # #     # Display chat messages

# # # #     for message in st.session_state[
# # # #         "chat_history"
# # # #     ]:

# # # #         with st.chat_message(
# # # #             message["role"]
# # # #         ):

# # # #             st.markdown(
# # # #                 message["content"]
# # # #             )


# # # #     # Chat input

# # # #     user_message = st.chat_input(
# # # #         "Tell me what changed..."
# # # #     )


# # # #     if user_message:

# # # #         # ------------------------------------
# # # #         # USER MESSAGE
# # # #         # ------------------------------------

# # # #         st.session_state[
# # # #             "chat_history"
# # # #         ].append({

# # # #             "role": "user",

# # # #             "content": user_message

# # # #         })


# # # #         with st.chat_message("user"):

# # # #             st.markdown(
# # # #                 user_message
# # # #             )


# # # #         # ------------------------------------
# # # #         # GENERATE RESCHEDULED PLAN
# # # #         # ------------------------------------

# # # #         with st.spinner(
# # # #             "🧠 AI is rescheduling your plan..."
# # # #         ):

# # # #             new_plan = reschedule_plan(

# # # #                 st.session_state[
# # # #                     "study_plan"
# # # #                 ],

# # # #                 user_message,

# # # #                 st.session_state[
# # # #                     "start_time"
# # # #                 ],

# # # #                 st.session_state[
# # # #                     "end_time"
# # # #                 ]

# # # #             )


# # # #         # ------------------------------------
# # # #         # SAVE NEW PLAN
# # # #         # ------------------------------------

# # # #         st.session_state[
# # # #             "rescheduled_plan"
# # # #         ] = new_plan


# # # #         # ------------------------------------
# # # #         # SHORT AI CHAT RESPONSE
# # # #         # ------------------------------------

# # # #         st.session_state[
# # # #             "chat_history"
# # # #         ].append({

# # # #             "role": "assistant",

# # # #             "content":
# # # #                 "✅ I've rescheduled your "
# # # #                 "study plan based on your new "
# # # #                 "available time. Your updated "
# # # #                 "plan is shown below."

# # # #         })


# # # #         # Refresh page

# # # #         st.rerun()


# # # # # ============================================
# # # # # RESCHEDULED PLAN
# # # # # ============================================

# # # # if "rescheduled_plan" in st.session_state:

# # # #     st.divider()

# # # #     st.header(
# # # #         "🔄 Your Rescheduled Plan"
# # # #     )


# # # #     # Display the plan ONLY here

# # # #     st.markdown(
# # # #         st.session_state[
# # # #             "rescheduled_plan"
# # # #         ]
# # # #     )












# # # import streamlit as st
# # # from datetime import time, date

# # # from agent import generate_study_plan
# # # from priority import calculate_priority
# # # from rescheduler import reschedule_plan
# # # from dashboard import show_dashboard
# # # from google_calendar import add_study_plan_to_calendar


# # # # ============================================
# # # # PAGE CONFIG
# # # # ============================================

# # # st.set_page_config(
# # #     page_title="AI Study Assistant",
# # #     page_icon="📚",
# # #     layout="centered"
# # # )


# # # # ============================================
# # # # TITLE
# # # # ============================================

# # # st.title("📚 AI Study Assistant")

# # # st.write(
# # #     "YOUR PERSONAL AI-POWERED ADAPTIVE STUDY PLANNER"
# # # )


# # # # ============================================
# # # # STUDENT INFORMATION
# # # # ============================================

# # # st.header("👨‍🎓 Student Information")


# # # name = st.text_input(
# # #     "Your Name"
# # # )


# # # subjects_input = st.text_input(
# # #     "Subjects",
# # #     placeholder="DSA, Java, Maths"
# # # )


# # # # ============================================
# # # # SUBJECT INFORMATION
# # # # ============================================

# # # subject_names = [
# # #     subject.strip()
# # #     for subject in subjects_input.split(",")
# # #     if subject.strip()
# # # ]


# # # if subject_names:

# # #     st.subheader(
# # #         "📊 Subject Information"
# # #     )

# # #     st.caption(
# # #         "This information is used to calculate "
# # #         "priority."
# # #     )


# # #     subject_data = []


# # #     for subject in subject_names:

# # #         st.markdown(
# # #             f"### 📚 {subject}"
# # #         )


# # #         col1, col2 = st.columns(2)


# # #         with col1:

# # #             exam_date = st.date_input(
# # #                 f"Exam Date — {subject}",
# # #                 value=date.today(),
# # #                 key=f"exam_{subject}"
# # #             )


# # #         with col2:

# # #             difficulty = st.selectbox(
# # #                 f"Difficulty — {subject}",
# # #                 [
# # #                     "Easy",
# # #                     "Medium",
# # #                     "Hard"
# # #                 ],
# # #                 index=1,
# # #                 key=f"difficulty_{subject}"
# # #             )


# # #         progress = st.slider(
# # #             f"Completed Syllabus — {subject}",
# # #             min_value=0,
# # #             max_value=100,
# # #             value=50,
# # #             step=5,
# # #             key=f"progress_{subject}"
# # #         )


# # #         # Calculate priority

# # #         priority_info = calculate_priority(

# # #             exam_date,

# # #             difficulty,

# # #             progress

# # #         )


# # #         subject_data.append({

# # #             "subject": subject,

# # #             "exam_date": exam_date,

# # #             "difficulty": difficulty,

# # #             "progress": progress,

# # #             "score": priority_info["score"],

# # #             "priority": priority_info["priority"],

# # #             "exam_score": priority_info["exam_score"],

# # #             "difficulty_score":
# # #                 priority_info[
# # #                     "difficulty_score"
# # #                 ],

# # #             "remaining_score":
# # #                 priority_info[
# # #                     "remaining_score"
# # #                 ]

# # #         })


# # #         # Show score

# # #         st.write(
# # #             f"🎯 Priority Score: "
# # #             f"**{priority_info['score']} / 100**"
# # #         )


# # #         st.write(
# # #             f"Priority: "
# # #             f"**{priority_info['priority']}**"
# # #         )


# # #         st.divider()


# # # # ============================================
# # # # TIME SLOT
# # # # ============================================

# # # st.subheader(
# # #     "📅 Choose Your Study Time"
# # # )


# # # start_time = st.time_input(
# # #     "Start Time",
# # #     value=time(18, 0)
# # # )


# # # end_time = st.time_input(
# # #     "End Time",
# # #     value=time(23, 0)
# # # )


# # # start_minutes = (
# # #     start_time.hour * 60
# # #     + start_time.minute
# # # )


# # # end_minutes = (
# # #     end_time.hour * 60
# # #     + end_time.minute
# # # )


# # # if end_minutes > start_minutes:

# # #     available_minutes = (
# # #         end_minutes
# # #         - start_minutes
# # #     )


# # #     available_hours = (
# # #         available_minutes / 60
# # #     )


# # #     st.info(
# # #         f"⏱️ Available study time: "
# # #         f"**{available_hours:.1f} hours**"
# # #     )


# # # else:

# # #     available_minutes = 0


# # #     st.error(
# # #         "⚠️ End time must be after "
# # #         "start time."
# # #     )


# # # # ============================================
# # # # GENERATE PLAN
# # # # ============================================

# # # if st.button(
# # #     "📚 Generate Study Plan",
# # #     use_container_width=True
# # # ):

# # #     if not name:

# # #         st.warning(
# # #             "Please enter your name."
# # #         )


# # #     elif not subject_names:

# # #         st.warning(
# # #             "Please enter at least one subject."
# # #         )


# # #     elif available_minutes <= 0:

# # #         st.error(
# # #             "Please select a valid study time."
# # #         )


# # #     else:

# # #         with st.spinner(
# # #             "🧠 AI is creating your "
# # #             "personalized study plan..."
# # #         ):

# # #             plan = generate_study_plan(

# # #                 subject_data,

# # #                 start_time,

# # #                 end_time

# # #             )


# # #         # Save everything

# # #         st.session_state[
# # #             "study_plan"
# # #         ] = plan["markdown"]


# # #         st.session_state[
# # #             "study_sessions"
# # #         ] = plan["sessions"]


# # #         st.session_state[
# # #             "subject_data"
# # #         ] = subject_data


# # #         st.session_state[
# # #             "name"
# # #         ] = name


# # #         st.session_state[
# # #             "start_time"
# # #         ] = start_time


# # #         st.session_state[
# # #             "end_time"
# # #         ] = end_time


# # #         st.session_state[
# # #             "available_minutes"
# # #         ] = available_minutes


# # #         # Clear old reschedule

# # #         if "rescheduled_plan" in st.session_state:

# # #             del st.session_state[
# # #                 "rescheduled_plan"
# # #             ]


# # #         st.session_state[
# # #             "chat_history"
# # #         ] = []



# # # # ============================================
# # # # STUDY DASHBOARD
# # # # ============================================

# # # if "subject_data" in st.session_state:

# # #     st.divider()

# # #     show_dashboard(
# # #         st.session_state["subject_data"]
# # #     )




# # # # ============================================
# # # # ORIGINAL STUDY PLAN
# # # # ============================================

# # # if "study_plan" in st.session_state:

# # #     st.divider()


# # #     st.header(
# # #         f"📅 "
# # #         f"{st.session_state['name']}'s "
# # #         f"Study Plan"
# # #     )


# # #     original_hours = (
# # #         st.session_state[
# # #             "available_minutes"
# # #         ] / 60
# # #     )


# # #     st.caption(
# # #         f"🕐 Study Slot: "
# # #         f"{st.session_state['start_time'].strftime('%I:%M %p')}"
# # #         f" – "
# # #         f"{st.session_state['end_time'].strftime('%I:%M %p')}"
# # #     )


# # #     st.caption(
# # #         f"⏱️ Available Study Time: "
# # #         f"{original_hours:.1f} hours"
# # #     )


# # #     st.markdown(
# # #         st.session_state[
# # #             "study_plan"
# # #         ]
# # #     )

# # #     st.info(
# # #     "💡 The AI prioritizes subjects using "
# # #     "exam urgency, difficulty, and remaining "
# # #     "syllabus. If your available time is too "
# # #     "short, lower-priority subjects may be "
# # #     "deferred."
# # # )


# # # # ============================================
# # # # PRIORITY ANALYSIS
# # # # ============================================

# # # if "subject_data" in st.session_state:

# # #     st.divider()


# # #     st.header(
# # #         "🎯 Priority Analysis"
# # #     )


# # #     st.write(
# # #         "The priority score is calculated using:"
# # #     )


# # #     st.markdown(
# # #         """
# # #         **40% Exam Urgency + 30% Difficulty + 30% Remaining Syllabus**
# # #         """
# # #     )


# # #     for item in sorted(
# # #         st.session_state["subject_data"],
# # #         key=lambda x: x["score"],
# # #         reverse=True
# # #     ):

# # #         with st.expander(
# # #             f"{item['subject']} — "
# # #             f"{item['priority']} "
# # #             f"({item['score']}/100)"
# # #         ):

# # #             st.write(
# # #                 f"📅 Exam Date: "
# # #                 f"{item['exam_date']}"
# # #             )


# # #             st.write(
# # #                 f"🎯 Difficulty: "
# # #                 f"{item['difficulty']}"
# # #             )


# # #             st.write(
# # #                 f"📊 Completed: "
# # #                 f"{item['progress']}%"
# # #             )


# # #             st.write(
# # #                 f"⏳ Remaining: "
# # #                 f"{100 - item['progress']}%"
# # #             )


# # #             st.write(
# # #                 f"📅 Exam Urgency Score: "
# # #                 f"{item['exam_score']}"
# # #             )


# # #             st.write(
# # #                 f"🎯 Difficulty Score: "
# # #                 f"{item['difficulty_score']}"
# # #             )


# # #             st.write(
# # #                 f"📚 Remaining Syllabus Score: "
# # #                 f"{item['remaining_score']}"
# # #             )


# # # # ============================================
# # # # AI RESCHEDULING ASSISTANT
# # # # ============================================

# # # if "study_plan" in st.session_state:

# # #     st.divider()


# # #     st.header(
# # #         "🤖 AI Rescheduling Assistant"
# # #     )


# # #     st.write(
# # #         "Something changed? "
# # #         "Tell the AI what happened."
# # #     )


# # #     st.info(
# # #         "Example: "
# # #         "\"I only have 1.5 hours today "
# # #         "because I have an appointment.\""
# # #     )


# # #     if "chat_history" not in st.session_state:

# # #         st.session_state[
# # #             "chat_history"
# # #         ] = []


# # #     for message in st.session_state[
# # #         "chat_history"
# # #     ]:

# # #         with st.chat_message(
# # #             message["role"]
# # #         ):

# # #             st.markdown(
# # #                 message["content"]
# # #             )


# # #     user_message = st.chat_input(
# # #         "Tell me what changed..."
# # #     )


# # #     if user_message:

# # #         st.session_state[
# # #             "chat_history"
# # #         ].append({

# # #             "role": "user",

# # #             "content": user_message

# # #         })


# # #         with st.chat_message("user"):

# # #             st.markdown(
# # #                 user_message
# # #             )


# # #         with st.spinner(
# # #             "🧠 Rescheduling..."
# # #         ):

# # #             new_plan = reschedule_plan(

# # #                 st.session_state[
# # #                     "subject_data"
# # #                 ],

# # #                 user_message,

# # #                 st.session_state[
# # #                     "start_time"
# # #                 ]

# # #             )


# # #         st.session_state[
# # #             "rescheduled_plan"
# # #         ] = new_plan


# # #         st.session_state[
# # #             "chat_history"
# # #         ].append({

# # #             "role": "assistant",

# # #             "content":
# # #                 "✅ I've rescheduled your "
# # #                 "plan using your priority "
# # #                 "scores. Your updated plan "
# # #                 "is shown below."

# # #         })


# # #         st.rerun()


# # # # ============================================
# # # # RESCHEDULED PLAN
# # # # ============================================

# # # if "rescheduled_plan" in st.session_state:

# # #     st.divider()


# # #     st.header(
# # #         "🔄 Your Rescheduled Plan"
# # #     )


# # #     st.markdown(
# # #         st.session_state[
# # #             "rescheduled_plan"
# # #         ]
# # #     )













# # import streamlit as st
# # from datetime import time, date

# # from agent import generate_study_plan
# # from priority import calculate_priority
# # from rescheduler import reschedule_plan
# # from dashboard import show_dashboard
# # from google_calendar import add_study_plan_to_calendar


# # # ============================================
# # # PAGE CONFIG
# # # ============================================

# # st.set_page_config(
# #     page_title="AI Study Assistant",
# #     page_icon="📚",
# #     layout="centered"
# # )


# # # ============================================
# # # TITLE
# # # ============================================

# # st.title("📚 AI Study Assistant")

# # st.write(
# #     "YOUR PERSONAL AI-POWERED ADAPTIVE STUDY PLANNER"
# # )


# # # ============================================
# # # STUDENT INFORMATION
# # # ============================================

# # st.header("👨‍🎓 Student Information")

# # name = st.text_input(
# #     "Your Name"
# # )

# # subjects_input = st.text_input(
# #     "Subjects",
# #     placeholder="DSA, Java, Maths"
# # )


# # # ============================================
# # # SUBJECT INFORMATION
# # # ============================================

# # subject_names = [
# #     subject.strip()
# #     for subject in subjects_input.split(",")
# #     if subject.strip()
# # ]


# # if subject_names:

# #     st.subheader(
# #         "📊 Subject Information"
# #     )

# #     st.caption(
# #         "This information is used to calculate "
# #         "priority."
# #     )

# #     subject_data = []

# #     for subject in subject_names:

# #         st.markdown(
# #             f"### 📚 {subject}"
# #         )

# #         col1, col2 = st.columns(2)

# #         with col1:

# #             exam_date = st.date_input(
# #                 f"Exam Date — {subject}",
# #                 value=date.today(),
# #                 key=f"exam_{subject}"
# #             )

# #         with col2:

# #             difficulty = st.selectbox(
# #                 f"Difficulty — {subject}",
# #                 [
# #                     "Easy",
# #                     "Medium",
# #                     "Hard"
# #                 ],
# #                 index=1,
# #                 key=f"difficulty_{subject}"
# #             )

# #         progress = st.slider(
# #             f"Completed Syllabus — {subject}",
# #             min_value=0,
# #             max_value=100,
# #             value=50,
# #             step=5,
# #             key=f"progress_{subject}"
# #         )

# #         # ----------------------------------------
# #         # CALCULATE PRIORITY
# #         # ----------------------------------------

# #         priority_info = calculate_priority(
# #             exam_date,
# #             difficulty,
# #             progress
# #         )

# #         subject_data.append({

# #             "subject": subject,

# #             "exam_date": exam_date,

# #             "difficulty": difficulty,

# #             "progress": progress,

# #             "score": priority_info["score"],

# #             "priority": priority_info["priority"],

# #             "exam_score": priority_info["exam_score"],

# #             "difficulty_score":
# #                 priority_info["difficulty_score"],

# #             "remaining_score":
# #                 priority_info["remaining_score"]

# #         })

# #         # ----------------------------------------
# #         # SHOW PRIORITY
# #         # ----------------------------------------

# #         st.write(
# #             f"🎯 Priority Score: "
# #             f"**{priority_info['score']} / 100**"
# #         )

# #         st.write(
# #             f"Priority: "
# #             f"**{priority_info['priority']}**"
# #         )

# #         st.divider()


# # # ============================================
# # # TIME SLOT
# # # ============================================

# # st.subheader(
# #     "📅 Choose Your Study Time"
# # )

# # start_time = st.time_input(
# #     "Start Time",
# #     value=time(18, 0)
# # )

# # end_time = st.time_input(
# #     "End Time",
# #     value=time(23, 0)
# # )


# # start_minutes = (
# #     start_time.hour * 60
# #     + start_time.minute
# # )

# # end_minutes = (
# #     end_time.hour * 60
# #     + end_time.minute
# # )


# # if end_minutes > start_minutes:

# #     available_minutes = (
# #         end_minutes
# #         - start_minutes
# #     )

# #     available_hours = (
# #         available_minutes / 60
# #     )

# #     st.info(
# #         f"⏱️ Available study time: "
# #         f"**{available_hours:.1f} hours**"
# #     )

# # else:

# #     available_minutes = 0

# #     st.error(
# #         "⚠️ End time must be after "
# #         "start time."
# #     )


# # # ============================================
# # # GENERATE PLAN
# # # ============================================

# # if st.button(
# #     "📚 Generate Study Plan",
# #     use_container_width=True
# # ):

# #     if not name:

# #         st.warning(
# #             "Please enter your name."
# #         )

# #     elif not subject_names:

# #         st.warning(
# #             "Please enter at least one subject."
# #         )

# #     elif available_minutes <= 0:

# #         st.error(
# #             "Please select a valid study time."
# #         )

# #     else:

# #         with st.spinner(
# #             "🧠 AI is creating your "
# #             "personalized study plan..."
# #         ):

# #             plan = generate_study_plan(
# #                 subject_data,
# #                 start_time,
# #                 end_time
# #             )

# #         # ----------------------------------------
# #         # SAVE PLAN
# #         # ----------------------------------------

# #         st.session_state[
# #             "study_plan"
# #         ] = plan["markdown"]

# #         st.session_state[
# #             "study_sessions"
# #         ] = plan["sessions"]

# #         st.session_state[
# #             "subject_data"
# #         ] = subject_data

# #         st.session_state[
# #             "name"
# #         ] = name

# #         st.session_state[
# #             "start_time"
# #         ] = start_time

# #         st.session_state[
# #             "end_time"
# #         ] = end_time

# #         st.session_state[
# #             "available_minutes"
# #         ] = available_minutes

# #         # ----------------------------------------
# #         # CLEAR OLD RESCHEDULE
# #         # ----------------------------------------

# #         if "rescheduled_plan" in st.session_state:

# #             del st.session_state[
# #                 "rescheduled_plan"
# #             ]

# #         # ----------------------------------------
# #         # CLEAR CHAT
# #         # ----------------------------------------

# #         st.session_state[
# #             "chat_history"
# #         ] = []


# # # ============================================
# # # STUDY DASHBOARD
# # # ============================================

# # if "subject_data" in st.session_state:

# #     st.divider()

# #     show_dashboard(
# #         st.session_state["subject_data"]
# #     )


# # # ============================================
# # # ORIGINAL STUDY PLAN
# # # ============================================

# # if "study_plan" in st.session_state:

# #     st.divider()

# #     st.header(
# #         f"📅 "
# #         f"{st.session_state['name']}'s "
# #         f"Study Plan"
# #     )

# #     original_hours = (
# #         st.session_state[
# #             "available_minutes"
# #         ] / 60
# #     )

# #     st.caption(
# #         f"🕐 Study Slot: "
# #         f"{st.session_state['start_time'].strftime('%I:%M %p')}"
# #         f" – "
# #         f"{st.session_state['end_time'].strftime('%I:%M %p')}"
# #     )

# #     st.caption(
# #         f"⏱️ Available Study Time: "
# #         f"{original_hours:.1f} hours"
# #     )

# #     # ----------------------------------------
# #     # SHOW PLAN
# #     # ----------------------------------------

# #     st.markdown(
# #         st.session_state[
# #             "study_plan"
# #         ]
# #     )

# #     # ========================================
# #     # GOOGLE CALENDAR
# #     # ========================================

# #     st.subheader(
# #         "📅 Google Calendar"
# #     )

# #     st.write(
# #         "Add your generated study plan "
# #         "directly to Google Calendar."
# #     )

# #     calendar_date = st.date_input(
# #         "Study Date",
# #         value=date.today(),
# #         key="calendar_date"
# #     )

# #     if st.button(
# #         "📅 Add Study Plan to Google Calendar",
# #         use_container_width=True
# #     ):

# #         try:

# #             events = add_study_plan_to_calendar(

# #                 st.session_state[
# #                     "study_sessions"
# #                 ],

# #                 calendar_date,

# #                 st.session_state[
# #                     "start_time"
# #                 ]

# #             )

# #             st.success(
# #                 f"✅ Added {len(events)} "
# #                 "study sessions to Google Calendar!"
# #             )

# #         except Exception as e:

# #             st.error(
# #                 f"❌ Google Calendar error: {e}"
# #             )

# #     # ----------------------------------------
# #     # INFORMATION
# #     # ----------------------------------------

# #     st.info(
# #         "💡 The AI prioritizes subjects using "
# #         "exam urgency, difficulty, and remaining "
# #         "syllabus. If your available time is too "
# #         "short, lower-priority subjects may be "
# #         "deferred."
# #     )


# # # ============================================
# # # PRIORITY ANALYSIS
# # # ============================================

# # if "subject_data" in st.session_state:

# #     st.divider()

# #     st.header(
# #         "🎯 Priority Analysis"
# #     )

# #     st.write(
# #         "The priority score is calculated using:"
# #     )

# #     st.markdown(
# #         """
# #         **40% Exam Urgency + 30% Difficulty + 30% Remaining Syllabus**
# #         """
# #     )

# #     for item in sorted(
# #         st.session_state["subject_data"],
# #         key=lambda x: x["score"],
# #         reverse=True
# #     ):

# #         with st.expander(
# #             f"{item['subject']} — "
# #             f"{item['priority']} "
# #             f"({item['score']}/100)"
# #         ):

# #             st.write(
# #                 f"📅 Exam Date: "
# #                 f"{item['exam_date']}"
# #             )

# #             st.write(
# #                 f"🎯 Difficulty: "
# #                 f"{item['difficulty']}"
# #             )

# #             st.write(
# #                 f"📊 Completed: "
# #                 f"{item['progress']}%"
# #             )

# #             st.write(
# #                 f"⏳ Remaining: "
# #                 f"{100 - item['progress']}%"
# #             )

# #             st.write(
# #                 f"📅 Exam Urgency Score: "
# #                 f"{item['exam_score']}"
# #             )

# #             st.write(
# #                 f"🎯 Difficulty Score: "
# #                 f"{item['difficulty_score']}"
# #             )

# #             st.write(
# #                 f"📚 Remaining Syllabus Score: "
# #                 f"{item['remaining_score']}"
# #             )


# # # ============================================
# # # AI RESCHEDULING ASSISTANT
# # # ============================================

# # if "study_plan" in st.session_state:

# #     st.divider()

# #     st.header(
# #         "🤖 AI Rescheduling Assistant"
# #     )

# #     st.write(
# #         "Something changed? "
# #         "Tell the AI what happened."
# #     )

# #     st.info(
# #         "Examples:\n\n"
# #         "• \"I only have 1.5 hours today "
# #         "because I have an appointment.\"\n\n"
# #         "• \"I have my DSA exam tomorrow "
# #         "and only 3 hours to study.\"\n\n"
# #         "• \"My DSA paper is the next morning "
# #         "and I've got 2 hours.\"\n\n"
# #         "• \"I have a DSA test in 2 days "
# #         "and 4 hours available.\""
# #     )

# #     if "chat_history" not in st.session_state:

# #         st.session_state[
# #             "chat_history"
# #         ] = []

# #     # ----------------------------------------
# #     # SHOW CHAT HISTORY
# #     # ----------------------------------------

# #     for message in st.session_state[
# #         "chat_history"
# #     ]:

# #         with st.chat_message(
# #             message["role"]
# #         ):

# #             st.markdown(
# #                 message["content"]
# #             )

# #     # ----------------------------------------
# #     # CHAT INPUT
# #     # ----------------------------------------

# #     user_message = st.chat_input(
# #         "Tell me what changed..."
# #     )

# #     if user_message:

# #         # Save user message

# #         st.session_state[
# #             "chat_history"
# #         ].append({

# #             "role": "user",

# #             "content": user_message

# #         })

# #         with st.chat_message("user"):

# #             st.markdown(
# #                 user_message
# #             )

# #         # ------------------------------------
# #         # RESCHEDULE
# #         # ------------------------------------

# #         with st.spinner(
# #             "🧠 Understanding your request "
# #             "and rescheduling..."
# #         ):

# #             new_plan = reschedule_plan(

# #                 st.session_state[
# #                     "subject_data"
# #                 ],

# #                 user_message,

# #                 st.session_state[
# #                     "start_time"
# #                 ]

# #             )

# #         # ------------------------------------
# #         # SAVE NEW PLAN
# #         # ------------------------------------

# #         st.session_state[
# #             "rescheduled_plan"
# #         ] = new_plan

# #         st.session_state[
# #             "chat_history"
# #         ].append({

# #             "role": "assistant",

# #             "content":
# #                 "✅ I've rescheduled your "
# #                 "plan using your priority "
# #                 "scores. Your updated plan "
# #                 "is shown below."

# #         })

# #         st.rerun()


# # # ============================================
# # # RESCHEDULED PLAN
# # # ============================================

# # if "rescheduled_plan" in st.session_state:

# #     st.divider()

# #     st.header(
# #         "🔄 Your Rescheduled Plan"
# #     )

# #     st.markdown(
# #         st.session_state[
# #             "rescheduled_plan"
# #         ]
# #     )

















# import streamlit as st
# from datetime import time, date

# from agent import generate_study_plan
# from priority import calculate_priority
# from rescheduler import reschedule_plan
# from dashboard import show_dashboard
# from google_calendar import add_study_plan_to_calendar


# # ============================================================
# # PAGE CONFIG
# # ============================================================

# st.set_page_config(
#     page_title="AI Study Assistant",
#     page_icon="📚",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )


# # ============================================================
# # CUSTOM CSS
# # ============================================================

# st.markdown("""
# <style>

#     /* ---------- MAIN ---------- */

#     .block-container {
#         max-width: 1200px;
#         padding-top: 2rem;
#         padding-bottom: 4rem;
#     }

#     /* ---------- HERO ---------- */

#     .hero {
#         padding: 2.2rem 2.5rem;
#         border-radius: 24px;
#         background:
#             linear-gradient(
#                 135deg,
#                 rgba(91, 76, 255, 0.18),
#                 rgba(30, 30, 40, 0.85)
#             );
#         border: 1px solid rgba(255,255,255,0.08);
#         margin-bottom: 2rem;
#     }

#     .hero-title {
#         font-size: 3rem;
#         font-weight: 800;
#         margin-bottom: 0.3rem;
#     }

#     .hero-subtitle {
#         font-size: 1.15rem;
#         opacity: 0.75;
#     }

#     /* ---------- SECTION ---------- */

#     .section-title {
#         font-size: 1.8rem;
#         font-weight: 750;
#         margin-top: 1.5rem;
#         margin-bottom: 0.3rem;
#     }

#     .section-subtitle {
#         opacity: 0.65;
#         margin-bottom: 1.2rem;
#     }

#     /* ---------- FEATURE CARDS ---------- */

#     .feature-card {
#         padding: 1.2rem;
#         border-radius: 18px;
#         border: 1px solid rgba(255,255,255,0.08);
#         background: rgba(255,255,255,0.035);
#         min-height: 120px;
#     }

#     .feature-icon {
#         font-size: 1.8rem;
#     }

#     .feature-title {
#         font-weight: 700;
#         margin-top: 0.4rem;
#     }

#     .feature-text {
#         opacity: 0.65;
#         font-size: 0.9rem;
#     }

#     /* ---------- PRIORITY CARDS ---------- */

#     .priority-card {
#         padding: 1.2rem;
#         border-radius: 18px;
#         border: 1px solid rgba(255,255,255,0.08);
#         background: rgba(255,255,255,0.035);
#     }

#     .priority-subject {
#         font-size: 1.15rem;
#         font-weight: 750;
#     }

#     .priority-score {
#         font-size: 1.8rem;
#         font-weight: 800;
#     }

#     .priority-label {
#         font-size: 0.85rem;
#         opacity: 0.7;
#     }

#     /* ---------- INFO BAR ---------- */

#     .info-bar {
#         padding: 1rem 1.2rem;
#         border-radius: 14px;
#         background: rgba(255,255,255,0.04);
#         border: 1px solid rgba(255,255,255,0.07);
#         margin: 1rem 0;
#     }

#     /* ---------- FOOTER ---------- */

#     .footer {
#         text-align: center;
#         opacity: 0.45;
#         padding-top: 3rem;
#         font-size: 0.85rem;
#     }

# </style>
# """, unsafe_allow_html=True)


# # ============================================================
# # SESSION STATE
# # ============================================================

# if "chat_history" not in st.session_state:
#     st.session_state["chat_history"] = []


# # ============================================================
# # HERO
# # ============================================================

# st.markdown("""
# <div class="hero">

#     <div class="hero-title">
#         📚 AI Study Assistant
#     </div>

#     <div class="hero-subtitle">
#         Your personal AI-powered adaptive study planner
#     </div>

# </div>
# """, unsafe_allow_html=True)


# # ============================================================
# # FEATURES
# # ============================================================

# feature_cols = st.columns(4)

# features = [
#     (
#         "🤖",
#         "AI Planning",
#         "Personalized study schedules"
#     ),
#     (
#         "🎯",
#         "Smart Priority",
#         "Exam + difficulty + progress"
#     ),
#     (
#         "🔄",
#         "Adaptive",
#         "Automatically reschedule plans"
#     ),
#     (
#         "📅",
#         "Calendar",
#         "Add your plan to Google Calendar"
#     )
# ]


# for col, feature in zip(
#     feature_cols,
#     features
# ):

#     icon, title, description = feature

#     with col:

#         st.markdown(
#             f"""
#             <div class="feature-card">

#                 <div class="feature-icon">
#                     {icon}
#                 </div>

#                 <div class="feature-title">
#                     {title}
#                 </div>

#                 <div class="feature-text">
#                     {description}
#                 </div>

#             </div>
#             """,
#             unsafe_allow_html=True
#         )


# st.write("")


# # ============================================================
# # SIDEBAR
# # ============================================================

# with st.sidebar:

#     st.markdown(
#         "## 📚 AI Study Assistant"
#     )

#     st.caption(
#         "Adaptive learning companion"
#     )

#     st.divider()

#     st.markdown("### How it works")

#     st.markdown(
#         """
#         **1. Add your subjects**

#         **2. Set exam dates**

#         **3. Set difficulty**

#         **4. Set syllabus progress**

#         **5. Choose your study time**

#         **6. Let AI build your plan**

#         **7. Reschedule naturally when plans change**
#         """
#     )

#     st.divider()

#     st.markdown("### 🧠 Priority Formula")

#     st.caption(
#         "Exam urgency — 40%"
#     )

#     st.caption(
#         "Difficulty — 30%"
#     )

#     st.caption(
#         "Remaining syllabus — 30%"
#     )

#     st.divider()

#     st.caption(
#         "Built with Streamlit + Hugging Face"
#     )


# # ============================================================
# # MAIN TABS
# # ============================================================

# tab_setup, tab_plan, tab_priority, tab_ai = st.tabs(
#     [
#         "⚙️ Setup",
#         "📅 Study Plan",
#         "🎯 Priority",
#         "🤖 AI Assistant"
#     ]
# )


# # ============================================================
# # TAB 1 — SETUP
# # ============================================================

# with tab_setup:

#     st.markdown(
#         '<div class="section-title">👨‍🎓 Student Setup</div>',
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         '<div class="section-subtitle">'
#         'Tell the AI about your subjects and availability.'
#         '</div>',
#         unsafe_allow_html=True
#     )

#     col1, col2 = st.columns(
#         [1, 2]
#     )

#     with col1:

#         name = st.text_input(
#             "Your Name",
#             placeholder="e.g. Tanmay",
#             key="student_name"
#         )

#     with col2:

#         subjects_input = st.text_input(
#             "Subjects",
#             placeholder="DSA, Java, Maths",
#             key="subjects_input"
#         )


#     # --------------------------------------------------------
#     # SUBJECT DATA
#     # --------------------------------------------------------

#     subject_names = [
#         subject.strip()
#         for subject in subjects_input.split(",")
#         if subject.strip()
#     ]


#     if subject_names:

#         st.markdown(
#             '<div class="section-title">'
#             '📚 Subject Priorities'
#             '</div>',
#             unsafe_allow_html=True
#         )

#         st.caption(
#             "Priority is automatically calculated from "
#             "exam urgency, difficulty and remaining syllabus."
#         )


#         subject_data = []


#         for subject in subject_names:

#             with st.container(
#                 border=True
#             ):

#                 st.markdown(
#                     f"### 📖 {subject}"
#                 )

#                 c1, c2, c3 = st.columns(3)

#                 with c1:

#                     exam_date = st.date_input(
#                         "Exam Date",
#                         value=date.today(),
#                         key=f"exam_{subject}"
#                     )

#                 with c2:

#                     difficulty = st.selectbox(
#                         "Difficulty",
#                         [
#                             "Easy",
#                             "Medium",
#                             "Hard"
#                         ],
#                         index=1,
#                         key=f"difficulty_{subject}"
#                     )

#                 with c3:

#                     progress = st.slider(
#                         "Syllabus Completed",
#                         0,
#                         100,
#                         50,
#                         5,
#                         key=f"progress_{subject}"
#                     )


#                 priority_info = calculate_priority(
#                     exam_date,
#                     difficulty,
#                     progress
#                 )


#                 subject_data.append({

#                     "subject": subject,

#                     "exam_date": exam_date,

#                     "difficulty": difficulty,

#                     "progress": progress,

#                     "score":
#                         priority_info["score"],

#                     "priority":
#                         priority_info["priority"],

#                     "exam_score":
#                         priority_info["exam_score"],

#                     "difficulty_score":
#                         priority_info["difficulty_score"],

#                     "remaining_score":
#                         priority_info["remaining_score"]

#                 })


#                 st.markdown(
#                     f"""
#                     <div class="info-bar">

#                         🎯 Priority Score:
#                         <b>
#                             {priority_info['score']} / 100
#                         </b>

#                         &nbsp;&nbsp;|&nbsp;&nbsp;

#                         Priority:
#                         <b>
#                             {priority_info['priority']}
#                         </b>

#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )


#     # ========================================================
#     # STUDY WINDOW
#     # ========================================================

#     st.markdown(
#         '<div class="section-title">'
#         '⏰ Your Study Window'
#         '</div>',
#         unsafe_allow_html=True
#     )

#     st.caption(
#         "Choose exactly when you are available today."
#     )


#     c1, c2 = st.columns(2)

#     with c1:

#         start_time = st.time_input(
#             "Start Time",
#             value=time(18, 0),
#             key="start_time_input"
#         )

#     with c2:

#         end_time = st.time_input(
#             "End Time",
#             value=time(23, 0),
#             key="end_time_input"
#         )


#     start_minutes = (
#         start_time.hour * 60
#         + start_time.minute
#     )

#     end_minutes = (
#         end_time.hour * 60
#         + end_time.minute
#     )


#     if end_minutes > start_minutes:

#         available_minutes = (
#             end_minutes
#             - start_minutes
#         )

#         available_hours = (
#             available_minutes / 60
#         )

#         st.success(
#             f"⏱️ You have **{available_hours:.1f} hours** "
#             f"available for studying."
#         )

#     else:

#         available_minutes = 0

#         st.error(
#             "End time must be after start time."
#         )


#     st.write("")


#     # ========================================================
#     # GENERATE BUTTON
#     # ========================================================

#     generate = st.button(
#         "✨ Generate My Study Plan",
#         type="primary",
#         use_container_width=True
#     )


#     if generate:

#         if not name:

#             st.warning(
#                 "👤 Please enter your name."
#             )

#         elif not subject_names:

#             st.warning(
#                 "📚 Please enter at least one subject."
#             )

#         elif available_minutes <= 0:

#             st.error(
#                 "⏰ Please select a valid study window."
#             )

#         else:

#             with st.spinner(
#                 "🧠 AI is building your personalized plan..."
#             ):

#                 plan = generate_study_plan(
#                     subject_data,
#                     start_time,
#                     end_time
#                 )


#             st.session_state[
#                 "study_plan"
#             ] = plan["markdown"]

#             st.session_state[
#                 "study_sessions"
#             ] = plan["sessions"]

#             st.session_state[
#                 "subject_data"
#             ] = subject_data

#             st.session_state[
#                 "name"
#             ] = name

#             st.session_state[
#                 "start_time"
#             ] = start_time

#             st.session_state[
#                 "end_time"
#             ] = end_time

#             st.session_state[
#                 "available_minutes"
#             ] = available_minutes

#             st.session_state[
#                 "rescheduled_plan"
#             ] = None

#             st.session_state[
#                 "chat_history"
#             ] = []

#             st.success(
#                 "🎉 Your personalized study plan is ready!"
#             )


# # ============================================================
# # TAB 2 — STUDY PLAN
# # ============================================================

# with tab_plan:

#     if "study_plan" not in st.session_state:

#         st.info(
#             "👋 Generate a study plan from the "
#             "**Setup** tab to see it here."
#         )

#     else:

#         st.markdown(
#             '<div class="section-title">'
#             f"📅 {st.session_state['name']}'s Study Plan"
#             '</div>',
#             unsafe_allow_html=True
#         )


#         hours = (
#             st.session_state[
#                 "available_minutes"
#             ] / 60
#         )


#         c1, c2 = st.columns(2)

#         with c1:

#             st.metric(
#                 "Available Study Time",
#                 f"{hours:.1f} hrs"
#             )

#         with c2:

#             st.metric(
#                 "Study Window",
#                 (
#                     st.session_state[
#                         "start_time"
#                     ].strftime("%I:%M %p")
#                     + " – "
#                     + st.session_state[
#                         "end_time"
#                     ].strftime("%I:%M %p")
#                 )
#             )


#         st.write("")


#         # ----------------------------------------------------
#         # PLAN
#         # ----------------------------------------------------

#         with st.container(
#             border=True
#         ):

#             st.markdown(
#                 st.session_state[
#                     "study_plan"
#                 ]
#             )


#         # ----------------------------------------------------
#         # GOOGLE CALENDAR
#         # ----------------------------------------------------

#         st.write("")

#         st.markdown(
#             '<div class="section-title">'
#             '📅 Google Calendar'
#             '</div>',
#             unsafe_allow_html=True
#         )

#         st.caption(
#             "Turn your AI-generated schedule into real calendar events."
#         )


#         calendar_date = st.date_input(
#             "Calendar Date",
#             value=date.today(),
#             key="calendar_date"
#         )


#         if st.button(
#             "📅 Add Study Plan to Google Calendar",
#             type="primary",
#             use_container_width=True
#         ):

#             try:

#                 events = add_study_plan_to_calendar(

#                     st.session_state[
#                         "study_sessions"
#                     ],

#                     calendar_date,

#                     st.session_state[
#                         "start_time"
#                     ]

#                 )

#                 st.success(
#                     f"✅ Added {len(events)} "
#                     "study sessions to Google Calendar!"
#                 )

#             except Exception as e:

#                 st.error(
#                     f"❌ Google Calendar error: {e}"
#                 )


# # ============================================================
# # TAB 3 — PRIORITY
# # ============================================================

# with tab_priority:

#     if "subject_data" not in st.session_state:

#         st.info(
#             "Generate a study plan first."
#         )

#     else:

#         st.markdown(
#             '<div class="section-title">'
#             '🎯 Smart Priority Analysis'
#             '</div>',
#             unsafe_allow_html=True
#         )

#         st.markdown(
#             """
#             Your priority score is calculated using:

#             **40% Exam Urgency + 30% Difficulty + 
#             30% Remaining Syllabus**
#             """
#         )


#         st.write("")


#         sorted_subjects = sorted(
#             st.session_state[
#                 "subject_data"
#             ],
#             key=lambda x: x["score"],
#             reverse=True
#         )


#         # ----------------------------------------------------
#         # PRIORITY CARDS
#         # ----------------------------------------------------

#         cols = st.columns(
#             min(
#                 len(sorted_subjects),
#                 3
#             )
#         )


#         for index, item in enumerate(
#             sorted_subjects
#         ):

#             with cols[
#                 index % len(cols)
#             ]:

#                 st.markdown(
#                     f"""
#                     <div class="priority-card">

#                         <div class="priority-subject">
#                             📚 {item['subject']}
#                         </div>

#                         <div class="priority-score">
#                             {item['score']}/100
#                         </div>

#                         <div class="priority-label">
#                             {item['priority']} PRIORITY
#                         </div>

#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )


#         st.write("")


#         # ----------------------------------------------------
#         # DETAILED BREAKDOWN
#         # ----------------------------------------------------

#         for item in sorted_subjects:

#             with st.expander(
#                 f"📖 {item['subject']} — "
#                 f"{item['priority']} — "
#                 f"{item['score']}/100"
#             ):

#                 c1, c2 = st.columns(2)

#                 with c1:

#                     st.write(
#                         f"📅 **Exam:** "
#                         f"{item['exam_date']}"
#                     )

#                     st.write(
#                         f"🎯 **Difficulty:** "
#                         f"{item['difficulty']}"
#                     )

#                     st.write(
#                         f"📊 **Completed:** "
#                         f"{item['progress']}%"
#                     )

#                 with c2:

#                     st.write(
#                         f"📅 **Exam Urgency:** "
#                         f"{item['exam_score']}"
#                     )

#                     st.write(
#                         f"🎯 **Difficulty Score:** "
#                         f"{item['difficulty_score']}"
#                     )

#                     st.write(
#                         f"📚 **Remaining Syllabus:** "
#                         f"{item['remaining_score']}"
#                     )


#         st.info(
#             "💡 Higher priority means the AI is more "
#             "likely to allocate study time to that subject."
#         )


# # ============================================================
# # TAB 4 — AI ASSISTANT
# # ============================================================

# with tab_ai:

#     if "study_plan" not in st.session_state:

#         st.info(
#             "Generate a study plan first, then "
#             "you can ask the AI to adapt it."
#         )

#     else:

#         st.markdown(
#             '<div class="section-title">'
#             '🤖 AI Rescheduling Assistant'
#             '</div>',
#             unsafe_allow_html=True
#         )

#         st.markdown(
#             '<div class="section-subtitle">'
#             'Something changed? Just tell the AI naturally.'
#             '</div>',
#             unsafe_allow_html=True
#         )


#         # ----------------------------------------------------
#         # EXAMPLES
#         # ----------------------------------------------------

#         with st.container(
#             border=True
#         ):

#             st.markdown(
#                 "### 💬 Try saying..."
#             )

#             st.markdown(
#                 """
#                 • *I only have 2 hours today.*

#                 • *I have my DSA exam tomorrow and only 
#                 3 hours to study.*

#                 • *My DSA paper is the next morning and 
#                 I've got 2 hours.*

#                 • *I have a DSA test in 2 days and 
#                 4 hours available.*
#                 """
#             )


#         st.write("")


#         # ----------------------------------------------------
#         # CHAT HISTORY
#         # ----------------------------------------------------

#         for message in st.session_state[
#             "chat_history"
#         ]:

#             with st.chat_message(
#                 message["role"]
#             ):

#                 st.markdown(
#                     message["content"]
#                 )


#         # ----------------------------------------------------
#         # CHAT INPUT
#         # ----------------------------------------------------

#         user_message = st.chat_input(
#             "Tell me what changed..."
#         )


#         if user_message:

#             st.session_state[
#                 "chat_history"
#             ].append({

#                 "role": "user",

#                 "content": user_message

#             })


#             with st.chat_message(
#                 "user"
#             ):

#                 st.markdown(
#                     user_message
#                 )


#             with st.chat_message(
#                 "assistant"
#             ):

#                 with st.spinner(
#                     "🧠 Adapting your plan..."
#                 ):

#                     new_plan = reschedule_plan(

#                         st.session_state[
#                             "subject_data"
#                         ],

#                         user_message,

#                         st.session_state[
#                             "start_time"
#                         ]

#                     )


#                 st.markdown(
#                     "✅ I've adapted your study plan."
#                 )


#             st.session_state[
#                 "rescheduled_plan"
#             ] = new_plan


#             st.session_state[
#                 "chat_history"
#             ].append({

#                 "role": "assistant",

#                 "content":
#                     "✅ I've adapted your study plan."

#             })


#             st.rerun()


#         # ----------------------------------------------------
#         # RESCHEDULED PLAN
#         # ----------------------------------------------------

#         if (
#             st.session_state.get(
#                 "rescheduled_plan"
#             )
#         ):

#             st.divider()

#             st.markdown(
#                 '<div class="section-title">'
#                 '🔄 Your Updated Plan'
#                 '</div>',
#                 unsafe_allow_html=True
#             )


#             with st.container(
#                 border=True
#             ):

#                 st.markdown(
#                     st.session_state[
#                         "rescheduled_plan"
#                     ]
#                 )


#             st.success(
#                 "Your original plan remains available "
#                 "in the Study Plan tab."
#             )


# # ============================================================
# # FOOTER
# # ============================================================

# st.markdown(
#     """
#     <div class="footer">
#         📚 AI Study Assistant &nbsp;•&nbsp;
#         Built with Streamlit + Hugging Face &nbsp;•&nbsp;
#         Adaptive AI Study Planning
#     </div>
#     """,
#     unsafe_allow_html=True
# )














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
# SIMPLE CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1 {
        font-weight: 800;
    }

    h2, h3 {
        font-weight: 700;
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
    "Your personal AI-powered adaptive study planner"
)

st.write(
    "Plan smarter, adapt instantly, and stay on track with AI."
)


# ============================================================
# FEATURE OVERVIEW
# ============================================================

st.subheader("✨ What your assistant can do")

feature1, feature2, feature3, feature4 = st.columns(4)

with feature1:
    st.metric(
        "🤖 AI Planning",
        "Personalized"
    )
    st.caption(
        "Creates study plans based on your subjects and time."
    )

with feature2:
    st.metric(
        "🎯 Smart Priority",
        "AI-ranked"
    )
    st.caption(
        "Uses exams, difficulty and syllabus progress."
    )

with feature3:
    st.metric(
        "🔄 Adaptive",
        "Rescheduling"
    )
    st.caption(
        "Adjusts your plan when your availability changes."
    )

with feature4:
    st.metric(
        "📅 Calendar",
        "Google"
    )
    st.caption(
        "Adds your study sessions directly to Calendar."
    )


st.divider()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("📚 AI Study Assistant")

    st.caption(
        "Adaptive learning companion"
    )

    st.divider()

    st.subheader("How it works")

    st.markdown(
        """
        **1. Add your subjects**

        **2. Set exam dates**

        **3. Choose difficulty**

        **4. Add syllabus progress**

        **5. Choose your study window**

        **6. Generate your plan**

        **7. Reschedule naturally when needed**
        """
    )

    st.divider()

    st.subheader("🧠 Priority Formula")

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

    st.write(
        "Enter your subjects, exam information and available study time."
    )


    # --------------------------------------------------------
    # STUDENT INFORMATION
    # --------------------------------------------------------

    col1, col2 = st.columns(
        [1, 2]
    )

    with col1:

        name = st.text_input(
            "Your Name",
            placeholder="e.g. Tanmay"
        )

    with col2:

        subjects_input = st.text_input(
            "Subjects",
            placeholder="DSA, Java, Maths"
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

        st.subheader(
            "📚 Subject Information"
        )

        st.caption(
            "Set the exam date, difficulty and syllabus progress "
            "for each subject."
        )


        subject_data = []


        for subject in subject_names:

            with st.container(
                border=True
            ):

                st.subheader(
                    f"📖 {subject}"
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
                # PRIORITY
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


                priority_col1, priority_col2 = st.columns(2)


                with priority_col1:

                    st.metric(
                        "Priority Score",
                        f"{priority_info['score']} / 100"
                    )


                with priority_col2:

                    st.metric(
                        "Priority",
                        priority_info["priority"]
                    )


    # --------------------------------------------------------
    # STUDY WINDOW
    # --------------------------------------------------------

    st.divider()

    st.header(
        "⏰ Choose Your Study Window"
    )

    st.write(
        "Select exactly when you are available today."
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

            f"⏱️ Available study time: "
            f"**{available_hours:.1f} hours**"

        )


    else:

        available_minutes = 0


        st.error(
            "⚠️ End time must be after start time."
        )


    # --------------------------------------------------------
    # GENERATE BUTTON
    # --------------------------------------------------------

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
            # CLEAR OLD DATA
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
        # SUMMARY METRICS
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

        st.header(
            "📅 Google Calendar"
        )

        st.caption(
            "Turn your AI-generated study plan into real calendar events."
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
                    f"study sessions to Google Calendar!"

                )


            except Exception as e:

                st.error(
                    f"❌ Google Calendar error: {e}"
                )


        st.info(
            "💡 Your AI plan uses exam urgency, "
            "difficulty and remaining syllabus to "
            "decide what deserves more study time."
        )


# ============================================================
# PRIORITY TAB
# ============================================================

with priority_tab:

    if not st.session_state["subject_data"]:

        st.info(
            "Generate a study plan first to see "
            "your priority analysis."
        )

    else:

        st.header(
            "🎯 Smart Priority Analysis"
        )


        st.write(
            "The assistant calculates subject priority using:"
        )


        formula_col1, formula_col2, formula_col3 = st.columns(3)


        with formula_col1:

            st.metric(
                "📅 Exam Urgency",
                "40%"
            )


        with formula_col2:

            st.metric(
                "🎯 Difficulty",
                "30%"
            )


        with formula_col3:

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
        # PRIORITY CARDS
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


        st.divider()


        # ----------------------------------------------------
        # DETAILED ANALYSIS
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
            "💡 Higher priority subjects receive "
            "more attention when study time is limited."
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


        st.write(
            "Something changed? Tell the AI naturally "
            "and it will adapt your study plan."
        )


        # ----------------------------------------------------
        # EXAMPLES
        # ----------------------------------------------------

        with st.container(
            border=True
        ):

            st.subheader(
                "💬 Try saying..."
            )

            st.write(
                "• I only have 2 hours today."
            )

            st.write(
                "• I have my DSA exam tomorrow "
                "and only 3 hours to study."
            )

            st.write(
                "• My DSA paper is the next morning "
                "and I've got 2 hours."
            )

            st.write(
                "• I have a DSA test in 2 days "
                "and 4 hours available."
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
            # USER MESSAGE
            # -----------------------------------------------

            st.session_state[
                "chat_history"
            ].append({

                "role": "user",

                "content": user_message

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
            # SAVE
            # -----------------------------------------------

            st.session_state[
                "rescheduled_plan"
            ] = new_plan


            st.session_state[
                "chat_history"
            ].append({

                "role": "assistant",

                "content":
                    "✅ I've adapted your study plan."

            })


            st.rerun()


        # ----------------------------------------------------
        # RESCHEDULED PLAN
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
# DASHBOARD
# ============================================================

if st.session_state["subject_data"]:

    st.divider()

    with st.expander(
        "📊 Open Detailed Dashboard",
        expanded=False
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
    "📚 AI Study Assistant • "
    "Built with Streamlit + Hugging Face • "
    "Adaptive AI Study Planning"
)