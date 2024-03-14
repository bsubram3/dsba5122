import streamlit as st
import pandas as pd
import numpy as np

st.title('Create  Dynamic Visuals')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  dataframe = pd.read_csv(uploaded_file)
  st.write(dataframe)
  # iterating the columns
  st.title('Columns in the Dataset')
