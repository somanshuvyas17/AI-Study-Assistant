# # # # # # # import os
# # # # # # # from dotenv import load_dotenv
# # # # # # # from huggingface_hub import InferenceClient

# # # # # # # load_dotenv()

# # # # # # # client = InferenceClient(
# # # # # # #     api_key=os.getenv("HF_TOKEN"),
# # # # # # #     provider="auto"
# # # # # # # )


# # # # # # # def reschedule_plan(old_plan, new_hours, reason):

# # # # # # #     prompt = f"""
# # # # # # # You are an AI Study Assistant responsible for rescheduling study plans.

# # # # # # # Original study plan:

# # # # # # # {old_plan}

# # # # # # # The student now has only {new_hours} hours available.

# # # # # # # Reason:
# # # # # # # {reason}

# # # # # # # Create a new study plan that STRICTLY fits within {new_hours} hours.

# # # # # # # Rules:
# # # # # # # - Keep the highest-priority topics.
# # # # # # # - Prioritize urgent subjects.
# # # # # # # - Remove low-priority tasks first.
# # # # # # # - Do not exceed {new_hours} hours.
# # # # # # # - Include short breaks when appropriate.
# # # # # # # - Do not include unnecessary explanations.

# # # # # # # Use this format:

# # # # # # # 🔄 RESCHEDULED STUDY PLAN

# # # # # # # | Time | Subject | Topic | Duration | Priority |
# # # # # # # |------|---------|-------|----------|----------|

# # # # # # # Then write:

# # # # # # # Original available time: Calculate from the original plan
# # # # # # # New available time: {new_hours} hours
# # # # # # # """

# # # # # # #     response = client.chat.completions.create(
# # # # # # #         model="openai/gpt-oss-120b",
# # # # # # #         messages=[
# # # # # # #             {
# # # # # # #                 "role": "user",
# # # # # # #                 "content": prompt
# # # # # # #             }
# # # # # # #         ],
# # # # # # #         max_tokens=1000
# # # # # # #     )

# # # # # # #     return response.choices[0].message.content




# # # # # # import os
# # # # # # from dotenv import load_dotenv
# # # # # # from huggingface_hub import InferenceClient

# # # # # # load_dotenv()

# # # # # # client = InferenceClient(
# # # # # #     api_key=os.getenv("HF_TOKEN"),
# # # # # #     provider="auto"
# # # # # # )


# # # # # # def reschedule_plan(old_plan, new_hours, reason):

# # # # # #     prompt = f"""
# # # # # # You are an AI Study Assistant.

# # # # # # The student already has this study plan:

# # # # # # {old_plan}

# # # # # # The student now has only {new_hours} hours available.

# # # # # # Reason:
# # # # # # {reason}

# # # # # # Create a NEW study plan.

# # # # # # Rules:
# # # # # # 1. STRICTLY stay within {new_hours} hours.
# # # # # # 2. Keep the highest-priority topics.
# # # # # # 3. Prioritize urgent subjects.
# # # # # # 4. Remove low-priority topics first.
# # # # # # 5. Include short breaks if appropriate.
# # # # # # 6. Do not add unnecessary explanations.

# # # # # # Use this format:

# # # # # # ## 🔄 RESCHEDULED STUDY PLAN

# # # # # # | Time | Subject | Topic | Duration | Priority |
# # # # # # |------|---------|-------|----------|----------|

# # # # # # After the table, write:

# # # # # # **Original plan:** Previous schedule
# # # # # # **New available time:** {new_hours} hours
# # # # # # **Reason:** {reason}
# # # # # # """

# # # # # #     response = client.chat.completions.create(
# # # # # #         model="openai/gpt-oss-120b",
# # # # # #         messages=[
# # # # # #             {
# # # # # #                 "role": "user",
# # # # # #                 "content": prompt
# # # # # #             }
# # # # # #         ],
# # # # # #         max_tokens=1000
# # # # # #     )

# # # # # #     return response.choices[0].message.content



# # # # # import os
# # # # # from dotenv import load_dotenv
# # # # # from huggingface_hub import InferenceClient

# # # # # load_dotenv()

# # # # # client = InferenceClient(
# # # # #     api_key=os.getenv("HF_TOKEN"),
# # # # #     provider="auto"
# # # # # )


# # # # # def reschedule_plan(old_plan, user_message):

# # # # #     prompt = f"""
# # # # # You are an AI Study Assistant that dynamically reschedules study plans.

# # # # # The student's ORIGINAL study plan is:

# # # # # {old_plan}

# # # # # The student sent this message:

# # # # # "{user_message}"

