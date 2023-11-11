# Movie Recommendation Site

![Project Screenshot](Movie-Recommendation-Demo.png)

## Check out this project [here](https://zayedtv.streamlit.app/)

## Overview

The Movie Recommendation Site is a Python-based web application that utilizes data science techniques to recommend movies to users based on their input. It leverages the concept of cosine similarity to find movies similar to the one the user selects. This project incorporates various Python packages, including scikit-learn, pandas, and pickle.

## Features

- **Cosine Similarity:** The core of the recommendation system uses cosine similarity to find movies with similar characteristics, making personalized movie suggestions.

- **Data Processing:** It preprocesses the movie dataset, combining features like movie overview and genre to create a meaningful representation for comparison.

- **Web Application:** The project is wrapped in a web interface built with Streamlit, allowing users to input a movie title and receive recommendations.

- **Movie Posters:** The system retrieves movie posters using The Movie Database (TMDb) API to provide a visual element to the recommendations.

## Project Structure

The project comprises two main components:

- **Data Preparation (Main.ipynb):** This script processes the movie dataset by combining relevant features, creating a term-document matrix, and calculating cosine similarity between movies. The results are pickled for easy access.

- **Web Application (app.py):** This is the front end of the project. It uses Streamlit to create a user-friendly interface. Users can input a movie title, and the application recommends similar movies with posters.

## Usage

1. **Data Preparation:**

   - Load the movie dataset using `movies=pd.read_csv('dataset.csv')`.
   - Combine movie overview and genre to form 'tags' and drop irrelevant columns.
   - Create a term-document matrix using CountVectorizer and calculate cosine similarity.
   - Pickle the `new_data` and `similarity` for later use.

2. **Web Application:**
   - Run the Streamlit app using `streamlit run app.py`.
   - Select a movie from the dropdown menu.
   - Click the "Show recommended" button to see movie recommendations.

## Prerequisites

- Python 3.x
- Libraries: pandas, scikit-learn, pickle, requests, Streamlit

## Credits

- Movie dataset: (Provide the source or origin of the dataset if applicable)
- The Movie Database (TMDb) API: (Insert TMDb API link)

## License

This project is open-source and available under the MIT License. See the [LICENSE](License) file for details.

## Contact

- Author: [Zayed Umer](https://github.com/zayedu)
