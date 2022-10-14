from django.db import connection
from django.conf import settings
import os
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import json
import logging
import threading
import socket


local = threading.local()

# 优雅地记录日志
class RequestLogFilter(logging.Filter):
    """
    日志过滤器
    """

    def filter(self, record):
        record.sip = getattr(local, 'sip', 'none')
        record.dip = getattr(local, 'dip', 'none')
        record.body = getattr(local, 'body', 'none')
        record.path = getattr(local, 'path', 'none')
        record.method = getattr(local, 'method', 'none')
        record.username = getattr(local, 'username', 'none')
        record.status_code = getattr(local, 'status_code', 'none')
        record.reason_phrase = getattr(local, 'reason_phrase', 'none')

        return True


class RequestLogMiddleware(MiddlewareMixin):
    """
    将request的信息记录在当前的请求线程上。
    """

    def __init__(self, get_response=None):
        super().__init__()
        self.get_response = get_response
        self.apiLogger = logging.getLogger('web.log')

    def __call__(self, request):

        try:
            body = json.loads(request.body)
        except Exception:
            body = dict()

        if request.method == 'GET':
            body.update(dict(request.GET))
        else:
            body.update(dict(request.POST))

        local.body = body
        local.path = request.path
        local.method = request.method
        # local.username = request.user
        local.username = body.get('username', None)
        local.sip = request.META.get('REMOTE_ADDR', '')
        local.dip = socket.gethostbyname(socket.gethostname())

        response = self.get_response(request)
        local.status_code = response.status_code
        local.reason_phrase = response.reason_phrase
        self.apiLogger.info('system-auto')

        return response


def terminal_width():
    """
    Function to compute the terminal width.
    WARNING: This is not my code, but I've been using it forever and
    I don't remember where it came from.
    """
    width = 0
    try:
        import struct, fcntl, termios
        s = struct.pack('HHHH', 0, 0, 0, 0)
        x = fcntl.ioctl(1, termios.TIOCGWINSZ, s)
        width = struct.unpack('HHHH', x)[1]
    except:
        pass
    if width <= 0:
        try:
            width = int(os.environ['COLUMNS'])
        except:
            pass
    if width <= 0:
        width = 80
    return width

class SqlPrintingMiddleware(MiddlewareMixin):
    """
    Middleware which prints out a list of all SQL queries done
    for each view that is processed.  This is only useful for debugging.
    """
    def __init__(self, get_response):
        '''服务器重启之后，接收第一个请求时调用'''
        super().__init__()
        self.get_response = get_response

    def process_response(self, request, response):
        indentation = 0
        if len(connection.queries) > 0 and settings.DEBUG:
            # width = terminal_width()
            width = 160
            total_time = 0.0
            for query in connection.queries:
                # print("query是什么---", query)
                nice_sql = query['sql'].replace('"', '').replace(',',', ')
                sql = "\033[1;31m[%s]\033[0m %s" % (query['time'], nice_sql)
                total_time = total_time + float(query['time'])
                while len(sql) > width-indentation:
                    print ("%s%s" % (" "*indentation, sql[:width-indentation]))
                    sql = sql[width-indentation:]
                print ("%s%s\n" % (" "*indentation, sql))
            replace_tuple = (" "*indentation, str(total_time))
            print ("%s\033[1;32m[TOTAL TIME: %s seconds]\033[0m" % replace_tuple)
        return response


class TestMiddleware(MiddlewareMixin):
    '''中间件类'''
    def __init__(self, get_response):
        '''服务器重启之后，接收第一个请求时调用'''
        super().__init__()
        print('----init---')
        self.get_response = get_response

    def process_request(self, request):
        '''产生request对象之后，url匹配之前调用'''
        print('----process_request---')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''在url匹配之后，视图函数调用之前'''
        print('----process_view---')

    def process_response(self, request, response):
        '''在view视图函数调用之后，内容返回浏览器调用之前'''
        print('----process_response---')
        return response
