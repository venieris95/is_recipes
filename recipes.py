import streamlit as st
from pathlib import path

st.set_page_config(
    page_title="Recipe List",
    page_icon="🍪",
)

st.title("Main Page")
st.sidebar.title("Recipes")
recipes = st.selectbox('Select a recipe',('Cookie', 'Brownie', 'Protein bar'))
if recipes == "Cookie": 
  recipe = Path('recipes/cookie.txt').read_text()
  st.write(recipe)
if recipes == "Brownie": 
  recipe = Path('recipes/brownie.txt').read_text()
  st.write(recipe)
if recipes == "Protein bar": 
  recipe = Path('recipes/protbar.txt').read_text()
  st.write(recipe)
