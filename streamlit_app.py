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
my_furit_list=my_fruit_list.set_index('Fruit',inplace=True) 
#Added inplace=True
 
##picklist 
#streamlit.multiselect("Pick Your Fruits Here :" , list(my_fruit_list.index))
#streamlit.multiselect("Pick Your Fruits Here :" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_selected=streamlit.multiselect("Pick Your Fruits Here :" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_show)
