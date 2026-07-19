import streamlit as st

from main import translate_cantonese
from speech import speech_to_text


st.title("粤语 AI 翻译 Agent")


text = st.text_area(
    "输入粤语文字"
)


audio_file = st.file_uploader(
    "上传粤语语音",
    type=["mp3","wav","m4a"]
)


if audio_file:

    with open(
        "audio.mp3",
        "wb"
    ) as f:

        f.write(
            audio_file.read()
        )


    text = speech_to_text(
        "audio.mp3"
    )


    st.write(
        "识别结果："
    )

    st.write(text)



if st.button("翻译"):

    if text:

        result = translate_cantonese(text)

        st.success(result)