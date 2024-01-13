import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as numpy
from PIL import Image

model = pickle.load(open('model.sav', 'rb'))

