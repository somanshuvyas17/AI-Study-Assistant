# # # # # # # # # import os
# # # # # # # # # from dotenv import load_dotenv
# # # # # # # # # from huggingface_hub import InferenceClient

# # # # # # # # # load_dotenv()

# # # # # # # # # client = InferenceClient(
# # # # # # # # #     api_key=os.getenv("HF_TOKEN"),
# # # # # # # # #     provider="auto"
# # # # # # # # # )


# # # # # # # # # def generate_study_plan(subjects, hours):

# # # # # # # # #     prompt = f"""
# # # # # # # # # You are an AI Study Assistant.

# # # # # # # # # Create a realistic study plan for a student.

# # # # # # # # # Subjects: {subjects}
# # # # # # # # # Available study time: {hours} hours

# # # # # # # # # Rules:
# # # # # # # # # - Divide the available time between the subjects.
# # # # # # # # # - Prioritize difficult and important subjects.
# # # # # # # # # - Include short breaks.
# # # # # # # # # - Do not exceed {hours} hours of study time.
# # # # # # # # # - Keep the response concise.
# # # # # # # # # - Do not include external resources.

# # # # # # # # # Use this format:

# # # # # # # # # 📚 STUDY PLAN

# # # # # # # # # | Time | Subject | Topic | Duration | Priority |
# # # # # # # # # |------|---------|-------|----------|----------|

# # # # # # # # # Include breaks where appropriate.
# # # # # # # # # """

# # # # # # # # #     response = client.chat.completions.create(
# # # # # # # # #         model="openai/gpt-oss-120b",
# # # # # # # # #         messages=[
# # # # # # # # #             {
# # # # # # # # #                 "role": "user",
# # # # # # # # #                 "content": prompt
# # # # # # # # #             }
# # # # # # # # #         ],
# # # # # # # # #         max_tokens=1000
# # # # # # # # #     )

# # # # # # # # #     return response.choices[0].message.content

# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     print(generate_study_plan("DSA, Java, Maths", 2))



# # # # # # # # import os
# # # # # # # # from dotenv import load_dotenv
# # # # # # # # from huggingface_hub import InferenceClient

# # # # # # # # load_dotenv()

# # # # # # # # client = InferenceClient(
# # # # # # # #     api_key=os.getenv("HF_TOKEN"),
# # # # # # # #     provider="auto"
# # # # # # # # )


# # # # # # # # def generate_study_plan(subjects, hours):

# # # # # # # #     prompt = f"""
# # # # # # # # You are an AI Study Assistant.

# # # # # # # # Create a realistic study plan for a student.

# # # # # # # # Subjects: {subjects}
# # # # # # # # Available study time: {hours} hours

# # # # # # # # Rules:
# # # # # # # # - Use exactly the available study time as much as possible.
# # # # # # # # - Prioritize difficult subjects.
# # # # # # # # - Include short breaks.
# # # # # # # # - Do not exceed {hours} hours.
# # # # # # # # - Choose useful topics for each subject.
# # # # # # # # - Keep the response concise.

# # # # # # # # Use this exact format:

# # # # # # # # ## 📚 STUDY PLAN

# # # # # # # # | Time | Subject | Topic | Duration | Priority |
# # # # # # # # |------|---------|-------|----------|----------|

# # # # # # # # Include breaks where appropriate.
# # # # # # # # """

# # # # # # # #     response = client.chat.completions.create(
# # # # # # # #         model="openai/gpt-oss-120b",
# # # # # # # #         messages=[
# # # # # # # #             {
# # # # # # # #                 "role": "user",
# # # # # # # #                 "content": prompt
# # # # # # # #             }
# # # # # # # #         ],
# # # # # # # #         max_tokens=1000
# # # # # # # #     )

# # # # # # # #     return response.choices[0].message.content






# # # # # # # import os
# # # # # # # from dotenv import load_dotenv
# # # # # # # from huggingface_hub import InferenceClient

# # # # # # # load_dotenv()

# # # # # # # client = InferenceClient(
# # # # # # #     api_key=os.getenv("HF_TOKEN"),
# # # # # # #     provider="auto"
# # # # # # # )


# # # # # # # def generate_study_plan(subjects, hours):

# # # # # # #     prompt = f"""
# # # # # # # You are an AI Study Assistant.

# # # # # # # Create a realistic study plan for a student.

# # # # # # # Subjects: {subjects}
# # # # # # # Available study time: {hours} hours.

# # # # # # # Rules:
# # # # # # # - Create a plan for exactly {hours} hours of study.
# # # # # # # - Divide the time intelligently between the subjects.
# # # # # # # - Prioritize difficult subjects.
# # # # # # # - Include short breaks.
# # # # # # # - Do not exceed the available study time.
# # # # # # # - Choose appropriate topics for each subject.
# # # # # # # - Keep the response concise.

# # # # # # # Return ONLY the study plan.

# # # # # # # Use this format:

# # # # # # # ## 📚 STUDY PLAN

# # # # # # # | Time | Subject | Topic | Duration | Priority |
# # # # # # # |------|---------|-------|----------|----------|

# # # # # # # Include breaks where appropriate.
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

# # # # # # #     # Get AI response
# # # # # # #     plan = response.choices[0].message.content

# # # # # # #     # Make sure we never return None
# # # # # # #     if plan is None:
# # # # # # #         return "⚠️ The AI did not return a study plan. Please try again."

# # # # # # #     return plan


