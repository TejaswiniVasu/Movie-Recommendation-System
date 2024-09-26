
import streamlit as st
import pandas as pd
import os

# Load the dataset
movies_df = pd.read_csv('/content/drive/MyDrive/Movie_Recommendation_System/cleaned_rotten_tomatoes_movies.csv')

# Title and subtitle
st.title("Movie Recommender System Using Machine Learning")
st.write("Type or select a movie from the dropdown")

# Dropdown for movie selection
selected_movie = st.selectbox("Select a movie", movies_df['title'].unique())

# Function to get movie recommendations (replace with actual recommendation logic)
def get_recommendations(selected_movie, movies_df, n=5):
    # Dummy logic: sample n random movies as recommendations
    # Replace this with the logic of your recommendation system
    recommended_movies = movies_df.sample(n)
    return recommended_movies

# Show recommendation button
if st.button('Show Recommendation'):
    st.write("You selected:", selected_movie)
    
    # Get recommendations
    recommended_movies = get_recommendations(selected_movie, movies_df)
    
    st.write("Recommended Movies:")
    for index, row in recommended_movies.iterrows():
        st.write(row['title'])
        # Replace with actual poster link from your dataset if available
        st.image('https://via.placeholder.com/150', caption=row['title'])  # Placeholder image URL