# # # # # Your job is to understand what changed and create a new study plan.

# # # # # Rules:
# # # # # - Identify the student's new available time from their message.
# # # # # - If they say they only have 2 hours, the new plan MUST NOT exceed 2 hours.
# # # # # - Prioritize urgent and difficult subjects.
# # # # # - Keep important unfinished topics.
# # # # # - Remove low-priority topics first.
# # # # # - Include short breaks when appropriate.
# # # # # - Do not exceed the student's newly available time.
# # # # # - Do not invent extra available time.
# # # # # - Keep the response concise.

# # # # # Use this format:

# # # # # ## 🔄 RESCHEDULED STUDY PLAN

# # # # # | Time | Subject | Topic | Duration | Priority |
# # # # # |------|---------|-------|----------|----------|

# # # # # Then include:

# # # # # **Why it was rescheduled:** 
# # # # # Briefly explain the adjustment.

# # # # # **New available time:**
# # # # # State the amount of time detected from the student's message.
# # # # # """

# # # # #     response = client.chat.completions.create(
# # # # #         model="openai/gpt-oss-120b",
# # # # #         messages=[
# # # # #             {
# # # # #                 "role": "user",
# # # # #                 "content": prompt
# # # # #             }
# # # # #         ],
# # # # #         max_tokens=1000
# # # # #     )

# # # # #     return response.choices[0].message.content






# # # # import os
# # # # from dotenv import load_dotenv
# # # # from huggingface_hub import InferenceClient

# # # # load_dotenv()

# # # # client = InferenceClient(
# # # #     api_key=os.getenv("HF_TOKEN"),
# # # #     provider="auto"
# # # # )


# # # # # ----------------------------------------
# # # # # FORMAT TIME
# # # # # ----------------------------------------

# # # # def format_time(minutes):

# # # #     hour = (minutes // 60) % 24
# # # #     minute = minutes % 60

# # # #     period = "AM" if hour < 12 else "PM"

# # # #     display_hour = hour % 12

# # # #     if display_hour == 0:
# # # #         display_hour = 12

# # # #     return f"{display_hour}:{minute:02d} {period}"


# # # # # ----------------------------------------
# # # # # RESCHEDULE
# # # # # ----------------------------------------

# # # # def reschedule_plan(
# # # #     old_plan,
# # # #     user_message,
# # # #     original_start,
# # # #     original_end
# # # # ):

# # # #     # ----------------------------------------
# # # #     # ASK AI TO UNDERSTAND USER REQUEST
# # # #     # ----------------------------------------

# # # #     prompt = f"""
# # # # You are an AI Study Assistant.

# # # # The student has this original study plan:

# # # # {old_plan}

# # # # The student's message is:

# # # # "{user_message}"

# # # # Understand what changed.

# # # # Determine:
# # # # 1. How many hours the student has available now.
# # # # 2. Which topics should receive the highest priority.
# # # # 3. Which topics can be reduced or removed.

# # # # Return ONLY:

# # # # AVAILABLE_HOURS | number

# # # # Example:

# # # # AVAILABLE_HOURS | 2
# # # # """

# # # #     response = client.chat.completions.create(

# # # #         model="openai/gpt-oss-120b",

# # # #         messages=[
# # # #             {
# # # #                 "role": "user",
# # # #                 "content": prompt
# # # #             }
# # # #         ],

# # # #         max_tokens=300,

# # # #         extra_body={
# # # #             "reasoning_effort": "low"
# # # #         }
# # # #     )


# # # #     text = response.choices[0].message.content


# # # #     # ----------------------------------------
# # # #     # FIND NEW HOURS
# # # #     # ----------------------------------------

# # # #     new_hours = None


# # # #     if text:

# # # #         for line in text.split("\n"):

# # # #             if "AVAILABLE_HOURS" in line:

# # # #                 try:

# # # #                     new_hours = float(
# # # #                         line.split("|")[1].strip()
# # # #                     )

# # # #                 except:

# # # #                     new_hours = None


# # # #     # ----------------------------------------
# # # #     # FALLBACK
# # # #     # ----------------------------------------

# # # #     if not new_hours:

# # # #         import re

# # # #         numbers = re.findall(
# # # #             r"\d+(?:\.\d+)?",
# # # #             user_message
# # # #         )

# # # #         if numbers:

# # # #             new_hours = float(
# # # #                 numbers[0]
# # # #             )


# # # #     if not new_hours:

# # # #         return (
# # # #             "⚠️ I couldn't determine your "
# # # #             "new available time. "
# # # #             "Please tell me something like: "
# # # #             "\"I only have 2 hours today.\""
# # # #         )