# # # # # # # # Test the function directly
# # # # # # # if __name__ == "__main__":

# # # # # # #     plan = generate_study_plan(
# # # # # # #         "DSA, Java, Maths",
# # # # # # #         6
# # # # # # #     )

# # # # # # #     print(plan)






# # # # # # import os
# # # # # # from dotenv import load_dotenv
# # # # # # from huggingface_hub import InferenceClient

# # # # # # load_dotenv()

# # # # # # client = InferenceClient(
# # # # # #     api_key=os.getenv("HF_TOKEN"),
# # # # # #     provider="auto"
# # # # # # )


# # # # # # def generate_study_plan(subjects, hours):

# # # # # #     prompt = f"""
# # # # # # You are an AI Study Assistant.

# # # # # # Create a simple study plan.

# # # # # # Subjects: {subjects}
# # # # # # Available time: {hours} hours.

# # # # # # Create a plan that fits within {hours} hours.

# # # # # # Use this format:

# # # # # # ## 📚 STUDY PLAN

# # # # # # | Time | Subject | Topic | Duration | Priority |
# # # # # # |------|---------|-------|----------|----------|

# # # # # # Include short breaks.
# # # # # # Keep the answer concise.
# # # # # # """

# # # # # #     response = client.chat.completions.create(
# # # # # #         model="openai/gpt-oss-120b",
# # # # # #         messages=[
# # # # # #             {
# # # # # #                 "role": "user",
# # # # # #                 "content": prompt
# # # # # #             }
# # # # # #         ],
# # # # # #         max_tokens=3000,
# # # # # #         extra_body={
# # # # # #             "reasoning_effort": "low"
# # # # # #         }
# # # # # #     )

# # # # # #     print("\nDEBUG RESPONSE:")
# # # # # #     print(response)

# # # # # #     plan = response.choices[0].message.content

# # # # # #     if plan:
# # # # # #         return plan

# # # # # #     return "⚠️ The AI returned no visible text."


# # # # # # if __name__ == "__main__":

# # # # # #     plan = generate_study_plan(
# # # # # #         "DSA, Java, Maths",
# # # # # #         6
# # # # # #     )

# # # # # #     print("\n\nFINAL PLAN:")
# # # # # #     print(plan)



# # # # # import os
# # # # # from dotenv import load_dotenv
# # # # # from huggingface_hub import InferenceClient

# # # # # load_dotenv()

# # # # # client = InferenceClient(
# # # # #     api_key=os.getenv("HF_TOKEN"),
# # # # #     provider="auto"
# # # # # )


# # # # # def get_ai_topics(subjects):

# # # # #     prompt = f"""
# # # # # You are a study planning assistant.

# # # # # The student's subjects are:
# # # # # {subjects}

# # # # # For EACH subject, suggest:
# # # # # 1. One important topic to study
# # # # # 2. Priority: High, Medium, or Low

# # # # # Return ONLY in this format:

# # # # # Subject | Topic | Priority

# # # # # Example:
# # # # # DSA | Linked Lists | High
# # # # # Java | OOP and Inheritance | Medium
# # # # # Maths | Integration | High

# # # # # Do not add explanations.
# # # # # """

# # # # #     response = client.chat.completions.create(
# # # # #         model="openai/gpt-oss-120b",
# # # # #         messages=[
# # # # #             {
# # # # #                 "role": "user",
# # # # #                 "content": prompt
# # # # #             }
# # # # #         ],
# # # # #         max_tokens=500,
# # # # #         extra_body={
# # # # #             "reasoning_effort": "low"
# # # # #         }
# # # # #     )

# # # # #     text = response.choices[0].message.content

# # # # #     if not text:
# # # # #         return []

# # # # #     return text.strip().split("\n")


# # # # # def generate_study_plan(subjects, hours):

# # # # #     # EXACT amount of time requested by user
# # # # #     total_minutes = int(hours * 60)

# # # # #     subject_list = [
# # # # #         subject.strip()
# # # # #         for subject in subjects.split(",")
# # # # #         if subject.strip()
# # # # #     ]

# # # # #     # Ask AI for topics and priorities
# # # # #     ai_lines = get_ai_topics(subjects)

# # # # #     topics = []

# # # # #     for line in ai_lines:

# # # # #         if "|" in line:

# # # # #             parts = [
# # # # #                 x.strip()
# # # # #                 for x in line.split("|")
# # # # #             ]

# # # # #             if len(parts) >= 3:

# # # # #                 topics.append({
# # # # #                     "subject": parts[0],
# # # # #                     "topic": parts[1],
# # # # #                     "priority": parts[2]
# # # # #                 })


# # # # #     # If AI response cannot be parsed,
# # # # #     # create fallback topics.
# # # # #     if not topics:

# # # # #         for subject in subject_list:

# # # # #             topics.append({
# # # # #                 "subject": subject,
# # # # #                 "topic": "Important topics and practice",
# # # # #                 "priority": "High"
# # # # #             })


# # # # #     # Make sure we have at least one topic
# # # # #     if len(topics) == 0:

# # # # #         topics = [{
# # # # #             "subject": "General Study",
# # # # #             "topic": "Revision and practice",
# # # # #             "priority": "High"
# # # # #         }]


# # # # #     # ------------------------------------------------
# # # # #     # EXACT TIME ALLOCATION
# # # # #     # ------------------------------------------------

# # # # #     number_of_topics = len(topics)

# # # # #     base_time = total_minutes // number_of_topics

