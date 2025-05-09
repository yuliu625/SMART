"""

"""

import base64
from PIL import Image
from io import BytesIO


def base64_to_pil(
    image_base64: str,
) -> Image.Image:
    image_data = base64.b64decode(image_base64)
    image = Image.open(BytesIO(image_data))
    return image

