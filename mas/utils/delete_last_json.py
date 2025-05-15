"""

"""

import re


def delete_last_json(text: str):
    pattern = r'```json(.*?)```'
    matches = list(re.finditer(pattern, text, re.DOTALL))
    last = matches[-1]
    start, end = last.span()
    return text[:start] + text[end:]
