import streamlit as st

st.markdown('<div class="main-content">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2], gap="large")
with col1:
    st.image("./assets/prof.jpg", width=230)

with col2:
    st.markdown("""
    <div class="custom-card" style="text-align: center;">
        <h1 style="margin-bottom: 12px;">Vidya Baviskar</h1>
        <p style="font-size: 1rem; text-align: center; color: #70798c; line-height: 1; margin-top: 6px; margin-bottom: 10px; font-weight: 400;">
            I don't just write code <br> I build solutions, lead with curiosity, and grow through every bug I fix.
        </p>
        <div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Full Stack Developer</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Problem Solver</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Tech Enthusiast</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="custom-card">
    <h2>🎓 Education</h2>
    <div style="display: grid; gap: 20px;">
        <div style="background: rgba(112, 121, 140, 0.1); padding: 20px; border-radius: 15px; border-left: 4px solid #70798c;">
            <div style="display: flex; justify-content: space-between; align-items: start; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 300px;">
                    <h4 style=" color: #252323; font-size: 1.1rem;">BTech in Computer Science Engineering</h4>
                    <p style=" color: #70798c; font-weight: 500;">G H Raisoni College of Engineering and Technology, Jalgaon</p>
                </div>
                <div style=" min-width: 120px;">
                    <p style="margin-right: 40%; font-weight: 600; color: #252323;">2022-2026</p>
                    <p style="margin: 0; color: #a99985; font-size: 1.1rem; font-weight: 600;">8.2 CGPA</p>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
 <div class="custom-card">
        <h2 style="margin-bottom: 12px;">Technical Skills</h2>
        <div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Python</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">JavaScript</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">HTML</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">CSS</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Github</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Streamlit</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">ReactJs</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Firebase</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">SQL</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Problem Solving</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Gen AI</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Langchain</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">OpenAI</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Hugging Face API</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Vector Database</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">LLM</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Machine Learning</span>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Deep Learning</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-card">
    <h2>💼 Experience</h2>
    <div style="background: linear-gradient(135deg, rgba(112, 121, 140, 0.1) 0%, rgba(169, 153, 133, 0.1) 100%); padding: 25px; border-radius: 20px; border: 1px solid rgba(112, 121, 140, 0.3);">
        <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 15px; flex-wrap: wrap;">
            <div>
                <h3 style="margin: 0; color: #252323; font-size: 1.3rem;">Web Developer</h3>
                <h4 style="margin: 5px 0; color: #70798c; font-weight: 600;">Streamline TechIn</h4>
                <p style="margin: 0; color: #a99985; font-style: italic;">A tech business providing web development services</p>
            </div>
            <span style="background: linear-gradient(45deg, #70798c, #a99985); color: white; padding: 8px 16px; border-radius: 20px; font-size: 0.9rem; font-weight: 500;">Internship</span>
        </div>
        <ul style="color: #70798c; line-height: 1.6; padding-left: 20px; margin: 0;">
            <li>Expanded the backend of a responsive e-commerce website using Node.js and Firebase, including user authentication, product management, and real-time database integration.</li>
            <li>Collaborated with the frontend team, providing API endpoints and assisting with React.js and Tailwind CSS integration.</li>
            <li>Optimized data flow and improved performance to ensure a clean, user-friendly interface across devices.</li>
            <li>Led the deployment and final testing to launch the project successfully.</li>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
