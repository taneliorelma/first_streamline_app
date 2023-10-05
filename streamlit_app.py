import streamlit as st

st.title('My Parents New Healthy Diner')
st.header('Breakfast menu')
  
st.text('🥣 Omega 3 and Blueberry oatmeal')
st.text('🥗 Kale, Spinach, Rocket Smoothie')
st.text('🐔 Hard-boiled Free-range Egg')
st.text('🥑🍞 Avocado toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
st.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
st.dataframe(my_fruit_list)

