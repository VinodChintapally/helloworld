import streamlit as st

# Set the port for Streamlit
st.set_option('server.port', 8000)

# Title of the web app
st.title("Azure Web App Connection Check")

# Simple test to show a connection check
st.write("This is a simple Streamlit app deployed on Azure Web App.")

# Button to check connection
if st.button("Check Connection"):
    st.success("Connection successful! Your app is running on Azure.")