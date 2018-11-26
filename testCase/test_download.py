# encoding:utf-8
'''
Created on 2018年11月26日

@author: chengchen
'''
import unittest
import requests
import json
from common import urlParam, paramete, statusCode


class TestAPI(unittest.TestCase):
    def setUp(self):
        print("start test")
        pass

    def tearDown(self):
        print("end test")
        pass


class test_Download(TestAPI):
    def test_download(self):

        Download_url = urlParam.urlParam.download_url
        form_data = paramete.paramete.form_download
        headers = {'content-type': 'application/json'};

        if '7cbda4fbecbd4c7a8d95ba1f995c5b5e' in form_data.values():
            print "数据完整性如下:"
            r = requests.post(url=Download_url, data=json.dumps(form_data), headers=headers)
            print r.text

            status = statusCode.codeStatus(r)
            print(status)


if __name__ == '__main__':
    unittest.main()