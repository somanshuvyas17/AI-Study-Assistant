# # # # import os
# # # # from datetime import datetime, timedelta

# # # # from google.auth.transport.requests import Request
# # # # from google.oauth2.credentials import Credentials
# # # # from google_auth_oauthlib.flow import InstalledAppFlow
# # # # from googleapiclient.discovery import build


# # # # # ============================================
# # # # # GOOGLE CALENDAR SETTINGS
# # # # # ============================================

# # # # SCOPES = [
# # # #     "https://www.googleapis.com/auth/calendar.events"
# # # # ]

# # # # CREDENTIALS_FILE = "credentials.json"
# # # # TOKEN_FILE = "token.json"


# # # # # ============================================
# # # # # GOOGLE CALENDAR LOGIN
# # # # # ============================================

# # # # def get_calendar_service():

# # # #     credentials = None

# # # #     # Check existing login
# # # #     if os.path.exists(TOKEN_FILE):

# # # #         credentials = Credentials.from_authorized_user_file(
# # # #             TOKEN_FILE,
# # # #             SCOPES
# # # #         )

# # # #     # Refresh expired token
# # # #     if credentials and credentials.expired:

# # # #         if credentials.refresh_token:

# # # #             credentials.refresh(
# # # #                 Request()
# # # #             )

# # # #     # First-time login
# # # #     if not credentials or not credentials.valid:

# # # #         if not os.path.exists(
# # # #             CREDENTIALS_FILE
# # # #         ):

# # # #             raise FileNotFoundError(
# # # #                 "credentials.json not found."
# # # #             )

# # # #         flow = InstalledAppFlow.from_client_secrets_file(
# # # #             CREDENTIALS_FILE,
# # # #             SCOPES
# # # #         )

# # # #         credentials = flow.run_local_server(
# # # #             port=0
# # # #         )

# # # #         # Save login
# # # #         with open(
# # # #             TOKEN_FILE,
# # # #             "w"
# # # #         ) as token:

# # # #             token.write(
# # # #                 credentials.to_json()
# # # #             )

# # # #     service = build(
# # # #         "calendar",
# # # #         "v3",
# # # #         credentials=credentials
# # # #     )

# # # #     return service


# # # # # ============================================
# # # # # ADD STUDY EVENT
# # # # # ============================================

# # # # def add_calendar_event(
# # # #     service,
# # # #     subject,
# # # #     topic,
# # # #     start_datetime,
# # # #     duration_minutes
# # # # ):

# # # #     end_datetime = (
# # # #         start_datetime
# # # #         + timedelta(
# # # #             minutes=duration_minutes
# # # #         )
# # # #     )

# # # #     event = {

# # # #         "summary":
# # # #             f"📚 {subject} - {topic}",

# # # #         "description":
# # # #             "AI Study Assistant generated "
# # # #             "study session.",

# # # #         "start": {

# # # #             "dateTime":
# # # #                 start_datetime.isoformat(),

# # # #             "timeZone":
# # # #                 "Asia/Kolkata"

# # # #         },

# # # #         "end": {

# # # #             "dateTime":
# # # #                 end_datetime.isoformat(),

# # # #             "timeZone":
# # # #                 "Asia/Kolkata"

# # # #         }

# # # #     }

# # # #     created_event = service.events().insert(

# # # #         calendarId="primary",

# # # #         body=event

# # # #     ).execute()

# # # #     return created_event


# # # # # ============================================
# # # # # ADD COMPLETE STUDY PLAN
# # # # # ============================================

# # # # def add_study_plan_to_calendar(
# # # #     plan,
# # # #     study_date,
# # # #     start_time
# # # # ):

# # # #     service = get_calendar_service()

# # # #     current_datetime = datetime.combine(
# # # #         study_date,
# # # #         start_time
# # # #     )

# # # #     created_events = []

# # # #     for item in plan:

# # # #         event = add_calendar_event(

# # # #             service,

# # # #             item["subject"],

# # # #             item["topic"],

# # # #             current_datetime,

# # # #             item["duration"]

# # # #         )

# # # #         created_events.append(
# # # #             event
# # # #         )

# # # #         current_datetime += timedelta(
# # # #             minutes=item["duration"]
# # # #         )

# # # #     return created_events












# # # import os
# # # from datetime import datetime, timedelta

# # # from google.auth.transport.requests import Request
# # # from google.oauth2.credentials import Credentials
# # # from google_auth_oauthlib.flow import InstalledAppFlow
# # # from googleapiclient.discovery import build


