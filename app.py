import streamlit as st
import os

st.set_page_config(
    page_title="Neel Yadav | VisionAI Portfolio",
    page_icon="🚀",
    layout="wide"
)

# =========================
# PREMIUM CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #07111f, #101827, #172033);
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    padding: 45px 25px;
    border-radius: 25px;
    text-align: center;
    background: linear-gradient(
        135deg,
        rgba(0, 220, 255, 0.12),
        rgba(120, 70, 255, 0.12)
    );
    border: 1px solid rgba(0, 220, 255, 0.25);
    box-shadow: 0 0 35px rgba(0, 220, 255, 0.08);
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 52px;
    margin-bottom: 5px;
}

.hero h3 {
    font-size: 25px;
}

.card {
    background: rgba(255,255,255,0.06);
    padding: 22px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 15px;
}

.project {
    background: rgba(15,23,42,0.9);
    padding: 18px;
    border-radius: 15px;
    margin: 10px 0;
    border-left: 4px solid #00e5ff;
}

.section-title {
    font-size: 30px;
    font-weight: bold;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# PROJECT DATA
# =========================

projects = [
    ("🖱️", "Virtual Mouse Control",
     "Control the computer mouse using hand gestures.",
     "Python • OpenCV • MediaPipe"),

    ("🔊", "Virtual Volume Control",
     "Control system volume using hand gestures.",
     "Python • OpenCV • MediaPipe"),

    ("💡", "Virtual Brightness Control",
     "Control screen brightness using hand gestures.",
     "Python • OpenCV • MediaPipe"),

    ("✋", "Finger Counter",
     "Detect and count raised fingers using computer vision.",
     "Python • OpenCV • MediaPipe"),

    ("✌️", "Rock Paper Scissors",
     "Play Rock Paper Scissors using hand gestures.",
     "Python • OpenCV • MediaPipe"),

    ("😀", "Face Attendance",
     "Computer vision based face attendance system.",
     "Python • OpenCV • Face Recognition"),

    ("😷", "Face Mask Detection",
     "Detect whether a person is wearing a face mask.",
     "Python • OpenCV • TensorFlow"),

    ("😴", "Drowsiness Detection",
     "Detect possible drowsiness using facial features.",
     "Python • OpenCV • MediaPipe"),

    ("🎨", "Virtual Drawing Board",
     "Draw virtually using hand and finger tracking.",
     "Python • OpenCV • MediaPipe"),

    ("📽️", "Gesture Presentation Control",
     "Control presentation slides using hand gestures.",
     "Python • OpenCV • MediaPipe"),

    ("🎵", "Gesture Media Player",
     "Control media playback using hand gestures.",
     "Python • OpenCV • MediaPipe"),

    ("🤟", "AI Sign Language Recognition",
     "Recognize sign-language gestures using a trained ML model.",
     "Python • Machine Learning • OpenCV • MediaPipe")
]


# =========================
# SIDEBAR
# =========================

st.sidebar.title("🚀 VisionAI Portfolio")
st.sidebar.markdown("---")

st.sidebar.write("👨‍💻 **Neel Yadav**")
st.sidebar.write("Computer Vision & AI Developer")

st.sidebar.markdown("---")

section = st.sidebar.radio(
    "📂 Navigation",
    [
        "🏠 Home",
        "👨‍💻 About",
        "🛠️ Skills",
        "📁 Projects",
        "📄 Resume",
        "🏆 Achievements",
        "📞 Contact"
    ]
)

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Portfolio")
st.sidebar.progress(100)
st.sidebar.success("12 / 12 Projects")

st.sidebar.markdown("---")

st.sidebar.caption(
    "Python • OpenCV • MediaPipe • TensorFlow • Streamlit"
)


# =========================
# HOME
# =========================

if section == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🚀 VisionAI Portfolio</h1>
        <h3>Neel Yadav</h3>
        <p>
        Computer Vision • Artificial Intelligence • Python
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>👋 Welcome</h2>
        <p>
        Welcome to my Computer Vision portfolio.
        This website showcases 12 projects developed during
        my IOFT training using Python, OpenCV, MediaPipe,
        TensorFlow and Streamlit.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📊 Portfolio Statistics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Projects", "12")

    with c2:
        st.metric("Primary Language", "Python")

    with c3:
        st.metric("Framework", "Streamlit")

    with c4:
        st.metric("CV Libraries", "OpenCV + MediaPipe")

    st.divider()

    st.markdown("## ⭐ Featured Projects")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>🖱️ Virtual Mouse Control</h3>
        <p>
        Control the computer mouse using hand gestures
        and real-time hand tracking.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h3>🤟 AI Sign Language Recognition</h3>
        <p>
        Machine-learning based recognition of
        sign-language gestures.
        </p>
        </div>
        """, unsafe_allow_html=True)


# =========================
# ABOUT
# =========================

elif section == "👨‍💻 About":

    st.title("👨‍💻 About Me")

    st.markdown("""
    <div class="card">
    <h2>Neel Yadav</h2>

    <p>
    I am developing my skills in Artificial Intelligence,
    Machine Learning and Computer Vision.
    </p>

    <p>
    This portfolio contains projects created during
    my IOFT training using Python and modern Computer
    Vision technologies.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 My Focus")

    st.write("""
    • Computer Vision

    • Artificial Intelligence

    • Machine Learning

    • Python Development

    • AI-based Applications
    """)


# =========================
# SKILLS
# =========================

elif section == "🛠️ Skills":

    st.title("🛠️ Technical Skills")

    skills = {
        "Python": 95,
        "OpenCV": 90,
        "MediaPipe": 90,
        "Streamlit": 90,
        "TensorFlow": 75,
        "Machine Learning": 75
    }

    for skill, value in skills.items():
        st.write(f"**{skill}**")
        st.progress(value)


# =========================
# PROJECTS
# =========================

elif section == "📁 Projects":

    st.title("📂 Computer Vision Projects")

    search = st.text_input(
        "🔍 Search Project",
        placeholder="Example: Mouse, Face, Gesture..."
    )

    for number, (emoji, name, description, tech) in enumerate(
        projects, 1
    ):

        if search and search.lower() not in name.lower():
            continue

        with st.expander(
            f"Project {number} — {emoji} {name}"
        ):

            st.write(description)

            st.markdown("### 🛠️ Technologies")
            st.info(tech)

            st.success("✅ Project completed")


# =========================
# RESUME
# =========================

elif section == "📄 Resume":

    st.title("📄 My Resume")

    st.markdown("""
    <div class="card">
    <h2>Neel Yadav</h2>
    <p>
    AI • Computer Vision • Python Developer
    </p>
    </div>
    """, unsafe_allow_html=True)

    if os.path.exists("resume.pdf"):

        st.success("✅ Resume available")

        with open("resume.pdf", "rb") as file:

            st.download_button(
                label="📥 Download Resume",
                data=file,
                file_name="Neel_Yadav_Resume.pdf",
                mime="application/pdf"
            )

        st.markdown("### 👀 Resume Preview")

        st.write(
            "Use the Download Resume button above to view your PDF."
        )

    else:

        st.warning(
            "⚠️ Resume PDF has not been uploaded yet."
        )

        st.info(
            "Upload a file named 'resume.pdf' to the GitHub repository."
        )


# =========================
# ACHIEVEMENTS
# =========================

elif section == "🏆 Achievements":

    st.title("🏆 Achievements")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Projects Completed", "12")

    with c2:
        st.metric("Portfolio Completion", "100%")

    with c3:
        st.metric("Computer Vision Projects", "12")

    st.divider()

    st.success(
        "🎓 Computer Vision & AI projects developed during IOFT training."
    )


# =========================
# CONTACT
# =========================

elif section == "📞 Contact":

    st.title("📞 Contact")

    st.markdown("""
    <div class="card">
    <h2>👨‍💻 Neel Yadav</h2>

    <p>
    AI • Computer Vision Developer
    </p>

    <p>
    🎓 Training: IOFT
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "🚀 Thank you for visiting my VisionAI Portfolio!"
    )


# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "© 2026 Neel Yadav | VisionAI Portfolio | "
    "Python • OpenCV • MediaPipe • TensorFlow • Streamlit"
)
