"""

"""

from mas import pdfs_to_txts


def main(
    pdf_dir: str,
    output_dir: str,
):
    pdfs_to_txts(pdf_dir=pdf_dir, output_dir=output_dir, loading_method='rule')
    pdfs_to_txts(pdf_dir=pdf_dir, output_dir=output_dir, loading_method='ocr')
    pdfs_to_txts(pdf_dir=pdf_dir, output_dir=output_dir, loading_method='vlm')


if __name__ == '__main__':
    pdf_dir = r""
    output_dir = r""

    main(pdf_dir=pdf_dir, output_dir=output_dir)
