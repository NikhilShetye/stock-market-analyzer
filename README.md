# 📈 AI Stock Analyzer

An end-to-end stock analysis and prediction system built using **Pandas, Machine Learning, and FastAPI**, designed for real-world fintech applications.

---

## 🚀 Features

* 📊 Stock data analysis (max, min, volatility)
* 📉 Daily return calculation
* 📈 Moving average trend detection
* 🤖 ML-based price prediction
* 🌐 REST API for integration (Android-ready)

---

## 🧠 Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn (Linear Regression)
* FastAPI

---

## 📡 API Endpoints

| Endpoint    | Description            |
| ----------- | ---------------------- |
| `/analysis` | Returns stock insights |
| `/predict`  | Predicts next price    |

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📊 Sample Output

```json
{
  "max_close": 2850.5,
  "min_close": 1200.3,
  "avg_close": 2100.7,
  "volatility": 0.018
}
```

---

## 🔮 Prediction Example

```json
{
  "predicted_price": 2750.23
}
```

---

## 📱 Future Scope

* Android app integration
* Real-time stock API
* Advanced ML models (LSTM)

---

## 👨‍💻 Author

Nikhil Shetye
