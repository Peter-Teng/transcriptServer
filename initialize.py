from flask import request
import traceback
import yaml
from modelscope.hub.snapshot_download import snapshot_download
from Service.transcript import transcriptModel
from Service.embedding import embeddingService
from Handlers import transcript, embedding
from Utils.Logger import *
from Utils.embeddingExtractor import *
from Utils.Exceptions import *


# init all routes
def initRoutes(app, conf):
    @app.route(conf["transcript_route"], methods=['GET', 'POST'])
    def handle_transcript():
        if request.method == "POST":
            return transcript.transcriptHandler.post(request)
        else:
            raise BadRequestException()
    
    @app.route(conf["embedding_route"], methods=['GET', 'POST'])
    def handle_embedding():
        if request.method == "POST":
            return embedding.registerHandler.post(request)
        else:
            raise BadRequestException()


def initModels(conf):
    snapshot_download(model_id='iic/speech_campplus_sv_zh_en_16k-common_advanced', revision="v1.0.0", local_dir=conf["embedding_model"])   
    snapshot_download(model_id='iic/SenseVoiceSmall', local_dir=conf["transcript_model"])
    snapshot_download(model_id='iic/speech_fsmn_vad_zh-cn-16k-common-pytorch', local_dir=conf["vad_model"])
    

def init(app, args):
    # initialize service
    # load config
    with open('config.yaml', 'r', encoding='utf-8') as file:
        conf = yaml.load(file, Loader=yaml.FullLoader)
    initRoutes(app, conf)
    # initialize global exception handler
    initExceptionHandler(app)

    # Initialize singleton classes here!
    initLogger()
    if args.download:
        initModels(conf)
    initExtractor(conf)
    LOGGER = getLogger()
    LOGGER.info("------------Initializing------------")
    if args.device == -1:
        args.device = 'cpu'
    else:
        args.device = 'cuda:%s' % args.device
    
    # initialize service
    transcriptModel(conf)
    embeddingService(conf)

    print("--Server Started--")


def initExceptionHandler(app):
    # global Exception handler
    @app.errorhandler(Exception)
    def framework_error(e):
        LOGGER = getLogger()
        if isinstance(e, APIException):  # if the exception is defined by users
            LOGGER.error("ERROR[%s-%s] : %s - Traceback Information:\n %s" % (
                e.msg, e.code, e.description, traceback.format_exc()))
            return {'code': e.code, 'describe': e.msg, 'objList':[]}, e.httpCode
        else:  # other exceptions
            if not app.config['DEBUG']:
                LOGGER.error("ERROR : [%s] \n%s" % (repr(e), traceback.format_exc()))
                return {'code': -5, 'describe': repr(e), 'objList':[]}, 500
            else:
                return e
