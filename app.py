import streamlit as st
import pandas as pd
import sys

class AppException(Exception):
    def __init__(self, message, original_exception):
        super().__init__(f"{message}: {original_exception}")
        self.original_exception = original_exception

class Recommendation:
    def __init__(self):
        # Load the dataset (make sure this is correct and in the same repo)
        self.movies = pd.read_csv('cleaned_rotten_tomatoes_movies.csv')
    
    def train_engine(self):
        # Add the training logic here (if applicable)
        st.write("Training recommendation engine...")

    def recommend(self, selected_movie):
        # Replace this logic with your actual recommendation logic
        # This should return recommended movie names and poster URLs
        
        # Dummy logic to simulate recommendation
        # Replace with your actual logic
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

if __name__ == "__main__":
    st.header('Movie Recommender System')
    st.text("This is a content-based recommendation system!")

    # Initialize the recommendation engine
    obj = Recommendation()

    # Dropdown for movie selection
    movie_list = obj.movies['title'].values
    selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

    # Button to trigger training
    if st.button('Train Recommender System'):
        obj.train_engine()
    
    # Button to show movie recommendations
    if st.button('Show Recommendation'):
        obj.recommendations_engine(selected_movie)
