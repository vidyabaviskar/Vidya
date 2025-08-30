
# Vidya -🌐Portfolio Website

An interactive personal portfolio website built with Streamlit and Python, designed to showcase my skills, projects, and achievements. The portfolio features a custom contact form integrated with Google Sheets API for data storage, and is deployed seamlessly on Streamlit Cloud.


## Tech Stack

**Client & Framework:** Streamlit, HTML/CSS

**Server:** Python

**Database:** Google Sheets (via Google Sheets API + Service Account)

**Deployment**: Streamlit Cloud


## ✨ Features

- 🎨 Modern UI/UX: Custom CSS with animations, transitions, and responsive design.
- 📬 Contact Form: Users can send messages directly through the website with validation and error handling.
- 💾 Google Sheets Integration: Stores form submissions securely in Google Sheets using the Google Sheets API.
- 🖼️ Image Encoding: Optimized image storage and rendering for faster load times.
- 🚀 Deployed on Streamlit Cloud: Accessible anytime, anywhere with smooth performance.
## Project Structure

```bash
  ├── streamlit_app.py                # Main Streamlit app
  ├── forms/                # Contact form component
  ├── assets/               # Images and media
  ├── views/               # Pages
  ├── .streamlit/
  │   └── config.toml       # Theme and UI settings
  │   └── secrets.toml       # Secrets of Project 
  └── README.md             # Project documentation
  
```
## Installation

1. Clone this repository

```bash
  git clone https://github.com/vidyabaviskar/Vidya.git
  cd Vidya
```
2. Create a virtual environment & install dependencies
```bash
  pip install -r requirements.txt
```

3. Add your Google Service Account credentials in .streamlit/secrets.toml:

```bash
[gcp_service_account]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----YOUR-KEY-----END PRIVATE KEY-----\n"
client_email = "your-service-account-email"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account"
sheet_name = "your-google-sheet-name"
```
4. Run the Streamlit app locally
```bash
streamlit run streamli_app.py
```

## Deployment

The project is deployed on Streamlit Cloud. Simply push your repository and link it to Streamlit for automatic deployment.


👉 Live Demo: https://vidya-baviskar.streamlit.app/


