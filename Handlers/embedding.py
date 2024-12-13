
from Utils import Logger
import time
import json
from Utils.Exceptions import *
from Service.embedding import embeddingService

class registerHandler():
    def post(request):
        LOGGER = Logger.getLogger()
        LOGGER.info("[%s] - Receive from [%s] - Path[%s]" % (request.method, request.remote_addr, request.path))
        try:
            params = json.loads(request.get_data())
            path = params['path']
            speaker = params['speaker']
        except Exception as e:
            print(repr(e))
            raise ParamFormatException()
        
        start = time.time()  # 记录开始时间
        service = embeddingService()
        data = service.register(path, speaker)
        elapse_time = time.time() - start
        LOGGER.debug("Inference Time : %2.2f ms" % (elapse_time * 1000))
        LOGGER.debug(str(data))
        return {"code": "0", "describe": "success", "data": data}