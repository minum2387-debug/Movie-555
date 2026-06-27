import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommendation System")
st.write("Select a movie to get the Top 5 recommendations.")

# -------------------------------
# Load Dataset
# -------------------------------
try:
    movies = pd.read_csv("movies_250.csv")
except:
    st.error("movies_250.csv not found.")
    st.stop()

# Fill missing values
movies["genre"] = movies["genre"].fillna("")
movies["title"] = movies["title"].fillna("")

# -------------------------------
# Similarity Matrix
# -------------------------------
cv = CountVectorizer()

genre_matrix = cv.fit_transform(movies["genre"])

similarity = cosine_similarity(genre_matrix)

# -------------------------------
# Recommendation Function
# -------------------------------
def recommend(movie_name):

    movie_name = movie_name.lower()

    if movie_name not in movies["title"].str.lower().values:
        return []

    index = movies[movies["title"].str.lower() == movie_name].index[0]

    distances = list(enumerate(similarity[index]))

    distances = sorted(distances,
                       key=lambda x: x[1],
                       reverse=True)

    recommendations = []

    for i in distances[1:6]:

        recommendations.append({
            "Title": movies.iloc[i[0]]["title"],
            "Genre": movies.iloc[i[0]]["genre"],
            "Rating": movies.iloc[i[0]]["rating"]
        })

    return recommendations

# -------------------------------
# User Input
# -------------------------------
movie = st.selectbox(
    "Choose a Movie",
    sorted(movies["title"].unique())
)

if st.button("Recommend"):

    results = recommend(movie)

    if len(results) == 0:
        st.error("Movie not found.")
    else:
        st.subheader("Top 5 Recommended Movies")

        for i, m in enumerate(results, start=1):
            st.write(f"### {i}. {m['Title']}")
            st.write("Genre :", m["Genre"])
            st.write("Rating :", m["Rating"])
            st.write("---")

# -------------------------------
# Show Dataset
# -------------------------------
if st.checkbox("Show Dataset"):
    st.dataframe(movies)