# # # # #     remainder = total_minutes % number_of_topics


# # # # #     for i in range(number_of_topics):

# # # # #         topics[i]["duration"] = base_time

# # # # #         # Distribute remaining minutes
# # # # #         if i < remainder:
# # # # #             topics[i]["duration"] += 1


# # # # #     # ------------------------------------------------
# # # # #     # CREATE TIME SCHEDULE
# # # # #     # ------------------------------------------------

# # # # #     current_minutes = 9 * 60

# # # # #     plan = []

# # # # #     for item in topics:

# # # # #         start_hour = current_minutes // 60
# # # # #         start_minute = current_minutes % 60

# # # # #         end_minutes = (
# # # # #             current_minutes
# # # # #             + item["duration"]
# # # # #         )

# # # # #         end_hour = end_minutes // 60
# # # # #         end_minute = end_minutes % 60


# # # # #         start_time = (
# # # # #             f"{start_hour:02d}:{start_minute:02d}"
# # # # #         )

# # # # #         end_time = (
# # # # #             f"{end_hour:02d}:{end_minute:02d}"
# # # # #         )


# # # # #         plan.append({
# # # # #             "start": start_time,
# # # # #             "end": end_time,
# # # # #             "subject": item["subject"],
# # # # #             "topic": item["topic"],
# # # # #             "duration": item["duration"],
# # # # #             "priority": item["priority"]
# # # # #         })


# # # # #         current_minutes = end_minutes


# # # # #     # ------------------------------------------------
# # # # #     # CREATE MARKDOWN TABLE
# # # # #     # ------------------------------------------------

# # # # #     output = "## 📚 STUDY PLAN\n\n"

# # # # #     output += (
# # # # #         "| Time | Subject | Topic | Duration | Priority |\n"
# # # # #     )

# # # # #     output += (
# # # # #         "|------|---------|-------|----------|----------|\n"
# # # # #     )


# # # # #     for item in plan:

# # # # #         output += (
# # # # #             f"| {item['start']} - {item['end']} "
# # # # #             f"| {item['subject']} "
# # # # #             f"| {item['topic']} "
# # # # #             f"| {item['duration']} min "
# # # # #             f"| {item['priority']} |\n"
# # # # #         )


# # # # #     # Calculate actual total
# # # # #     actual_total = sum(
# # # # #         item["duration"]
# # # # #         for item in plan
# # # # #     )


# # # # #     output += (
# # # # #         f"\n**Total Study Time: "
# # # # #         f"{actual_total // 60} hours "
# # # # #         f"{actual_total % 60} minutes**"
# # # # #     )


# # # # #     return output


# # # # # if __name__ == "__main__":

# # # # #     plan = generate_study_plan(
# # # # #         "DSA, Java, Maths",
# # # # #         5
# # # # #     )

# # # # #     print(plan)





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
# # # # # GET TOPICS FROM AI
# # # # # ----------------------------------------

# # # # def get_ai_topics(subjects):

# # # #     prompt = f"""
# # # # You are an AI Study Assistant.

# # # # The student's subjects are:

# # # # {subjects}

# # # # For each subject, suggest ONE important topic.

# # # # Also assign a priority:
# # # # High, Medium, or Low.

# # # # Return ONLY this format:

# # # # Subject | Topic | Priority

# # # # Example:

# # # # DSA | Linked Lists | High
# # # # Java | OOP and Inheritance | Medium
# # # # Maths | Integration | High

# # # # Do not add explanations.
# # # # """

# # # #     response = client.chat.completions.create(

# # # #         model="openai/gpt-oss-120b",

# # # #         messages=[
# # # #             {
# # # #                 "role": "user",
# # # #                 "content": prompt
# # # #             }
# # # #         ],

# # # #         max_tokens=500,

# # # #         extra_body={
# # # #             "reasoning_effort": "low"
# # # #         }
# # # #     )

# # # #     text = response.choices[0].message.content

# # # #     if not text:
# # # #         return []

# # # #     return text.strip().split("\n")


# # # # # ----------------------------------------
# # # # # GENERATE STUDY PLAN
# # # # # ----------------------------------------

# # # # def generate_study_plan(
# # # #     subjects,
# # # #     start_time,
# # # #     end_time
# # # # ):

# # # #     # Convert start and end time to minutes

# # # #     start_minutes = (
# # # #         start_time.hour * 60
# # # #         + start_time.minute
# # # #     )

# # # #     end_minutes = (
# # # #         end_time.hour * 60
# # # #         + end_time.minute
# # # #     )


# # # #     # Make sure end time is after start time

# # # #     if end_minutes <= start_minutes:

# # # #         return (
# # # #             "⚠️ End time must be after "
# # # #             "start time."
# # # #         )


# # # #     # EXACT AVAILABLE TIME

# # # #     total_minutes = (
# # # #         end_minutes - start_minutes
# # # #     )


# # # #     # ----------------------------------------
# # # #     # GET AI TOPICS
# # # #     # ----------------------------------------

# # # #     ai_lines = get_ai_topics(subjects)


# # # #     topics = []


# # # #     for line in ai_lines:

# # # #         if "|" in line:

# # # #             parts = [
# # # #                 x.strip()
# # # #                 for x in line.split("|")
# # # #             ]

# # # #             if len(parts) >= 3:

# # # #                 topics.append({

# # # #                     "subject": parts[0],

# # # #                     "topic": parts[1],

