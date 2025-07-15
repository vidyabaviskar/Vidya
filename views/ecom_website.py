import streamlit as st
import streamlit.components.v1 as components

st.title("E-commerce Website: Reego Chairs")

st.subheader("Project Description")
st.write(
    """
    **Reego Chairs** is a modern e-commerce platform for ergonomic office chairs. 
    The website features a clean UI, product catalog, shopping cart, and secure checkout. 
    Built with React and deployed on Vercel, it offers a seamless shopping experience.
    """
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        '<a href="https://reego-chairs.vercel.app/" target="_blank" style="text-decoration: none;">'
        '<button style="font-size: 18px; padding: 10px 24px; border-radius: 8px;">🌐 Live Demo</button>'
        '</a>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<a href="https://github.com/vidyabaviskar/project1" target="_blank" style="text-decoration: none;">'
        '<button style="font-size: 18px; padding: 10px 24px; border-radius: 8px;">💻 GitHub Repository</button>'
        '</a>',
        unsafe_allow_html=True
    )

st.subheader("Live Preview")
components.iframe("https://reego-chairs.vercel.app/", height=600)
