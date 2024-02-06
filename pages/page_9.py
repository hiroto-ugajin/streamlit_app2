import streamlit as st 
from PIL import Image

st.subheader('メディアを表示するメソッド')

image = Image.open('./data/pc.png')
st.image(image, width=250, caption='イメージ')
st.divider()

st.caption('音声ファイルの再生')
audio_file = open('./data/drum.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')
st.divider()

st.caption('動画ファイルの再生')
video_file = open ('./data/hanabi_anime.mov', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