# # # #                     "priority": parts[2]

# # # #                 })


# # # #     # ----------------------------------------
# # # #     # FALLBACK
# # # #     # ----------------------------------------

# # # #     if not topics:

# # # #         subject_list = [

# # # #             subject.strip()

# # # #             for subject in subjects.split(",")

# # # #             if subject.strip()

# # # #         ]


# # # #         for subject in subject_list:

# # # #             topics.append({

# # # #                 "subject": subject,

# # # #                 "topic": "Important topics and practice",

# # # #                 "priority": "High"

# # # #             })


# # # #     if not topics:

# # # #         topics.append({

# # # #             "subject": "General Study",

# # # #             "topic": "Revision and practice",

# # # #             "priority": "High"

# # # #         })


# # # #     # ----------------------------------------
# # # #     # LIMIT TOPICS
# # # #     # ----------------------------------------

# # # #     # We don't want too many tiny sessions.

# # # #     max_topics = min(len(topics), 4)

# # # #     topics = topics[:max_topics]


# # # #     # ----------------------------------------
# # # #     # EXACT TIME ALLOCATION
# # # #     # ----------------------------------------

# # # #     number_of_topics = len(topics)

# # # #     base_time = (
# # # #         total_minutes // number_of_topics
# # # #     )

# # # #     remainder = (
# # # #         total_minutes % number_of_topics
# # # #     )


# # # #     for i in range(number_of_topics):

# # # #         topics[i]["duration"] = base_time

# # # #         if i < remainder:

# # # #             topics[i]["duration"] += 1


# # # #     # ----------------------------------------
# # # #     # BUILD PLAN
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
# # # #     # CREATE MARKDOWN TABLE
# # # #     # ----------------------------------------

# # # #     output = "## 📚 STUDY PLAN\n\n"


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


# # # #     # ----------------------------------------
# # # #     # VERIFY TOTAL TIME
# # # #     # ----------------------------------------

# # # #     actual_total = sum(

# # # #         item["duration"]

# # # #         for item in plan

# # # #     )


# # # #     output += (
# # # #         f"\n**⏱️ Total Study Time: "
# # # #         f"{actual_total // 60} hours "
# # # #         f"{actual_total % 60} minutes**"
# # # #     )


# # # #     return output


# # # # # ----------------------------------------
# # # # # TEST
# # # # # ----------------------------------------

# # # # if __name__ == "__main__":

# # # #     plan = generate_study_plan(

# # # #         "DSA, Java, Maths",

# # # #         __import__("datetime").time(18, 0),

# # # #         __import__("datetime").time(23, 0)

# # # #     )

# # # #     print(plan)










# # # import os

# # # from dotenv import load_dotenv
# # # from huggingface_hub import InferenceClient


# # # load_dotenv()


# # # client = InferenceClient(
# # #     api_key=os.getenv("HF_TOKEN"),
# # #     provider="auto"
# # # )


# # # # ============================================
# # # # FORMAT TIME
# # # # ============================================

# # # def format_time(minutes):

# # #     hour = (minutes // 60) % 24
# # #     minute = minutes % 60

# # #     period = "AM" if hour < 12 else "PM"

# # #     display_hour = hour % 12

# # #     if display_hour == 0:
# # #         display_hour = 12

# # #     return f"{display_hour}:{minute:02d} {period}"


# # # # ============================================
# # # # GET TOPIC FROM AI
# # # # ============================================

# # # def get_ai_topics(subjects):

# # #     prompt = f"""
# # # You are an AI Study Assistant.

# # # The student has these subjects:

# # # {subjects}

# # # Suggest ONE important topic for each subject.

# # # Return ONLY:

# # # Subject | Topic

# # # Example:

# # # DSA | Linked Lists
# # # Java | Object Oriented Programming
# # # Maths | Integration

# # # Do not assign priority.
# # # Do not add explanations.
# # # """

# # #     response = client.chat.completions.create(

# # #         model="openai/gpt-oss-120b",

# # #         messages=[
# # #             {
# # #                 "role": "user",
# # #                 "content": prompt
# # #             }
# # #         ],

# # #         max_tokens=500,

# # #         extra_body={
# # #             "reasoning_effort": "low"
# # #         }
# # #     )


# # #     text = response.choices[0].message.content


# # #     if not text:

# # #         return {}


# # #     topics = {}


# # #     for line in text.strip().split("\n"):

# # #         if "|" in line:

# # #             parts = [
# # #                 x.strip()
# # #                 for x in line.split("|")
# # #             ]


# # #             if len(parts) >= 2:

# # #                 subject = parts[0]

# # #                 topic = parts[1]


# # #                 if (
# # #                     subject.lower()
# # #                     not in ["subject", "subjects"]
# # #                 ):

# # #                     topics[
# # #                         subject.lower()
# # #                     ] = topic


# # #     return topics


# # # # ============================================
# # # # GENERATE STUDY PLAN
# # # # ============================================

# # # def generate_study_plan(
# # #     subject_data,
# # #     start_time,
# # #     end_time
# # # ):

# # #     # ----------------------------------------
# # #     # CALCULATE TOTAL TIME
# # #     # ----------------------------------------

# # #     start_minutes = (
# # #         start_time.hour * 60
# # #         + start_time.minute
# # #     )


# # #     end_minutes = (
# # #         end_time.hour * 60
# # #         + end_time.minute
# # #     )


# # #     if end_minutes <= start_minutes:

