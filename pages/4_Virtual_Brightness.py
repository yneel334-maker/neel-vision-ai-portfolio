import streamlit as st

st.title("🔆 Virtual Brightness Control")

st.subheader("Project Overview")

st.write("""
This project demonstrates a Virtual Brightness Control system
using hand gestures.

The brightness level can be controlled by changing the
distance between the thumb and index finger.
""")

st.markdown("### 🛠️ Technologies Used")

st.write("""
- Python
- OpenCV
- MediaPipe
- Screen Brightness Control
""")

st.markdown("### ✋ Gesture Controls")

st.write("""
• Thumb + Index Finger Close → Decrease Brightness
• Thumb + Index Finger Far Apart → Increase Brightness
• Hand Tracking → Real-time brightness control
""")

st.markdown("### ⚙️ Working")

st.write("""
The webcam detects the hand and tracks the thumb and index
finger landmarks. Their distance is converted into a
brightness percentage.
""")

st.success("Virtual Brightness Control — Project 3")

st.info("🎥 Demo video will be added later.")
