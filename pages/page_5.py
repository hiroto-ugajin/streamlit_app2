import streamlit as st
import math
from PIL import Image

st.subheader('スライダーウィジェット')

st.text('自然数のスライダーです\n'
    '簡単な計算結果も表示されます🤔\n'
    '"math"をimportしているので、平方根も計算されます\n'
    'このページは、たった14行のcodeです😅')

x= st.slider('x')

st.write(x, 'を2倍にすると', 2*x)

st.write(x, 'を２乗すると', x*x)

st.write(x, 'の平方根は', math.sqrt(x))

b = Image.open('./data/math.png')
st.image(b, width=200)