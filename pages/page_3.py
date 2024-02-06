import streamlit as st
import pandas as pd

st.text('私のトレーニングの記録です')

df = pd.read_csv('./data/refre.csv')
# , index_col='2014'
st.dataframe(df)
st.line_chart(df)
st.bar_chart(df)
#    st.bar_chart(df.set_index('2014'))


    