# # #         return (
# # #             "⚠️ End time must be after "
# # #             "start time."
# # #         )


# # #     total_minutes = (
# # #         end_minutes - start_minutes
# # #     )


# # #     # ----------------------------------------
# # #     # GET SUBJECT NAMES
# # #     # ----------------------------------------

# # #     subjects = [
# # #         item["subject"]
# # #         for item in subject_data
# # #     ]


# # #     subject_string = ", ".join(subjects)


# # #     # ----------------------------------------
# # #     # ASK AI FOR TOPICS
# # #     # ----------------------------------------

# # #     ai_topics = get_ai_topics(
# # #         subject_string
# # #     )


# # #     # ----------------------------------------
# # #     # ADD TOPICS TO SUBJECT DATA
# # #     # ----------------------------------------

# # #     for item in subject_data:

# # #         topic = ai_topics.get(
# # #             item["subject"].lower()
# # #         )


# # #         if topic:

# # #             item["topic"] = topic

# # #         else:

# # #             item["topic"] = (
# # #                 "Important topics and practice"
# # #             )


# # #     # ----------------------------------------
# # #     # SORT BY PRIORITY SCORE
# # #     # ----------------------------------------

# # #     subject_data.sort(
# # #         key=lambda x: x["score"],
# # #         reverse=True
# # #     )


# # #     # ----------------------------------------
# # #     # EXACT TIME ALLOCATION
# # #     # ----------------------------------------

# # #     number_of_subjects = len(
# # #         subject_data
# # #     )


# # #     if number_of_subjects == 0:

# # #         return "⚠️ No subjects found."


# # #     # Give every subject a minimum
# # #     # amount of time when possible.

# # #     minimum_time = 15


# # #     if total_minutes >= (
# # #         number_of_subjects
# # #         * minimum_time
# # #     ):

# # #         for item in subject_data:

# # #             item["duration"] = minimum_time


# # #         remaining_minutes = (
# # #             total_minutes
# # #             -
# # #             (
# # #                 number_of_subjects
# # #                 * minimum_time
# # #             )
# # #         )


# # #     else:

# # #         remaining_minutes = total_minutes

# # #         for item in subject_data:

# # #             item["duration"] = 0


# # #     # ----------------------------------------
# # #     # DISTRIBUTE REMAINING TIME
# # #     # BY PRIORITY SCORE
# # #     # ----------------------------------------

# # #     total_score = sum(
# # #         item["score"]
# # #         for item in subject_data
# # #     )


# # #     if total_score <= 0:

# # #         total_score = number_of_subjects


# # #     for item in subject_data:

# # #         share = (
# # #             item["score"]
# # #             / total_score
# # #         )


# # #         extra_time = int(
# # #             remaining_minutes * share
# # #         )


# # #         item["duration"] += extra_time


# # #     # ----------------------------------------
# # #     # FIX ROUNDING DIFFERENCE
# # #     # ----------------------------------------

# # #     allocated = sum(
# # #         item["duration"]
# # #         for item in subject_data
# # #     )


# # #     difference = (
# # #         total_minutes - allocated
# # #     )


# # #     # Add leftover minutes to
# # #     # highest-priority subject.

# # #     subject_data[0]["duration"] += difference


# # #     # ----------------------------------------
# # #     # BUILD TIME SCHEDULE
# # #     # ----------------------------------------

# # #     current_minutes = start_minutes


# # #     plan = []


# # #     for item in subject_data:

# # #         duration = item["duration"]


# # #         if duration <= 0:

# # #             continue


# # #         session_start = current_minutes

# # #         session_end = (
# # #             current_minutes
# # #             + duration
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

# # #             "duration": duration,

# # #             "priority": item["priority"],

# # #             "score": item["score"]

# # #         })


# # #         current_minutes = session_end


# # #     # ----------------------------------------
# # #     # CREATE MARKDOWN
# # #     # ----------------------------------------

# # #     output = "## 📚 STUDY PLAN\n\n"


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
# # #         f"\n**⏱️ Total Study Time: "
# # #         f"{actual_total // 60} hours "
# # #         f"{actual_total % 60} minutes**"
# # #     )


# # #     return output






# # import os

# # from dotenv import load_dotenv
# # from huggingface_hub import InferenceClient


# # load_dotenv()


# # client = InferenceClient(
# #     api_key=os.getenv("HF_TOKEN"),
# #     provider="auto"
# # )


# # # ============================================
# # # FORMAT TIME
# # # ============================================

# # def format_time(minutes):

# #     hour = (minutes // 60) % 24
# #     minute = minutes % 60

# #     period = "AM" if hour < 12 else "PM"

# #     display_hour = hour % 12

# #     if display_hour == 0:
# #         display_hour = 12

# #     return f"{display_hour}:{minute:02d} {period}"


# # # ============================================
# # # GET TOPICS FROM AI
# # # ============================================

# # def get_ai_topics(subjects):

# #     prompt = f"""
# # You are an AI Study Assistant.

# # The student has these subjects:

# # {subjects}

# # Suggest ONE important topic for each subject.

# # Return ONLY:

# # Subject | Topic

# # Example:

# # DSA | Linked Lists
# # Java | Object Oriented Programming
# # Maths | Integration

# # Do not assign priority.
# # Do not add explanations.
# # """

# #     response = client.chat.completions.create(
# #         model="openai/gpt-oss-120b",
# #         messages=[
# #             {
# #                 "role": "user",
# #                 "content": prompt
# #             }
# #         ],
# #         max_tokens=500,
# #         extra_body={
# #             "reasoning_effort": "low"
# #         }
# #     )

