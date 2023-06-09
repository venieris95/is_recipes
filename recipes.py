import streamlit as st
from PIL import Image
import requests
import time
import io

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
def get_file_contents(file_url):
    response = requests.get(file_url)
    return response.text

def check_credentials():
    """Returns `True` if the user had a correct password."""
    def credentials_entered():
        """Checks whether a password entered by the user is correct."""
        if (st.session_state["username"] == st.secrets["username"] and st.session_state["password"] == st.secrets["password"]):
            st.session_state["credentials_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["credentials_correct"] = False

    if "credentials_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.warning("Credentials: username: interactivesystems2023 | password: presentation_demo")
        st.text_input("Username", on_change=credentials_entered, key="username")
        st.text_input("Password", type="password", on_change=credentials_entered, key="password")
        return False
    elif not st.session_state["credentials_correct"]:
        # Password not correct, show input + error.
        st.warning("Credentials: username: interactivesystems2023 | password: presentation_demo")
        st.text_input("Username", on_change=credentials_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=credentials_entered, key="password")
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

owl = Image.open(requests.get("https://github.com/venieris95/is_recipes/blob/main/owl.png?raw=true",
                              stream=True).raw)
st.set_page_config(page_title="S.P.O.O.N. Recipes", page_icon=owl, layout="wide")

st.title("Welcome to S.P.O.O.N. Digital Scale Interface")

if check_credentials():
    st.subheader("Shape up your cooking experience with our spoon-shaped digital scale! Simply press 'Load recipe on S.P.O.O.N.' to display the recipe that you like on the device!")
    
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            imgUrl = "https://raw.githubusercontent.com/venieris95/is_recipes/cfd0bc60d81d9da4e4b93119417e6bcbebd935ac/Brownie_Dessert.jpg"
            r = requests.get(imgUrl, stream=True)
            image = Image.open(io.BytesIO(r.content))
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
    
            with st.expander("View Recipe"):
                brownies_url = "https://raw.githubusercontent.com/venieris95/is_recipes/main/recipes/brownie.txt"
                brownies_recipe = get_file_contents(brownies_url)
                st.text_area("Recipe", value=brownies_recipe, height=400)
    
                if st.button('Load recipe on S.P.O.O.N.', key='Brownies'):
                    st.success('Recipe selected!', icon="✅")
                    time.sleep(2)
                    st.experimental_rerun()
    
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            image = Image.open(
                requests.get("https://github.com/venieris95/is_recipes/blob/main/640px-Cookie_stack.jpg?raw=true",
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
    
            with st.expander("View Recipe"):
                cookie_url = "https://raw.githubusercontent.com/venieris95/is_recipes/main/recipes/cookie.txt"
                cookie_recipe = get_file_contents(cookie_url)
                st.text_area("Recipe", value=cookie_recipe, height=400)
    
                if st.button('Load recipe on S.P.O.O.N.', key='Cookie'):
                    st.success('Recipe selected!', icon="✅")
                    time.sleep(2)
                    st.experimental_rerun()
    
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            image = Image.open(requests.get("https://github.com/venieris95/is_recipes/blob/main/protein_bar.jpeg?raw=true",
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
    
            with st.expander("View Recipe"):
                protbar_url = "https://raw.githubusercontent.com/venieris95/is_recipes/main/recipes/protbar.txt"
                protbar_recipe = get_file_contents(protbar_url)
                st.text_area("Recipe", value=protbar_recipe, height=400)
    
                if st.button('Load recipe on S.P.O.O.N.', key='Protein Bar'):
                    st.success('Recipe selected!', icon="✅")
                    time.sleep(2)
                    st.experimental_rerun()
