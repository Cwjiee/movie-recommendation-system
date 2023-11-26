import streamlit as st
import time
import data

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎥",
    layout="wide",
)

##### UI #####

st.title('Movie Recommendation System')

title = st.text_input(label="Movie Title")

if st.button('recommend'):

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    results = data.recommend_movies(title)
    st.dataframe(results, hide_index=True)
