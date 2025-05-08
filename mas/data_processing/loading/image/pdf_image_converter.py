"""
将pdf转换为图片的工具类。
"""

import fitz

from pathlib import Path


class PdfImageConverter:
    def __init__(self):
        ...

    def convert_pdf_to_images(
        self,
        pdf_path: str | Path,
        output_folder: str | Path = None
    ) -> None:
        """
        使用pymupdf将pdf进行转换。

        Args:
            pdf_path: 待转换的pdf的路径。
            output_folder: 转换后图片的保存路径。如果不提供，默认以pdf同名保存至同一路径下。

        Returns:
            转换，保存结果。
        """
        # 处理路径。
        pdf_path = Path(pdf_path)
        output_folder = pdf_path.parent / pdf_path.stem if output_folder is None else Path(output_folder)
        output_folder.mkdir(exist_ok=True, parents=True)
        # 读取文件。
        pdf_document = fitz.open(pdf_path)
        for page_num in range(pdf_document.page_count):
            # 加载每一页。
            page = pdf_document.load_page(page_num)
            # 将每一页转换为图片 (pixmap)。
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            # 设置图片保存路径。
            image_path = output_folder / f'page_{page_num + 1}.png'
            # 保存为PNG文件。
            pix.save(image_path)
        # 关闭PDF文件。
        pdf_document.close()
        print(f"{pdf_path.name} have been saved as images in {output_folder}.")

    def batch_convert_pdf_to_images(
        self,
        pdf_dir: str | Path,
        dir_to_save: str | Path = None,
    ):
        """
        检索一个文件夹下的所有pdf文件，将它们转换为图片，在另一个文件夹下以同名子文件夹保存。

        可能会进行的重构:
            - 递归查找所有的pdf文件。但是简单的方法会失去原本的文件树结构。
            - 额外指定分辨率。这里默认安装该项目对应的任务可以正常进行的2倍分辨率进行。

        Args:
            pdf_dir: 保存pdf的文件夹。
            dir_to_save: 要保存的新的文件夹路径。

        Returns:
            批量转换，保存结果。
        """
        # 处理路径。
        pdf_dir = Path(pdf_dir)
        dir_to_save = Path(dir_to_save)
        dir_to_save.mkdir(exist_ok=True, parents=True)
        # 识别文件
        pdf_path_list = list(pdf_dir.glob('*.pdf'))  # 以rglob方法就可以递归搜索了。
        for pdf_path in pdf_path_list:
            self.convert_pdf_to_images(pdf_path, dir_to_save / pdf_path.name)
        print(f"{pdf_dir} have been saved as images in {dir_to_save}.")


if __name__ == '__main__':
    pass
