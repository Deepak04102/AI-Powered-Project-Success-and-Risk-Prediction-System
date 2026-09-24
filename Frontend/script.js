const form = document.getElementById("predictionForm");

const loading = document.getElementById("loading");
const result = document.getElementById("result");

const successProbability =
    document.getElementById("successProbability");

const prediction =
    document.getElementById("prediction");

const riskLevel =
    document.getElementById("riskLevel");

const riskFactors =
    document.getElementById("riskFactors");

const recommendations =
    document.getElementById("recommendations");


form.addEventListener("submit", async function(event) {

    event.preventDefault();

    loading.style.display = "block";
    result.style.display = "none";

    // Collect project information
    const projectData = {

        budget: Number(document.getElementById("budget").value),

        planned_duration:
            Number(document.getElementById("planned_duration").value),

        team_size:
            Number(document.getElementById("team_size").value),

        team_experience:
            Number(document.getElementById("team_experience").value),

        requirement_stability:
            Number(document.getElementById("requirement_stability").value),

        previous_similar_projects:
            Number(document.getElementById("previous_similar_projects").value),

        complexity:
            Number(document.getElementById("complexity").value),

        client_involvement:
            Number(document.getElementById("client_involvement").value),

        resource_availability:
            Number(document.getElementById("resource_availability").value)
    };


    try {

        // Send data to Flask backend
        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(projectData)
            }
        );


        const data = await response.json();


        if (!response.ok) {
            throw new Error(data.error || "Prediction failed");
        }


        // Display success probability
        successProbability.textContent =
            data.success_probability;


        // Display prediction
        if (data.success_prediction === 1) {
            prediction.textContent = "Successful Project";
        } else {
            prediction.textContent = "High Risk of Project Failure";
        }


        // Display risk level
        riskLevel.textContent =
            data.risk_level;


        // Clear old risk factors
        riskFactors.innerHTML = "";


        // Add risk factors
        data.risk_factors.forEach(function(factor) {

            const li = document.createElement("li");

            li.textContent = factor;

            riskFactors.appendChild(li);
        });


        // Clear old recommendations
        recommendations.innerHTML = "";


        // Add recommendations
        data.recommendations.forEach(function(recommendation) {

            const li = document.createElement("li");

            li.textContent = recommendation;

            recommendations.appendChild(li);
        });


        // Show result
        result.style.display = "block";

    }

    catch (error) {

        alert("Error: " + error.message);

    }

    finally {

        loading.style.display = "none";

    }

});