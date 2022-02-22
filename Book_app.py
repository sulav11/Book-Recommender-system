
import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.neighbors import NearestNeighbors



ratings = pickle.load(open('ratings.pkl','rb'))
book_dataset = pickle.load(open('book_dataset.pkl','rb'))
book_sparse = pickle.load(open('book_sparse.pkl','rb'))
pivot_table = pickle.load(open('pivot_table.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
image_df = pickle.load(open('image_df.pkl','rb'))
author = pickle.load(open('author.pkl','rb'))

st.title("Welcome to the collection of books!")

def recommend(book):
    n = np.where(pivot_table.index == book)[0][0]
    recommended_books= []
    distances, suggestions = model.kneighbors(pivot_table.iloc[n, :].values.reshape(1, -1))
    for i in range(6):
        recommended_books.append(pivot_table.index[suggestions[0,i]])
    return recommended_books    

option = st.selectbox(
     'What book would you like to read?',
     (ratings['Book-Title']))

st.write('Recommended books:', option)

if st.button('Recommend'):

    col1, col2, col3,col4,col5,col6 = st.columns(6)
    recommended_book_name = recommend(option)
    i=0

    with col1:
        a = image_df[image_df['Book-Title'] == recommended_book_name[i] ]['Image-URL-L'].index[0]
        st.image(image_df[image_df['Book-Title'] == recommended_book_name[i]]['Image-URL-L'][a])
        st.write(recommended_book_name[i])
        b = author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'].index[0]
        st.caption(author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'][b])
        c = ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'].index[0]
        st.write(ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'][c])
        st.caption(f'Price : {np.random.choice([i for i in np.linspace(49.99,99.99, num=5, endpoint=False)])}')
        
        i+=1
        

    with col2:
        a = image_df[image_df['Book-Title'] == recommended_book_name[i] ]['Image-URL-L'].index[0]
        st.image(image_df[image_df['Book-Title'] == recommended_book_name[i]]['Image-URL-L'][a])
        st.write(recommended_book_name[i])
        b = author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'].index[0]
        st.caption(author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'][b])
        c = ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'].index[0]
        st.write(ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'][c])
        st.caption(f'Price : {np.random.choice([i for i in np.linspace(49.99,99.99, num=5, endpoint=False)])}')
        
        i+=1
        

    with col3:
        a = image_df[image_df['Book-Title'] == recommended_book_name[i] ]['Image-URL-L'].index[0]
        st.image(image_df[image_df['Book-Title'] == recommended_book_name[i]]['Image-URL-L'][a])
        st.write(recommended_book_name[i])
        b = author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'].index[0]
        st.caption(author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'][b]) 
        c = ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'].index[0]
        st.write(ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'][c])
        st.caption(f'Price : {np.random.choice([i for i in np.linspace(49.99,99.99, num=5, endpoint=False)])}')
        
        i+=1

    with col4:
        a = image_df[image_df['Book-Title'] == recommended_book_name[i] ]['Image-URL-L'].index[0]
        st.image(image_df[image_df['Book-Title'] == recommended_book_name[i]]['Image-URL-L'][a])
        st.write(recommended_book_name[i])
        b = author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'].index[0]
        st.caption(author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'][b])
        c = ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'].index[0]
        st.write(ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'][c])
        st.caption(f'Price : {np.random.choice([i for i in np.linspace(49.99,99.99, num=5, endpoint=False)])}')
        
        i+=1
        
    with col5:
        a = image_df[image_df['Book-Title'] == recommended_book_name[i] ]['Image-URL-L'].index[0]
        st.image(image_df[image_df['Book-Title'] == recommended_book_name[i]]['Image-URL-L'][a])
        st.write(recommended_book_name[i])
        b = author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'].index[0]
        st.caption(author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'][b])
        c = ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'].index[0]
        st.write(ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'][c])
        st.caption(f'Price : {np.random.choice([i for i in np.linspace(49.99,99.99, num=5, endpoint=False)])}')
        
        i+=1
        

    with col6:
        a = image_df[image_df['Book-Title'] == recommended_book_name[i] ]['Image-URL-L'].index[0]
        st.image(image_df[image_df['Book-Title'] == recommended_book_name[i]]['Image-URL-L'][a])
        st.write(recommended_book_name[i])
        b = author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'].index[0]
        st.caption(author[author['Book-Title'] == recommended_book_name[i]]['Book-Author'][b])
        c = ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'].index[0]
        st.write(ratings[ratings['Book-Title'] == recommended_book_name[i]]['Avg_rating'][c])
        st.caption(f'Price : {np.random.choice([i for i in np.linspace(49.99,99.99, num=5, endpoint=False)])}')
        
        i+=1
        
