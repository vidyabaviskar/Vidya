import streamlit as st
import time
import os

os.environ["STREAMLIT_WATCHDOG"] = "false"
# Page configuration
st.set_page_config(
    page_title="Vidya Baviskar - Portfolio",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Root variables */
    :root {
        --primary-bg: #fdf0d5;
        --secondary-bg: #dad2bc;
        --accent-color: #003049;
        --text-color: #003049;
        --card-bg: rgba(218, 210, 188, 0.3);
        --border-color: #780000;
        --hover-color: #a99985;
        --gradient-1: linear-gradient(135deg, #fdf0d5 0%, #dad2bc 100%);
        --gradient-2: linear-gradient(45deg, #780000, #a99985);
        --shadow: 0 8px 32px rgba(37, 35, 35, 0.1);
        --shadow-hover: 0 12px 40px rgba(37, 35, 35, 0.15);
    }
    
    /* Global styles */
    .stApp {
        background: var(--gradient-1);
        font-family: 'Inter', sans-serif;
    }
    
    /* Custom loader */
    .loader-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: var(--primary-bg);
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        animation: fadeOut 0.5s ease-in-out 1.5s forwards;
    }
    
    .loader {
        position: relative;
        width: 60px;
        height: 60px;
    }
    
    .loader::before,
    .loader::after {
        content: '';
        position: absolute;
        border-radius: 50%;
        animation: pulse 1s ease-in-out infinite;
    }
    
    .loader::before {
        width: 60px;
        height: 60px;
        background: var(--gradient-2);
        animation: scale 1s ease-in-out infinite;
    }
    
    .loader::after {
        width: 60px;
        height: 60px;
        background: var(--primary-bg);
        top: 10px;
        left: 10px;
        animation: scale 1s ease-in-out infinite reverse;
    }
    
    @keyframes scale {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.2); opacity: 0.7; }
    }
    
    @keyframes fadeOut {
        to { opacity: 0; visibility: hidden; }
    }
    
    /* Enhanced sidebar */
    
    .sidebar .sidebar-content {
        padding: 2rem 1rem;
    }
    
    /* Sidebar navigation styling */
    .stSelectbox > div > div {
        border: 2px solid var(--border-color) !important;
        border-radius: 15px !important;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        box-shadow: var(--shadow-hover);
        transform: translateY(-2px);
    }
    
    /* Main content container */
    .main-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
        animation: slideIn 0.4s ease-out;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Enhanced cards */
    .custom-card {
        background: var(--card-bg);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(112, 121, 140, 0.2);
        border-radius: 20px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: var(--shadow);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .custom-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(112, 121, 140, 0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.4s;
        opacity: 0;
    }
    
    .custom-card:hover {
        transform: translateY(-8px);
        box-shadow: var(--shadow-hover);
    }
    
    .custom-card:hover::before {
        animation: shimmer 0.4s ease-in-out;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); opacity: 0; }
    }
    
    /* Typography */
    h1, h2, h3 {
        color: var(--text-color) !important;
        font-weight: 600;
        background: var(--gradient-2);
        -webkit-background-clip: text;
        # -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem !important;
    }
    
    h1 {
        font-size: 3rem !important;
        animation: slideInFromTop 1s ease-out;
    }
    
    h2 {
        font-size: 2rem !important;
        animation: slideInFromLeft 0.4s ease-out;
    }
    
    @keyframes slideInFromTop {
        from { opacity: 0; transform: translateY(-50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideInFromLeft {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    /* Enhanced buttons */
    .stButton > button {
        background: var(--gradient-2) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: var(--shadow) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: var(--shadow-hover) !important;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    /* Image styling */
    .profile-image {
        border-radius: 50%;
        border: 4px solid var(--border-color);
        box-shadow: var(--shadow);
        transition: all 0.3s ease;
        animation: float 3s ease-in-out infinite;
    }
    
    .profile-image:hover {
        transform: scale(1.05);
        box-shadow: var(--shadow-hover);
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }   
    
    /* Error and success messages */
    .stAlert {
        border-radius: 15px !important;
        border: none !important;
        animation: slideInFromRight 0.5s ease-out;
    }
    
    @keyframes slideInFromRight {
        from { opacity: 0; transform: translateX(30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    /* Links */
    a {
        color: var(--border-color) !important;
        text-decoration: none !important;
        transition: all 0.3s ease !important;
    }
    
    a:hover {
        color: var(--hover-color) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-content {
            padding: 1rem;
        }
        
        h1 {
            font-size: 2rem !important;
        }
        
        .custom-card {
            padding: 1.5rem;
            margin: 0.5rem 0;
        }
    }
    
    /* Sidebar logo enhancement */
    .css-1v0mbdj img {
        border-radius: 50%;
        border: 3px solid rgba(245, 241, 237, 0.8);
        box-shadow: 0 4px 20px rgba(37, 35, 35, 0.2);
        transition: all 0.3s ease;
    }
    
    .css-1v0mbdj img:hover {
        transform: scale(1.1) rotate(5deg);
    }
    
    /* Sidebar text enhancement */
    .sidebar .sidebar-content .element-container {
        animation: fadeInUp 1s ease-out;
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    
    <!-- Loader HTML -->
    <div class="loader-container" id="loader">
        <div class="loader"></div>
    </div>
    
    <script>
    setTimeout(function() {
        document.getElementById('loader').style.display = 'none';
    }, 3000);
    </script>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Add a small delay to show the loader
time.sleep(0.1)

# Page definitions
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="👤",
    default=True,
)

certificates_page = st.Page(
    page="views/certificates.py",
    title="Certificates",
    icon="🎓",
)

projects_page = st.Page(
    page="views/projects.py",
    title="Projects",
    icon="💼",
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

social_page = st.Page(
    page="views/social.py",
    title="Contact Me",
    icon="🌐",
)

services_page = st.Page(
    page="views/services.py",
    title="Services",
    icon="🛠️",
)

contact_page = st.Page(
    page="forms/contact.py",
    title="Contact Form",
    icon="📞",
)

# Navigation
pg = st.navigation({
    "🌟 Personal": [about_page, achievements_page, volunteering_page, projects_page, certificates_page, social_page],
    "💼 Professional": [services_page],
})

# Enhanced sidebar
st.logo("assets/prof.jpg")
st.sidebar.markdown("""
<div style='text-align: center; background-color: #003049; color: #f5f1ed; padding: 20px; border-radius: 15px; margin: 10px 0;'>
    <p style='font-size: 16px; font-weight: 500; margin: 0;'>
        ✨ Crafted with passion by Vidya ✨
    </p>
    <p style='font-size: 12px; color: #f5f1ed; opacity: 0.8; margin: 5px 0 0 0;'>
        Building the future, one line of code at a time
    </p>
</div>
""", unsafe_allow_html=True)

# Run the navigation
pg.run()
