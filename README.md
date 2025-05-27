# **Hybrid Movie Recommendation System**
![Demo Video](https://github.com/HeshamEL-Shreif/Hybrid-Recommendation-System/blob/main/video/video_G.gif)


A client-server movie recommendation application built with PyQt5 for the GUI (client) and a custom hybrid recommender model combining collaborative filtering and content-based filtering on the backend.
the backend is fully containerized using Docker to ensure portability and ease of deployment.
----

## **Project Description**

This project is a hybrid movie recommender system that integrates collaborative filtering (SVD from Surprise) and content-based filtering (genre embeddings + cosine similarity). Users interact with a graphical interface built using PyQt5, select a user ID, and receive movie recommendations. The system is designed with modularity in mind and emphasizes clean code structure, reproducibility, and evaluation.

----

## **Pipeline Overview**

```text
|--> Data Loading
    |--> Movies.csv
    |--> Ratings.csv
    |--> Genres_encoded.csv
|
|--> Preprocessing
    |--> Encode genres
    |--> Filter users and movies
|
|--> Model Building
    |--> Content-based Similarity Matrix
    |--> Collaborative Filtering using SVD
    |--> Weighted Hybrid Model
|
|--> Inference
    |--> User selects highly-rated movies
    |--> Predict hybrid scores for unseen movies
    |--> Rank and recommend
|
|--> Evaluation (offline)
    |--> RMSE, Precision@K, Recall@K, MAP, NDCG
|
|--> GUI Interface
    |--> PyQt5 GUI for movie recommendations
```
⸻

## Features
- Hybrid recommender (Content-Based + Collaborative Filtering)
- SVD Collaborative Filtering using surprise library
- Modular architecture (separate logic and UI)

⸻
## Usage

To run the GUI

python main.py

Make sure the dataset is located in `data/ml-latest-small/` with the following files:
- movies.csv
- ratings.csv
- enres_encoded.csv

⸻
Docker Image
The Docker image is publicly available on Docker Hub:

docker pull mohamedalaa72/movie-backend2

⸻
Deployment
The containerized application has been successfully deployed on Claw.cloud. You can now access the movie recommendation system remotely without any setup.

✅ Dockerized for consistent environments across platforms

🌐 Deployed on Claw.cloud for public access and demonstration

📦 Includes all necessary dependencies specified in requirements.txt

