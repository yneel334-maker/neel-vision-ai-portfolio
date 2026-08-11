import streamlit as st

st.title("🖱️ Virtual Mouse Control")

st.subheader("Project Overview")

st.write("""
This project demonstrates a Virtual Mouse Control system
using hand gestures.

The system uses a webcam to detect hand landmarks and
allows the user to control mouse actions without touching
a physical mouse.
""")

st.markdown("### 🛠️ Technologies Used")
st.write("""
- Python
- OpenCV
- MediaPipe
- PyAutoGUI
""")

st.markdown("### ✋ Gesture Controls")
st.write("""
• Index Finger → Move mouse cursor  
• Index + Thumb Pinch → Left Click  
• Two fingers → Scroll  
""")

st.success("Virtual Mouse Control — Project 1")

st.info("Demo video is not included because the project is being prepared using a mobile devPythonusi.")
