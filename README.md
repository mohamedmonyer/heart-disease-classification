# Heart Disease Classification

## Project Overview

This project uses machine learning to classify heart disease data using Logistic Regression and Decision Tree models.

The goal is to practice data preparation, model training, and evaluation using Python and scikit-learn.

## Tools & Libraries

- Python
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn
- joblib

## Project Workflow

1. Load and explore the dataset.
2. Prepare the features and target.
3. Split the data into training and testing sets.
4. Build a Logistic Regression pipeline using StandardScaler.
5. Train and evaluate a Decision Tree model.
6. Compare the models using 5-fold cross-validation.
7. Evaluate the selected model on the test set.
8. Save the trained Logistic Regression pipeline.

## Results

- Test Accuracy: 86.89%
- Test samples: 61
- Logistic Regression achieved better overall cross-validation results than Decision Tree.

## Project Files

- `heart_disease_classification.ipynb`: Data exploration, training, and evaluation.
- `heart.csv`: Dataset used in the project.
- `heart_disease_model.joblib`: Saved trained model pipeline.

## Disclaimer

This is an educational machine learning project. It is not intended for clinical diagnosis or medical decision-making.