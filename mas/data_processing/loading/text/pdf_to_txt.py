"""

"""

from .text_processor import PymupdfTextLoader

from pathlib import Path


def pdfs_to_txts(
    pdf_dir: str | Path,
    output_dir: str | Path,
    loading_method: str,
):
    pdf_dir = Path(pdf_dir)
    output_dir = Path(output_dir) / loading_method
    output_dir.mkdir(exist_ok=True, parents=True)

    pdf_paths = list(pdf_dir.glob('*.pdf'))

    for pdf_path in pdf_paths:
        output_path = output_dir / f"{pdf_path.stem}.txt"
        if not output_path.exists():
            pdf_loader = PymupdfTextLoader(pdf_path)
            documents = pdf_loader.run(loading_method=loading_method)
            content = documents[0].page_content
            with open(output_path, "w", encoding='utf-8') as text_file:
                text_file.write(content)

