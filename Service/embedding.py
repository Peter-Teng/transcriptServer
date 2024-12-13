from Utils import Logger
from Utils.Exceptions import InferenceException
from Utils.singleton import singleton
from Utils.embeddingExtractor import *

@singleton
class embeddingService:
    def __init__(self, conf) -> None:
        self.LOGGER = Logger.getLogger()
        self.conf = conf
        self.extractor = getExtractor()

    def register(self, path, speaker):
        try:
            self.extractor.compute_embedding(wav_file=path, speaker=speaker)
        except Exception as e:
            raise InferenceException(description="Description:[%s]" % e)
        return "OK"
