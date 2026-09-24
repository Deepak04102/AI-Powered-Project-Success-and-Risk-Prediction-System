import pandas as pd
import numpy as np

np.random.seed(42)

# Number of projects
n = 1000

# -----------------------------------------
# Generate project features
# -----------------------------------------

df = pd.DataFrame({
    "budget": np.random.randint(100000, 2000000, n),
    "planned_duration": np.random.randint(2, 25, n),
    "team_size": np.random.randint(2, 21, n),
    "team_experience": np.random.randint(1, 16, n),
    "requirement_stability": np.random.randint(1, 11, n),
    "previous_similar_projects": np.random.randint(0, 16, n),
    "complexity": np.random.randint(1, 11, n),
    "client_involvement": np.random.randint(1, 11, n),
    "resource_availability": np.random.randint(1, 11, n)
})

# -----------------------------------------
# Create project risk score
# -----------------------------------------

# Budget adequacy
# More budget generally means lower risk
budget_score = (
    (df["budget"] - 100000) / 1900000
) * 10

# Team experience
experience_score = np.minimum(
    df["team_experience"], 10
)

# Previous similar project experience
previous_score = np.minimum(
    df["previous_similar_projects"], 10
)

# Basic risk factors
risk_score = (
    0.15 * (10 - budget_score)
    + 0.08 * (df["planned_duration"] / 24 * 10)
    + 0.10 * (10 - experience_score)
    + 0.18 * (10 - df["requirement_stability"])
    + 0.10 * (10 - previous_score)
    + 0.20 * df["complexity"]
    + 0.09 * (10 - df["client_involvement"])
    + 0.10 * (10 - df["resource_availability"])
)

# -----------------------------------------
# Important project interactions
# -----------------------------------------

# Large team + high complexity = additional risk
risk_score += np.where(
    (df["team_size"] >= 12) & (df["complexity"] >= 7),
    1.5,
    0
)

# Small team + long project = additional risk
risk_score += np.where(
    (df["team_size"] <= 5) & (df["planned_duration"] >= 18),
    1.5,
    0
)

# Low experience + high complexity = additional risk
risk_score += np.where(
    (df["team_experience"] <= 4) & (df["complexity"] >= 8),
    2.0,
    0
)

# Poor resources + high complexity = additional risk
risk_score += np.where(
    (df["resource_availability"] <= 4) & (df["complexity"] >= 7),
    1.5,
    0
)

# Stable requirements + good resources = lower risk
risk_score -= np.where(
    (df["requirement_stability"] >= 8) &
    (df["resource_availability"] >= 8),
    1.5,
    0
)

# Experienced team + previous similar projects = lower risk
risk_score -= np.where(
    (df["team_experience"] >= 8) &
    (df["previous_similar_projects"] >= 5),
    1.5,
    0
)

# -----------------------------------------
# Add small amount of randomness
# -----------------------------------------

risk_score += np.random.normal(0, 0.5, n)

# -----------------------------------------
# Convert risk into success
# -----------------------------------------

threshold = np.median(risk_score)

df["success"] = (
    risk_score < threshold
).astype(int)

# -----------------------------------------
# Save dataset
# -----------------------------------------

df.to_csv(
    "dataset/projects.csv",
    index=False
)

print("Dataset created successfully!")
print("Number of projects:", len(df))

print("\nFirst 5 rows:")
print(df.head())

print("\nSuccess distribution:")
print(df["success"].value_counts())

print("\nDataset columns:")
print(df.columns.tolist())