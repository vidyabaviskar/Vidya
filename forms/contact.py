import re
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_gsheet_client_and_sheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        dict(st.secrets["gcp_service_account"]), scope
    )
    client = gspread.authorize(creds)
    sheet = client.open(st.secrets["gcp_service_account"]["sheet_name"]).sheet1
    return client, sheet

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not name:
                st.error("Please provide your name ")
                st.stop()

            if not email:
                st.error("Please provide your Email ")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide your valid Email Address")
                st.stop()

            if not message:
                st.error("Please write a message")
                st.stop()

            # Use non-cached client and sheet
            _, sheet = get_gsheet_client_and_sheet()
            # sheet.append_row([name, email, message])
            st.success("Your message has been sent successfully!")