import streamlit as st

st.title("🤟 AI Sign Language Recognition")

st.subheader("Project Overview")

st.write("""
This project uses Machine Learning and Computer Vision
to recognize hand signs from a sign-language dataset.

The model is trained on labeled sign-language data and
predicts the corresponding sign from a new input.
""")

st.markdown("### 🧠 AI / ML Pipeline")

st.write("""
1. 📂 Collect Sign Language Dataset
2. 🧹 Data Preprocessing
3. 🔢 Feature Extraction
4. ✂️ Train-Test Split
5. 🧠 Model Training
6. 📊 Model Evaluation
7. 🤟 Sign Prediction
""")

st.markdown("### 🛠️ Technologies Used")

st.write("""
- Python
- Pandas
- NumPy
- Scikit-learn
- OpenCV
- MediaPipe
- Streamlit
""")

st.markdown("### 📊 Dataset")

st.info("""
The model will be trained using a labeled sign-language
dataset. Each sample contains input features and its
corresponding sign/gesture label.
""")

st.markdown("### 🧠 Machine Learning Model")

st.write("""
The dataset will be evaluated and an appropriate
classification algorithm will be selected based on
performance and accuracy.
""")

st.markdown("### 🎯 Expected Output")

st.write("""
Input → Hand Sign

AI Model → Prediction

Output → Recognized Sign
""")

st.success("AI Sign Language Recognition — Project 12")

st.info("📌 Dataset-based model training and prediction module will be added.")
