# _*_ coding: utf-8 _*_

import time
from ipware.ip import get_real_ip
from DjangoBlog.utils import cache


class OnlineMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        http_user_agent = request.META.get('HTTP_USER_AGENT', [])
        if 'Spider' in http_user_agent or 'spider' in http_user_agent:
            return response

        cast_time = time.time() - start_time
        response.content = response.content.replace(b'<!!LOAD_TIMES!!>', str.encode(str(cast_time)[:5]))
        return response
