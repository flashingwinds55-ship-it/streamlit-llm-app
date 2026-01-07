from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def get_llm_response(input_text, expert_type):
    if expert_type == "A":
        system_prompt = "あなたは優秀なファッションスタイリストです。"
    else:
        system_prompt = "あなたは優秀な旅行プランナーです。"

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [SystemMessage(content=system_prompt),
                HumanMessage(content=input_text)]
    result = llm(messages)
    return result.content

st.title("専門家チャットアプリ")
st.write("##### 動作モード1: ファッションスタイリスト")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで、ファッション専門家のアドバイスが得られます。")
st.write("##### 動作モード2: 旅行プランナー")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで、旅行プランナーのアドバイスが得られます。")

selected_mode = st.radio(
    "動作モードを選択してください。",
    ["ファッションスタイリスト", "旅行プランナー"]

)
st.divider()

if selected_mode == "ファッションスタイリスト":
    input_message = st.text_input(label="ファッションに関する質問を入力してください。")
    expert_type = "A"
else:
    input_message = st.text_input(label="旅行に関する質問を入力してください。")
    expert_type = "B"

if st.button("実行"):
    st.divider()
    if input_message.strip():
        response = get_llm_response(input_message, expert_type)
        st.write(response)
    else:
        st.error("入力フォームが空です。質問を入力してください。")
