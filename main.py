from openai import OpenAI

from config import API_KEY, MODEL
from prompt import SYSTEM_PROMPT
from knowledge import search_slang


client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)


def translate_cantonese(text):

    slang_info = search_slang(text)


    extra_prompt = ""

    if slang_info:
        extra_prompt = f"""

以下是检测到的粤语特殊表达：

{slang_info}

请结合这些解释进行准确翻译。
"""


    response = client.chat.completions.create(

        model=MODEL,

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": text + extra_prompt
            }

        ]

    )


    return response.choices[0].message.content



if __name__ == "__main__":

    user_input = input("请输入粤语：")

    result = translate_cantonese(user_input)

    print(result)