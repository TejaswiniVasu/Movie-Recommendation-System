import streamlit as st
import pandas as pd

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f0f5;
        font-family: Arial, sans-serif;
    }
    h1 {
        color: #ff4b4b;
        font-size: 3em;
        text-align: center;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #ff6666;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the dataset
movies_df = pd.read_csv('cleaned_rotten_tomatoes_movies.csv')

# Title and subtitle
st.markdown("<h1>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.write("Select a movie from the dropdown to get recommendations:")

# Dropdown for movie selection
selected_movie = st.selectbox("Select a movie", movies_df['title'].unique())

# Show recommendation button
if st.button('Show Recommendation'):
    # Placeholder for recommendation logic
    st.write(f"You selected: **{selected_movie}**")
    
    # Dummy recommended movies (replace with actual recommendation logic)
    recommended_movies = movies_df.sample(5)  # Sample 5 random movies for demonstration
    
    st.write("### Recommended Movies:")
    # Display recommended movies and placeholder images
    cols = st.columns(5)  # Display movies in a row
    for idx, col in enumerate(cols):
        with col:
            col.write(recommended_movies.iloc[idx]['title'])
            col.image('https://via.placeholder.com/150', width=150)  # Placeholder image
