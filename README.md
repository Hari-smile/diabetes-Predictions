# diabetes-Predictions
A Machine Learning project that predicts whether a patient is diabetic using multiple classification algorithms, hyperparameter tuning, and model evaluation metrics. Built with Python and Scikit-learn
This project predicts whether a person is diabetic based on medical attributes using Machine Learning algorithms. Multiple classification models were trained, compared, and evaluated using different performance metrics. The best-performing model was selected and deployed for prediction.

The dataset contains medical information of patients such as:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

**Target Variable**

- Outcome
  - 0 → Non-Diabetic
  - 1 → Diabetic

## 📊 Data Preprocessing

- Checked missing values
- Performed Exploratory Data Analysis (EDA)
- Feature Selection
- Train-Test Split
- Feature Scaling (where required)

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)

---

## ⚙ Hyperparameter Tuning

To improve model performance:

- GridSearchCV
- RandomizedSearchCV

were used to optimize model parameters.

---

## 📈 Evaluation Metrics

The models were evaluated using:

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

## 🎯 Best Model

The best-performing model was selected based on the evaluation metrics and used for final predictions.
