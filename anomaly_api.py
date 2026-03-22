from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("anomaly_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json.get("value")
        value = float(data)

        prediction = model.predict([[value]])[0]
        anomaly = int(prediction == -1)

        return jsonify({
            "value": value,
            "anomaly": anomaly
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)