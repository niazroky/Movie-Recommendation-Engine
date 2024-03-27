"""Movie Recommendation Engine"""

# Import necessary libraries
import streamlit as st
import pickle
import requests

# Load the pickle files containing movie data and similarity matrix
movies = pickle.load(open("movie_data.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))

# Extract movie titles from the loaded movie data
movie_titles = movies['title'].values

# Streamlit header for the recommendation engine
st.header("Movie Recommendation Engine")

# Dropdown to select a movie
selected_movie = st.selectbox("Select movie: ", movie_titles)

# Function to fetch movie poster given a movie ID using themoviedb API
def fetch_poster(movie_id):
    """
    Fetches the poster URL for a given movie ID using the themoviedb API.

    Args:
        movie_id (int): The ID of the movie.

    Returns:
        str: The URL of the movie poster.
    """
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend similar movies based on selected movie
def recommend(movie):
    """
    Recommends similar movies based on the selected movie.

    Args:
        movie (str): The title of the selected movie.

    Returns:
        tuple: A tuple containing recommended movie titles and their poster URLs.
    """
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommended_movie=[]
    recommended_poster=[]
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movies_id))
    return recommended_movie, recommended_poster

# Button to trigger movie recommendation
if st.button("Recommended Similar Movies: "):
    movie_name, movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
