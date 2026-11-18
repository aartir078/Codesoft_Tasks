
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = pd.DataFrame({
    "title": [
        # Action and Superhero
        "The Dark Knight",
        "Batman Begins",
        "The Dark Knight Rises",
        "Iron Man",
        "The Avengers",
        "Avengers Endgame",
        "Spider-Man",
        "Spider-Man No Way Home",
        "Black Panther",
        "Wonder Woman",

        # Science Fiction
        "Interstellar",
        "Inception",
        "The Matrix",
        "The Martian",
        "Gravity",
        "Dune",
        "Avatar",
        "Star Wars",
        "Tenet",
        "Arrival",

        # Romance and Drama
        "Titanic",
        "The Notebook",
        "La La Land",
        "Me Before You",
        "The Fault in Our Stars",
        "Pride and Prejudice",
        "A Star Is Born",
        "Forrest Gump",
        "The Pursuit of Happyness",
        "The Shawshank Redemption",

        # Animation and Family
        "Toy Story",
        "Toy Story 3",
        "Finding Nemo",
        "Finding Dory",
        "The Lion King",
        "Frozen",
        "Inside Out",
        "Coco",
        "Up",
        "Zootopia",

        # Thriller, Mystery and Crime
        "Shutter Island",
        "Gone Girl",
        "Se7en",
        "The Prestige",
        "Joker",
        "John Wick",
        "Mission Impossible",
        "Now You See Me",
        "Knives Out",
        "The Conjuring"
    ],

    "genre": [
        # Action and Superhero
        "action crime superhero thriller",
        "action crime superhero origin",
        "action crime superhero thriller",
        "action superhero science fiction",
        "action superhero adventure team",
        "action superhero adventure team",
        "action superhero adventure",
        "action superhero adventure science fiction",
        "action superhero science fiction adventure",
        "action superhero fantasy adventure",

        # Science Fiction
        "science fiction space adventure drama",
        "science fiction thriller dream action",
        "science fiction action futuristic",
        "science fiction space survival drama",
        "science fiction space survival thriller",
        "science fiction fantasy adventure",
        "science fiction fantasy adventure",
        "science fiction space adventure fantasy",
        "science fiction action thriller",
        "science fiction alien mystery drama",

        # Romance and Drama
        "romance drama disaster",
        "romance drama relationship",
        "romance musical drama",
        "romance drama emotional",
        "romance drama illness",
        "romance drama historical",
        "romance music drama",
        "drama romance comedy life",
        "drama biography inspirational",
        "drama crime prison inspirational",

        # Animation and Family
        "animation comedy family adventure",
        "animation comedy family adventure",
        "animation adventure family ocean",
        "animation adventure family ocean",
        "animation family adventure musical",
        "animation fantasy family musical",
        "animation family emotional comedy",
        "animation family music adventure",
        "animation family adventure emotional",
        "animation comedy family adventure animals",

        # Thriller, Mystery and Crime
        "thriller mystery psychological crime",
        "thriller mystery crime drama",
        "thriller crime mystery serial killer",
        "thriller mystery magic drama",
        "crime thriller psychological drama",
        "action crime thriller assassin",
        "action spy thriller adventure",
        "crime thriller mystery magic",
        "crime mystery comedy detective",
        "horror supernatural mystery thriller"
    ]
})

vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])
similarity = cosine_similarity(genre_matrix)

def recommend_movies(movie_title, number=3):
    movie_index = movies[
        movies["title"] == movie_title
    ].index[0]

    scores = list(enumerate(similarity[movie_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = [
        (movies.iloc[index]["title"], round(float(score), 3))
        for index, score in scores
        if index != movie_index
    ]

    return recommendations[:number]

st.set_page_config(page_title="Movie Recommendation AI",
                   page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie to discover similar movies.")

selected_movie = st.selectbox(
    "Choose a movie",
    movies["title"].tolist()
)

number = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=5,
    value=3
)

if st.button("Recommend Movies"):
    results = recommend_movies(selected_movie, number)

    st.subheader("Recommended Movies")

    for title, score in results:
        st.write(f"🎥 **{title}**")
        st.caption(f"Similarity score: {score}")
