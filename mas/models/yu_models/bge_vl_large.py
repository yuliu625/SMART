"""

"""

from transformers import AutoModel
import torch
from PIL import Image

from langchain_core.embeddings import Embeddings


class BGEVLLarge(Embeddings):
    def __init__(
        self,
        model_path: str,
    ):
        self.model = AutoModel.from_pretrained(model_path, trust_remote_code=True)
        self.model.set_processor(model_path)
        self.model.eval()

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self.embed_text(texts)

    def embed_query(self, query: str) -> list[float]:
        return self.embed_text([query])[0]

    def embed_text(
        self,
        inputs: list[str]
    ) -> list[list[float]]:
        with torch.no_grad():
            text_features = self.model.encode(text=inputs)
        #     text_features = [self.model.encode(
        #         text=text,
        #     ) for text in inputs]
        # return [text_feature.tolist()[0] for text_feature in text_features]
        return text_features.tolist()

    def embed_image(
        self,
        uris: list[str],
    ) -> list[list[float]]:
        with torch.no_grad():
            image_features = self.model.encode(
                images=uris,
            )
        return image_features.tolist()

