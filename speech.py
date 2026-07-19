from openai import OpenAI
from config import API_KEY


client = OpenAI(
    api_key=API_KEY
)


def speech_to_text(audio_file):

    audio = open(
        audio_file,
        "rb"
    )

    result = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio,
        language="zh"
    )

    return result.text