# #     text = response.choices[0].message.content

# #     if not text:
# #         return {}

# #     topics = {}

# #     for line in text.strip().split("\n"):

# #         if "|" in line:

# #             parts = [
# #                 x.strip()
# #                 for x in line.split("|")
# #             ]

# #             if len(parts) >= 2:

# #                 subject = parts[0]
# #                 topic = parts[1]

# #                 if subject.lower() not in [
# #                     "subject",
# #                     "subjects"
# #                 ]:

# #                     topics[
# #                         subject.lower()
# #                     ] = topic

# #     return topics


# # # ============================================
# # # GENERATE STUDY PLAN
# # # ============================================

# # def generate_study_plan(
# #     subject_data,
# #     start_time,
# #     end_time
# # ):

# #     # ----------------------------------------
# #     # CALCULATE TOTAL TIME
# #     # ----------------------------------------

# #     start_minutes = (
# #         start_time.hour * 60
# #         + start_time.minute
# #     )

# #     end_minutes = (
# #         end_time.hour * 60
# #         + end_time.minute
# #     )

# #     if end_minutes <= start_minutes:

# #         return (
# #             "⚠️ End time must be after "
# #             "start time."
# #         )

# #     total_minutes = (
# #         end_minutes - start_minutes
# #     )

# #     # ----------------------------------------
# #     # GET SUBJECT NAMES
# #     # ----------------------------------------

# #     subjects = [
# #         item["subject"]
# #         for item in subject_data
# #     ]

# #     subject_string = ", ".join(subjects)

# #     # ----------------------------------------
# #     # GET AI TOPICS
# #     # ----------------------------------------

# #     ai_topics = get_ai_topics(
# #         subject_string
# #     )

# #     # ----------------------------------------
# #     # ADD TOPICS
# #     # ----------------------------------------

# #     for item in subject_data:

# #         topic = ai_topics.get(
# #             item["subject"].lower()
# #         )

# #         if topic:

# #             item["topic"] = topic

# #         else:

# #             item["topic"] = (
# #                 "Important topics and practice"
# #             )

# #     # ----------------------------------------
# #     # SORT BY PRIORITY
# #     # ----------------------------------------

# #     subject_data.sort(
# #         key=lambda x: x["score"],
# #         reverse=True
# #     )

# #     # ----------------------------------------
# #     # SMART SUBJECT SELECTION
# #     # ----------------------------------------

# #     # Minimum realistic study session

# #     minimum_time = 20

# #     selected_subjects = []

# #     deferred_subjects = []

# #     remaining_time = total_minutes

# #     for item in subject_data:

# #         if remaining_time >= minimum_time:

# #             selected_subjects.append(item)

# #             remaining_time -= minimum_time

# #         else:

# #             deferred_subjects.append(item)

# #     # ----------------------------------------
# #     # IF ONLY ONE SUBJECT FITS
# #     # ----------------------------------------

# #     if not selected_subjects and subject_data:

# #         selected_subjects.append(
# #             subject_data[0]
# #         )

# #         deferred_subjects = subject_data[1:]

# #     # ----------------------------------------
# #     # ALLOCATE TIME BY PRIORITY
# #     # ----------------------------------------

# #     selected_score = sum(
# #         item["score"]
# #         for item in selected_subjects
# #     )

# #     if selected_score <= 0:

# #         selected_score = len(
# #             selected_subjects
# #         )

# #     # Give minimum time first

# #     allocated_minimum = (
# #         len(selected_subjects)
# #         * minimum_time
# #     )

# #     extra_time = (
# #         total_minutes
# #         - allocated_minimum
# #     )

# #     for item in selected_subjects:

# #         item["duration"] = minimum_time

# #         share = (
# #             item["score"]
# #             / selected_score
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
# #         total_minutes - allocated
# #     )

# #     if selected_subjects:

# #         selected_subjects[0][
# #             "duration"
# #         ] += difference

# #     # ----------------------------------------
# #     # CREATE SCHEDULE
# #     # ----------------------------------------

# #     current_minutes = start_minutes

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

# #             "topic": item["topic"],

# #             "duration": duration,

# #             "priority": item["priority"],

# #             "score": item["score"]

# #         })

# #         current_minutes = session_end

# #     # ----------------------------------------
# #     # BUILD OUTPUT
# #     # ----------------------------------------

# #     output = "## 📚 STUDY PLAN\n\n"

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
# #         f"\n**⏱️ Total Study Time: "
# #         f"{actual_total // 60} hours "
# #         f"{actual_total % 60} minutes**"
# #     )

# #     # ----------------------------------------
# #     # DEFERRED SUBJECTS
# #     # ----------------------------------------

# #     if deferred_subjects:

# #         output += (
# #             "\n\n## ⏸️ DEFERRED SUBJECTS\n\n"
# #         )

# #         output += (
# #             "These subjects were not included "
# #             "because there was not enough time:\n\n"
# #         )

# #         for item in deferred_subjects:

# #             output += (
# #                 f"- **{item['subject']}** "
# #                 f"— {item['priority']} Priority "
# #                 f"({item['score']}/100)\n"
# #             )

# #         output += (
# #             "\n💡 These subjects should be "
# #             "considered in the next study session."
# #         )

# #     return {
# #     "markdown": output,
# #     "sessions": plan
# # }








