import streamlit as st
import pandas as pd
import requests as rq
import snowflake.connector
from urllib.error import URLError

# import streamlit as st
st.title('My Parents New Healthy Diner')
st.header('Breakfast menu')
  
st.text('🥣 Omega 3 and Blueberry oatmeal')
st.text('🥗 Kale, Spinach, Rocket Smoothie')
st.text('🐔 Hard-boiled Free-range Egg')
st.text('🥑🍞 Avocado toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)

# create a repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = rq.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

# New Section to display fruityvice api response
st.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)
except URLError as e:
  st.error()

# import snowflake.connector
st.header("The fruit load list contains:")
# Snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
       return my_cur.fetchall()

# Add button to load the fruit
if st.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  st.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list 
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding " + new_fruit

add_my_fruit = st.text_input('What fruit would you like to add?')
if st.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  st.text(back_from_function)


# don't run anything past here while we troubleshoot 
st.stop()
# st.write('Thanks for adding ', add_my_fruit)





















