# # # SCOPES = [
# # #     "https://www.googleapis.com/auth/calendar.events"
# # # ]

# # # CREDENTIALS_FILE = "credentials.json"
# # # TOKEN_FILE = "token.json"


# # # def get_calendar_service():

# # #     credentials = None

# # #     if os.path.exists(TOKEN_FILE):

# # #         credentials = Credentials.from_authorized_user_file(
# # #             TOKEN_FILE,
# # #             SCOPES
# # #         )

# # #     if credentials and credentials.expired:

# # #         if credentials.refresh_token:

# # #             credentials.refresh(
# # #                 Request()
# # #             )

# # #     if not credentials or not credentials.valid:

# # #         if not os.path.exists(
# # #             CREDENTIALS_FILE
# # #         ):

# # #             raise FileNotFoundError(
# # #                 "credentials.json not found."
# # #             )

# # #         flow = InstalledAppFlow.from_client_secrets_file(
# # #             CREDENTIALS_FILE,
# # #             SCOPES
# # #         )

# # #         credentials = flow.run_local_server(
# # #             port=0
# # #         )

# # #         with open(
# # #             TOKEN_FILE,
# # #             "w"
# # #         ) as token:

# # #             token.write(
# # #                 credentials.to_json()
# # #             )

# # #     service = build(
# # #         "calendar",
# # #         "v3",
# # #         credentials=credentials
# # #     )

# # #     return service


# # # def add_calendar_event(
# # #     service,
# # #     subject,
# # #     topic,
# # #     start_datetime,
# # #     duration_minutes
# # # ):

# # #     end_datetime = (
# # #         start_datetime
# # #         + timedelta(
# # #             minutes=duration_minutes
# # #         )
# # #     )

# # #     event = {

# # #         "summary":
# # #             f"📚 {subject} - {topic}",

# # #         "description":
# # #             "AI Study Assistant generated "
# # #             "study session.",

# # #         "start": {

# # #             "dateTime":
# # #                 start_datetime.isoformat(),

# # #             "timeZone":
# # #                 "Asia/Kolkata"

# # #         },

# # #         "end": {

# # #             "dateTime":
# # #                 end_datetime.isoformat(),

# # #             "timeZone":
# # #                 "Asia/Kolkata"

# # #         }

# # #     }

# # #     created_event = service.events().insert(

# # #         calendarId="primary",

# # #         body=event

# # #     ).execute()

# # #     return created_event


# # # def add_study_plan_to_calendar(
# # #     plan,
# # #     study_date,
# # #     start_time
# # # ):

# # #     service = get_calendar_service()

# # #     current_datetime = datetime.combine(
# # #         study_date,
# # #         start_time
# # #     )

# # #     created_events = []

# # #     for item in plan:

# # #         event = add_calendar_event(

# # #             service,

# # #             item["subject"],

# # #             item["topic"],

# # #             current_datetime,

# # #             item["duration"]

# # #         )

# # #         created_events.append(
# # #             event
# # #         )

# # #         current_datetime += timedelta(
# # #             minutes=item["duration"]
# # #         )

# # #     return created_events


















# # import os
# # import json
# # from datetime import datetime, timedelta

# # import streamlit as st

# # from google.auth.transport.requests import Request
# # from google.oauth2.credentials import Credentials
# # from google_auth_oauthlib.flow import InstalledAppFlow
# # from googleapiclient.discovery import build


# # # ============================================================
# # # GOOGLE CALENDAR
# # # ============================================================

# # SCOPES = [
# #     "https://www.googleapis.com/auth/calendar.events"
# # ]


# # # ============================================================
# # # GET GOOGLE CREDENTIALS
# # # ============================================================

# # def get_credentials():

# #     credentials = None

# #     # --------------------------------------------------------
# #     # OPTION 1: STREAMLIT CLOUD SECRETS
# #     # --------------------------------------------------------

# #     if "GOOGLE_CREDENTIALS" in st.secrets:

# #         credentials_data = st.secrets[
# #             "GOOGLE_CREDENTIALS"
# #         ]

# #         if isinstance(
# #             credentials_data,
# #             str
# #         ):

# #             credentials_data = json.loads(
# #                 credentials_data
# #             )

# #         credentials = Credentials.from_authorized_user_info(
# #             credentials_data,
# #             SCOPES
# #         )

# #         return credentials


# #     # --------------------------------------------------------
# #     # OPTION 2: LOCAL TOKEN
# #     # --------------------------------------------------------

# #     token_file = "token.json"

# #     if os.path.exists(token_file):

