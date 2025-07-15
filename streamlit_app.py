import streamlit as st
# import pathlib

# def load_css(file_path):
#     with open(file_path) as f:
#         st.html(f"<style>{f.read()}</style>")

# css_path = pathlib.Path("assests/styles.css")
# load_css(css_path)


# -----✅ Define Pages (with emojis instead of :material icons:)
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



# -----✅ NAVIGATION WITH SECTIONS
pg = st.navigation({
    "Info": [about_page, achievements_page, volunteering_page, contact_page],
    "Projects": [project_1_page, project_2_page, project_3_page],
})

# -----✅ Sidebar Brand
st.logo("assests/prof_pic.png")  # NOTE: Fixed typo "assests" → "assets"
st.sidebar.text("✨ Made with love by Vidya ✨")

# -----✅ Render selected page
pg.run()
