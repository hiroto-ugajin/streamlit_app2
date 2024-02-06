import streamlit as st
from PIL import Image

st.subheader('自己紹介')
st.text('私は宇賀神浩人\n'
    'プログラミングの勉強中です。\n'
    'とても楽しいです。')
a = '''
import streamlit as st
st.title('私のアプリ)
'''
st.code (a, language='python')

b = Image.open('./data/satsuki_marathon.jpg')
st.image(b, width=400)