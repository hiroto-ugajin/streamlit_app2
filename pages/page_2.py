import streamlit as st

st.text('あなたのことを、教えてください。情報は収集していません。下段に私からの挨拶が返信されるだけです。')

with st.form(key = 'profile_form'):
    name = st.text_input("名前")
    address = st.text_input("住所")
    age_category = st.selectbox(
    '年齢層',
    ('子ども（18才未満)', '大人（18才以上)'))
    sex = st.radio(
    '性別',
    ('男性', '女性'))
    hobby = st.multiselect('趣味', ('読書📖', 'スポーツ🏃‍♀️', '料理🍝', 'パソコン💻'))
    
#     start_date = st.date_input(
#             '誕生日',
#             datetime.data(2022, 1,1)
#     )
    
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")

    if submit_btn :      
        st.text(f"ようこそ、{name}さん。よくお越し下さいました。{address}は素敵なところですネ😆")
        st.text(f"年齢層：{age_category}")
        st.text(f"性別：{sex}")
        st.text(f'趣味：{", ".join(hobby)}')
        # st.text(f'誕生日：{start_date}')