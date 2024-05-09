import streamlit as st
import pandas as pd
import pickle
from streamlit.components.v1 import html
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity  = pickle.load(open('similarity.pkl', 'rb'))
movie = pd.DataFrame(movie_dict)
st.title('Recommendation system')

def recommend(obj):
    index = movie[movie['title'] == obj].index[0]
    distance = similarity[index]
    recommeded_movie = []
    movie_list = sorted(list(enumerate(distance)),reverse=True, key=lambda x: x[1])[1:6]
    for i in movie_list :
        recommeded_movie.append(movie.iloc[i[0]].title)
    return recommeded_movie

option = st.selectbox('which movie you wanna see',movie['title'].values)
if st.button('recommend') :
    rexo = recommend(option)
    for i in rexo :
        st.write(i)

