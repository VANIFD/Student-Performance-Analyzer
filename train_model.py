import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# -----------------------
# LOAD DATA
# -----------------------
df = pd.read_csv('student_data.csv')

# Example feature names – adjust to your dataset
features = ['attendance', 'assignment_score', 'behavior_score']
target = 'final_grade'

X = df[features]
y = df[target]

# -----------------------
# SCALING (optional)
# -----------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------
# TRAIN MODEL
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# -----------------------
# SAVE MODEL & SCALER
# -----------------------
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

print("Model training completed and saved!")
