from faster_whisper import WhisperModel
import streamlit as st


@st.cache_resource
def get_model():

    return WhisperModel(
        "tiny",
        device="cpu",
        compute_type="int8"
    )


model = get_model()


def speech_to_text(audio_path):

    segments, info = model.transcribe(
        audio_path,
        language="zh"
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text