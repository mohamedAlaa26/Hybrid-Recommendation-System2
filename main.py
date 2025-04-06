# main.py
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QComboBox, QPushButton, QListWidget,
                             QLabel, QGroupBox, QSpinBox, QListWidgetItem)
from PyQt5.QtCore import Qt, QTimer
from rec_engine.inference import HybridRecommender

class MovieRecommenderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadData()

    def initUI(self):
        self.setWindowTitle('Hybrid Movie Recommendation System')
        self.setGeometry(100, 100, 900, 600)

        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        user_group = QGroupBox("Select User")
        user_layout = QHBoxLayout()
        self.user_combo = QComboBox()
        self.show_button = QPushButton("Show Rated Movies")
        self.show_button.clicked.connect(self.showUserMovies)
        user_layout.addWidget(QLabel("User ID:"))
        user_layout.addWidget(self.user_combo)
        user_layout.addWidget(self.show_button)
        user_group.setLayout(user_layout)

        recommend_group = QGroupBox("Recommendation Settings")
        recommend_layout = QHBoxLayout()
        self.num_recommendations = QSpinBox()
        self.num_recommendations.setMinimum(1)
        self.num_recommendations.setMaximum(30)
        self.num_recommendations.setValue(5)
        self.recommend_button = QPushButton("Get Recommendations")
        self.recommend_button.clicked.connect(self.getRecommendations)
        recommend_layout.addWidget(QLabel("Number of recommendations:"))
        recommend_layout.addWidget(self.num_recommendations)
        recommend_layout.addWidget(self.recommend_button)
        recommend_group.setLayout(recommend_layout)

        display_group = QGroupBox("Movies")
        display_layout = QHBoxLayout()
        self.user_movies_list = QListWidget()
        self.recommended_list = QListWidget()

        user_box = QVBoxLayout()
        user_box.addWidget(QLabel("User Rated Movies (≥4.0):"))
        user_box.addWidget(self.user_movies_list)

        recommend_box = QVBoxLayout()
        recommend_box.addWidget(QLabel("Recommended Movies:"))
        recommend_box.addWidget(self.recommended_list)

        display_layout.addLayout(user_box)
        display_layout.addLayout(recommend_box)
        display_group.setLayout(display_layout)

        main_layout.addWidget(user_group)
        main_layout.addWidget(recommend_group)
        main_layout.addWidget(display_group)
        self.setCentralWidget(central_widget)

    def loadData(self):
        self.recommender = HybridRecommender(
            "data/ml-latest-small/movies.csv",
            "data/ml-latest-small/ratings.csv",
            "data/ml-latest-small/Genres_encoded.csv"
        )
        self.user_combo.addItems([str(uid) for uid in self.recommender.get_users()])

    def showUserMovies(self):
        self.user_movies_list.clear()
        self.recommended_list.clear()

        user_id = int(self.user_combo.currentText())
        user_ratings = self.recommender.get_user_high_rated_movies(user_id)

        for _, row in user_ratings.iterrows():
            title = self.recommender.get_movie_title(row['movieId'])
            if title:
                self.user_movies_list.addItem(QListWidgetItem(title))

    def getRecommendations(self):
        self.recommended_list.clear()
        self.recommended_list.addItem(QListWidgetItem("Calculating recommendations..."))
        QTimer.singleShot(1500, self.recommend)

    def recommend(self):
        self.recommended_list.clear()
        user_id = int(self.user_combo.currentText())
        num_recs = self.num_recommendations.value()

        recommendations = self.recommender.recommend(user_id, top_n=num_recs)

        if not recommendations:
            self.recommended_list.addItem("No recommendations found.")
            return

        for i, title in enumerate(recommendations):
            self.recommended_list.addItem(QListWidgetItem(f"{i+1}. {title}"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MovieRecommenderApp()
    window.show()
    sys.exit(app.exec_())