import streamlit as st

st.title("🖥️ Gesture Presentation Control")

st.subheader("Project Overview")

st.write("""
This Computer Vision project allows users to control
presentation slides using hand gestures.

The system detects predefined hand gestures and maps them
to presentation actions such as next slide and previous slide.
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
👉 Right Hand Gesture → Next Slide

👈 Left Hand Gesture → Previous Slide

✋ Open Palm → Presentation Control

✊ Specific Gesture → Additional Action
""")

st.markdown("### ⚙️ Working")

st.write("""
The webcam captures the user's hand. MediaPipe detects
hand landmarks and the program identifies the gesture.
The corresponding keyboard or mouse action is then
performed automatically.
""")

st.success("Gesture Presentation Control — Project 10")

st.info("🎥 Demo video will be added later.")
