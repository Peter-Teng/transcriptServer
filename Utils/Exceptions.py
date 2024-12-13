from Utils.ApiException import APIException


# Customize Exception Classes
class BadRequestException(APIException):
    httpCode = 400
    msg = 'Bad request! (Not Supported Method)'
    code = -1


class ParamFormatException(APIException):
    httpCode = 400
    msg = 'Request parameters NOT correct'
    code = -2


class InferenceException(APIException):
    httpCode = 500
    msg = 'Inference Error (See logs for more information)'
    code = -3
