import streamlit 
import pandas as pa

streamlit.title('My Parents New Healthy Diner') 
streamlit.header(' 🍲 Breakfast Menu  ')
streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boilded Free-Range Egg')
streamlit.text('🥑 🍞  Avocado Toast') 
streamlit.header(' 🍎 Build your Own Fruit Smoothie 🍇 ')   

my_fruit_list=pa.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.text(my_fruit_list.set_index('Fruit'))
#my_furit_list=my_fruit_list.set_index('Fruit')
#streamlit.text(list(my_fruit_list))
##picklist 
#streamlit.multiselect("Pick Your Fruits Here1:" , list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
