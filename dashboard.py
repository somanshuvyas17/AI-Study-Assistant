# # import streamlit as st


# # # ============================================
# # # STUDY DASHBOARD
# # # ============================================

# # def show_dashboard(subject_data):

# #     st.header("📊 Study Dashboard")

# #     if not subject_data:
# #         st.info("No subjects available yet.")
# #         return

# #     # ----------------------------------------
# #     # OVERALL PROGRESS
# #     # ----------------------------------------

# #     total_progress = sum(
# #         item["progress"]
# #         for item in subject_data
# #     )

# #     overall_progress = (
# #         total_progress / len(subject_data)
# #     )

# #     st.subheader("📈 Overall Progress")

# #     st.progress(
# #         overall_progress / 100
# #     )

# #     st.write(
# #         f"**{overall_progress:.1f}% completed**"
# #     )


# #     # ----------------------------------------
# #     # PRIORITY COUNTS
# #     # ----------------------------------------

# #     high = sum(
# #         1
# #         for item in subject_data
# #         if item["priority"] == "High"
# #     )

# #     medium = sum(
# #         1
# #         for item in subject_data
# #         if item["priority"] == "Medium"
# #     )

# #     low = sum(
# #         1
# #         for item in subject_data
# #         if item["priority"] == "Low"
# #     )


# #     col1, col2, col3 = st.columns(3)


# #     with col1:

# #         st.metric(
# #             "🔴 High Priority",
# #             high
# #         )


# #     with col2:

# #         st.metric(
# #             "🟡 Medium Priority",
# #             medium
# #         )


# #     with col3:

# #         st.metric(
# #             "🟢 Low Priority",
# #             low
# #         )


# #     st.divider()


# #     # ----------------------------------------
# #     # SUBJECT PROGRESS
# #     # ----------------------------------------

# #     st.subheader("📚 Subject Progress")


# #     for item in sorted(
# #         subject_data,
# #         key=lambda x: x["score"],
# #         reverse=True
# #     ):

# #         subject = item["subject"]

# #         progress = item["progress"]

# #         score = item["score"]

# #         priority = item["priority"]


# #         # Priority emoji

# #         if priority == "High":

# #             emoji = "🔴"

# #         elif priority == "Medium":

# #             emoji = "🟡"

# #         else:

# #             emoji = "🟢"


# #         st.markdown(
# #             f"### {subject}"
# #         )


# #         st.write(
# #             f"{emoji} **{priority} Priority** "
# #             f"— Score: **{score}/100**"
# #         )


# #         st.progress(
# #             progress / 100
# #         )


# #         st.write(
# #             f"📊 Completed: **{progress}%**"
# #         )


# #         st.divider()




# import streamlit as st

# from priority import calculate_priority


# # ============================================
# # STUDY DASHBOARD
# # ============================================

# def show_dashboard(subject_data):

#     st.header("📊 Study Dashboard")

#     if not subject_data:

#         st.info(
#             "No subjects available yet."
#         )

#         return


#     # ========================================
#     # OVERALL PROGRESS
#     # ========================================

#     total_progress = sum(
#         item["progress"]
#         for item in subject_data
#     )

#     overall_progress = (
#         total_progress / len(subject_data)
#     )


#     st.subheader(
#         "📈 Overall Progress"
#     )


#     st.progress(
#         overall_progress / 100
#     )


#     st.write(
#         f"**{overall_progress:.1f}% completed**"
#     )


#     # ========================================
#     # PRIORITY COUNTS
#     # ========================================

#     high = sum(
#         1
#         for item in subject_data
#         if item["priority"] == "High"
#     )


#     medium = sum(
#         1
#         for item in subject_data
#         if item["priority"] == "Medium"
#     )


#     low = sum(
#         1
#         for item in subject_data
#         if item["priority"] == "Low"
#     )


#     col1, col2, col3 = st.columns(3)


#     with col1:

#         st.metric(
#             "🔴 High Priority",
#             high
#         )


#     with col2:

#         st.metric(
#             "🟡 Medium Priority",
#             medium
#         )


#     with col3:

#         st.metric(
#             "🟢 Low Priority",
#             low
#         )


#     st.divider()


#     # ========================================
#     # SUBJECT PROGRESS
#     # ========================================

#     st.subheader(
#         "📚 Subject Progress"
#     )


#     for i, item in enumerate(subject_data):

#         subject = item["subject"]


#         if item["priority"] == "High":

#             emoji = "🔴"

#         elif item["priority"] == "Medium":

#             emoji = "🟡"

#         else:

#             emoji = "🟢"


#         with st.expander(
#             f"{emoji} {subject} "
#             f"— {item['priority']} "
#             f"({item['score']}/100)"
#         ):


#             # --------------------------------
#             # CURRENT PROGRESS
#             # --------------------------------

#             st.write(
#                 f"Current Progress: "
#                 f"**{item['progress']}%**"
#             )


#             st.progress(
#                 item["progress"] / 100
#             )


#             # --------------------------------
#             # UPDATE PROGRESS
#             # --------------------------------

