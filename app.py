
import streamlit as st
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
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a young American native speaker. Translate Japanese into natural American English that real native speakers actually say in daily conversation, texting, social media, and gaming voice chat. Do not translate word-for-word. Always understand the context and choose the most natural American phrase. If a literal translation sounds unnatural, replace it with what a native speaker would actually say. Avoid forced slang, old-fashioned phrases, textbook English, and awkward direct translations. Keep it casual, realistic, and natural. Also show a native-sounding katakana pronunciation under each English sentence."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    st.write(response.choices[0].message.content)