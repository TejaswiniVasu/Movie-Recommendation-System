import streamlit as st
import pandas as pd
import sys

class AppException(Exception):
    def __init__(self, message, original_exception):
        super().__init__(f"{message}: {original_exception}")
        self.original_exception = original_exception

class Recommendation:
    def __init__(self):
        # Load the dataset from the repository
        self.movies = pd.read_csv('cleaned_rotten_tomatoes_movies.csv')  # Use relative path here

    
    def recommend(self, selected_movie):
        # Replace this logic with your actual recommendation logic
        # This should return recommended movie names and poster URLs
        
        # Dummy logic to simulate recommendation (replace with real recommendation logic)
        recommended_movies = self.movies.sample(5)
        recommended_movie_names = recommended_movies['title'].tolist()
        recommended_movie_posters = ['https://via.placeholder.com/150'] * 5  # Replace with actual poster URLs
        return recommended_movie_names, recommended_movie_posters

    def recommendations_engine(self, selected_movie):
        try:
            # Get movie names and poster URLs from recommendation system
            recommended_movie_names, recommended_movie_posters = self.recommend(selected_movie)

            # Create columns for displaying recommendations
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(recommended_movie_names[0])
                st.image(recommended_movie_posters[0])
            with col2:
                st.text(recommended_movie_names[1])
                st.image(recommended_movie_posters[1])
            with col3:
                st.text(recommended_movie_names[2])
                st.image(recommended_movie_posters[2])
            with col4:
                st.text(recommended_movie_names[3])
                st.image(recommended_movie_posters[3])
            with col5:
                st.text(recommended_movie_names[4])
                st.image(recommended_movie_posters[4])
        except Exception as e:
            raise AppException("Error in generating recommendations", e)

# Add Netflix style colors with Markdown and HTML
st.markdown("""
    <style>
        .stApp {
            background-color: #141414;  /* Netflix black background */
            color: white;  /* Netflix text color */
        }
        h1 {
            color: #E50914;  /* Netflix red for header */
        }
        .css-1offfwp e1tzin5v0 {
            background-color: #E50914;
        }
        .stButton button {
            background-color: #E50914;  /* Netflix red button */
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.header('🎬 Movie Recommendation System')
    st.markdown("<h3 style='color:#E50914;'>Select a movie from the dropdown to get recommendations</h3>", unsafe_allow_html=True)

    # Initialize the recommendation engine
    obj = Recommendation()

    # Dropdown for movie selection
    movie_list = obj.movies['title'].values
    selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

    # Button to show movie recommendations
    if st.button('Show Recommendation'):
        obj.recommendations_engine(selected_movie)
