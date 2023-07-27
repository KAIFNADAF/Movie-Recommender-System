import streamlit as st
import pickle
import pandas as pd
import requests

PAGE_TITLE = "Movie Recommender System"
PAGE_ICON = "🎥"
NAME = "Kaif Nadaf"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


from PIL import Image



def fetch_poster(movie_id):
    responce = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = responce.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    
    recommended_movie_posters = []
    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movie_posters

movies_dict = pickle.load(open('C:/Users/KAIF/Desktop/Movie recommender System/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('C:/Users/KAIF/Desktop/Movie recommender System/similarity.pkl', 'rb'))
st.title("Movie Recommender System")

options = st.selectbox(
    'Enter movie name',
    movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(options)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])      

#fotter
st.write('---')
st.write('© Kaif Nadaf  |  Last updated: July 2023')

background_image = 'background.jpeg'
st.markdown(
    f"""
    <style>
    body {{
        background-image: url("{background_image}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)