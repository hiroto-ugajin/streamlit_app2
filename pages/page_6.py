import streamlit as st 
import pandas as pd

st.text('データ表示系メソッド')
st.subheader('テーブルウィジェット')

st.caption('静的なテーブルを作成する')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.table(df)
st.divider()

st.caption('インタラクティブなテーブルを作成する')
st.caption('コピーやソートが可能です')
st.dataframe(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
st.divider()

st.caption('テーブルのスタイルを編集する')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.dataframe(df.style.background_gradient())
st.divider()

st.caption('テーブルのデータを編集できる')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.data_editor(df, num_rows = "dynamic")
