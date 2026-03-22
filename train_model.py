import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

# Generate normal data
data = np.random.normal(0, 1, 1000).reshape(-1, 1)

# Train model
model = IsolationForest(contamination=0.1)
model.fit(data)

# Save model
joblib.dump(model, "anomaly_model.pkl")

print("✅ Model trained and saved!")