import streamlit as st

st.title("✊✋✌️ Rock Paper Scissors")

st.subheader("Project Overview")

st.write("""
This Computer Vision project recognizes hand gestures
for Rock, Paper and Scissors.

The system uses a camera and hand tracking to identify
the user's gesture and compare it with the computer's choice.
""")

st.markdown("### 🛠️ Technologies Used")

st.write("""
- Python
- OpenCV
- MediaPipe
- Random
""")

st.markdown("### ✋ Gestures")

st.write("""
🪨 Rock → Closed Fist

📄 Paper → Open Palm

✂️ Scissors → Two Fingers
""")

st.markdown("### ⚙️ Working")

st.write("""
The webcam captures the user's hand.
MediaPipe detects hand landmarks and the program analyzes
the finger positions to determine whether the gesture is
Rock, Paper or Scissors.
""")

st.success("Rock Paper Scissors — Project 5")

st.info("🎥 Demo video will be added later.")
