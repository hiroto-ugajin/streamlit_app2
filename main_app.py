import streamlit as st
from PIL import Image

st.title("私のアプリ")
st.caption("これはテスト用です")

b = Image.open('./data/lamp.png')
st.image(b, width=200)
# 動画の表示のコード
video_file = open("./data/anime_castle.mov", "rb")
video_bytes = video_file.read()
st.video(video_bytes)