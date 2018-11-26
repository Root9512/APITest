# encoding:utf-8
'''
Created on 2018年11月26日

@author: chengchen
'''
import unittest
import requests
from requests.exceptions import HTTPError
import json
from common import urlParam, paramete, statusCode


class TestAPI(unittest.TestCase):
    def setUp(self):
        print("start test")
        pass

    def tearDown(self):
        print("end test")
        pass

class test_resumeDownloads(TestAPI):
    def test_resumeDownloads(self):
        ResumeDownloads_url = urlParam.urlParam.resumeDownloads_url
        form_data = paramete.paramete.form_resumeDownloads
        headers = {'content-type': 'application/json'}

        if 'true' in form_data.values():
            print "数据完整性如下:"
            r = requests.post(url=ResumeDownloads_url, data=json.dumps(form_data), headers=headers)
            print r.text

            status = statusCode.codeStatus(r)
            print(status)



if __name__ == '__main__':
    unittest.main()