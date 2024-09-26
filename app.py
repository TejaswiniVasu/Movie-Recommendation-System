import streamlit as st
import pandas as pd

# Load the dataset (ensure that the file exists in the same repository)
try:
    movies_df = pd.read_csv('cleaned_rotten_tomatoes_movies.csv')
except FileNotFoundError:
    st.error("The movie dataset file was not found. Please make sure the file is uploaded correctly.")
except pd.errors.EmptyDataError:
    st.error("The movie dataset file is empty. Please check the file content.")

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

# Title and subtitle
st.markdown("<h1>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.write("Select a movie from the dropdown to get recommendations:")

# Dropdown for movie selection (ensure the DataFrame is loaded before proceeding)
if 'movies_df' in locals() and not movies_df.empty:
    selected_movie = st.selectbox("Select a movie", movies_df['title'].unique())

    # Show recommendation button
    if st.button('Show Recommendation'):
        st.write(f"You selected: **{selected_movie}**")
        
        # Dummy recommended movies (replace with actual recommendation logic)
        recommended_movies = movies_df.sample(5)  # Sample 5 random movies for demonstration
        
        st.write("### Recommended Movies:")
        cols = st.columns(5)  # Display movies in a row
        for idx, col in enumerate(cols):
            with col:
                col.write(recommended_movies.iloc[idx]['title'])
                col.image('https://via.placeholder.com/150', width=150)  # Placeholder image
else:
    st.error("The movie dataset is not available or is empty.")
