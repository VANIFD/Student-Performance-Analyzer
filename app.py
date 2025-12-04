import streamlit as st
import pickle
import numpy as np

# Load model & scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


# Suggestion system
def suggest_improvements(attendance, assignment_score, behavior_score):
    suggestions = []

    if attendance < 75:
        suggestions.append("📌 Increase attendance to above 80% for better understanding.")

    if assignment_score < 50:
        suggestions.append("📘 Work on assignments regularly and revise old topics.")

    if behavior_score < 3:
        suggestions.append("🤝 Improve class behavior and participate actively.")

    if not suggestions:
        suggestions.append("🎉 Excellent performance! Keep it up!")

    return suggestions


# Streamlit UI
st.title("🎓 Student Performance Analyzer")
st.subheader("Predict student performance and get personalized suggestions.")

# Input fields
attendance = st.slider("Attendance (%)", 0, 100, 75)
assignment_score = st.slider("Assignment Score (0–100)", 0, 100, 60)
behavior_score = st.slider("Behavior Score (1–5)", 1, 5, 4)

if st.button("Predict Performance"):
    # Convert inputs into array
    input_data = np.array([[attendance, assignment_score, behavior_score]])

    # Scale inputs
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]

    st.success(f"📊 **Predicted Final Grade: {prediction:.2f}**")

    # Show suggestions
    st.write("### 🔧 Suggested Improvements:")
    suggestions = suggest_improvements(attendance, assignment_score, behavior_score)

    for s in suggestions:
        st.write("- " + s)
