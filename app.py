import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as numpy
from PIL import Image

model = pickle.load(open('model.sav', 'rb'))

st.title('Player Salary Predictor')
st.sidebar.header('Player Data')
image = Image.open('bg.jpg')
st.image(image, '')