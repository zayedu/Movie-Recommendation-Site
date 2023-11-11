import streamlit as st
import pickle

import requests

movies=pickle.load(open('movies_list.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))

movies_list=movies['title'].values

st.header("Zayed's Movie Recommendation System")
selection=st.selectbox('Select a movie from the dropdown menu', movies_list)

def fetch_poster(movie_id):
  url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
  data = requests.get(url)
  data = data.json()
  poster_path=data['poster_path']
  full_path="https://image.tmdb.org/t/p/w500/" + poster_path
  return full_path

  
  
def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    recommended_movies=[]
    recommended_posters=[]
    for i in distance[1:6]:
      movies_id=movies.iloc[i[0]].id
      recommended_movies.append(movies.iloc[i[0]].title)
      recommended_posters.append(fetch_poster(movies_id))
    return recommended_movies,recommended_posters
        
if st.button("Show recommnnded"):
  movie_names,movies_poster=recommend(selection)
  col1,col2,col3,col4,col5=st.columns(5)
  with col1:
    st.text(movie_names[0])
    st.image(movies_poster[0])
  with col2:
    st.text(movie_names[1])
    st.image(movies_poster[1])
  with col3:
    st.text(movie_names[2])
    st.image(movies_poster[2])
  with col4:
    st.text(movie_names[3])
    st.image(movies_poster[3])
  with col5:
    st.text(movie_names[4])
    st.image(movies_poster[4])
  