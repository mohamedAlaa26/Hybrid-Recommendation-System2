# **Hybrid Movie Recommendation System**
![Demo Video](https://github.com/HeshamEL-Shreif/Hybrid-Recommendation-System/blob/main/video/video_G.gif)
A client-server movie recommendation application built with PyQt5 for the GUI (client) and a custom hybrid recommender model combining collaborative filtering and content-based filtering on the backend.

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
- PyQt5 GUI for interactive user experience
- Cosine similarity over genre embeddings
- SVD Collaborative Filtering using surprise library
- Modular architecture (separate logic and UI)
- Evaluation metrics included (RMSE, Precision@K, Recall@K)
- Well-documented codebase with design proposal

⸻
## Usage

To run the GUI

python main.py

Make sure the dataset is located in `data/ml-latest-small/` with the following files:
- movies.csv
- ratings.csv
- enres_encoded.csv

⸻

## File Structure
```
.
├── data/
│   └── ml-latest-small/
│       ├── movies.csv
│       ├── ratings.csv
│       └── Genres_encoded.csv
│
├── gui/
│   └── main.py                 # PyQt5 GUI
│
├── recommender/
│   ├── recommender.py          # Recommender logic
│   └── evaluation.py           # Evaluation metrics
│
├── notebook/
│   └── scratch_exploration.ipynb  # EDA and experimentation
│
├── proposal/
│   └── design_proposal.pdf     # Pipeline + Design Proposal
│
├── requirements.txt
├── README.md
└── .gitignore
```
⸻

## Design Proposal
```
+-------------------+
| 1. Data Loading   |
|-------------------|
| - movies.csv      |
| - ratings.csv     |
| - genres_encoded  |
+-------------------+
         |
         v
+----------------------+
| 2. Preprocessing     |
|----------------------|
| - Encode genres      |
| - Build index maps   |
| - Filter users/movies|
+----------------------+
         |
         v
+----------------------------+
| 3. Modeling                |
|----------------------------|
| a) Content-Based Filtering |
|    - Cosine Similarity     |
|    - Genre vectors         |
|                            |
| b) Collaborative Filtering |
|    - SVD (Surprise)        |
|    - User-Movie Matrix     |
+----------------------------+
         |
         v
+--------------------------------+
| 4. Hybrid Recommendation       |
|--------------------------------|
| - Combine scores               |
|   (e.g., 70% content + 30% CF) |
| - Exclude seen movies          |
| - Sort and rank                |
+--------------------------------+
         |
         v
+--------------------------+
| 5. Inference Engine      |
|--------------------------|
| - Accept user input      |
| - Return top-N movies    |
+--------------------------+
         |
         v
+----------------------------+
| 6. GUI (PyQt5 Client)      |
|----------------------------|
| - User selects ID          |
| - Shows rated movies       |
| - Displays recommendations |
+----------------------------+
         |
         v
+---------------------------+
| 7. Evaluation Metrics     |
|---------------------------|
| - RMSE                    |
| - Precision@K             |
| - Recall@K                |
| - NDCG / MAP              |
+---------------------------+
```
