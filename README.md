# 🫀 Heart Failure Prediction System (Personal Learning Project)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-v1.26-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Educational](https://img.shields.io/badge/Educational-SelfLearning-orange)

---

## **Description**

This is a **personal learning project** designed to help me understand how to build a **machine learning predictive model** and deploy it as a web application.
It predicts the **risk of heart failure** using clinical and lifestyle data.

> ⚠️ **Note:** This project is for **self-learning and educational purposes only**. It is **not intended for medical diagnosis or treatment**.

The project uses a **Random Forest Classifier** and a **Streamlit UI** to demonstrate the full ML workflow: preprocessing, training, testing, and deployment.

---

## **Table of Contents**

1. [Features](#features)
2. [Dataset](#dataset)
3. [Installation & Usage](#installation--usage)
4. [Sample Inputs](#sample-inputs)
5. [Risk Factors](#risk-factors)
6. [Technology Stack](#technology-stack)
7. [Contributors](#contributors)
8. [License](#license)
9. [Future Scope](#future-scope)

---

## **Features**

* Predicts **High Risk** or **Low Risk** of heart failure.
* Accepts **user-friendly input fields** (plain language, no medical expertise required).
* Demonstrates **ML workflow**: preprocessing, scaling, training, and prediction.
* Real-time prediction through a **Streamlit web interface**.
* Personal learning project for **practice in ML and deployment**.

---

## **Dataset**

This project uses the **Heart Failure Prediction Dataset** from Kaggle:

➡️ [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/guriya79/heart-failure-prediction-dataset)

**Dataset Features:**

* Age, Sex
* Anaemia, Diabetes, High Blood Pressure
* Ejection Fraction (%)
* Platelets (thousands/mL)
* Serum Creatinine (mg/dL), Serum Sodium (mEq/L)
* Smoking

---

## **Installation & Usage**

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/heart-failure-prediction.git
cd heart-failure-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

### 4. Use the Website/App

* Enter sample health data to see predictions.
* Observe how input features influence the model output.
* Website: [Heart Failure Risk Prediction using Random Forest](https://heart-failure-prediction-using-random-forest-cseb2rlzkv9csuajb.streamlit.app/)

> ⚠️ **Reminder:** This Website/App is for **personal learning only** and **not a real diagnostic tool**.

---

## **Sample Inputs**

### High Risk Example

| Field                    | Value |
| ------------------------ | ----- |
| Age                      | 75    |
| Anaemia                  | Yes   |
| Diabetes                 | Yes   |
| Ejection Fraction (%)    | 25    |
| High Blood Pressure      | Yes   |
| Platelets (thousands/mL) | 220   |
| Serum Creatinine (mg/dL) | 2.2   |
| Serum Sodium (mEq/L)     | 128   |
| Sex                      | Male  |
| Smoking                  | Yes   |

### Low Risk Example

| Field                    | Value |
| ------------------------ | ----- |
| Age                      | 58    |
| Anaemia                  | No    |
| Diabetes                 | No    |
| Ejection Fraction (%)    | 45    |
| High Blood Pressure      | No    |
| Platelets (thousands/mL) | 280   |
| Serum Creatinine (mg/dL) | 1.0   |
| Serum Sodium (mEq/L)     | 138   |
| Sex                      | Male  |
| Smoking                  | No    |

---

## **Risk Factors**

| Factor                                    | High Risk            | Low Risk                                                     |
| ----------------------------------------- | -------------------- | ------------------------------------------------------------ |
| Age                                       | ≥70                  | <60                                                          |
| Heart Pump Efficiency (Ejection Fraction) | <35%                 | 50–70%                                                       |
| Anaemia                                   | Yes                  | No                                                           |
| Diabetes                                  | Yes                  | No                                                           |
| High Blood Pressure                       | Yes                  | No                                                           |
| Kidney Function (Creatinine)              | >1.5 mg/dL           | 0.6–1.3 mg/dL                                                |
| Blood Sodium                              | <133 mEq/L           | 135–145 mEq/L                                                |
| Platelets                                 | Abnormal             | Normal (250–400k/mL)                                         |
| CPK (Enzyme Level)                        | Very High (>600)     | Normal/Moderate (≈180–350)                                   |
| Sex                                       | Male slightly higher | Female slightly lower (estrogen protection, until menopause) |
| Smoking                                   | Yes                  | No                                                           |

> Women have slightly lower risk due to hormonal protection, but risk increases after menopause (~45–55 years).

---

## **Technology Stack**

* **Python** – ML modeling and preprocessing
* **scikit-learn** – Random Forest & scaling
* **Streamlit** – Web interface deployment
* **NumPy & Pandas** – Data handling
* **pickle** – Model serialization

---

## **Contributors**

* Albert Antony S (personal learning project)

---

## **License**

This project is licensed under the **MIT License**.

---

## **Future Scope (Educational Enhancements)**

* Display **risk probability (%)** to learn probability interpretation.
* Add **visualizations** of feature importance to understand model decisions.
* Compare **multiple ML models** (Random Forest, Logistic Regression, XGBoost) for learning model evaluation.
* Expand dataset to practice **advanced ML techniques**.
* Add **graphs/charts** for better visualization of risk factors.

