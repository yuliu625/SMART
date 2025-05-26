"""

"""

import base64
from PIL import Image
from io import BytesIO


class PILImageBridge:
    @staticmethod
    def base64_to_pil(
        image_base64: str,
    ) -> Image.Image:
        """
        将base64字符串转换为原始图片。

        主要用于:
            - 可视化查看图片。测试转换正常。
            - 读写。转换为模型可接受格式，转换为VLM-API可传输格式。

        Args:
            image_base64: 图片的base64编码后的字符串。

        Returns:
            (Image)，二进制图片格式。
        """
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))
        return image

    @staticmethod
    def uri_to_base64(
        uri: str,
    ) -> str:
        """
        从uri读取图片转换为base64字符串。

        Args:
            uri: 图片的uri。

        Returns:
            (str), base64字符串。
        """
        with open(uri, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

