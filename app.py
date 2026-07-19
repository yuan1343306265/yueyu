import streamlit as st

from main import translate_cantonese


st.title("粤语翻译 Agent")

st.write("输入粤语，AI自动翻译成普通话")


text = st.text_area(
    "请输入粤语："
)


if st.button("翻译"):

    if text:

        result = translate_cantonese(text)

        st.success("翻译结果")

        st.write(result)

    else:

        st.warning("请输入内容")