# #         credentials = Credentials.from_authorized_user_file(
# #             token_file,
# #             SCOPES
# #         )


# #     # --------------------------------------------------------
# #     # REFRESH TOKEN
# #     # --------------------------------------------------------

# #     if credentials and credentials.expired:

# #         if credentials.refresh_token:

# #             credentials.refresh(
# #                 Request()
# #             )


# #     # --------------------------------------------------------
# #     # LOCAL FIRST-TIME LOGIN
# #     # --------------------------------------------------------

# #     if not credentials or not credentials.valid:

# #         credentials_file = "credentials.json"


# #         if not os.path.exists(
# #             credentials_file
# #         ):

# #             raise FileNotFoundError(
# #                 "Google credentials are not configured. "
# #                 "Add Google credentials to Streamlit Secrets "
# #                 "when deploying."
# #             )


# #         flow = InstalledAppFlow.from_client_secrets_file(

# #             credentials_file,

# #             SCOPES

# #         )


# #         credentials = flow.run_local_server(
# #             port=0
# #         )


# #         # Save locally

# #         with open(
# #             token_file,
# #             "w"
# #         ) as token:

# #             token.write(
# #                 credentials.to_json()
# #             )


# #     return credentials


# # # ============================================================
# # # GET CALENDAR SERVICE
# # # ============================================================

# # def get_calendar_service():

# #     credentials = get_credentials()

# #     service = build(

# #         "calendar",

# #         "v3",

# #         credentials=credentials

# #     )

# #     return service


# # # ============================================================
# # # ADD ONE EVENT
# # # ============================================================

# # def add_calendar_event(

# #     service,

# #     subject,

# #     topic,

# #     start_datetime,

# #     duration_minutes

# # ):

# #     end_datetime = (

# #         start_datetime

# #         + timedelta(
# #             minutes=duration_minutes
# #         )

# #     )


# #     event = {

# #         "summary":
# #             f"📚 {subject} - {topic}",

# #         "description":
# #             "AI Study Assistant generated "
# #             "study session.",

# #         "start": {

# #             "dateTime":
# #                 start_datetime.isoformat(),

# #             "timeZone":
# #                 "Asia/Kolkata"

# #         },

# #         "end": {

# #             "dateTime":
# #                 end_datetime.isoformat(),

# #             "timeZone":
# #                 "Asia/Kolkata"

# #         }

# #     }


# #     created_event = service.events().insert(

# #         calendarId="primary",

# #         body=event

# #     ).execute()


# #     return created_event


# # # ============================================================
# # # ADD COMPLETE STUDY PLAN
# # # ============================================================

# # def add_study_plan_to_calendar(

# #     plan,

# #     study_date,

# #     start_time

# # ):

# #     service = get_calendar_service()


# #     current_datetime = datetime.combine(

# #         study_date,

# #         start_time

# #     )


# #     created_events = []


# #     for item in plan:

# #         event = add_calendar_event(

# #             service,

# #             item["subject"],

# #             item["topic"],

# #             current_datetime,

# #             item["duration"]

# #         )


# #         created_events.append(
# #             event
# #         )


# #         current_datetime += timedelta(

# #             minutes=item["duration"]

# #         )


# #     return created_events





# import os
# import json
# from datetime import datetime, timedelta

# import streamlit as st

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build


# # ============================================================
# # GOOGLE CALENDAR SETTINGS
# # ============================================================

# SCOPES = [
#     "https://www.googleapis.com/auth/calendar.events"
# ]

# TOKEN_FILE = "token.json"
# CREDENTIALS_FILE = "credentials.json"


# # ============================================================
# # GET GOOGLE CREDENTIALS
# # ============================================================

# def get_credentials():

#     credentials = None

#     # ========================================================
#     # OPTION 1 — STREAMLIT CLOUD SECRETS
#     # ========================================================

#     try:

#         if "GOOGLE_CREDENTIALS" in st.secrets:

#             credentials_data = st.secrets[
#                 "GOOGLE_CREDENTIALS"
#             ]

#             # If stored as a JSON string
#             if isinstance(
#                 credentials_data,
#                 str
#             ):

#                 credentials_data = json.loads(
#                     credentials_data
#                 )

#             credentials = (
#                 Credentials.from_authorized_user_info(
#                     credentials_data,
#                     SCOPES
#                 )
#             )

#             # Refresh if necessary
#             if credentials.expired:

#                 if credentials.refresh_token:

#                     credentials.refresh(
#                         Request()
#                     )

#             if credentials.valid:

#                 return credentials

#     except Exception:

#         # No Streamlit secrets locally.
#         # Continue with local authentication.
#         pass


