# Tech Stack Recommender

An AI-based career recommendation system that recommends suitable career paths based on a user's technical skills.

## Project Overview

This project uses a content-based recommendation approach to match user skills with the skills required for different job roles.

The system uses TF-IDF vectorization and cosine similarity to calculate how closely the user's skills match each career path.

## Objectives

- Take technical skills as user input
- Compare user skills with job-role requirements
- Calculate similarity scores
- Recommend the top 3 matching career paths

## Dataset

The project uses a custom `raw_skills.csv` dataset containing 8 job roles and their required technical skills.

The job roles include:

- Data Scientist
- DevOps Engineer
- Backend Developer
- Cloud Architect
- Machine Learning Engineer
- Data Analyst
- Cybersecurity Analyst
- Full Stack Developer

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## How It Works

1. Load the job-role dataset using Pandas.
2. Accept the user's skills as input.
3. Convert job-role skills into TF-IDF vectors.
4. Convert the user's skills into a TF-IDF vector.
5. Calculate cosine similarity between the user's skills and each job role.
6. Sort the job roles according to their similarity scores.
7. Display the top 3 recommended career paths.

## Example Input

```text
Python, Cloud, Automation