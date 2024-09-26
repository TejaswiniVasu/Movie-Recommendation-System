import streamlit as st
import pandas as pd

# Basic app configuration and layout
st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")

# CSS for background and styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        color: white;
        background-color: #ff4b4b;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and subtitle
st.title("🎬 Movie Recommender System Using Machine Learning")
st.write("Select a movie from the dropdown to get recommendations")

# Load the dataset
movies_df = pd.read_csv('cleaned_rotten_tomatoes_movies.csv')  # No need for full path if it's in the same directory


# Dropdown for movie selection
selected_movie = st.selectbox("Select a movie", movies_df['title'].unique())

# Show recommendation button
if st.button('Show Recommendation'):
    # Placeholder for recommendation logic
    # Here we can filter and show similar movies
    st.write(f"You selected: **{selected_movie}**")
    
    # Dummy recommended movies (replace with actual recommendation logic)
    recommended_movies = movies_df.sample(3)  # Sample 3 random movies for demonstration
    
    st.write("Recommended Movies:")
    for index, row in recommended_movies.iterrows():
        st.write(row['title'])
        st.image('https://via.placeholder.com/150')  # Placeholder image URL, replace with actual poster links
