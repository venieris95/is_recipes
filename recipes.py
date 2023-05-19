import streamlit as st

st.set_page_config(
    page_title="Recipe List",
    page_icon="🍪",
)

st.title("Main Page")
st.sidebar.title("Recipes")
recipes = st.selectbox('Select a recipe',('Cookie', 'Brownie', 'Protein bar'))
if recipes == "Cookie": 
  recipe = Path('cookie.py').read_text()
  st.write(recipe)
if recipes == "Brownie": 
  recipe = Path('brownie.txt').read_text()
  st.write(recipe)
if recipes == "Protein bar": 
  recipe = Path('protbar.txt').read_text()
  st.write(recipe)
