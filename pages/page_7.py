import streamlit as st

st.subheader('入力ウィジェット')

st.caption('ボタン')
st.button('空ボタン')
# ボタンが押されたかどうかを確認するための変数
button_clicked = st.button("実ボタン")
# ボタンがクリックされた場合の処理
if button_clicked:
    st.write("ボタンがクリックされました！")
st.divider()


st.caption('リンクを別ウィンドウで開く')
# ボタンが押されたかどうかの状態を保持する変数
button_clicked = st.button("Quizアプリ")
# ボタンが押されたときの処理
if button_clicked:
    # ブラウザで新しいウィンドウでリンクを開く
    st.markdown('[Visit another window](https://ugajin-quiz-999.xyz)', unsafe_allow_html=True)
st.divider()

st.caption('チェックボックス')
if st.checkbox('checkbox'):
    st.write('チェックボックスにチェック✅が入りました。')
st.divider()

st.caption('ラジオボタン')    
season = st.radio('好きな季節は？', ('春','夏','秋','冬'))
button_pressed = st.button('確定')
if button_pressed:
    st.write(f'私は{season}が大好きです！')
st.divider()
    
st.caption('セレクトボックス')      
slct = st.selectbox('セレクトボックス',('selectbox1', 'selectbox2', 'selectbox3'))
st.write(f'{slct}が選択されました')
st.divider()

st.caption('マルチセレクトボックス') 
hobby = st.multiselect('趣味', ('読書📖', 'スポーツ🏃‍♀️', '料理🍝', 'パソコン💻')) 
button_touched = st.button('決定')  
if button_touched:
    st.text(f'趣味：{", ".join(hobby)}')
    st.write(f'私の趣味は{"と".join(hobby)}です！')
st.divider()

st.caption('スライダー') 
st.slider('年齢は？',0,120,25)
st.divider()
