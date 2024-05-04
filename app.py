import streamlit as st
import pandas as pd
import base64
import random
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv("movies.csv")

# Set page width
st.set_page_config(layout="wide")

# Sidebar
st.sidebar.title("Movie Data App")

# Function to generate and download Markdown file
def download_markdown(data):
    markdown_text = data.to_markdown(index=False)
    b64 = base64.b64encode(markdown_text.encode()).decode()
    href = f'<a href="data:text/csv;base64,{b64}" download="movies.md" class="download-link">Download Markdown File</a>'
    st.sidebar.markdown(href, unsafe_allow_html=True)

# Main content
st.title("Movie Data App")

# Display the DataFrame
st.write(data)

# Add a button to download the Markdown file
if st.button("Download Markdown"):
    download_markdown(data)

# Display the Markdown content
st.subheader("Preview Markdown:")
markdown_text = data.to_markdown(index=False)
st.markdown(markdown_text, unsafe_allow_html=True)

# Generate random data for the chart
num_points = 20
random_data = [random.randint(0, 100) for _ in range(num_points)]

# Create a line chart
st.subheader("Random Data Chart")
plt.plot(random_data)
st.pyplot(plt)
