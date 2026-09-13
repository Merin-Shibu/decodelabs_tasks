import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the job-role dataset
data = pd.read_csv("raw_skills.csv")

print("Dataset loaded successfully!")
print("Number of job roles:", len(data))
print("\nJob roles:")
print(data["job_role"].to_string(index=False))
print("\nSkills for each job role:")
print(data[["job_role", "skills"]].to_string(index=False))
# Get user's skills
user_input = input("\nEnter your skills (comma-separated): ")

print("\nYour skills:", user_input)
# Convert job-role skills into TF-IDF vectors
vectorizer = TfidfVectorizer()

skill_vectors = vectorizer.fit_transform(data["skills"])

# Convert user's skills into a TF-IDF vector
user_vector = vectorizer.transform([user_input])

# Calculate similarity between user skills and job roles
similarity_scores = cosine_similarity(user_vector, skill_vectors)[0]

# Add similarity scores to the dataset
data["similarity"] = similarity_scores

# Sort job roles by similarity score
recommendations = data.sort_values(
    by="similarity",
    ascending=False
)

# Display the top 3 recommendations
print("\nTop 3 Recommended Career Paths:")
print("-" * 40)

for rank, (_, row) in enumerate(
    recommendations.head(3).iterrows(), start=1
):
    print(
        f"{rank}. {row['job_role']} - "
        f"{row['similarity'] * 100:.2f}% match"
    )

print("-" * 40)