# # # #     # ----------------------------------------
# # # #     # CONVERT TO MINUTES
# # # #     # ----------------------------------------

# # # #     new_minutes = int(
# # # #         new_hours * 60
# # # #     )


# # # #     # ----------------------------------------
# # # #     # ORIGINAL START TIME
# # # #     # ----------------------------------------

# # # #     start_minutes = (
# # # #         original_start.hour * 60
# # # #         + original_start.minute
# # # #     )


# # # #     # ----------------------------------------
# # # #     # GET NEW TOPICS
# # # #     # ----------------------------------------

# # # #     topic_prompt = f"""
# # # # You are an AI Study Assistant.

# # # # Original study plan:

# # # # {old_plan}

# # # # The student now has only {new_hours} hours.

# # # # Student message:

# # # # "{user_message}"

# # # # Choose the most important topics from the original plan.

# # # # Prioritize:
# # # # 1. High priority topics
# # # # 2. Difficult topics
# # # # 3. Urgent topics
# # # # 4. Topics that should not be skipped

# # # # Return ONLY:

# # # # Subject | Topic | Priority
# # # # """

# # # #     topic_response = client.chat.completions.create(

# # # #         model="openai/gpt-oss-120b",

# # # #         messages=[
# # # #             {
# # # #                 "role": "user",
# # # #                 "content": topic_prompt
# # # #             }
# # # #         ],

# # # #         max_tokens=500,

# # # #         extra_body={
# # # #             "reasoning_effort": "low"
# # # #         }
# # # #     )


# # # #     topic_text = (
# # # #         topic_response
# # # #         .choices[0]
# # # #         .message
# # # #         .content
# # # #     )


# # # #     topics = []


# # # #     if topic_text:

# # # #         for line in topic_text.split("\n"):

# # # #             if "|" in line:

# # # #                 parts = [
# # # #                     x.strip()
# # # #                     for x in line.split("|")
# # # #                 ]

# # # #                 if len(parts) >= 3:

# # # #                     topics.append({

# # # #                         "subject": parts[0],

# # # #                         "topic": parts[1],

# # # #                         "priority": parts[2]

# # # #                     })


# # # #     # ----------------------------------------
# # # #     # FALLBACK
# # # #     # ----------------------------------------

# # # #     if not topics:

# # # #         topics = [{

# # # #             "subject": "Important Topics",

# # # #             "topic": "Revision",

# # # #             "priority": "High"

# # # #         }]


# # # #     topics = topics[:4]


# # # #     # ----------------------------------------
# # # #     # EXACT TIME ALLOCATION
# # # #     # ----------------------------------------

# # # #     number_of_topics = len(topics)

# # # #     base_time = (
# # # #         new_minutes // number_of_topics
# # # #     )

# # # #     remainder = (
# # # #         new_minutes % number_of_topics
# # # #     )


# # # #     for i in range(number_of_topics):

# # # #         topics[i]["duration"] = base_time

# # # #         if i < remainder:

# # # #             topics[i]["duration"] += 1


# # # #     # ----------------------------------------
# # # #     # BUILD NEW SCHEDULE
# # # #     # ----------------------------------------

# # # #     current_minutes = start_minutes

# # # #     plan = []


# # # #     for item in topics:

# # # #         duration = item["duration"]

# # # #         session_start = current_minutes

# # # #         session_end = (
# # # #             current_minutes + duration
# # # #         )


# # # #         plan.append({

# # # #             "start": format_time(
# # # #                 session_start
# # # #             ),

# # # #             "end": format_time(
# # # #                 session_end
# # # #             ),

# # # #             "subject": item["subject"],

# # # #             "topic": item["topic"],

# # # #             "duration": duration,

# # # #             "priority": item["priority"]

# # # #         })


# # # #         current_minutes = session_end


# # # #     # ----------------------------------------
# # # #     # OUTPUT
# # # #     # ----------------------------------------

# # # #     output = "## 🔄 RESCHEDULED STUDY PLAN\n\n"


# # # #     output += (
# # # #         "| Time | Subject | Topic | Duration | Priority |\n"
# # # #     )

# # # #     output += (
# # # #         "|------|---------|-------|----------|----------|\n"
# # # #     )


# # # #     for item in plan:

# # # #         output += (

# # # #             f"| {item['start']} - {item['end']} "

# # # #             f"| {item['subject']} "

# # # #             f"| {item['topic']} "

# # # #             f"| {item['duration']} min "

# # # #             f"| {item['priority']} |\n"

# # # #         )


# # # #     actual_total = sum(

# # # #         item["duration"]

# # # #         for item in plan

