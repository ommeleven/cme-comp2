import streamlit as st
from navbar import show_navbar
import numpy as np
import pandas as pd

# Display the top bar
show_navbar()

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
