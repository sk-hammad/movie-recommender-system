import streamlit as st
import pickle

# Load movie data and similarity matrix
new_movie = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = new_movie[new_movie['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(new_movie.iloc[i[0]].title)
    return recommended_movies

# Streamlit app
st.title('Movie Recommender System')

selected_movie = st.selectbox('Select a movie:', new_movie['title'])

if st.button('Recommend'):
    recommended_movies = recommend(selected_movie)
    st.write('**Top 5 Recommended Movies:**')
    for movie in recommended_movies:
        st.write(f'- {movie}')

