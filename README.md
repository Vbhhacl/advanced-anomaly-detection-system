
#  Advanced Anomaly Detection System 

An end-to-end Machine Learning pipeline designed to monitor real-time data streams and flag statistical irregularities. This system integrates a predictive model with a REST API and a simulation dashboard to visualize anomaly detection as it happens.

---

## 🏗️ System Architecture

The project is divided into four core components:

* **Model Trainer (`train_model.py`)**: Script to preprocess data and train the detection algorithm.
* **Inference Engine (`anomaly_api.py`)**: A Flask/FastAPI backend that serves the trained model via REST endpoints.
* **Real-time Simulator (`realtime_simulator.py`)**: A script that generates synthetic data streams to test the model's limits.
* **Web Dashboard**: Located in `templates` and `statics`, providing a visual representation of the data flow and anomaly spikes.

---

## 📈 Real-Time Monitoring Output

The system evaluates incoming values and assigns a classification based on the learned decision boundary.

### Sample Detection Logs:

| Timestamp | Data Value | Status | Label |
| :--- | :--- | :--- | :--- |
| 21:55:06 | -0.7259 | ✅ Normal | `model=0` |
| 21:55:04 | 0.0103 | ✅ Normal | `model=0` |
| 21:55:03 | -5.3221 | 🚨 Anomaly | `model=1` |
| 21:55:02 | 5.4508 | 🚨 Anomaly | `model=1` |

---

## 🚀 Quick Start

### 1. Environment Setup
Clone the repository and initialize a virtual environment:
```
git clone https://github.com/Vbhhacl/advanced-anomaly-detection-system.git
cd advanced-anomaly-detection-system
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Execution
First, ensure the model is trained, then start the API and Simulator:
```
python train_model.py
python anomaly_api.py
python realtime_simulator.py
```

---

## 📂 Project Structure
```
├── statics/             # CSS and JS for the dashboard
├── templates/           # HTML templates
├── anomaly_api.py       # API for model serving
├── anomaly_model.pkl    # Serialized ML model
├── realtime_simulator.py # Data stream generator
├── requirements.txt     # Project dependencies
├── train_model.py       # Model training logic
└── .gitignore           # Version control exclusions
```

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **ML Libraries:** Scikit-Learn, NumPy, Pandas
* **API Framework:** Flask / FastAPI
* **Frontend:** HTML5, CSS3, JavaScript

---

**Author:** [Vbhhacl](https://github.com/Vbhhacl)
