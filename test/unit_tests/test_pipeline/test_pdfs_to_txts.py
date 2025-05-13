"""

"""

from mas.data_processing.loading.text.pdf_to_txt import pdfs_to_txts


def test_pdfs_to_txts():
    pdfs_to_txts(
        pdf_dir=r"D:\dataset\risk_mas_t\original_pdf",
        output_dir=r"D:\dataset\risk_mas_t/txt_pdf",
        loading_method='ocr'
    )


if __name__ == '__main__':
    test_pdfs_to_txts()