# # # #     )


# # # #     output += (
# # # #         f"\n**⏱️ New Study Time: "
# # # #         f"{actual_total // 60} hours "
# # # #         f"{actual_total % 60} minutes**"
# # # #     )


# # # #     output += (
# # # #         f"\n\n**🔄 Reason:** {user_message}"
# # # #     )


# # # #     return output







# # # import re

# # # from agent import format_time


# # # # ============================================
# # # # EXTRACT NEW TIME
# # # # ============================================

# # # def extract_minutes(message):

# # #     message = message.lower()


# # #     # Example:
# # #     # "I only have 1.5 hours"

# # #     hour_match = re.search(
# # #         r"(\d+(?:\.\d+)?)\s*(?:hours?|hrs?|hr)",
# # #         message
# # #     )


# # #     if hour_match:

# # #         hours = float(
# # #             hour_match.group(1)
# # #         )

# # #         return int(hours * 60)


# # #     # Example:
# # #     # "I only have 90 minutes"

# # #     minute_match = re.search(
# # #         r"(\d+)\s*(?:minutes?|mins?|min)",
# # #         message
# # #     )


# # #     if minute_match:

# # #         return int(
# # #             minute_match.group(1)
# # #         )


# # #     return None


# # # # ============================================
# # # # RESCHEDULE PLAN
# # # # ============================================

# # # def reschedule_plan(
# # #     subject_data,
# # #     user_message,
# # #     original_start
# # # ):

# # #     # ----------------------------------------
# # #     # GET NEW AVAILABLE TIME
# # #     # ----------------------------------------

# # #     new_minutes = extract_minutes(
# # #         user_message
# # #     )


# # #     if not new_minutes:

# # #         return (
# # #             "⚠️ I couldn't determine "
# # #             "your new available time.\n\n"
# # #             "Try something like:\n"
# # #             "\"I only have 2 hours today.\""
# # #         )


# # #     # ----------------------------------------
# # #     # SORT BY PRIORITY
# # #     # ----------------------------------------

# # #     subject_data = sorted(
# # #         subject_data,
# # #         key=lambda x: x["score"],
# # #         reverse=True
# # #     )


# # #     number_of_subjects = len(
# # #         subject_data
# # #     )


# # #     # ----------------------------------------
# # #     # MINIMUM TIME
# # #     # ----------------------------------------

# # #     minimum_time = 10


# # #     if new_minutes >= (
# # #         number_of_subjects
# # #         * minimum_time
# # #     ):

# # #         for item in subject_data:

# # #             item["duration"] = minimum_time


# # #         remaining = (
# # #             new_minutes
# # #             -
# # #             (
# # #                 number_of_subjects
# # #                 * minimum_time
# # #             )
# # #         )


# # #     else:

# # #         remaining = new_minutes

# # #         for item in subject_data:

# # #             item["duration"] = 0


# # #     # ----------------------------------------
# # #     # PRIORITY-BASED DISTRIBUTION
# # #     # ----------------------------------------

# # #     total_score = sum(
# # #         item["score"]
# # #         for item in subject_data
# # #     )


# # #     for item in subject_data:

# # #         share = (
# # #             item["score"]
# # #             / total_score
# # #         )


# # #         extra = int(
# # #             remaining * share
# # #         )


# # #         item["duration"] += extra


# # #     # ----------------------------------------
# # #     # FIX ROUNDING
# # #     # ----------------------------------------

# # #     allocated = sum(
# # #         item["duration"]
# # #         for item in subject_data
# # #     )


# # #     difference = (
# # #         new_minutes - allocated
# # #     )


# # #     subject_data[0]["duration"] += (
# # #         difference
# # #     )


# # #     # ----------------------------------------
# # #     # CREATE NEW SCHEDULE
# # #     # ----------------------------------------

# # #     current_minutes = (
# # #         original_start.hour * 60
# # #         + original_start.minute
# # #     )


# # #     plan = []


# # #     for item in subject_data:

# # #         if item["duration"] <= 0:

# # #             continue


# # #         session_start = current_minutes


# # #         session_end = (
# # #             current_minutes
# # #             + item["duration"]
# # #         )


# # #         plan.append({

# # #             "start": format_time(
# # #                 session_start
# # #             ),

# # #             "end": format_time(
# # #                 session_end
# # #             ),

# # #             "subject": item["subject"],

# # #             "topic": item["topic"],

# # #             "duration": item["duration"],

# # #             "priority": item["priority"]

# # #         })


# # #         current_minutes = session_end


# # #     # ----------------------------------------
# # #     # OUTPUT
# # #     # ----------------------------------------

