import streamlit as st

st.title("👤 Face Attendance System")

st.subheader("Project Overview")

st.write("""
This Computer Vision project demonstrates an automated
face-recognition-based attendance system.

The system identifies registered faces and records the
attendance of recognized users.
""")

st.markdown("### 🛠️ Technologies Used")

st.write("""
- Python
- OpenCV
- Face Recognition
- NumPy
""")

st.markdown("### ⚙️ Features")

st.write("""
• Face Detection  
• Face Recognition  
• Automatic Attendance  
• Date and Time Recording  
• Multiple Face Support
""")

st.markdown("### 📋 Working")

st.write("""
The camera captures faces and compares them with the
registered face data. When a known person is recognized,
their name and attendance time can be recorded.
""")

st.success("Face Attendance System — Project 6")

st.info("🎥 Demo video will be added later.")
