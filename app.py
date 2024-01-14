import streamlit as st

import pickle
import pandas as pd


def recommendation(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance= simlarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key = lambda x : x[1])[1:6]
    
    reccomend_movies = []
    for i in movies_list:
        reccomend_movies.append(movies.iloc[i[0]].title)
    return reccomend_movies

    

st.title("movie recommender")

movies_dict = pickle.load(open('movies_dict3.pkl','rb'))
movies= pd.DataFrame(movies_dict)


simlarity = pickle.load(open('similarity.pkl','rb'))
options = st.selectbox("choose the name  the movie",movies['title'].values)
 
 
if st.button("recommend"):
    recommd =  recommendation(options)
    for i in recommd:
         st.write(i)
 