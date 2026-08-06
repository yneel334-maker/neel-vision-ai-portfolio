import streamlit as st

st.set_page_config(
    page_title="VisionAI Portfolio",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#111827,#1e293b);
color:white;
}

h1,h2,h3,h4,h5,p{
color:white;
}

.hero{
padding:35px;
border-radius:20px;
background:rgba(255,255,255,0.08);
backdrop-filter:blur(10px);
text-align:center;
margin-bottom:20px;
}

.card{
background:#1f2937;
padding:20px;
border-radius:18px;
margin:10px;
border:1px solid #334155;
}

.project{
background:#111827;
padding:15px;
border-radius:15px;
margin-top:12px;
border-left:5px solid cyan;
}

</style>
""",unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1>🚀 VisionAI Portfolio</h1>
<h3>Neel Yadav</h3>
<p>Python | OpenCV | MediaPipe | TensorFlow | Streamlit</p>
</div>
""",unsafe_allow_html=True)

st.header("👨‍💻 About Me")

st.write("""
I am currently pursuing Computer Vision and AI training at IOFT.
This portfolio showcases my 12 Python projects developed using
OpenCV, MediaPipe and Streamlit.
""")

st.divider()

st.header("🛠 Skills")

st.write("Python")
st.progress(90)

st.write("OpenCV")
st.progress(90)

st.write("MediaPipe")
st.progress(85)

st.write("TensorFlow")
st.progress(70)

st.write("Streamlit")
st.progress(95)

st.divider()

st.header("📂 AI Projects")

projects=[
"🖱 Virtual Mouse Control",
"🔊 Virtual Volume Control",
"💡 Virtual Brightness Control",
"✋ Finger Counter",
"✌ Rock Paper Scissors",
"😀 Face Attendance",
"😷 Face Mask Detection",
"😴 Drowsiness Detection",
"🎨 Virtual Drawing Board",
"📽 Gesture Presentation Control",
"🎵 Gesture Media Player",
"🤟 AI Sign Language Recognition"
]

for i,p in enumerate(projects,1):
    with st.expander(f"Project {i} - {p}"):
        st.write("### Description")
        st.write("Project description will be added here.")

        st.write("### Technologies")
        st.code("""
Python
OpenCV
MediaPipe
Streamlit
""")

        st.info("Output images and code will be added later.")
</style>
""",unsafe_allow_html=True)

st.title("🚀 VisionAI Portfolio")

st.subheader("Neel Yadav")

st.write("### Python • OpenCV • MediaPipe • TensorFlow")

st.divider()

st.markdown(
"""
<div class='card'>

## 👋 Welcome

This portfolio contains 12 Computer Vision projects developed using Python.

</div>
""",
unsafe_allow_html=True
)

st.header("📂 Projects")

projects=[
"🖱 Virtual Mouse Control",
"🔊 Virtual Volume Control",
"💡 Virtual Brightness Control",
"✋ Finger Counter",
"✌ Rock Paper Scissors",
"😀 Face Attendance",
"😷 Face Mask Detection",
"😴 Drowsiness Detection",
"🎨 Virtual Drawing Board",
"📽 Gesture Presentation Control",
"🎵 Gesture Media Player",
"🤟 AI Sign Language Recognition"
]

for p in projects:
    st.markdown(
        f"<div class='project'>{p}</div>",
        unsafe_allow_html=True
    )
st.divider()

st.header("📊 Portfolio Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Projects", "12")

with col2:
    st.metric("Languages", "Python")

with col3:
    st.metric("Framework", "Streamlit")

with col4:
    st.metric("Libraries", "OpenCV + MediaPipe")

st.divider()

st.header("🔍 Search Project")

search = st.text_input("Search your project")

if search:
    for project in projects:
        if search.lower() in project.lower():
            st.success(project)

st.divider()

st.header("⭐ Featured Projects")

feature1, feature2 = st.columns(2)

with feature1:
    st.markdown("""
### 🖱 Virtual Mouse Control

Control your mouse using hand gestures.

**Technology**
- Python
- OpenCV
- MediaPipe

Status: ✅ Completed
""")

with feature2:
    st.markdown("""
### 😷 Face Mask Detection

Detect whether a person is wearing a mask.

**Technology**
- Python
- OpenCV
- TensorFlow

Status: ✅ Completed
""")

st.divider()

st.header("📞 Contact")

st.info("""
👨‍💻 Neel Yadav

AI • Computer Vision Developer

Training : IOFT
""")

st.caption("© 2026 Neel Yadav | VisionAI Portfolio")
# ==========================
# PART 3 - PROJECT GALLERY
# ==========================

st.divider()

st.header("🏆 Project Gallery")

for i, project in enumerate(projects, start=1):
    with st.container():
        st.markdown(f"## {i}. {project}")

        col1, col2 = st.columns([2,1])

        with col1:
            st.write("""
This Computer Vision project is developed using Python,
OpenCV and MediaPipe.

Features:
- Real-time Detection
- AI Based Processing
- Easy to Use
- High Accuracy
            """)

        with col2:
            st.info("📷 Output Image\n(Coming Soon)")

        with st.expander("💻 View Python Code"):
            st.code("""
# Python Code
# This project's source code
# will be added here.
""",language="python")

        st.success("Status : Ready")
        st.divider()

# ==========================
# ACHIEVEMENTS
# ==========================

st.header("🏅 Achievements")

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Projects",12)

with c2:
    st.metric("Python",100)

with c3:
    st.metric("Completion","100%")

st.divider()

# ==========================
# FOOTER
# ==========================

st.markdown("""
---
<center>

### 🚀 VisionAI Portfolio

Developed by **Neel Yadav**

Python • OpenCV • MediaPipe • Streamlit

© 2026 All Rights Reserved

</center>
""",unsafe_allow_html=True)
# ==========================================
# PART 4 - PREMIUM SIDEBAR & FINAL SECTION
# ==========================================

st.sidebar.title("🚀 VisionAI Portfolio")
st.sidebar.markdown("---")

st.sidebar.success("👨‍💻 Developer")
st.sidebar.write("Neel Yadav")

st.sidebar.markdown("---")

st.sidebar.subheader("📂 Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "🏠 Home",
        "👨‍💻 About",
        "🛠 Skills",
        "📁 Projects",
        "🏆 Achievements",
        "📞 Contact"
    ]
)

st.sidebar.markdown("---")

st.sidebar.subheader("📈 Portfolio Progress")

st.sidebar.progress(100)

st.sidebar.success("12 / 12 Projects")

st.sidebar.markdown("---")

st.sidebar.info("""
Technology Used

✅ Python

✅ OpenCV

✅ MediaPipe

✅ Streamlit

✅ TensorFlow
""")

st.sidebar.markdown("---")

st.header("⭐ Why This Portfolio?")

st.write("""
This portfolio showcases all my Computer Vision projects
developed during my IOFT training.

Every project is built using modern AI technologies
like OpenCV, MediaPipe, TensorFlow and Streamlit.
""")

st.divider()

st.header("🎯 Future Improvements")

future = [
"✅ Add Output Images",
"✅ Add Project Source Code",
"✅ Add Demo Videos",
"✅ Download Project Button",
"✅ GitHub Integration",
"✅ Responsive Design",
"✅ Dark/Light Mode"
]

for item in future:
    st.write(item)

st.divider()

st.balloons()

st.success("🎉 Thank you for visiting my VisionAI Portfolio!")