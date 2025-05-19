"""

"""

from pathlib import Path


def load_txt(file_path: str | Path) -> str:
    """
    从指定路径读取.txt文件的文本。

    Args:
        file_path: .txt文件的路径。

    Returns:
        读取的str文本。
    """
    file_path = Path(file_path)
    text = file_path.read_text(encoding='utf-8')
    return text

