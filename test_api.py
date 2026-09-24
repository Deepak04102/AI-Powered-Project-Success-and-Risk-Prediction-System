import requests

url = "http://127.0.0.1:5000/predict"

project = {
    "budget": 80000,
    "planned_duration": 10,
    "team_size": 8,
    "team_experience": 7,
    "requirement_stability": 8,
    "previous_similar_projects": 6,
    "complexity": 4,
    "client_involvement": 8,
    "resource_availability": 9
}

project = {
    "budget": 450000,
    "planned_duration": 14,
    "team_size": 5,
    "team_experience": 5,
    "requirement_stability": 5,
    "previous_similar_projects": 3,
    "complexity": 6,
    "client_involvement": 5,
    "resource_availability": 5
}

project = {
    "budget": 200000,
    "planned_duration": 20,
    "team_size": 3,
    "team_experience": 2,
    "requirement_stability": 3,
    "previous_similar_projects": 1,
    "complexity": 9,
    "client_involvement": 3,
    "resource_availability": 2
}

response = requests.post(url, json=project)

print("Status Code:", response.status_code)
print("Prediction:")
print(response.json())