"""
多模态的情况下，以list[dict]传递HumanMessage时，对于content=[text_dict | image_dict]的封装。
"""


def get_image_content_dict_from_base64(
    base64_str: str,
    image_type: str = 'png',
) -> dict:
    image_content_dict = {
        'type': 'image',
        'source_type': 'base64',
        'mime_type': f'image/{image_type}',
        'data': base64_str,
    }
    return image_content_dict


def get_text_content(
    text: str,
):
    text_content_dict = {
        'type': 'text',
        'text': text,
    }
    return text_content_dict
