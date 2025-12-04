# Student-Performance-Analyzer
# 🎓 Student Performance Analyzer
A Machine Learning project that predicts a student's final academic performance based on attendance, assignment scores, and behavior. The system also provides personalized improvement suggestions.

This project uses:
- **Python**
- **Scikit-Learn**
- **Random Forest Regressor**
- **Streamlit (Web UI)**
- **Pickle (Model Deployment)**

---

## ⭐ Features

### 🔍 **1. ML-Based Grade Prediction**
The model predicts a student's final grade using:
- Attendance (%)
- Assignment scores
- Behavior rating

### 🧠 **2. Machine Learning Pipeline**
- Data preprocessing  
- Feature scaling  
- Model training (RandomForestRegressor)  
- Model saving (`model.pkl`)  
- Deployed using Streamlit  

### 🛠 **3. Improvement Suggestions**
The system recommends personalized actions based on student weaknesses.  
Example suggestions:
- Increase attendance  
- Improve assignment performance  
- Enhance classroom behavior  

### 🌐 **4. Streamlit Web App**
A simple user interface where teachers or admins can input student details and instantly view:
- Predicted grade  
- Suggestions  

---

student_performance_analyzer/
│
├── app.py # Streamlit UI
├── train_model.py # Script to train and save the ML model
├── student_data.csv # Training dataset
├── model.pkl # Saved ML model
├── scaler.pkl # Saved StandardScaler
└── README.md # Documentation


---

## 📦 Installation

Install all dependencies:

```bash
pip install -r requirements.txt

requirements.txt

streamlit
pandas
numpy
scikit-learn


🧠 Training the Machine Learning Model

Run the training script:
python train_model.py

This will generate:

model.pkl

scaler.pkl

Both files are required for prediction.

🚀 Running the Streamlit App

Use the command below:
streamlit run app.py

The app will open automatically in your browser at:
http://localhost:8501



## 📁 Project Structure

