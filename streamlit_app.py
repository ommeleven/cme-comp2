import streamlit as st
from navbar import show_navbar
import numpy as np
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="Single-Page Streamlit App", layout="wide")

# CSS to hide the sidebar hamburger menu and footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Initialize session state for page tracking
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Display the top navigation bar
show_navbar()

# Page content logic
if st.session_state.page == 'home':
    st.title("Home Page")
    st.write("This is the home page. Use the top bar to navigate to other pages.")

elif st.session_state.page == 'page1':
    st.title("Page 1 - Data Overview")
    
    # Example data
    data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=['A', 'B', 'C']
    )

    st.write("Here is a random data table:")
    st.dataframe(data)

    st.write("And here is a line chart of the data:")
    st.line_chart(data)

elif st.session_state.page == 'page2':
    st.title("Page 2 - User Input")

    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}! Welcome to Page 2.")
    
    number = st.slider("Pick a number", 0, 100)
    st.write(f"You selected: {number}")

elif st.session_state.page == 'page3':
    st.title("Page 3 - Data Overview")
    
    # Example data
    data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=['A', 'B', 'C']
    )

    st.write("Here is a random data table:")
    st.dataframe(data)

    st.write("And here is a line chart of the data:")
    st.line_chart(data)
