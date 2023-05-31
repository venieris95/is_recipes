import streamlit as st
from PIL import Image
import requests
import time
import io

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="S.P.O.O.N. Recipes", page_icon= "🍪", layout="wide")


# ---- HEADER SECTION ----
with st.container():
    st.title("S.P.O.O.N. Recipes")
    st.subheader(
        "Here you can find delicious recipes to display on your digital scale. Simply press the button and follow along!"
    )

# ---- RECIPES ----



with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open(requests.get("https://github.com/venieris95/is_recipes/blob/cfd0bc60d81d9da4e4b93119417e6bcbebd935ac/640px-Cookie_stack.jpg",
                                  stream=True).raw)
        new_img = image.resize((300, 300))
        st.image(new_img)
    with text_column:
        st.subheader("Cookies")
        st.write(
            """
            Get ready to experience the ultimate cookie bliss with our delightful cookie recipe. 
            These heavenly treats are a perfect combination of soft and chewy, with a hint of crispiness around the edges. 
            Packed with your choice of delicious mix-ins like chocolate chips, nuts, or dried fruits, these cookies offer a burst of flavors with every bite. Whether you enjoy them with a glass of milk or share them with friends and family, these homemade cookies are guaranteed to bring a smile to your face.
            """
        )
        if st.button('Display recipe', key="Cookies"):
            st.success('Recipe selected!', icon="✅")
            time.sleep(2)
            st.experimental_rerun()

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open(requests.get("https://github.com/venieris95/is_recipes/blob/cfd0bc60d81d9da4e4b93119417e6bcbebd935ac/protein_bar.jpeg",
                                  stream=True.raw))
        new_img = image.resize((300, 300))
        st.image(new_img)
    with text_column:
        st.subheader("Protein Bars")
        st.write(
            """
            Elevate your snacking game with our homemade protein bar recipe. 
            These wholesome bars are designed to provide a boost of energy and satisfy your hunger on-the-go. 
            Packed with a nutritious blend of high-quality protein, healthy fats, and natural sweeteners, they offer a guilt-free indulgence that keeps you fueled throughout the day. 
            With a variety of flavors and customizable ingredients, you can create protein bars tailored to your taste preferences and dietary needs. Whether you're hitting the gym or need a quick and nutritious snack, these protein bars are the perfect choice.
            """
        )
        if st.button('Display recipe',key='Protein Bars'):
            st.success('Recipe selected!', icon="✅")
            time.sleep(2)
            st.experimental_rerun()
