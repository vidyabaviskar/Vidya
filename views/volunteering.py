import streamlit as st
import base64
from pathlib import Path

def image_to_base64(image_path: Path) -> str:
    """Reads an image file and returns its Base64 encoded string representation."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except FileNotFoundError:
        st.error(f"Image not found at {image_path}. Please check the file path.")
        return ""

ghrhack_img_1_path = Path("assets/ghrhack.jpg")
ghrhack_img_2_path = Path("assets/ghrhack1.jpg")


ghrhack_img_1_b64 = image_to_base64(ghrhack_img_1_path)
ghrhack_img_2_b64 = image_to_base64(ghrhack_img_2_path)

st.markdown(f"""
<div class="custom-card">
    <h1 style="margin-bottom: 12px;">Volunteering</h1>
    <div class="volunteer-item" style="margin-bottom: 2rem;">
        <h3 style="font-size: 1.8rem; text-align: left; color: #70798c;">Student Placement Coordinator</h3>
        <ul style="font-size: 1.1rem; text-align: left; color: #70798c; line-height: 1.6; font-weight: 400; padding-left: 20px; margin-top: 10px;">
           <li>🥇 Identified and shared placement and internship opportunities with students</li>
           <li>🤝 Coordinated between students and recruiters for smooth placement processes</li>
           <li>📅 Organized placement drives, workshops, and training sessions</li>
           <li>📝 Assisted in resume building and interview preparation for students</li>
           <li>💬 Communicated updates and information to students and faculty</li>
        </ul>
    </div>
    <div class="volunteer-item">
        <h3 style="font-size: 1.8rem; text-align: left; color: #70798c;">Overall Coordinator of GHRhack-1.0</h3>
        <ul style="font-size: 1.1rem; text-align: left; color: #70798c; line-height: 1.6; font-weight: 400; padding-left: 20px; margin-top: 10px;">
           <li>🥇 Coordinated with various teams to ensure smooth execution of the hackathon</li>
           <li>🤝 Managed participant registrations and inquiries</li>
           <li>📅 Organized workshops and mentoring sessions for participants</li>
           <li>📝 Assisted in the development of hackathon guidelines and resources</li>
           <li>💬 Communicated updates and information to participants and stakeholders</li>
        </ul>
        <div style="display: flex; gap: 15px; margin-top: 15px;">
            <img src="data:image/jpeg;base64,{ghrhack_img_1_b64}" alt="GHRhack Image 1" style="width: 50%; border-radius: 10px; object-fit: contain;">
            <img src="data:image/jpeg;base64,{ghrhack_img_2_b64}" alt="GHRhack Image 2" style="width: 50%; height: 350px; border-radius: 10px; object-fit: contain;">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

