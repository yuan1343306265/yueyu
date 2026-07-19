import whisper
import streamlit as st


@st.cache_resource
def load_whisper():

    return whisper.load_model("tiny")


model = load_whisper()


def speech_to_text(audio_file):

    result = model.transcribe(
        audio_file,
        language="zh"
    )

    return result["text"]