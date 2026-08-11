import streamlit as st

st.title("🎨 Virtual Drawing Board")

st.subheader("Project Overview")

st.write("""
This Computer Vision project demonstrates a virtual drawing
board controlled using hand gestures.

The user can draw on the screen without touching a physical
surface by moving their finger in front of a camera.
""")

st.markdown("### 🛠️ Technologies Used")

st.write("""
- Python
- OpenCV
- MediaPipe
""")

st.markdown("### 🎯 Features")

st.write("""
• Real-Time Hand Tracking
• Finger Detection
• Air Drawing
• Virtual Canvas
• Gesture-Based Interaction
• Contactless Drawing
""")

st.markdown("### ⚙️ Working")

st.write("""
The webcam detects the user's hand and tracks the index finger.
The movement of the finger is converted into drawing strokes
on a virtual canvas.
""")

st.success("Virtual Drawing Board — Project 9")

st.info("🎥 Demo video will be added later.")
