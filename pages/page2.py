import streamlit as st
from navbar import show_navbar

# Display the top bar
show_navbar()

st.title("Page 2 - User Input")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Welcome to Page 2.")
    
number = st.slider("Pick a number", 0, 100)
st.write(f"You selected: {number}")
