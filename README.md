🎬 Movie Recommendation System

Project Overview

The Movie Recommendation System is a machine learning application that recommends movies based on their genres. The system uses content-based filtering with cosine similarity to suggest the top five movies similar to the movie selected by the user.

The application is built using Python, Pandas, Scikit-learn, and Streamlit.

---

Features

- Interactive Streamlit web application
- Select a movie from a dropdown list
- Get Top 5 movie recommendations
- Displays movie genre and rating
- Simple and user-friendly interface

---

Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn

---

Dataset

The dataset contains 250 Tollywood movies with the following columns:

- movie_id
- title
- genre
- rating

The dataset contains no duplicate movie titles and no null values.

---

Machine Learning Technique

- Content-Based Filtering
- CountVectorizer
- Cosine Similarity

---

Project Structure

Movie Recommendation System/

├── app.py

├── movies_250.csv

├── requirements.txt

└── README.md

---

Installation

Install the required packages:

pip install -r requirements.txt

---

Run the Application

Run the following command:

streamlit run app.py

The application will open in your browser at:

http://localhost:8501

---

Future Enhancements

- Movie posters
- Search functionality
- Multiple language support
- Improved recommendation algorithm
- User ratings and reviews

---

Author

Poojitha Kanamoni

B.Tech (Artificial Intelligence & Machine Learning)

Movie Recommendation System Internship Project