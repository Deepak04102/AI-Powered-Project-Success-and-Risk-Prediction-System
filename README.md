# AI-Powered Project Success & Risk Prediction System

An AI/ML-based web application that predicts the **success probability of a project** and identifies potential **project risks before project execution**.

The system uses project-planning factors such as budget, duration, team experience, complexity, requirement stability, client involvement, and resource availability to generate a project success prediction.

---

##  Features

* Predicts whether a project is likely to be successful or unsuccessful
* Provides project success probability
* Classifies project risk as **Low, Medium, or High**
* Identifies potential project risk factors
* Provides recommendations for reducing identified risks
* Uses a Random Forest Machine Learning model
* Provides a Flask REST API
* Includes a web-based user interface
* Uses only pre-project planning information for prediction

---

##  Machine Learning Model

The project uses a **Random Forest Classifier** for project success classification.

### Model Configuration

* Algorithm: Random Forest Classifier
* Number of trees: 200
* Dataset size: 1,000 project records
* Training data: 80%
* Testing data: 20%
* Test Accuracy: **87%**

### Evaluation

| Metric    | Score |
| --------- | ----: |
| Accuracy  |   87% |
| Precision |  ~87% |
| Recall    |  ~87% |
| F1-Score  |  ~87% |

> **Note:** The dataset used in this project is synthetically generated for academic/prototype purposes. The reported accuracy represents performance on this dataset and should not be interpreted as real-world project prediction accuracy.

---

##  Input Features

The model uses 9 project-planning features:

| Feature                   | Description                                     |
| ------------------------- | ----------------------------------------------- |
| Budget                    | Estimated project budget                        |
| Planned Duration          | Expected project duration in months             |
| Team Size                 | Number of team members                          |
| Team Experience           | Relevant team experience in years               |
| Requirement Stability     | Stability of project requirements (1–10)        |
| Previous Similar Projects | Number of previously completed similar projects |
| Complexity                | Project complexity (1–10)                       |
| Client Involvement        | Level of client involvement (1–10)              |
| Resource Availability     | Availability of required resources (1–10)       |

---

##  System Architecture

```text
              User
               │
               ▼
       Web-Based Frontend
        HTML/CSS/JavaScript
               │
               ▼
          Flask REST API
               │
               ▼
        Input Data Processing
               │
               ▼
     Random Forest Classifier
               │
               ▼
       Success Prediction
               │
        ┌──────┴──────┐
        ▼             ▼
 Success Probability  Prediction
        │
        ▼
      Risk Analysis
        │
   ┌────┴─────┐
   ▼          ▼
Risk Factors  Recommendations
```

---

##  Project Structure

```text
AI-Powered-Project-Success-and-Risk-Prediction-System/
│
├── Backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── dataset/
│   └── projects.csv
│
├── model/
│   └── model.pkl
│
├── generate_dataset.py
├── train_model.py
├── test_api.py
└── README.md
```

---

##  Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

### Backend

* Flask
* Flask-CORS
* REST API

### Frontend

* HTML
* CSS
* JavaScript

---

##  Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd AI-Powered-Project-Success-and-Risk-Prediction-System
```

### 3. Install required Python libraries

```bash
pip install pandas numpy scikit-learn joblib flask flask-cors requests
```

---

##  Generate the Dataset

Run:

```bash
python generate_dataset.py
```

This creates the project dataset:

```text
dataset/projects.csv
```

The dataset contains **1,000 synthetic project records**.

---

##  Train the Model

Run:

```bash
python train_model.py
```

The trained Random Forest model will be saved as:

```text
model/model.pkl
```

---
##  Run the Flask Backend

Open a terminal inside the `Backend` folder:

```bash
cd Backend
python app.py
```

The Flask server will run at:

```text
http://127.0.0.1:5000/
```

---

##  API Endpoint

### Prediction API

```text
POST /predict
```

Example request:

```json
{
    "budget": 800000,
    "planned_duration": 10,
    "team_size": 8,
    "team_experience": 7,
    "requirement_stability": 8,
    "previous_similar_projects": 6,
    "complexity": 4,
    "client_involvement": 8,
    "resource_availability": 9
}
```

Example response:

```json
{
    "success_prediction": 1,
    "success_probability": 92.0,
    "risk_level": "Low",
    "risk_factors": [
        "No major risk factors identified"
    ],
    "recommendations": [
        "Continue regular monitoring of project requirements, resources, and team performance."
    ]
}
```

---

##  Test the API

Make sure the Flask server is running and execute:

```bash
python test_api.py
```

The script sends sample project data to the `/predict` endpoint and displays the API response.

---

##  Run the Frontend

Open the `frontend` folder in VS Code and run:

```text
index.html
```

You can use the **Live Server** extension in VS Code.

Make sure the Flask backend is running before submitting the prediction form.

---

##  Risk Analysis

The system checks several project conditions to identify potential risks.

Examples:

* High project complexity
* Unstable requirements
* Low resource availability
* Low team experience
* Limited previous similar-project experience
* Low client involvement
* Long planned duration
* Limited budget

The system then provides recommendations corresponding to the identified risk factors.

---

##  Project Objectives

* Predict project success before project execution
* Identify potential project risks at the planning stage
* Use machine learning for data-driven project assessment
* Estimate project success probability
* Provide actionable risk recommendations
* Provide an easy-to-use web interface

---

##  Future Enhancements

* Use real-world project datasets
* Compare multiple ML algorithms
* Add model explainability and feature importance visualization
* Add project prediction history
* Add database integration
* Improve risk classification using a separately trained risk model
* Deploy the application to a cloud platform
* Develop a React-based frontend
* Add user authentication and project dashboards

---