# # #     output = (
# # #         "## 🔄 RESCHEDULED STUDY PLAN\n\n"
# # #     )


# # #     output += (
# # #         "| Time | Subject | Topic | "
# # #         "Duration | Priority |\n"
# # #     )


# # #     output += (
# # #         "|------|---------|-------|"
# # #         "----------|----------|\n"
# # #     )


# # #     for item in plan:

# # #         output += (

# # #             f"| {item['start']} - "
# # #             f"{item['end']} "

# # #             f"| {item['subject']} "

# # #             f"| {item['topic']} "

# # #             f"| {item['duration']} min "

# # #             f"| {item['priority']} |\n"

# # #         )


# # #     actual_total = sum(
# # #         item["duration"]
# # #         for item in plan
# # #     )


# # #     output += (
# # #         f"\n**⏱️ New Study Time: "
# # #         f"{actual_total // 60} hours "
# # #         f"{actual_total % 60} minutes**"
# # #     )


# # #     output += (
# # #         f"\n\n**🔄 Reason:** "
# # #         f"{user_message}"
# # #     )


# # #     return output







# # import re

# # from agent import format_time


# # # ============================================
# # # EXTRACT NEW TIME
# # # ============================================

# # def extract_minutes(message):

# #     message = message.lower()

# #     hour_match = re.search(
# #         r"(\d+(?:\.\d+)?)\s*(?:hours?|hrs?|hr)",
# #         message
# #     )

# #     if hour_match:

# #         hours = float(
# #             hour_match.group(1)
# #         )

# #         return int(hours * 60)

# #     minute_match = re.search(
# #         r"(\d+)\s*(?:minutes?|mins?|min)",
# #         message
# #     )

# #     if minute_match:

# #         return int(
# #             minute_match.group(1)
# #         )

# #     return None


# # # ============================================
# # # RESCHEDULE PLAN
# # # ============================================

# # def reschedule_plan(
# #     subject_data,
# #     user_message,
# #     original_start
# # ):

# #     # ----------------------------------------
# #     # GET NEW AVAILABLE TIME
# #     # ----------------------------------------

# #     new_minutes = extract_minutes(
# #         user_message
# #     )

# #     if not new_minutes:

# #         return (
# #             "⚠️ I couldn't determine your "
# #             "new available time.\n\n"
# #             "Try something like:\n"
# #             "\"I only have 2 hours today.\""
# #         )

# #     # ----------------------------------------
# #     # SORT BY PRIORITY
# #     # ----------------------------------------

# #     subject_data = sorted(
# #         subject_data,
# #         key=lambda x: x["score"],
# #         reverse=True
# #     )

# #     # ----------------------------------------
# #     # SMART SELECTION
# #     # ----------------------------------------

# #     minimum_time = 20

# #     selected_subjects = []

# #     deferred_subjects = []

# #     remaining_time = new_minutes

# #     for item in subject_data:

# #         if remaining_time >= minimum_time:

# #             selected_subjects.append(item)

# #             remaining_time -= minimum_time

# #         else:

# #             deferred_subjects.append(item)

# #     # If no subject fits

# #     if not selected_subjects and subject_data:

# #         selected_subjects.append(
# #             subject_data[0]
# #         )

# #         deferred_subjects = subject_data[1:]

# #     # ----------------------------------------
# #     # PRIORITY ALLOCATION
# #     # ----------------------------------------

# #     total_score = sum(
# #         item["score"]
# #         for item in selected_subjects
# #     )

# #     if total_score <= 0:

# #         total_score = len(
# #             selected_subjects
# #         )

# #     minimum_total = (
# #         len(selected_subjects)
# #         * minimum_time
# #     )

# #     extra_time = (
# #         new_minutes
# #         - minimum_total
# #     )

# #     for item in selected_subjects:

# #         item["duration"] = minimum_time

# #         share = (
# #             item["score"]
# #             / total_score
# #         )

# #         additional = int(
# #             extra_time * share
# #         )

# #         item["duration"] += additional

# #     # ----------------------------------------
# #     # FIX ROUNDING
# #     # ----------------------------------------

# #     allocated = sum(
# #         item["duration"]
# #         for item in selected_subjects
# #     )

# #     difference = (
# #         new_minutes - allocated
# #     )

# #     if selected_subjects:

# #         selected_subjects[0][
# #             "duration"
# #         ] += difference

# #     # ----------------------------------------
# #     # BUILD SCHEDULE
# #     # ----------------------------------------

# #     current_minutes = (
# #         original_start.hour * 60
# #         + original_start.minute
# #     )

# #     plan = []

