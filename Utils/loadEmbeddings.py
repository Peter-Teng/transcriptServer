import os
import torch
from Utils.embeddingExtractor import getExtractor

def load():
    embeddings_dir = getExtractor().embedding_dir
    data = []
    for embedding in os.listdir(embeddings_dir):
        cur = {}
        cur["name"] = embedding.split(".")[0]
        cur["embedding"] = torch.load(os.path.join(embeddings_dir, embedding))
        data.append(cur)
    return data