import streamlit as st

st.title("🎵 Gesture Media Player")

st.subheader("Project Overview")

st.write("""
This Computer Vision project demonstrates a gesture-controlled
media player.

Hand gestures can be used to perform basic media-control
actions without directly touching the keyboard or mouse.
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
▶️ Play / Pause → Gesture-based action

⏭️ Next Track → Specific hand gesture

⏮️ Previous Track → Specific hand gesture

🔊 Volume → Hand gesture
""")

st.markdown("### ⚙️ Working")

st.write("""
The webcam captures the user's hand. MediaPipe detects
hand landmarks and identifies predefined gestures.
Each recognized gesture is mapped to a media-player action.
""")

st.success("Gesture Media Player — Project 11")

st.info("🎥 Demo video will be added later.")