#             new_progress = st.slider(

#                 f"Update {subject} progress",

#                 min_value=0,

#                 max_value=100,

#                 value=item["progress"],

#                 step=5,

#                 key=f"dashboard_progress_{i}"

#             )


#             # --------------------------------
#             # SAVE BUTTON
#             # --------------------------------

#             if st.button(
#                 f"💾 Save {subject} Progress",
#                 key=f"save_progress_{i}"
#             ):

#                 item["progress"] = (
#                     new_progress
#                 )
                


#                 st.success(
#                     f"{subject} progress "
#                     f"updated to "
#                     f"{new_progress}%!"
#                 )


#                 st.rerun()


#             st.write(
#                 f"📅 Exam Date: "
#                 f"{item['exam_date']}"
#             )


#             st.write(
#                 f"🎯 Difficulty: "
#                 f"{item['difficulty']}"
#             )


#             st.write(
#                 f"⏳ Remaining: "
#                 f"{100 - item['progress']}%"
#             )









import streamlit as st

from priority import calculate_priority


# ============================================
# STUDY DASHBOARD
# ============================================

def show_dashboard(subject_data):

    st.header("📊 Study Dashboard")

    if not subject_data:
        st.info("No subjects available yet.")
        return

    # ========================================
    # OVERALL PROGRESS
    # ========================================

    total_progress = sum(
        item["progress"]
        for item in subject_data
    )

    overall_progress = (
        total_progress / len(subject_data)
    )

    st.subheader("📈 Overall Progress")

    st.progress(
        overall_progress / 100
    )

    st.write(
        f"**{overall_progress:.1f}% completed**"
    )

    # ========================================
    # PRIORITY COUNTS
    # ========================================

    high = sum(
        1
        for item in subject_data
        if item["priority"] == "High"
    )

    medium = sum(
        1
        for item in subject_data
        if item["priority"] == "Medium"
    )

    low = sum(
        1
        for item in subject_data
        if item["priority"] == "Low"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🔴 High Priority",
            high
        )

    with col2:
        st.metric(
            "🟡 Medium Priority",
            medium
        )

    with col3:
        st.metric(
            "🟢 Low Priority",
            low
        )

    st.divider()

    # ========================================
    # SUBJECT PROGRESS
    # ========================================

    st.subheader("📚 Subject Progress")

    for i, item in enumerate(subject_data):

        subject = item["subject"]

        # Priority emoji
        if item["priority"] == "High":
            emoji = "🔴"

        elif item["priority"] == "Medium":
            emoji = "🟡"

        else:
            emoji = "🟢"

        # Subject expandable section
        with st.expander(
            f"{emoji} {subject} — "
            f"{item['priority']} "
            f"({item['score']}/100)"
        ):

            # --------------------------------
            # CURRENT PROGRESS
            # --------------------------------

            st.write(
                f"Current Progress: "
                f"**{item['progress']}%**"
            )

            st.progress(
                item["progress"] / 100
            )

            # --------------------------------
            # UPDATE PROGRESS
            # --------------------------------

            new_progress = st.slider(
                f"Update {subject} progress",

                min_value=0,

                max_value=100,

                value=item["progress"],

                step=5,

                key=f"dashboard_progress_{i}"
            )

            # --------------------------------
            # SAVE PROGRESS
            # --------------------------------

            if st.button(
                f"💾 Save {subject} Progress",
                key=f"save_progress_{i}"
            ):

                # Update progress
                item["progress"] = new_progress

                # --------------------------------
                # RECALCULATE PRIORITY
                # --------------------------------

                priority_info = calculate_priority(

                    item["exam_date"],

                    item["difficulty"],

                    new_progress

                )

                # Update priority information
                item["score"] = (
                    priority_info["score"]
                )

                item["priority"] = (
                    priority_info["priority"]
                )

                item["exam_score"] = (
                    priority_info["exam_score"]
                )

                item["difficulty_score"] = (
                    priority_info["difficulty_score"]
                )

                item["remaining_score"] = (
                    priority_info["remaining_score"]
                )

                st.success(
                    f"✅ {subject} progress "
                    f"updated to "
                    f"{new_progress}%!"
                )

                st.rerun()

            # --------------------------------
            # SUBJECT DETAILS
            # --------------------------------

            st.write(
                f"📅 Exam Date: "
                f"**{item['exam_date']}**"
            )

            st.write(
                f"🎯 Difficulty: "
                f"**{item['difficulty']}**"
            )

            st.write(
                f"⏳ Remaining Syllabus: "
                f"**{100 - item['progress']}%**"
            )

            st.write(
                f"🎯 Priority Score: "
                f"**{item['score']}/100**"
            )

            st.write(
                f"📅 Exam Urgency Score: "
                f"**{item['exam_score']}**"
            )

            st.write(
                f"🎯 Difficulty Score: "
                f"**{item['difficulty_score']}**"
            )

            st.write(
                f"📚 Remaining Syllabus Score: "
                f"**{item['remaining_score']}**"
            )