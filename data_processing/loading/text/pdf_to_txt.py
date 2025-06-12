"""

"""

from .text_processor import PymupdfTextLoader

from pathlib import Path

from typing import Literal


def pdfs_to_txts(
    pdf_dir: str | Path,
    output_dir: str | Path,
    loading_method: Literal['rule', 'ocr', 'vlm'],
):
    # 处理路径。这里默认按照loading_method创建子文件夹。
    pdf_dir = Path(pdf_dir)
    output_dir = Path(output_dir) / loading_method
    output_dir.mkdir(exist_ok=True, parents=True)
    # 获取所有的pdf文件。
    pdf_paths = list(pdf_dir.glob('*.pdf'))

    for pdf_path in pdf_paths:
        # 命名为pdf相同名称但是扩展名不同。
        output_path = output_dir / f"{pdf_path.name}.txt"
        # 会检查存在情况，增量式更新。
        if not output_path.exists():
            pdf_loader = PymupdfTextLoader(pdf_path)
            documents = pdf_loader.run(loading_method=loading_method)
            # 序列化，仅保存content。
            content = documents[0].page_content
            with open(output_path, "w", encoding='utf-8') as text_file:
                text_file.write(content)

