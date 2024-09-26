import streamlit as st
import pandas as pd

# Load the dataset from the local directory in GitHub repository
movies_df = pd.read_csv('cleaned_rotten_tomatoes_movies.csv')

# Title and subtitle
st.title("Movie Recommender System Using Machine Learning")
st.write("Type or select a movie from the dropdown")

# Dropdown for movie selection
selected_movie = st.selectbox("Select a movie", movies_df['title'].unique())

# Show recommendation button
if st.button('Show Recommendation'):
    # Placeholder for recommendation logic
    st.write("You selected:", selected_movie)
    
    # Dummy recommended movies (replace with actual recommendation logic)
    recommended_movies = movies_df.sample(5)  # Sample 5 random movies for demonstration
    
    st.write("Recommended Movies:")
    for index, row in recommended_movies.iterrows():
        st.write(row['title'])
        st.image('https://via.placeholder.com/150')  # Placeholder image URL, replace with actual poster links