#     # ========================================================
#     # OPTION 2 — LOCAL TOKEN
#     # ========================================================

#     if os.path.exists(
#         TOKEN_FILE
#     ):

#         try:

#             credentials = (
#                 Credentials.from_authorized_user_file(
#                     TOKEN_FILE,
#                     SCOPES
#                 )
#             )

#         except Exception:

#             credentials = None


#     # ========================================================
#     # REFRESH LOCAL TOKEN
#     # ========================================================

#     if credentials:

#         if credentials.expired:

#             if credentials.refresh_token:

#                 try:

#                     credentials.refresh(
#                         Request()
#                     )

#                 except Exception:

#                     credentials = None


#     # ========================================================
#     # IF LOCAL TOKEN IS VALID
#     # ========================================================

#     if credentials and credentials.valid:

#         return credentials


#     # ========================================================
#     # OPTION 3 — FIRST-TIME LOCAL LOGIN
#     # ========================================================

#     if not os.path.exists(
#         CREDENTIALS_FILE
#     ):

#         raise FileNotFoundError(
#             "Google authentication is not configured. "
#             "credentials.json was not found."
#         )


#     # Start Google OAuth
#     flow = InstalledAppFlow.from_client_secrets_file(

#         CREDENTIALS_FILE,

#         SCOPES

#     )


#     credentials = flow.run_local_server(
#         port=0
#     )


#     # Save token locally
#     with open(
#         TOKEN_FILE,
#         "w"
#     ) as token:

#         token.write(
#             credentials.to_json()
#         )


#     return credentials


# # ============================================================
# # GET GOOGLE CALENDAR SERVICE
# # ============================================================

# def get_calendar_service():

#     credentials = get_credentials()

#     service = build(

#         "calendar",

#         "v3",

#         credentials=credentials

#     )

#     return service


# # ============================================================
# # ADD ONE CALENDAR EVENT
# # ============================================================

# def add_calendar_event(

#     service,

#     subject,

#     topic,

#     start_datetime,

#     duration_minutes

# ):

#     end_datetime = (

#         start_datetime

#         + timedelta(
#             minutes=duration_minutes
#         )

#     )


#     # --------------------------------------------------------
#     # EVENT DETAILS
#     # --------------------------------------------------------

#     event = {

#         "summary":
#             f"📚 {subject} - {topic}",

#         "description":
#             "AI Study Assistant generated "
#             "study session.",

#         "start": {

#             "dateTime":
#                 start_datetime.isoformat(),

#             "timeZone":
#                 "Asia/Kolkata"

#         },

#         "end": {

#             "dateTime":
#                 end_datetime.isoformat(),

#             "timeZone":
#                 "Asia/Kolkata"

#         }

#     }


#     # --------------------------------------------------------
#     # CREATE EVENT
#     # --------------------------------------------------------

#     created_event = (

#         service.events()
#         .insert(

#             calendarId="primary",

#             body=event

#         )
#         .execute()

#     )


#     return created_event


# # ============================================================
# # ADD COMPLETE STUDY PLAN TO CALENDAR
# # ============================================================

# def add_study_plan_to_calendar(

#     plan,

#     study_date,

#     start_time

# ):

#     # --------------------------------------------------------
#     # CONNECT TO GOOGLE CALENDAR
#     # --------------------------------------------------------

#     service = get_calendar_service()


#     # --------------------------------------------------------
#     # INITIAL START TIME
#     # --------------------------------------------------------

#     current_datetime = datetime.combine(

#         study_date,

#         start_time

#     )


#     created_events = []


#     # ========================================================
#     # CREATE EVENTS
#     # ========================================================

#     for item in plan:

#         subject = item.get(
#             "subject",
#             "Study"
#         )

#         topic = item.get(
#             "topic",
#             "Study Session"
#         )

#         duration = int(
#             item.get(
#                 "duration",
#                 30
#             )
#         )


#         # ----------------------------------------------------
#         # CREATE EVENT
#         # ----------------------------------------------------

#         event = add_calendar_event(

#             service,

#             subject,

#             topic,

#             current_datetime,

#             duration

#         )


#         created_events.append(
#             event
#         )


#         # ----------------------------------------------------
#         # MOVE TO NEXT SESSION
#         # ----------------------------------------------------

#         current_datetime += timedelta(

#             minutes=duration

#         )


#     return created_events






import os
import json
from datetime import datetime, timedelta

import streamlit as st

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# ============================================================
# GOOGLE CALENDAR SETTINGS
# ============================================================

