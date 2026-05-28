
import streamlit as st
st.set_page_config(

    page_title="ネイティブ英語翻訳AI",

    page_icon="🌐",

    layout="centered"

)

st.markdown("""

<style>

.stApp {

    background-color: #0f1117;

    color: white;

}

textarea, input {

    border-radius: 18px !important;

}

.stButton button {

    border-radius: 16px;

    height: 50px;

    font-size: 18px;

}

</style>

""", unsafe_allow_html=True)
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("ネイティブ英語翻訳AI")

password = st.text_input("パスワード", type="password")

if password != st.secrets["APP_PASSWORD"]:
    st.stop()

text = st.text_area("日本語を入力してね")

if st.button("翻訳する"):

    response = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": """You are a Gen Z American. Translate Japanese into natural American English that real native speakers actually use in daily conversation, texting, social media, and gaming voice chat. Do not shorten words into abbreviations like BRB, IMO, IDK, or OMG unless people would naturally say them in that exact situation. Avoid forced slang. Keep the English natural and realistic. Also show a native-sounding katakana pronunciation under each English sentence.

Examples:

めんどくさい
-> That's annoying.

生活習慣壊れてる
-> Your sleep schedule is messed up.

きもい
-> That's cringe.
"""

            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    st.write(response.choices[0].message.content)