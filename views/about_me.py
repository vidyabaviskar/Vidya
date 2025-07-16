import streamlit as st


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assests/prof_pic.png", width=230)
with col2:
    st.title("Vidya Baviskar", anchor=False)
    st.write(
        "I don’t just write code — I build solutions, lead with curiosity, and grow through every bug I fix."
    )
    # if st.button("Contact Me "):
    #     show_contact_form()

column1, column2, column3 = st.columns([3, 2, 1], gap="medium", vertical_alignment="center")
with column1:
    st.subheader("Education", anchor=False)
    st.markdown(
        "- **BTech in CSE** from G H Raisoni College of Engineering and Technology, Jalgaon \n"
        "- **HSC** from Moolji Jetha College, Jalgaon \n"
        "- **SSC** from New English Medium School, Jalgaon"
    )

with column2:
    st.markdown(
        "- 2022-2026 \n - 2020-2022 \n - 2018-2020"
    )
   

with column3:
    st.markdown(
        "- 8.2 CGPA \n - 69% \n - 91.42%"
    )


st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Programming Languages: Python, JavaScript \n
    - Database:  MongoDB, SQL, Firebase \n
    - Frameworks and Libraries:  Flask, Django, Node.js, Vite,  React, Tailwind CSS, Streamlit \n
    - Tools: Git, GitHub, VS Code, Vercel, Cnava \n
    """
)


st.write("\n")
st.subheader("Internships", anchor=False)
st.write(
    """
    Web Developer - Streamline TechIn \n
    A tech business that provides web development services  
    - Expanded the backend of a responsive e-commerce website using Node.js and Firebase, including user 
    authentication, product management, and real-time database integration. 
    - Collaborated with the frontend team, providing API endpoints and helping with React.js and Tailwind CSS 
    integration.  
    - Optimized data flow and improved performance to ensure a clean, user-friendly interface across devices. 
    - Led the deployment and final testing to launch the project successfully.
    """
)
