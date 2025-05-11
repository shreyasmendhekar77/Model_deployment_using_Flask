# 🏠 Boston House Price Prediction - End-to-End ML Deployment

This project predicts Boston house prices using a Machine Learning model deployed with Flask. It covers the complete lifecycle from training to deploying the model as a web app.

---

## 🚀 Project Overview

- **Model:** Linear Regression
- **Dataset:** Boston Housing Dataset (from `sklearn.datasets`)
- **Framework:** Flask (for deployment)
- **Purpose:** Learn end-to-end ML deployment — including model building, saving, serving with Flask, and running as a web app.

---

## 🛠 Software Requirements

- Python 3.7+
- Git & GitHub
- VSCode (or any IDE)
- Git CLI
- Flask
- pickle (for model serialization)
- HTML/CSS (for basic frontend)

---

## 🧱 Project Structure

```
Boston_House_Price_Prediction/
│
├── static/                 # CSS and image assets
│
├── templates/              # HTML templates
│   └── index.html
│
├── model/                  # Serialized model
│   └── boston_model.pkl
│
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Files/folders to ignore
```

---

## 📦 Installation & Setup

### 🔁 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Boston_House_Price_Prediction.git
cd Boston_House_Price_Prediction
```

### 🐍 2. Create virtual environment and activate

```bash
python -m venv venv
source venv/bin/activate        # For Linux/macOS
venv\Scripts\activate           # For Windows
```

### 📦 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Training

Train the model in a separate script (optional), save it as `boston_model.pkl` using `pickle`.

---

## 🌐 Run the Web App

```bash
python app.py
```

Go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## 📋 Features

- Simple form to input housing attributes (e.g., CRIM, RM, TAX, etc.)
- Predicts and displays the estimated price of a house.
- Lightweight Flask backend.
- Clean and responsive UI.

---

## 📌 Future Enhancements

- Use a more advanced model (e.g., Random Forest, XGBoost)
- Add input validations and model explanation (SHAP/LIME)
- Containerize using Docker and deploy to AWS/Heroku

---

## 🤝 Contribution

Feel free to fork this repo and improve it. PRs are welcome!

---

## 📝 License

This project is licensed under the MIT License.


