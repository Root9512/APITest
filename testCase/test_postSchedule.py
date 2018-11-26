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


class test_postSchedule(TestAPI):
    def test_findPostSchedule(self):
        PostSchedule_url = urlParam.urlParam.findPostSchedule_url
        form_data = paramete.paramete.form_findPostSchedule
        headers = {'content-type': 'application/json'}

        r = requests.post(url=PostSchedule_url, data=json.dumps(form_data), headers=headers)
        content = r.text

        if '查询简历匹配详情成功' in content:
            print "数据完整性如下:",content

            status = statusCode.codeStatus(r)
            print(status)



if __name__ == '__main__':
    unittest.main()