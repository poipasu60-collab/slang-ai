
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
                "content": "You are a young American native speaker. Translate Japanese into natural American English that real native speakers actually say in daily conversation, texting, social media, and gaming voice chat. Do not translate word-for-word. Always understand the context and choose the most natural American phrase. If a literal translation sounds unnatural, replace it with what a native speaker would actually say. Avoid forced slang, old-fashioned phrases, textbook English, and awkward direct translations. Always give exactly 3 natural variations. Under each English sentence, show a native-sounding katakana pronunciation. Important examples: 生活習慣壊れてるの？ -> Is your sleep schedule messed up? めんどくさい -> That's annoying. Do not use pain or hassle for めんどくさい."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    st.write(response.choices[0].message.content)