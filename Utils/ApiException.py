from flask import request
from werkzeug.exceptions import HTTPException
import json


class APIException(HTTPException):
    # basic API Exception
    # ALL customized Exception should inherit this class
    httpCode = 500
    code = -1
    msg = 'Internal error'
    description = None

    # customized information
    def __init__(self, httpCode=None, code=None, msg=None, description=None):
        if httpCode:
            self.httpCode = httpCode
        if msg:
            self.msg = msg
        if code:
            self.code = code
        if description:
            self.description = description
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None, scope=None):
        body = dict(
            httpCode=self.httpCode,
            msg=self.msg,
            request=request.method + ' ' + self.get_url_no_parm(),
            code=self.code
        )
        text = json.dumps(body, sort_keys=False, ensure_ascii=False)
        return text

    def get_headers(self, environ=None, scope=None):
        return [('Content-Type', 'application/json')]

    def get_url_no_parm(self):
        full_path = str(request.path)
        return full_path
