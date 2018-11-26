#encoding:utf-8
'''
Created on 2018年9月17日

@author: chengchen
'''
import unittest  
import requests
import json
from common import urlParam, paramete, statusCode
from common.logger import Log

class TestAPI(unittest.TestCase):    
    def setUp(self):                 
        print("start test")  
        pass

    def tearDown(self):             
        print("end test")  
        pass

class test_List(TestAPI):
    log = Log()
    def test_getList(self):

        List_url = urlParam.urlParam.getList_url
        form_data = paramete.paramete.form_getList
        headers = {'content-type': 'application/json'}

        r = requests.post(url=List_url, data=json.dumps(form_data), headers=headers)
        content = r.text
        
        if '查询简历信息成功'in content:
            print "数据完整性如下:",content
            self.log.info("查询简历信息结果：\n %s"%content)
            status = statusCode.codeStatus(r)
            print(status)




if __name__ == '__main__':
    unittest.main()  