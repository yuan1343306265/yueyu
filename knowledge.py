import json
import os


def search_slang(text):

    file_path = os.path.join(
        os.path.dirname(__file__),
        "knowledge",
        "slang.json"
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        slang_dict = json.load(f)


    result = []

    for word, meaning in slang_dict.items():

        if word in text:
            result.append(
                f"{word}: {meaning}"
            )

    return "\n".join(result)