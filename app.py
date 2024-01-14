import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

model = pickle.load(open('model.sav', 'rb'))

st.title('Player Salary Predictor')
st.sidebar.header('Player Data')
image = Image.open('bg.jpg')
st.image(image, '')

#Sidebar inputs

def user_report() :
    rating = st.sidebar.slider('Rating', 50, 100, 1)
    jersey = st.sidebar.slider('Jersey', 0, 100, 1)
    team = st.sidebar.slider('Team', 0, 30, 1)
    position = st.sidebar.slider('Position', 0, 10, 1)
    country = st.sidebar.slider('Country', 0, 3, 1)
    draft_year = st.sidebar.slider('Draft Year', 2000, 2020, 2000)
    draft_round = st.sidebar.slider('Draft Round', 1, 10, 1)
    draft_peak = st.sidebar.slider('Draft Peak', 1, 30, 1)

    #saving the values
    user_report_data = {
        'rating' : rating,
        'jersey' : jersey,
        'team' : team,
        'position' : position,
        'country' : country,
        'draft_year' : draft_year,
        'draft_round' : draft_round,
        'draft_peak' : draft_peak
    }

    #Creating dataframe of given values so as to pass it to model
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()
st.header('Player Data')
st.write(user_data)

salary = model.predict(user_data)
st.subheader('Player Salary')
st.subheader('$'+str(np.round(salary[0], 2)))