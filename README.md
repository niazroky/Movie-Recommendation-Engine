# Movie Recommendation System

This project is a content-based movie recommendation system built using Python and Streamlit. The recommendation system leverages cosine similarity to suggest similar movies based on their genre and overview.

## Overview

The recommendation system is designed to help users discover new movies that are similar to ones they enjoy. It utilizes a dataset of movie information, including titles, genres, overviews, and movie IDs. By comparing the features of a selected movie with others in the dataset, the system identifies similar movies and presents them to the user.

## Features

- **Movie Selection**: Users can select a movie from a dropdown menu.
- **Similar Movie Recommendations**: Upon selecting a movie, the system provides recommendations for similar movies.
- **Movie Posters**: Along with movie titles, the system displays posters of recommended movies fetched from the [themoviedb API](https://www.themoviedb.org/documentation/api).

## Files

- **movie_data.pkl**: Pickle file containing movie data, including titles, genres, overviews, and movie IDs.
- **similarity.pkl**: Pickle file containing the cosine similarity matrix computed between movies.
- **app.py**: The main application file containing the Streamlit code for the recommendation system.
- **README.md**: This file, providing an overview and instructions for the project.
- Other necessary files and dependencies for running the application.

## Getting Started

1. Clone the repository to your local machine.
2. Ensure you have Python and Streamlit installed.
3. Run `streamlit run app.py` in your terminal to launch the application.
4. Select a movie from the dropdown menu to receive recommendations.

## Dependencies

- Streamlit
- Pickle
- Requests

## Usage

- Select a movie from the dropdown menu.
- Click the "Recommended Similar Movies" button to view similar movie recommendations.
- Explore the recommended movies and enjoy discovering new titles.

## Acknowledgments

- The movie data used in this project is sourced from [themoviedb API](https://www.themoviedb.org/documentation/api).
- Special thanks to Streamlit for providing an intuitive platform for building interactive web applications with Python.

## Author

[Md. Niazul Islam Roky

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