# #     for item in selected_subjects:

# #         duration = item["duration"]

# #         session_start = current_minutes

# #         session_end = (
# #             current_minutes
# #             + duration
# #         )

# #         plan.append({

# #             "start": format_time(
# #                 session_start
# #             ),

# #             "end": format_time(
# #                 session_end
# #             ),

# #             "subject": item["subject"],

# #             "topic": item.get(
# #                 "topic",
# #                 "Revision"
# #             ),

# #             "duration": duration,

# #             "priority": item["priority"]

# #         })

# #         current_minutes = session_end

# #     # ----------------------------------------
# #     # OUTPUT
# #     # ----------------------------------------

# #     output = (
# #         "## 🔄 RESCHEDULED STUDY PLAN\n\n"
# #     )

# #     output += (
# #         "| Time | Subject | Topic | "
# #         "Duration | Priority |\n"
# #     )

# #     output += (
# #         "|------|---------|-------|"
# #         "----------|----------|\n"
# #     )

# #     for item in plan:

# #         output += (
# #             f"| {item['start']} - "
# #             f"{item['end']} "
# #             f"| {item['subject']} "
# #             f"| {item['topic']} "
# #             f"| {item['duration']} min "
# #             f"| {item['priority']} |\n"
# #         )

# #     actual_total = sum(
# #         item["duration"]
# #         for item in plan
# #     )

# #     output += (
# #         f"\n**⏱️ New Study Time: "
# #         f"{actual_total // 60} hours "
# #         f"{actual_total % 60} minutes**"
# #     )

# #     # ----------------------------------------
# #     # DEFERRED
# #     # ----------------------------------------

# #     if deferred_subjects:

# #         output += (
# #             "\n\n## ⏸️ DEFERRED SUBJECTS\n\n"
# #         )

# #         output += (
# #             "These subjects were deferred "
# #             "because of limited available time:\n\n"
# #         )

# #         for item in deferred_subjects:

# #             output += (
# #                 f"- **{item['subject']}** "
# #                 f"— {item['priority']} Priority "
# #                 f"({item['score']}/100)\n"
# #             )

# #         output += (
# #             "\n💡 They can be prioritized "
# #             "in your next study session."
# #         )

# #     output += (
# #         f"\n\n**🔄 Reason:** "
# #         f"{user_message}"
# #     )

# #     return output





# import re

# from agent import format_time


# # ============================================
# # EXTRACT AVAILABLE TIME
# # ============================================

# def extract_minutes(message):

#     message = message.lower()

#     # Example:
#     # "I only have 3 hours"

#     hour_match = re.search(
#         r"(\d+(?:\.\d+)?)\s*(?:hours?|hrs?|hr)",
#         message
#     )

#     if hour_match:

#         hours = float(
#             hour_match.group(1)
#         )

#         return int(hours * 60)

#     # Example:
#     # "I only have 90 minutes"

#     minute_match = re.search(
#         r"(\d+)\s*(?:minutes?|mins?|min)",
#         message
#     )

#     if minute_match:

#         return int(
#             minute_match.group(1)
#         )

#     return None


# # ============================================
# # DETECT EXAM CRISIS
# # ============================================

# def detect_exam_crisis(message):

#     message = message.lower()

#     exam_keywords = [
#         "exam tomorrow",
#         "test tomorrow",
#         "exam is tomorrow",
#         "test is tomorrow",
#         "exam day after tomorrow",
#         "exam in 1 day",
#         "test in 1 day",
#         "exam today",
#         "test today"
#     ]

#     return any(
#         keyword in message
#         for keyword in exam_keywords
#     )


# # ============================================
# # FIND SUBJECT MENTIONED
# # ============================================

# def find_exam_subject(
#     message,
#     subject_data
# ):

#     message_lower = message.lower()

#     for item in subject_data:

#         subject = item["subject"].lower()

#         if subject in message_lower:

#             return item

#     return None


# # ============================================
# # RESCHEDULE PLAN
# # ============================================

# def reschedule_plan(
#     subject_data,
#     user_message,
#     original_start
# ):

#     # ----------------------------------------
#     # GET AVAILABLE TIME
#     # ----------------------------------------

#     new_minutes = extract_minutes(
#         user_message
#     )

#     if not new_minutes:

#         return (
#             "⚠️ I couldn't determine your "
#             "new available time.\n\n"
#             "Try something like:\n"
#             "\"I only have 2 hours today.\""
#         )


#     # ----------------------------------------
#     # CHECK FOR EXAM CRISIS
#     # ----------------------------------------

#     exam_crisis = detect_exam_crisis(
#         user_message
#     )


