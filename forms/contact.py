import re
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json") 
    firebase_admin.initialize_app(cred)

db = firestore.client()

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

            # Store data in Firestore
            db.collection("contacts").add({
                "name": name,
                "email": email,
                "message": message
            })
            st.success("Your message has been sent successfully!")
            