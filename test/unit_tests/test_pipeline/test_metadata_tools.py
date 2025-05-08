"""

"""

from mas.data_processing.metadata_tools import MetadataTools


def test_metadata_tools():
    metadata_tools = MetadataTools()
    print(metadata_tools.get_image_metadata(r"D:\dataset\risk_mas_t\image_pdf\1910.13461v1.pdf\page_1.png"))


if __name__ == '__main__':
    test_metadata_tools()
