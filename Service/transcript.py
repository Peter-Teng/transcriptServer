import torch
from Utils import Logger
from Utils.Exceptions import InferenceException
from Utils.singleton import singleton
from Utils.embeddingExtractor import getExtractor
from Utils.loadEmbeddings import load
import soundfile
import librosa
import numpy as np
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

@singleton
class transcriptModel:
    def __init__(self, conf) -> None:
        self.LOGGER = Logger.getLogger()
        self.LOGGER.info("------------NOW Initializing Model------------")
        self.conf = conf
        self.transcript_model_id = self.conf["transcript_model"]
        self.vad_model_id = self.conf["vad_model"]
        self.transcript_model = AutoModel(
            model=self.transcript_model_id,
            trust_remote_code=False,
            disable_update=True,
            device="cuda:0",
        )        
        self.vad_model = AutoModel(model=self.vad_model_id, trust_remote_code=False, disable_update=True, device="cuda:0",)
        self.extractor = getExtractor()
        self.LOGGER.info("------------Model Initialized------------")

    def transcript(self, path):
        try:
            speech, sample_rate = soundfile.read(path)
            # 对双声道的音频不支持，降为单声道
            if speech.ndim == 2 and speech.shape[1] == 2:
                speech = np.mean(speech, axis=1)
            # resample audio to 16kHz(因为fsmn-vad模型支持16KHz的音频的分割)
            if sample_rate != 16000:
                speech = librosa.resample(speech, orig_sr = sample_rate, target_sr = 16000)
            chuncksInfo = self.vad_model.generate(input=speech, chunk_size=speech.shape[0])
            results = []
            speakers = load()
            i = 0
            for chunk in chuncksInfo[0]['value']:
                # 计算音频开始和结束的时间（chunk[0]是开始时间，[1]是结束的时间，单位都是毫秒，所以分割点要×16000（采样率）再÷1000）
                start = chunk[0] * 16
                end = chunk[1] * 16
                speaker = self.get_speaker(speech[start:end], speakers)
                sentence = self.transcript_model.generate(
                    input=speech[start:end],
                    cache={},
                    language="auto",  # "zh", "en", "yue", "ja", "ko", "nospeech"
                    use_itn=True,
                    batch_size_s=60,
                    chunk_size=end-start
                )
                content = rich_transcription_postprocess(sentence[0]["text"])
                results.append({"speaker": speaker, "content": content})
                i += 1 
        except Exception as e:
            raise InferenceException(description="Description:[%s]" % e)
        ret = []
        ret.append({"transcript_results" : results})
        return ret
    
    
    def get_speaker(self, speech, speakers):
        speaking_embedding = self.extractor.compute_embedding(speech, save=False)
        max_score = 0
        speaking = "unknown"
        for speaker in speakers:
            similarity = torch.nn.CosineSimilarity(dim=-1, eps=1e-6)
            score = similarity(speaking_embedding, speaker["embedding"]).item()
            if score > max_score:
                max_score = score
                speaking = speaker["name"]
        if max_score < self.conf["simularity_threshold"]:
            return "unknown"
        return speaking