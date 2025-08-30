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

kavach_img_1_path = Path("assets/kavach.jpg")
kavach_img_2_path = Path("assets/kavach1.jpg")
agnethon_img_1_path = Path("assets/agnethon.jpg")
agnethon_img_2_path = Path("assets/agnethon1.jpg")
udyamotsav_img_1_path = Path("assets/udyamotsav.jpg")

kavach_img_1_b64 = image_to_base64(kavach_img_1_path)
kavach_img_2_b64 = image_to_base64(kavach_img_2_path)
agnethon_img_1_b64 = image_to_base64(agnethon_img_1_path)
agnethon_img_2_b64 = image_to_base64(agnethon_img_2_path)
udyamotsav_img_1_b64 = image_to_base64(udyamotsav_img_1_path)

st.markdown(f"""
<div class="custom-card">
        <h1 style="margin-bottom: 12px;">Achievements</h1>
        <!-- Achievement 1: Kavach Hackathon -->
        <div class="achievement-item" style="margin-bottom: 2rem;">
            <h3 style="font-size: 1.8rem; text-align: left; color: #70798c;">Finalist of Kavach Hackathon 2022</h3>
            <ul style="font-size: 1.1rem; text-align: left; color: #70798c; line-height: 1.6; font-weight: 400; padding-left: 20px; margin-top: 10px;">
                <li>🥇 Top 5 finalist in National Level Hackathon 2023 for developing an innovative Fake News Detection System</li>
                <li>💡 Innovative solution to build SDK for the detection of fake news</li>
                <li>⏱️ 36 hours of coding and 6 hours of presentation</li>
                <li>📜 Awarded with a certificate of excellence</li>
            </ul>
            <div style="display: flex; gap: 15px; margin-top: 2rem;">
                <img src="data:image/jpeg;base64,{kavach_img_1_b64}" alt="Kavach Hackathon Image 1" style="width: 50%; border-radius: 20px; object-fit: contain;">
                <img src="data:image/jpeg;base64,{kavach_img_2_b64}" alt="Kavach Hackathon Image 2" style="width: 50%; height:350px; border-radius: 20px; object-fit: contain;">
            </div> 
        </div>
        <!-- Achievement 2: Udyamotsav -->
        <div class="achievement-item" style="margin-bottom: 2rem;">
            <h3 style="font-size: 1.8rem; text-align: left; color: #70798c;">Finalist of Udyamotsav 2025</h3>
            <ul style="font-size: 1.1rem; text-align: left; color: #70798c; line-height: 1.6; font-weight: 400; padding-left: 20px; margin-top: 10px;">
                <li>🎤 National Level Pitching Round 2025 for pitching an innovative Advance Drug Inventory and Supply Chain Management System</li>
                <li>🗃️ Innovative solution to build a web application for the management of drug inventory and supply chain</li>
                <li>📜 Awarded with a certificate of excellence</li>
            </ul>
            <div style="display: flex; gap: 15px; margin-top: 2rem;">
                <img src="data:image/jpeg;base64,{udyamotsav_img_1_b64}" alt="Udyamotsav Image 1" style="width: 50%; height: 350px; border-radius: 20px; object-fit: contain;">
            </div>
        </div>
        <!-- Achievement 3: Agnethon Hackathon -->
        <div class="achievement-item">
            <h3 style="font-size: 1.8rem; text-align: left; color: #70798c;">Finalist of Agnethon Hackathon 2025</h3>
            <ul style="font-size: 1.1rem; text-align: left; color: #70798c; line-height: 1.6; font-weight: 400; padding-left: 20px; margin-top: 10px;">
                <li>🏅 Secured 6th place in National Level Hackathon 2024 for developing an innovative Committee Permission Management System</li>
                <li>💻 Innovative solution to build a web application for the management of committee permissions</li>
                <li>⏱️ 36 hours of coding</li>
                <li>📜 Awarded with a certificate of excellence</li>
            </ul>
            <div style="display: flex; gap: 15px; margin-top: 2rem;">
                <img src="data:image/jpeg;base64,{agnethon_img_1_b64}" alt="Agnethon Image 1" style="width: 50%; border-radius: 20px; object-fit: contain;">
                <img src="data:image/jpeg;base64,{agnethon_img_2_b64}" alt="Agnethon Image 2" style="width: 50%; height:350px; border-radius: 20px; object-fit: contain;">
            </div>
        </div>
</div>
""", unsafe_allow_html=True)