# import os
# import json
# import re
# import streamlit as st

# from dotenv import load_dotenv
# from huggingface_hub import InferenceClient


# # ============================================================
# # LOAD ENVIRONMENT VARIABLES
# # ============================================================

# load_dotenv()


# # ============================================================
# # GET HUGGING FACE TOKEN
# # ============================================================

# HF_TOKEN = os.getenv("HF_TOKEN")

# # If running on Streamlit Cloud, use Streamlit Secrets
# if not HF_TOKEN:

#     try:
#         HF_TOKEN = st.secrets["HF_TOKEN"]

#     except Exception:
#         HF_TOKEN = None


# # ============================================================
# # CHECK TOKEN
# # ============================================================

# if not HF_TOKEN:

#     st.error(
#         "❌ Hugging Face API token not found. "
#         "Add HF_TOKEN to your .env file locally "
#         "or Streamlit Secrets when deploying."
#     )

#     st.stop()


# # ============================================================
# # HUGGING FACE CLIENT
# # ============================================================

# client = InferenceClient(
#     api_key=HF_TOKEN,
#     provider="auto"
# )


# # ============================================================
# # MODEL
# # ============================================================

# MODEL = "meta-llama/Llama-3.1-8B-Instruct"


# # ============================================================
# # HELPER — EXTRACT JSON
# # ============================================================

# def extract_json(text):

#     """
#     Extract JSON from the model response.
#     """

#     text = text.strip()

#     # Remove markdown code fences

#     text = re.sub(
#         r"```json",
#         "",
#         text,
#         flags=re.IGNORECASE
#     )

#     text = re.sub(
#         r"```",
#         "",
#         text
#     )

#     text = text.strip()


#     # Find JSON object

#     start = text.find("{")

#     end = text.rfind("}")

#     if start != -1 and end != -1:

#         json_text = text[
#             start:end + 1
#         ]

#         try:

#             return json.loads(
#                 json_text
#             )

#         except json.JSONDecodeError:

#             pass


#     return None


# # ============================================================
# # GENERATE STUDY PLAN
# # ============================================================

# def generate_study_plan(
#     subject_data,
#     start_time,
#     end_time
# ):

#     """
#     Generate a personalized study plan.

#     Returns:

#     {
#         "markdown": "...",
#         "sessions": [...]
#     }
#     """


#     # --------------------------------------------------------
#     # CALCULATE AVAILABLE TIME
#     # --------------------------------------------------------

#     start_minutes = (
#         start_time.hour * 60
#         + start_time.minute
#     )

#     end_minutes = (
#         end_time.hour * 60
#         + end_time.minute
#     )

#     available_minutes = (
#         end_minutes
#         - start_minutes
#     )


#     if available_minutes <= 0:

#         return {

#             "markdown":
#                 "❌ Invalid study time.",

#             "sessions": []

#         }


#     # --------------------------------------------------------
#     # SUBJECT INFORMATION
#     # --------------------------------------------------------

#     subject_text = ""


#     for item in subject_data:

#         subject_text += f"""

# Subject: {item['subject']}

# Exam Date: {item['exam_date']}

# Difficulty: {item['difficulty']}

# Syllabus Completed: {item['progress']}%

# Priority Score: {item['score']}/100

# Priority Level: {item['priority']}

# Exam Urgency Score: {item['exam_score']}

# Difficulty Score: {item['difficulty_score']}

# Remaining Syllabus Score: {item['remaining_score']}

# """


#     # --------------------------------------------------------
#     # AI PROMPT
#     # --------------------------------------------------------

#     prompt = f"""
# You are an intelligent AI Study Planner.

# Create a realistic study plan for a student.

# The student has exactly:

# {available_minutes} minutes

# available between:

# {start_time.strftime('%I:%M %p')}

# and

# {end_time.strftime('%I:%M %p')}.


# SUBJECT INFORMATION:

# {subject_text}


# IMPORTANT RULES:

# 1. Use the ENTIRE available study time.

# 2. Do not create a plan shorter than the available time.

# 3. Allocate more time to higher-priority subjects.

# 4. Consider exam urgency.

# 5. Consider subject difficulty.

# 6. Consider remaining syllabus.

# 7. Every subject does NOT need equal time.

# 8. Include short breaks when appropriate.

# 9. The total duration of all sessions and breaks must fit
#    exactly inside the student's available time.

# 10. Do not schedule anything outside the given time window.

# 11. Create realistic topics/tasks.

# 12. If the exam is very close, prioritize revision,
#     important concepts and practice questions.

# 13. Avoid vague activities such as
#     "study DSA".

# 14. Give specific tasks such as
#     "Practice binary search problems".

# 15. Return ONLY valid JSON.

# Return this exact structure:

# {{
#     "sessions": [
#         {{
#             "subject": "DSA",
#             "topic": "Binary Search",
#             "duration": 45,
#             "type": "Study"
#         }},
#         {{
#             "subject": "BREAK",
#             "topic": "Short Break",
#             "duration": 10,
#             "type": "Break"
#         }}
#     ]
# }}

# The duration values must be integers representing minutes.

# The total duration of ALL sessions must equal:

# {available_minutes}

# Do not include any text outside the JSON.
# """


#     # --------------------------------------------------------
#     # CALL HUGGING FACE
#     # --------------------------------------------------------

#     try:

#         response = client.chat.completions.create(

#             model=MODEL,

#             messages=[

