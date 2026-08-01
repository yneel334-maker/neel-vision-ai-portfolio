import streamlit as st

st.set_page_config(
    page_title="VisionAI Portfolio",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0F172A,#111827,#1E293B);
}

h1,h2,h3,p{
    color:white;
}

.card{
    background:#1f2937;
    border-radius:20px;
    padding:20px;
    margin:15px;
    box-shadow:0 0 15px rgba(0,255,255,.25);
}

.project{
    background:#111827;
    border-left:5px solid #00E5FF;
    padding:15px;
    margin-top:10px;
    border-radius:15px;
}

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
