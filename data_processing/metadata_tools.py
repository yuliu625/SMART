"""
metadata内容:
text:
{
    'modality': 'text',
    'pdf_name': <Path.name>,
    'pdf_path': <Path>,
}
image:
{
    'modality': 'image',
    'pdf_name': <Path.parent.name>,
    'page_num': <Path.name>,
    'image_path': <Path>,
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
            pdf_path=str(pdf_path),
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
            image_path=str(image_path),
        )
        return metadata

    def get_full_text_metadata(
        self,
        pdf_path: str | Path,
        embedding_method: str
    ) -> dict:
        metadata = self.get_text_metadata(pdf_path)
        metadata['embedding_method'] = embedding_method
        return metadata

    def get_full_image_metadata(
        self,
        image_path: str | Path,
        embedding_method: str
    ) -> dict:
        metadata = self.get_image_metadata(image_path)
        metadata['embedding_method'] = embedding_method
        return metadata

