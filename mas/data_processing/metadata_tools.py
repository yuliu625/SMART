"""
metadata内容:
text:
{
    'modality': 'text',
    'pdf_name': <Path.name>,
}
image:
{
    'modality': 'image',
    'pdf_name': <Path.parent.name>,
    'page_num': <Path.name>,
}
"""


from pathlib import Path


class MetadataTools:
    def __init__(self):
        pass

    def get_text_metadata(
        self,
        pdf_path: str | Path,
    ) -> dict:
        pdf_path = Path(pdf_path)
        metadata = dict(
            modality='text',
            pdf_name=str(pdf_path.name),
        )
        return metadata

    def get_image_metadata(
        self,
        image_path: str | Path,
    ) -> dict:
        image_path = Path(image_path)
        metadata = dict(
            modality='image',
            pdf_name=str(image_path.parent.name),
            page_num=str(image_path.name),
        )
        return metadata

