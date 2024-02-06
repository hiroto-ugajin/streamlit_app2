import streamlit as st
import requests
from PIL import Image

def get_address(zipcode):
    # 郵便番号検索APIのURL
    api_url = 'https://zipcloud.ibsnet.co.jp/api/search'

    # APIに渡すパラメータ
    params = {'zipcode': zipcode}

    # APIリクエスト
    response = requests.get(api_url, params=params)

    # レスポンスのJSONを取得
    data = response.json()

    # 住所情報がある場合は取得し、ない場合はエラーメッセージを返す
    if data['results']:
        address = data['results'][0]['address1'] + data['results'][0]['address2'] + data['results'][0]['address3']
        return address
    else:
        return '該当する住所が見つかりません'

# Streamlitアプリケーションの開始
st.title('郵便番号検索アプリ')

# 入力ボックスの表示
zipcode = st.text_input('郵便番号を入力してください')

# 入力ボックスが空でない場合、APIを呼び出して結果を表示
if zipcode:
    address = get_address(zipcode)
    st.write('検索結果:', address)
    
    
b = Image.open('./data/post.png')
st.image(b, width=100)
