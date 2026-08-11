import streamlit as st

st.title("😷 Face Mask Detection")

st.subheader("Project Overview")

st.write("""
This Computer Vision project detects whether a person
is wearing a face mask or not.

The system uses image processing and machine learning
techniques to classify the detected face.
""")

st.markdown("### 🛠️ Technologies Used")

st.write("""
- Python
- OpenCV
- TensorFlow / Keras
- NumPy
""")

st.markdown("### 🎯 Features")

st.write("""
• Face Detection
• Mask Detection
• No-Mask Detection
• Real-Time Processing
• AI-Based Classification
""")

st.markdown("### ⚙️ Working")

st.write("""
The camera captures the person's face. The face region is
processed by the trained classification model, which predicts
whether the person is wearing a mask or not.
""")

st.success("Face Mask Detection — Project 7")

st.info("🎥 Demo video will be added later.")
