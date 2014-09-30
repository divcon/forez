# -*- coding: utf-8 -*-
import httplib2
import json


class api_request(object):
    _headers = None
    _host = None
    body = None
    url = None
    #host = "http://211.189.127.73:8000"
    test = None

    def __init__(self, test):
        self.test=test

    def http_request(self, url, method="GET", headers=None, body=None):
        h = httplib2.Http()
        request_url = self.host + url
        request_body = None
        request_header = dict()
        request_header.update(self.headers)
        if not headers is None:
            request_header.update(headers)
            print request_header
        if not body is None:
            request_body = json.dumps(body)
            print str(type(body))
            print str(type(request_body))
            print request_body
        resp, content = h.request(request_url, method=method, body=request_body, headers=request_header)
        return resp, content

    def get_request(self, url=None, header=None, query=None):
        pass

    @property
    def headers(self):
        self._headers = dict()
        self._headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json; charset=UTF-8',
        }
        return self._headers
 
    @property
    def host(self):
        if self.test == True:
            self._host = "http://localhost:8000"
        else:
            self._host = "http://211.189.127.73:8000"
        return self._host