#     exam_subject = None

#     if exam_crisis:

#         exam_subject = find_exam_subject(
#             user_message,
#             subject_data
#         )


#     # ========================================
#     # EXAM CRISIS MODE
#     # ========================================

#     if exam_crisis and exam_subject:

#         return create_exam_crisis_plan(

#             exam_subject,

#             subject_data,

#             new_minutes,

#             original_start,

#             user_message

#         )


#     # ========================================
#     # NORMAL RESCHEDULING
#     # ========================================

#     return create_normal_reschedule(

#         subject_data,

#         new_minutes,

#         original_start,

#         user_message

#     )


# # ============================================
# # EXAM CRISIS PLAN
# # ============================================

# def create_exam_crisis_plan(
#     exam_subject,
#     subject_data,
#     new_minutes,
#     original_start,
#     user_message
# ):

#     # ----------------------------------------
#     # EXAM SUBJECT GETS MOST OF THE TIME
#     # ----------------------------------------

#     exam_subject_time = int(
#         new_minutes * 0.80
#     )


#     # Remaining time

#     remaining_time = (
#         new_minutes
#         - exam_subject_time
#     )


#     # ----------------------------------------
#     # OTHER HIGH PRIORITY SUBJECTS
#     # ----------------------------------------

#     other_subjects = [

#         item

#         for item in subject_data

#         if item["subject"]
#         != exam_subject["subject"]

#     ]


#     other_subjects.sort(
#         key=lambda x: x["score"],
#         reverse=True
#     )


#     # ----------------------------------------
#     # CREATE SESSION LIST
#     # ----------------------------------------

#     sessions = []


#     # Main exam subject

#     sessions.append({

#         "subject":
#             exam_subject["subject"],

#         "topic":
#             exam_subject.get(
#                 "topic",
#                 "Important exam topics"
#             ),

#         "duration":
#             exam_subject_time,

#         "priority":
#             "EXAM CRITICAL"

#     })


#     # Give remaining time to
#     # highest-priority other subject

#     if (
#         remaining_time >= 10
#         and other_subjects
#     ):

#         sessions.append({

#             "subject":
#                 other_subjects[0]["subject"],

#             "topic":
#                 other_subjects[0].get(
#                     "topic",
#                     "Quick revision"
#                 ),

#             "duration":
#                 remaining_time,

#             "priority":
#                 other_subjects[0]["priority"]

#         })


#     # ----------------------------------------
#     # BUILD TIME SCHEDULE
#     # ----------------------------------------

#     current_minutes = (
#         original_start.hour * 60
#         + original_start.minute
#     )


#     plan = []


#     for session in sessions:

#         start = current_minutes

#         end = (
#             current_minutes
#             + session["duration"]
#         )


#         plan.append({

#             "start":
#                 format_time(start),

#             "end":
#                 format_time(end),

#             "subject":
#                 session["subject"],

#             "topic":
#                 session["topic"],

#             "duration":
#                 session["duration"],

#             "priority":
#                 session["priority"]

#         })


#         current_minutes = end


#     # ----------------------------------------
#     # OUTPUT
#     # ----------------------------------------

#     output = (
#         "## 🚨 EXAM CRISIS MODE\n\n"
#     )


#     output += (
#         f"**Exam-focused subject:** "
#         f"{exam_subject['subject']}\n\n"
#     )


#     output += (
#         "Your exam urgency was detected, "
#         "so the plan focuses primarily on "
#         "this subject.\n\n"
#     )


#     output += (
#         "| Time | Subject | Topic | "
#         "Duration | Priority |\n"
#     )


#     output += (
#         "|------|---------|-------|"
#         "----------|----------|\n"
#     )


#     for item in plan:

#         output += (

#             f"| {item['start']} - "
#             f"{item['end']} "

#             f"| {item['subject']} "

#             f"| {item['topic']} "

#             f"| {item['duration']} min "

#             f"| {item['priority']} |\n"

#         )


#     actual_total = sum(
#         item["duration"]
#         for item in plan
#     )


#     output += (
#         f"\n**⏱️ Total Study Time: "
#         f"{actual_total // 60} hours "
#         f"{actual_total % 60} minutes**"
#     )


#     # ----------------------------------------
#     # DEFERRED SUBJECTS
#     # ----------------------------------------

#     deferred = [

#         item

#         for item in subject_data

#         if item["subject"]
#         != exam_subject["subject"]

#     ]


#     if deferred:

#         output += (
#             "\n\n## ⏸️ DEFERRED SUBJECTS\n\n"
#         )


