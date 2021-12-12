import streamlit as st


options = ['hello', 'world']
st.sidebar.selectbox('Options', options)
st.title("Hello world")
st.write("This is my first web hosted application")

video_file = open('covid.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
