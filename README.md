# ❤️ Heart Disease Classification

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://heart-disease-classification-9mre5jwjbhstri7xg2tejf.streamlit.app/)

An educational Machine Learning project that uses Logistic Regression to classify heart disease data. The project covers data preparation, model training, evaluation, cross-validation, and deployment using Streamlit.

## 🚀 Live Demo

**Try the application:** [Heart Disease Classification App](https://heart-disease-classification-9mre5jwjbhstri7xg2tejf.streamlit.app/)

## 🎯 Project Objectives

- Explore and prepare a dataset for machine learning.
- Train a Logistic Regression classification model.
- Compare Logistic Regression with a Decision Tree.
- Evaluate model performance using classification metrics.
- Apply 5-fold cross-validation.
- Deploy an interactive application using Streamlit.

## 🛠️ Tools and Technologies

- Python
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

## ⚙️ Project Workflow

1. Load and explore the dataset.
2. Separate features (`X`) from the target (`y`).
3. Split the data into training and testing sets.
4. Build a Logistic Regression pipeline using `StandardScaler`.
5. Train and evaluate the classification model.
6. Evaluate performance using a confusion matrix, precision, recall, and F1-score.
7. Compare Logistic Regression and Decision Tree using 5-fold cross-validation.
8. Save the trained pipeline using Joblib.
9. Build and deploy an interactive Streamlit application.

## 📊 Model Results

### Logistic Regression — Test Set

| Metric | Result |
|---|---:|
| Accuracy | 86.89% |
| Test samples | 61 |

### 5-Fold Cross-Validation

| Metric | Logistic Regression | Decision Tree |
|---|---:|---:|
| Accuracy | 83.80% | 79.30% |
| Precision | 82.10% | 82.90% |
| Recall | 90.10% | 79.50% |
| F1-score | 85.70% | 80.40% |

Logistic Regression achieved better overall cross-validation results in this experiment, particularly in recall and F1-score.

## 📁 Repository Structure

- `heart_disease_classification.ipynb` — Data exploration, model training, and evaluation.
- `heart_disease_data.csv` — Dataset used in the project.
- `heart_disease_model.joblib` — Saved Logistic Regression pipeline.
- `app.py` — Streamlit application.
- `requirements.txt` — Python dependencies.
- `.gitignore` — Files excluded from version control.

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/mohamedmonyer/heart-disease-classification.git
cd heart-disease-classification
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## ⚠️ Disclaimer

This project is for educational and learning purposes only. It is not a medical diagnostic tool and must not be used to make medical decisions. Model predictions are not a substitute for professional medical advice.

## 👨‍💻 Author

**Mohamed Monyer**

- [GitHub Repository](https://github.com/mohamedmonyer/heart-disease-classification)
- [Live Streamlit Application](https://heart-disease-classification-9mre5jwjbhstri7xg2tejf.streamlit.app/)

