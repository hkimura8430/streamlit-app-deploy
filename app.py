import streamlit as st

st.title("旅行チャットボット")

st.write("##### 希望の専門家を選択してください")
st.write("A:観光スポットに詳しい専門家")
st.write("B:グルメに詳しい専門家")

selected_item = st.radio(
    "お好きな専門家を選択してください。",
    ["A:観光スポットに詳しい専門家", "B:グルメに詳しい専門家"]
)

#LLMに投げるプロンプトを受け取る
input_message = st.text_input(label="質問を入力してください")

#LangChainを使ってLLMにプロンプトを渡す
if st.button("実行"):



