import streamlit as st

st.title("🔊 Virtual Volume Control")

st.subheader("Project Overview")

st.write("""
This project demonstrates a Virtual Volume Control system
using hand gestures.

The user can control the volume by changing the distance
between the thumb and index finger.
""")

st.markdown("### 🛠️ Technologies Used")
st.write("""
- Python
- OpenCV
- MediaPipe
- PyCaw
""")

st.markdown("### ✋ Gesture Control")

st.write("""
• Thumb + Index Finger Close → Decrease Volume
• Thumb + Index Finger Far → Increase Volume
• Hand Gesture → Real-time volume control
""")

st.success("Virtual Volume Control — Project 2")

st.info("Demo video is not included because the project is being prepared using a mobile device.")
