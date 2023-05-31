import streamlit as st
from PIL import Image
import requests
import time

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
        image = Image.open(requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Brownie_Dessert.jpg/640px-Brownie_Dessert.jpg",
                                  stream=True).raw)
        new_img = image.resize((300, 300))
        st.image(new_img)
    with text_column:
        st.subheader("Brownies")
        st.write(
            """
            Indulge in the rich, chocolatey goodness of our classic brownie recipe. 
            These fudgy delights are made with high-quality cocoa powder and melted chocolate, resulting in a dense and moist texture that will leave you craving for more. 
            Each bite is filled with a perfect balance of sweetness and decadence, making them an irresistible treat for any occasion. Whether you enjoy them warm with a scoop of vanilla ice cream or simply on their own, these brownies are sure to satisfy your sweet tooth.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")
        if st.button('Display recipe',key='Brownies'):
            st.success('Recipe selected!', icon="✅")
            time.sleep(2)
            st.experimental_rerun()


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open(requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Cookie_stack.jpg/640px-Cookie_stack.jpg",
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
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")
        if st.button('Display recipe', key="Cookies"):
            st.success('Recipe selected!', icon="✅")
            time.sleep(2)
            st.experimental_rerun()

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open(requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Milky-way-broken.JPG/640px-Milky-way-broken.JPG",
                                  stream=True).raw)
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
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")
        if st.button('Display recipe',key='Protein Bars'):
            st.success('Recipe selected!', icon="✅")
            time.sleep(2)
            st.experimental_rerun()
