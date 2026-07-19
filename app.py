import streamlit as st

from main import translate_cantonese
from speech import speech_to_text


st.title("粤语 AI 翻译 Agent")


st.divider()


# 文字输入

st.subheader("文字输入")

text_input = st.text_area(
    "请输入粤语"
)


if st.button("翻译文字"):

    if text_input:

        result = translate_cantonese(
            text_input
        )

        st.success(result)


st.divider()


# 语音输入

st.subheader("语音输入")


audio_file = st.file_uploader(
    "上传粤语语音",
    type=[
        "mp3",
        "wav",
        "m4a"
    ]
)


if audio_file:

    with open(
        "temp_audio.mp3",
        "wb"
    ) as f:

        f.write(
            audio_file.read()
        )


    if st.button("识别并翻译语音"):

        with st.spinner(
            "正在识别粤语..."
        ):

            text = speech_to_text(
                "temp_audio.mp3"
            )


        st.info(
            "识别结果：" + text
        )


        result = translate_cantonese(
            text
        )


        st.success(
            result
        )