from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("../model/model.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "AI Project Success and Risk Prediction API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get project data
        data = request.get_json()

        # Create input dataframe
        input_data = pd.DataFrame([{
            "budget": data["budget"],
            "planned_duration": data["planned_duration"],
            "team_size": data["team_size"],
            "team_experience": data["team_experience"],
            "requirement_stability": data["requirement_stability"],
            "previous_similar_projects": data["previous_similar_projects"],
            "complexity": data["complexity"],
            "client_involvement": data["client_involvement"],
            "resource_availability": data["resource_availability"]
        }])

        # -----------------------------
        # ML Prediction
        # -----------------------------

        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]

        success_probability = probabilities[1] * 100

        # -----------------------------
        # Risk Level
        # -----------------------------

        if success_probability >= 70:
            risk_level = "Low"
        elif success_probability >= 40:
            risk_level = "Medium"
        else:
            risk_level = "High"

        # -----------------------------
        # Prediction Label
        # -----------------------------

        if prediction == 1:
            prediction_label = "Project Likely to Succeed"
        else:
            prediction_label = "High Risk of Project Failure"

        # -----------------------------
        # Identify Risk Factors
        # -----------------------------

        risk_factors = []
        recommendations = []

        if data["complexity"] >= 8:
            risk_factors.append("Very high project complexity")
            recommendations.append(
                "Break the project into smaller manageable modules."
            )
        elif data["complexity"] >= 6:
            risk_factors.append("Moderate project complexity")
            recommendations.append(
                "Create clear milestones and monitor complex tasks closely."
            )

        if data["requirement_stability"] <= 4:
            risk_factors.append("Unstable project requirements")
            recommendations.append(
                "Finalize and document requirements before development."
            )
        elif data["requirement_stability"] <= 6:
            risk_factors.append("Moderately stable project requirements")
            recommendations.append(
                "Review requirements regularly to minimize changes."
            )

        if data["resource_availability"] <= 4:
            risk_factors.append("Low resource availability")
            recommendations.append(
                "Ensure required technical and human resources are available."
            )
        elif data["resource_availability"] <= 6:
            risk_factors.append("Moderate resource availability")
            recommendations.append(
                "Monitor resource allocation and address shortages early."
            )

        if data["team_experience"] <= 4:
            risk_factors.append("Low team experience")
            recommendations.append(
                "Assign experienced team members or provide additional training."
            )
        elif data["team_experience"] <= 6:
            risk_factors.append("Moderate team experience")
            recommendations.append(
                "Provide mentoring and technical guidance to the team."
            )

        if data["previous_similar_projects"] <= 2:
            risk_factors.append("Limited previous similar project experience")
            recommendations.append(
                "Study similar projects and use proven project practices."
            )
        elif data["previous_similar_projects"] <= 4:
            risk_factors.append("Limited experience with similar projects")
            recommendations.append(
                "Review lessons learned from similar projects."
            )

        if data["client_involvement"] <= 4:
            risk_factors.append("Low client involvement")
            recommendations.append(
                "Maintain regular communication with the client."
            )
        elif data["client_involvement"] <= 6:
            risk_factors.append("Moderate client involvement")
            recommendations.append(
                "Increase client communication and progress reviews."
            )

        if data["planned_duration"] >= 18:
            risk_factors.append("Long planned project duration")
            recommendations.append(
                "Divide the project into milestones and monitor progress regularly."
            )
        elif data["planned_duration"] >= 12:
            risk_factors.append("Moderately long project duration")
            recommendations.append(
                "Use milestone-based planning to keep the project on schedule."
            )

        if data["team_size"] <= 4 and data["planned_duration"] >= 12:
            risk_factors.append(
                "Small team for a long-duration project"
            )
            recommendations.append(
                "Consider increasing the team size or allocating additional resources."
            )

        if data["budget"] <= 300000:
            risk_factors.append("Limited project budget")
            recommendations.append(
                "Review the budget and prioritize important requirements."
            )
        elif data["budget"] <= 500000:
            risk_factors.append("Moderate project budget")
            recommendations.append(
                "Monitor project expenses carefully."
            )

        # ML-based risk
        if success_probability < 50:
            risk_factors.append(
                "ML model indicates high project failure risk"
            )
            recommendations.append(
                "Review project planning, resources, requirements, and team capability."
            )
        elif success_probability < 70:
            risk_factors.append(
                "ML model indicates moderate project success probability"
            )
            recommendations.append(
                "Closely monitor key project factors and address risks early."
            )

        # Default messages
        if not risk_factors:
            risk_factors.append(
                "No significant risk factors identified"
            )

        if not recommendations:
            recommendations.append(
                "Continue regular monitoring of project requirements, resources, and team performance."
            )

        # -----------------------------
        # Return Result
        # -----------------------------

        return jsonify({
            "success_prediction": int(prediction),
            "prediction_label": prediction_label,
            "success_probability": round(success_probability, 2),
            "risk_level": risk_level,
            "risk_factors": risk_factors,
            "recommendations": recommendations
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)