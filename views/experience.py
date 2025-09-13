import streamlit as st

st.title("Experience")

st.markdown("""
<style>
/* Container */
.timeline {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
}

/* The vertical line */
.timeline::after {
  content: '';
  position: absolute;
  width: 6px;
  background-color: #e0e0e0;
  top: 0;
  bottom: 0;
  left: 50%;
  margin-left: -3px;
  border-radius: 6px;
}

/* Timeline items */
.timeline-item {
  padding: 20px 30px;
  position: relative;
  background-color: inherit;
  width: 50%;
}

/* Left items */
.timeline-item.left {
  left: 0;
}

/* Right items */
.timeline-item.right {
  left: 50%;
}

/* Content card */
.timeline-content {
  padding: 20px;
  background-color: #ffffff;
  position: relative;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  color: #70798c;
  font-family: "Segoe UI", sans-serif;
  transition: transform 0.3s ease;
}

.timeline-content:hover {
  transform: translateY(-4px);
}

/* Circles on the line */
.timeline-item::before {
  content: ' ';
  position: absolute;
  top: 20px;
  right: -13px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background-color: #ffffff;
  border: 4px solid #70798c;
  z-index: 1;
}

.timeline-item.right::before {
  left: -13px;
}

/* Headings */
.timeline-content h3 {
  margin-top: 0;
  font-size: 1.4rem;
  color: #333333;
}

.timeline-content h4 {
  margin-top: 4px;
  font-size: 1rem;
  font-weight: 500;
  color: #555555;
}
</style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1 style='text-align:center; margin-bottom:30px;'>💼 Experience Timeline</h1>", unsafe_allow_html=True)

# Timeline structure
st.markdown("""
<div class="timeline">
  
  <div class="timeline-item left">
    <div class="timeline-content">
      <h3>Software Development Intern</h3>
      <h4>ABC Tech Solutions (June 2024 - Aug 2024)</h4>
      <p>🌐 Built REST APIs using FastAPI & PostgreSQL.<br>
         🚀 Optimized backend queries improving performance by 30%.<br>
         🤝 Collaborated with cross-functional teams in Agile sprints.</p>
    </div>
  </div>

  <div class="timeline-item right">
    <div class="timeline-content">
      <h3>AI Research Assistant</h3>
      <h4>XYZ University (Jan 2023 - May 2023)</h4>
      <p>🧠 Worked on NLP-based Fake News Detection models.<br>
         📊 Published research paper in International Journal.<br>
         🔍 Experimented with BERT and LLM fine-tuning.</p>
    </div>
  </div>

  <div class="timeline-item left">
    <div class="timeline-content">
      <h3>Full Stack Developer Intern</h3>
      <h4>Startup Hub (Jul 2022 - Dec 2022)</h4>
      <p>💻 Developed farmer community platform using React & Flask.<br>
         🌍 Integrated multilingual support with Google Translate API.<br>
         📈 Increased engagement by 45% with UX improvements.</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)
