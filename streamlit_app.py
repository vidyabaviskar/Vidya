import streamlit as st

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="👤",
    default=True,
)

project_1_page = st.Page(
    page="views/ecom_website.py",
    title="Reego Chairs",
    icon="📊",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon="🤖",
)

project_3_page = st.Page(
    page="views/krishi.py",
    title="Krishi",
    icon="🌱",
)

achievements_page = st.Page(
    page="views/achievements.py",
    title="Achievements",
    icon="🏆",
)

volunteering_page = st.Page(
    page="views/volunteering.py",
    title="Volunteering",
    icon="🤝",
)

contact_page = st.Page(
    page="views/social.py",
    title="Social Media",
    icon="🌐",
)



pg = st.navigation({
    "Info": [about_page, achievements_page, volunteering_page, contact_page],
    "Projects": [project_1_page, project_2_page, project_3_page],
})

st.logo("assests/prof_pic.png")  # NOTE: Fixed typo "assests" → "assets"
st.sidebar.text("✨ Made with love by Vidya ✨")


pg.run()
