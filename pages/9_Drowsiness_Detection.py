import streamlit as st

st.title("😴 Drowsiness Detection")

st.subheader("Project Overview")

st.write("""
This Computer Vision project detects signs of drowsiness
by analyzing facial features, especially the eyes.

The system can be useful for monitoring driver alertness
and generating an alert when prolonged eye closure is detected.
""")

st.markdown("### 🛠️ Technologies Used")

st.write("""
- Python
- OpenCV
- MediaPipe
- Computer Vision
""")

st.markdown("### 🎯 Features")

st.write("""
• Face Detection
• Eye Detection
• Eye Closure Analysis
• Drowsiness Detection
• Real-Time Monitoring
• Alert System
""")

st.markdown("### ⚙️ Working")

st.write("""
The camera captures the user's face and tracks facial
landmarks around the eyes. The system analyzes eye closure
over time and identifies possible signs of drowsiness.
""")

st.success("Drowsiness Detection — Project 8")

st.info("🎥 Demo video will be added later.")