#                 {
#                     "role": "system",
#                     "content":
#                         "You are an expert academic "
#                         "study planner. Return only "
#                         "valid JSON when requested."
#                 },

#                 {
#                     "role": "user",
#                     "content": prompt
#                 }

#             ],

#             max_tokens=1800,

#             temperature=0.3

#         )


#         output = (
#             response.choices[0]
#             .message.content
#         )


#     except Exception as e:

#         return {

#             "markdown":
#                 f"❌ Hugging Face error: {e}",

#             "sessions": []

#         }


#     # --------------------------------------------------------
#     # PARSE JSON
#     # --------------------------------------------------------

#     parsed = extract_json(
#         output
#     )


#     if not parsed:

#         return {

#             "markdown":
#                 "⚠️ The AI did not return "
#                 "a valid study plan. "
#                 "Please try again.",

#             "sessions": []

#         }


#     sessions = parsed.get(
#         "sessions",
#         []
#     )


#     if not sessions:

#         return {

#             "markdown":
#                 "⚠️ No study sessions "
#                 "were generated.",

#             "sessions": []

#         }


#     # --------------------------------------------------------
#     # CLEAN SESSIONS
#     # --------------------------------------------------------

#     cleaned_sessions = []


#     for session in sessions:

#         try:

#             subject = str(
#                 session.get(
#                     "subject",
#                     "Study"
#                 )
#             )

#             topic = str(
#                 session.get(
#                     "topic",
#                     "Study Session"
#                 )
#             )

#             duration = int(
#                 session.get(
#                     "duration",
#                     0
#                 )
#             )

#             session_type = str(
#                 session.get(
#                     "type",
#                     "Study"
#                 )
#             )


#             if duration <= 0:

#                 continue


#             cleaned_sessions.append({

#                 "subject":
#                     subject,

#                 "topic":
#                     topic,

#                 "duration":
#                     duration,

#                 "type":
#                     session_type

#             })

#         except Exception:

#             continue


#     # --------------------------------------------------------
#     # VALIDATE TOTAL TIME
#     # --------------------------------------------------------

#     total_duration = sum(

#         session["duration"]

#         for session in cleaned_sessions

#     )


#     # --------------------------------------------------------
#     # FIX SMALL ROUNDING DIFFERENCE
#     # --------------------------------------------------------

#     difference = (

#         available_minutes
#         - total_duration

#     )


#     if difference != 0:

#         # Add missing time to the final session

#         if cleaned_sessions:

#             cleaned_sessions[-1][
#                 "duration"
#             ] += difference


#     # --------------------------------------------------------
#     # CREATE MARKDOWN PLAN
#     # --------------------------------------------------------

#     markdown = create_markdown_plan(
#         cleaned_sessions,
#         start_time,
#         available_minutes
#     )


#     return {

#         "markdown":
#             markdown,

#         "sessions":
#             cleaned_sessions

#     }


# # ============================================================
# # CREATE MARKDOWN PLAN
# # ============================================================

# def create_markdown_plan(
#     sessions,
#     start_time,
#     available_minutes
# ):

#     """
#     Convert structured sessions into
#     a readable Markdown study plan.
#     """


#     current_minutes = (

#         start_time.hour * 60
#         + start_time.minute

#     )


#     markdown = ""


#     markdown += "## 📅 Today's Study Plan\n\n"


#     markdown += (
#         f"**Total Study Window:** "
#         f"{available_minutes // 60}h "
#         f"{available_minutes % 60}m\n\n"
#     )


#     markdown += (
#         "| Time | Activity | Duration |\n"
#     )

#     markdown += (
#         "|---|---|---|\n"
#     )


#     for session in sessions:

#         start_hour = (
#             current_minutes // 60
#         )

#         start_minute = (
#             current_minutes % 60
#         )


#         end_minutes = (

#             current_minutes
#             + session["duration"]

#         )


#         end_hour = (
#             end_minutes // 60
#         )

#         end_minute = (
#             end_minutes % 60
#         )


#         start_period = (
#             "AM"
#             if start_hour < 12
#             else "PM"
#         )

#         end_period = (
#             "AM"
#             if end_hour < 12
#             else "PM"
#         )


#         display_start_hour = (
#             start_hour % 12
#         )

#         display_end_hour = (
#             end_hour % 12
#         )


#         if display_start_hour == 0:

#             display_start_hour = 12


#         if display_end_hour == 0:

#             display_end_hour = 12


#         start_string = (
#             f"{display_start_hour}:"
#             f"{start_minute:02d} "
#             f"{start_period}"
#         )


#         end_string = (
#             f"{display_end_hour}:"
#             f"{end_minute:02d} "
#             f"{end_period}"
#         )


#         if session["type"].lower() == "break":

#             activity = (
#                 f"☕ **Break** — "
#                 f"{session['topic']}"
#             )

#         else:

#             activity = (
#              f"📚 **{session['subject']}** — "
#                 f"{session['topic']}"
#             )


#         markdown += (

#             f"| {start_string} – {end_string} "
#             f"| {activity} "
#             f"| {session['duration']} min |\n"

#         )


#         current_minutes = end_minutes


#     markdown += "\n"


#     markdown += (
#         "### 💡 Study Tip\n\n"
#         "Stay focused during each session and "
#         "avoid switching subjects unnecessarily. "
#         "Your plan prioritizes subjects based on "
#         "exam urgency, difficulty and remaining syllabus."
#     )


#     return markdown















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