#         output += (
#             "These subjects were deferred "
#             "because your exam is urgent:\n\n"
#         )


#         for item in deferred:

#             output += (

#                 f"- **{item['subject']}** "
#                 f"— {item['priority']} "
#                 f"({item['score']}/100)\n"

#             )


#     output += (
#         "\n\n🚨 **Recommendation:** "
#         "Focus on high-yield revision, "
#         "weak areas, and practice questions "
#         "for the upcoming exam."
#     )


#     return output


# # ============================================
# # NORMAL RESCHEDULING
# # ============================================

# def create_normal_reschedule(
#     subject_data,
#     new_minutes,
#     original_start,
#     user_message
# ):

#     subject_data = sorted(
#         subject_data,
#         key=lambda x: x["score"],
#         reverse=True
#     )


#     minimum_time = 20


#     selected_subjects = []

#     deferred_subjects = []


#     remaining_time = new_minutes


#     # ----------------------------------------
#     # SELECT SUBJECTS
#     # ----------------------------------------

#     for item in subject_data:

#         if remaining_time >= minimum_time:

#             selected_subjects.append(
#                 item
#             )

#             remaining_time -= (
#                 minimum_time
#             )

#         else:

#             deferred_subjects.append(
#                 item
#             )


#     if (
#         not selected_subjects
#         and subject_data
#     ):

#         selected_subjects.append(
#             subject_data[0]
#         )

#         deferred_subjects = (
#             subject_data[1:]
#         )


#     # ----------------------------------------
#     # PRIORITY ALLOCATION
#     # ----------------------------------------

#     total_score = sum(
#         item["score"]
#         for item in selected_subjects
#     )


#     if total_score <= 0:

#         total_score = len(
#             selected_subjects
#         )


#     minimum_total = (
#         len(selected_subjects)
#         * minimum_time
#     )


#     extra_time = (
#         new_minutes
#         - minimum_total
#     )


#     for item in selected_subjects:

#         item["duration"] = (
#             minimum_time
#         )


#         share = (
#             item["score"]
#             / total_score
#         )


#         additional = int(
#             extra_time * share
#         )


#         item["duration"] += (
#             additional
#         )


#     # ----------------------------------------
#     # FIX ROUNDING
#     # ----------------------------------------

#     allocated = sum(
#         item["duration"]
#         for item in selected_subjects
#     )


#     difference = (
#         new_minutes
#         - allocated
#     )


#     if selected_subjects:

#         selected_subjects[0][
#             "duration"
#         ] += difference


#     # ----------------------------------------
#     # BUILD SCHEDULE
#     # ----------------------------------------

#     current_minutes = (
#         original_start.hour * 60
#         + original_start.minute
#     )


#     plan = []


#     for item in selected_subjects:

#         duration = item["duration"]


#         start = current_minutes


#         end = (
#             current_minutes
#             + duration
#         )


#         plan.append({

#             "start":
#                 format_time(start),

#             "end":
#                 format_time(end),

#             "subject":
#                 item["subject"],

#             "topic":
#                 item.get(
#                     "topic",
#                     "Revision"
#                 ),

#             "duration":
#                 duration,

#             "priority":
#                 item["priority"]

#         })


#         current_minutes = end


#     # ----------------------------------------
#     # OUTPUT
#     # ----------------------------------------

#     output = (
#         "## 🔄 RESCHEDULED STUDY PLAN\n\n"
#     )


#     output += (
#         "| Time | Subject | Topic | "
#         "Duration | Priority |\n"
#     )


#     output += (
#         "|------|---------|-------|"
#         "----------|----------|\n"
#     )


#     for item in plan:

#         output += (

#             f"| {item['start']} - "
#             f"{item['end']} "

#             f"| {item['subject']} "

#             f"| {item['topic']} "

#             f"| {item['duration']} min "

#             f"| {item['priority']} |\n"

#         )


#     actual_total = sum(
#         item["duration"]
#         for item in plan
#     )


#     output += (
#         f"\n**⏱️ New Study Time: "
#         f"{actual_total // 60} hours "
#         f"{actual_total % 60} minutes**"
#     )


#     if deferred_subjects:

#         output += (
#             "\n\n## ⏸️ DEFERRED SUBJECTS\n\n"
#         )


#         output += (
#             "These subjects were deferred "
#             "because of limited available time:\n\n"
#         )


#         for item in deferred_subjects:

#             output += (

#                 f"- **{item['subject']}** "
#                 f"— {item['priority']} "
#                 f"({item['score']}/100)\n"

#             )


#     output += (
#         f"\n\n**🔄 Reason:** "
#         f"{user_message}"
#     )


#     return output



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