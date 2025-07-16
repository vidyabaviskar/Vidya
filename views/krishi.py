import streamlit as st
import streamlit.components.v1 as components

st.title("Krishi Forum: Farmer Web-Based Forum")

st.subheader("Project Description")
st.write(
    """
    **Krishi Forum** is a web-based platform designed for farmers to connect, share knowledge, and seek advice. 
    The forum features AI-powered moderation to ensure a safe and respectful environment, and supports real-time language translation for multilingual communication. 
    Built with modern web technologies, it empowers farmers from diverse backgrounds to collaborate and solve agricultural challenges together.
    """
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        '<a href="https://your-krishi-demo-link.com/" target="_blank" style="text-decoration: none;">'
        '<button style="font-size: 18px; padding: 10px 24px; border-radius: 8px;">🌾 Live Demo</button>'
        '</a>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<a href="https://github.com/yourusername/krishi-forum" target="_blank" style="text-decoration: none;">'
        '<button style="font-size: 18px; padding: 10px 24px; border-radius: 8px;">💻 GitHub Repository</button>'
        '</a>',
        unsafe_allow_html=True
    )


st.subheader("In Progress")
# components.iframe("https://your-krishi-demo-link.com/", height=600)
