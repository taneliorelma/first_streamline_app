import streamlit as st

st.title('My Parents New Healthy Diner')
st.header('Breakfast menu')
  
st.text('🥣 Omega 3 and Blueberry oatmeal')
st.text('🥗 Kale, Spinach, Rocket Smoothie')
st.text('🐔 Hard-boiled Free-range Egg')
st.text('🥑🍞 Avocado toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
