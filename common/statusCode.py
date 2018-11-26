#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests.exceptions import HTTPError


def codeStatus(self):
    if self.status_code == 200:
        print 'status_code:', self.status_code
    elif 300 <= self.status_code < 400:
        http_error_msg = u'%s HTTP Error: %s reason ' % (self.status_code, self.reason)
        print http_error_msg
        raise HTTPError(self.status_code)
    elif 400 <= self.status_code < 500:
        http_error_msg = u'%s HTTP Error: %s reason ' % (self.status_code, self.reason)
        print http_error_msg
        raise HTTPError(self.status_code)
    elif 500 <= self.status_code < 600:
        http_error_msg = u'%s HTTP Error: %s reason ' % (self.status_code, self.reason)
        print http_error_msg
        raise HTTPError(self.status_code)
    else:
        raise Exception('Error')
