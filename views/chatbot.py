import streamlit as st
import streamlit.components.v1 as components

st.title("PDF Reader Chatbot")

st.subheader("Project Description")
st.write(
    """
    **PDF Reader Chatbot** is an interactive Streamlit app that allows users to upload PDF documents and ask questions about their content. 
    The app leverages natural language processing to provide accurate answers based on the uploaded PDF. 
    Built with Python and Streamlit, it offers a user-friendly interface for document exploration.
    """
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        '<a href="https://pdf-reader-bot.streamlit.app/" target="_blank" style="text-decoration: none;">'
        '<button style="font-size: 18px; padding: 10px 24px; border-radius: 8px;">🤖 Live Demo</button>'
        '</a>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<a href="https://github.com/vidyabaviskar/streamlit-chatbot" target="_blank" style="text-decoration: none;">'
        '<button style="font-size: 18px; padding: 10px 24px; border-radius: 8px;">💻 GitHub Repository</button>'
        '</a>',
        unsafe_allow_html=True
    )

# st.subheader("Live Preview")
# components.iframe("https://pdf-reader-bot.streamlit.app/", height=600)
