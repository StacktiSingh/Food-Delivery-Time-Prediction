# 🚀 Smart Food Delivery Time Prediction System

A full-stack Machine Learning web application that predicts food delivery time based on real-world logistics, traffic, weather, and rider conditions.

This project includes:
- End-to-end ML pipeline
- High-performance Random Forest model
- Flask backend
- Modern Tailwind CSS frontend
- Animated delivery-time prediction popup

---

## 📌 Features

- ✅ Predicts food delivery time in minutes
- ✅ Uses real operational data & feature engineering
- ✅ Random Forest model with **R² ≈ 0.83**
- ✅ Flask-based backend API
- ✅ Tailwind CSS dark UI
- ✅ Popup meter animation with blur effect
- ✅ Dropdown-based categorical inputs
- ✅ Auto date feature generation
- ✅ Ready for production deployment

---

## 🧠 Machine Learning Model

- Algorithm: **Random Forest Regressor**
- Evaluation Metrics:
  - **MAE ≈ 3 minutes**
  - **R² ≈ 0.83**
- Features Used:
  - Distance
  - Traffic density
  - Weather
  - Pickup delay
  - Delivery rider conditions
  - Order time & date features
  - City & vehicle type

---

## 🖥 Tech Stack

- **Frontend:** HTML + Tailwind CSS
- **Backend:** Flask (Python)
- **ML Framework:** scikit-learn
- **Data Handling:** Pandas, NumPy
- **Model Storage:** Joblib

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repo
```bash
git clone https://github.com/StacktiSingh/Food-Delivery-Time-Prediction.git
cd your-repo-name

Install dependencies: pip install -r requirements.txt
Run the Flask app : python main.py
Open in browser : http://127.0.0.1:5000/
