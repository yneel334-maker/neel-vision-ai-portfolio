import streamlit as st

st.title("✋ Finger Counter")

st.subheader("Project Overview")

st.write("""
This Computer Vision project detects a hand and counts
the number of raised fingers in real time.
""")

st.markdown("### 🛠️ Technologies Used")

st.write("""
- Python
- OpenCV
- MediaPipe
""")

st.markdown("### ✋ Features")

st.write("""
• Hand detection  
• Finger landmark tracking  
• Automatic finger counting  
• Real-time processing  
• Supports different hand gestures
""")

st.markdown("### ⚙️ Working")

st.write("""
MediaPipe detects the hand landmarks. The program analyzes
the position of the fingers and determines how many fingers
are raised.
""")

st.success("Finger Counter — Project 4")

st.info("🎥 Demo video will be added later.")
