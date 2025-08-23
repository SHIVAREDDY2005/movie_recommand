import streamlit as st
import pickle
import pandas as pd
# import requests

# def poster(movie_id):
#     try:
#         response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8eb5a09a7a4f30f072b5d33382ca1556'.format(movie_id))
#         data=response.json()
#         return 'https://image.tmdb.org/t/p/w185/'+data['poster_path']
#     except:
#         return 'errordone'
#     #to get entire path we need  https://image.tmdb.org/t/p/w185/jGWpG4YhpQwVmjyHEGkxEkeRf0S.jpg last one is return from function
# def create_poster_Dataframe(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8eb5a09a7a4f30f072b5d33382ca1556".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w185/" + poster_path
#     return full_path

# def poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8eb5a09a7a4f30f072b5d33382ca1556".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w185/" + poster_path
#     return full_path


def recomand(movie):
    movie_indx=movie_names[movie_names['title']==movie].index[0]
    distance=similarity[movie_indx]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[0:5]
    result=[]
    # result_posters=[]
    for i in movies_list:
        print(i)
        #i contain id and similarity 
        # movie_id = movie_names.iloc[i[0]].movie_id
        result.append(movie_names.iloc[i[0]].title)
        #fetching poster 
        # result_posters.append(poster(movie_id))
    return result

movie_names_dict=pickle.load(open('movie.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

movie_names=pd.DataFrame(movie_names_dict)

#framework
st.title('Movie recommand')
selected_movie_name=st.selectbox(
    'Search for your favorate movie.I will recommand to similar movies...',(movie_names['title'].values))
if st.button('Recommand'):
    names=recomand(selected_movie_name)
    for i in names:
        st.write(i)

    # c1,c2,c3,c4,c5=st.columns(5)
    # with c1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with c2:
    #     st.text(names[1])
    #     st.image(posters[1])
    # with c3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with c4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with c5:
    #     st.text(names[4])
    #     st.image(posters[4])
    
    #to add poster image we use api keys
    #https://api.themoviedb.org/3/movie/285(this is movie id)?api_key=8eb5a09a7a4f30f072b5d33382ca1556(personal api  key)
    #like this data we get by that
    # {"adult":false,"backdrop_path":"/1jHxkVXMI5s3vRiyiZooUy1shB5.jpg","belongs_to_collection":{"id":295,"name":"Pirates of the Caribbean Collection","poster_path":"/4KUJ38SsViJTsUmTRvXxerBNwAv.jpg","backdrop_path":"/wxgD3fB5lQ2sGJLog0rvXW049Pf.jpg"},"budget":300000000,"genres":[{"id":12,"name":"Adventure"},{"id":14,"name":"Fantasy"},{"id":28,"name":"Action"}],"homepage":"https://movies.disney.com/pirates-of-the-caribbean-at-worlds-end","id":285,"imdb_id":"tt0449088","origin_country":["US"],"original_language":"en","original_title":"Pirates of the Caribbean: At World's End","overview":"Will Turner and Elizabeth Swann join forces with the revived Captain Barbossa to free Jack Sparrow from Davy Jones' locker. The group must navigate dangerous waters, confront many foes and, ultimately, choose sides in a battle wherein piracy itself hangs in the balance.","popularity":15.3031,"poster_path":"/jGWpG4YhpQwVmjyHEGkxEkeRf0S.jpg","production_companies":[{"id":130,"logo_path":"/c9dVHPOL3cqCr2593Ahk0nEKTEM.png","name":"Jerry Bruckheimer Films","origin_country":"US"},{"id":19936,"logo_path":null,"name":"Second Mate Productions","origin_country":"US"},{"id":2,"logo_path":"/wdrCwmRnLFJhEoH8GSfymY85KHT.png","name":"Walt Disney Pictures","origin_country":"US"}],"production_countries":[{"iso_3166_1":"US","name":"United States of America"}],"release_date":"2007-05-19","revenue":961691209,"runtime":169,"spoken_languages":[{"english_name":"English","iso_639_1":"en","name":"English"}],"status":"Released","tagline":"At the end of the world, the adventure begins.","title":"Pirates of the Caribbean: At World's End","video":false,"vote_average":7.262,"vote_count":14851}
    #using jsonviwer we can we data in fromat 
    #in that we get poster path tooo

