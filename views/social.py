import streamlit as st

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

st.title("Social Media")

icon_size = "64"  

social_links = [
    {
        "name": "LinkedIn",
        "url": "https://www.linkedin.com/in/vidyabaviskar/",
        "icon": "https://img.icons8.com/color/96/000000/linkedin.png"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/vidyabaviskar",
        "icon": "https://img.icons8.com/color/96/000000/github--v1.png"
    },
    {
        "name": "Instagram",
        "url": "https://www.instagram.com/_vidyabaviskar_/",
        "icon": "https://img.icons8.com/color/96/000000/instagram-new.png"
    },
    {
        "name": "Twitter",
        "url": "https://x.com/vidyabaviskar11",
        "icon": "https://img.icons8.com/color/96/000000/twitter--v1.png"
    }
]

cols = st.columns(len(social_links))
for col, link in zip(cols, social_links):
    col.markdown(
        f'<a href="{link["url"]}" target="_blank">'
        f'<img src="{link["icon"]}" alt="{link["name"]}" width="{icon_size}" style="margin-bottom: 10px;"/>'
        f'</a>',
        unsafe_allow_html=True
    )
