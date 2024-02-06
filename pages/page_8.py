import streamlit as st

st.subheader('入力ウィジェット2')

st.caption('テキストボックス')
a = st.text_input('テキスト入力', 'ここに入力下さい')
button_pressed = st.button('確定')
if button_pressed:
    st.write(a)
st.divider()

st.caption('テキストボックス')
a= st.number_input('数値入力')
button_pressed = st.button('数値確定')
if button_pressed:
    st.write(a)
st.divider()

st.caption('テキストエリア')
a = st.text_area('text_area')
button_pressed = st.button('文章確定')
if button_pressed:
    st.write(a)
st.divider()

st.caption('月日、時刻の設定：datetimeモジュールのインポートが必要です。')
a = '''
import datetime
'''
st.code (a, language='python')
import datetime
st.date_input('今日は何日？', datetime.date(2023, 7, 15))
st.time_input('今何時？',datetime.time(19,45))
# 現在の日付を取得
current_date = datetime.date.today()
st.write(f"現在の日付:{current_date}")
st.divider()

st.caption('カラーピッカー')
color = st.color_picker('色を選んでください', "#00ff00")
# 選択した色を表示
st.write(f'選択した色のcode: "{color}"')

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# MatplotlibのFigureとAxesを作成
fig, ax = plt.subplots()

# 四角形を描画
rectangle = patches.Rectangle((0.1, 0.1), 0.6, 0.6, linewidth=2, edgecolor=color, facecolor=color)
ax.add_patch(rectangle)

# グラフを表示
st.pyplot(fig)

# st.file_uploader（"ファイルを選んでください"）
