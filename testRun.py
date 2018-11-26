#encoding:utf-8
'''
Created on 2018年11月26日

@author: chengchen
'''
import smtplib
import unittest
import time
from HTMLTestRunnerCN import HTMLTestRunner
from email.mime.text import MIMEText
import os

'''
#自动发邮件
def send_mail(file_new):
    mail_from='cheng_chen@hoperun.com'
    mail_to='cheng_chen@hoperun.com'
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject']=u"自动化测试报告"
    smtp=smtplib.SMTP()
    smtp.connect('smtp.263.net')
    smtp.login('cheng_chen@hoperun.com','xmxel9516')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print('email has send out !')

#获取最新测试报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new
'''

test_dir = './testCase/'
# test_report = './Report/'
discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')  
'''print os.path.dirname(sys.argv[0])'''

    
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './Report/testReport' + now + 'test_result.html'
    fp = file(filename,"wb")
    runner = HTMLTestRunner(stream=fp,title = u'人资系统接口自动化测试报告',description =u'测试用例执行情况:',tester =u'成晨')
    runner.run(discover)
    fp.close()

'''
    new_report = new_report(test_report)
    send_mail(new_report)
'''