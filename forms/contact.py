import re
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None

def contact_form():
    st.markdown("""
    <style>
        div[data-testid="stForm"] {
            border: 1px solid rgba(255, 255, 255, 0.2);
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 2rem;
        }
        
        div[data-testid="stForm"] h2 {
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        st.markdown("<h2>📨 Get In Touch</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input(
                "First Name *", 
                placeholder="Enter your first name",
                help="Please provide your first name"
            )
        
        with col2:
            email = st.text_input(
                "Email Address *", 
                placeholder="your.email@example.com",
                help="We'll use this to get back to you"
            )
        
        message = st.text_area(
            "Your Message *", 
            placeholder="Tell me about your project, ideas, or just say hello!",
            height=100,
            help="Share your thoughts, project details, or any questions you have"
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submit_button = st.form_submit_button(
                "Send Message 🚀",
                use_container_width=True
            )

        if submit_button:
            if not name or len(name.strip()) < 2:
                st.error("🚫 Please provide a valid name (at least 2 characters)")
                st.stop()
                
            if not email:
                st.error("🚫 Please provide your email address")
                st.stop()
                
            if not is_valid_email(email):
                st.error("🚫 Please provide a valid email address (e.g., name@example.com)")
                st.stop()
                
            if not message or len(message.strip()) < 10:
                st.error("🚫 Please write a message (at least 10 characters)")
                st.stop()

            with st.spinner('Sending your message...'):
                try:
                    scope = [
                        "https://www.googleapis.com/auth/spreadsheets",
                        "https://www.googleapis.com/auth/drive"
                    ]
                    
                    creds_dict = dict(st.secrets["gcp_service_account"])
                    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
                    client = gspread.authorize(creds)
                    
                    sheet_name = st.secrets["gcp_service_account"]["sheet_name"]
                    sheet = client.open(sheet_name).sheet1
                    
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    sheet.append_row([name.strip(), email.strip(), message.strip(), timestamp])
                    
                    st.success("🎉 Thank you! Your message has been sent successfully!")
                    st.snow()

                    st.markdown("""
                    <div style="text-align: center; margin: 20px 0; padding: 20px; background: rgba(112, 121, 140, 0.1); border-radius: 15px; border-left: 4px solid #70798c;">
                        <p style="margin: 0; color: #70798c; font-weight: 500;">
                            ✅ I'll get back to you within 24 hours!
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                except KeyError as e:
                    st.error("❌ Configuration error: Missing credentials. Please contact the administrator.")
                    st.error(f"Missing key: {e}")
                    
                except gspread.SpreadsheetNotFound:
                    st.error("❌ Google Sheet not found. Please check the sheet name in configuration.")
                    
                except gspread.exceptions.APIError as e:
                    st.error("❌ Google Sheets API error. Please try again later.")
                    st.error(f"API Error: {e}")
                    
                except Exception as e:
                    st.error("❌ An unexpected error occurred. Please try again later.")
                    if st.secrets.get("debug_mode", False):
                        st.error(f"Debug info: {str(e)}")
