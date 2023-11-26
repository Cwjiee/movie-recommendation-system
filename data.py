import pandas as pd
import numpy as np
import os
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def load_data():
    df = pd.read_csv("datas/netflix_titles.csv")
    return df


def recommend_movies(title):
    df = load_data()

    df.drop_duplicates(subset=['title'], inplace=True)

    tfdif = TfidfVectorizer(stop_words='english')
    df['description'] = df['description'].fillna('')
    tfdif_matrix = tfdif.fit_transform(df['description'])

    cosine_sim = linear_kernel(tfdif_matrix, tfdif_matrix)
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()

    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    return df['title'].iloc[movie_indices]