SCOPES = [
    "https://www.googleapis.com/auth/calendar.events"
]

TOKEN_FILE = "token.json"
CREDENTIALS_FILE = "credentials.json"


# ============================================================
# GET GOOGLE CREDENTIALS
# ============================================================

def get_credentials():

    credentials = None

    # ========================================================
    # OPTION 1 — STREAMLIT CLOUD SECRETS
    # ========================================================

    try:

        if "GOOGLE_CREDENTIALS" in st.secrets:

            credentials_data = st.secrets[
                "GOOGLE_CREDENTIALS"
            ]

            # Streamlit may return the secret as a string
            if isinstance(credentials_data, str):

                credentials_data = json.loads(
                    credentials_data
                )

            credentials = (
                Credentials.from_authorized_user_info(
                    credentials_data,
                    SCOPES
                )
            )

            # Refresh expired credentials
            if credentials.expired:

                if credentials.refresh_token:

                    credentials.refresh(
                        Request()
                    )

            if credentials.valid:

                return credentials

    except Exception:

        # No valid Streamlit secret.
        # Continue with local authentication.
        pass


    # ========================================================
    # OPTION 2 — LOCAL token.json
    # ========================================================

    if os.path.exists(TOKEN_FILE):

        try:

            credentials = (
                Credentials.from_authorized_user_file(
                    TOKEN_FILE,
                    SCOPES
                )
            )

        except Exception:

            credentials = None


    # ========================================================
    # REFRESH LOCAL TOKEN
    # ========================================================

    if credentials:

        if credentials.expired:

            if credentials.refresh_token:

                try:

                    credentials.refresh(
                        Request()
                    )

                except Exception:

                    credentials = None


    # ========================================================
    # VALID LOCAL TOKEN
    # ========================================================

    if credentials and credentials.valid:

        return credentials


    # ========================================================
    # OPTION 3 — LOCAL FIRST-TIME GOOGLE LOGIN
    # ========================================================

    if not os.path.exists(CREDENTIALS_FILE):

        raise FileNotFoundError(
            "Google authentication is not configured. "
            "credentials.json was not found."
        )


    flow = InstalledAppFlow.from_client_secrets_file(

        CREDENTIALS_FILE,

        SCOPES

    )


    credentials = flow.run_local_server(
        port=0
    )


    # Save local token
    with open(
        TOKEN_FILE,
        "w"
    ) as token:

        token.write(
            credentials.to_json()
        )


    return credentials


# ============================================================
# GOOGLE CALENDAR SERVICE
# ============================================================

def get_calendar_service():

    credentials = get_credentials()

    service = build(

        "calendar",

        "v3",

        credentials=credentials

    )

    return service


# ============================================================
# ADD ONE CALENDAR EVENT
# ============================================================

def add_calendar_event(

    service,

    subject,

    topic,

    start_datetime,

    duration_minutes

):

    end_datetime = (

        start_datetime

        + timedelta(
            minutes=duration_minutes
        )

    )


    event = {

        "summary":
            f"📚 {subject} - {topic}",

        "description":
            "Study session created by "
            "AI Study Assistant.",

        "start": {

            "dateTime":
                start_datetime.isoformat(),

            "timeZone":
                "Asia/Kolkata"

        },

        "end": {

            "dateTime":
                end_datetime.isoformat(),

            "timeZone":
                "Asia/Kolkata"

        }

    }


    created_event = (

        service.events()
        .insert(

            calendarId="primary",

            body=event

        )
        .execute()

    )


    return created_event


# ============================================================
# ADD COMPLETE STUDY PLAN
# ============================================================

def add_study_plan_to_calendar(

    plan,

    study_date,

    start_time

):

    # Connect to Google Calendar
    service = get_calendar_service()


    # Initial study time
    current_datetime = datetime.combine(

        study_date,

        start_time

    )


    created_events = []


    # ========================================================
    # CREATE EACH STUDY SESSION
    # ========================================================

    for item in plan:

        subject = item.get(
            "subject",
            "Study"
        )

        topic = item.get(
            "topic",
            "Study Session"
        )

        duration = int(
            item.get(
                "duration",
                30
            )
        )


        # ----------------------------------------------------
        # CREATE EVENT
        # ----------------------------------------------------

        event = add_calendar_event(

            service,

            subject,

            topic,

            current_datetime,

            duration

        )


        created_events.append(
            event
        )


        # ----------------------------------------------------
        # MOVE TO NEXT SESSION
        # ----------------------------------------------------

        current_datetime += timedelta(

            minutes=duration

        )


    return created_events