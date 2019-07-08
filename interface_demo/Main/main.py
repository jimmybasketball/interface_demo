# -*- coding:utf-8 -*-
import unittest
from interface_demo.Main.HTMLTestRunner import HTMLTestRunner
from interface_demo.common.comm import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class Test(Common):
    def run(self):
        '''运行测试用例'''
        with open(self.Report, 'wb') as fp:
            discover = unittest.defaultTestLoader.discover \
                    (
                    # os.path.join(os.getcwd(),'cases'),
                    self.fillPath('cases'),
                    pattern='test_*.py'
                )
            print (discover)
            HTMLTestRunner(stream=fp, title=u"同步结果", description=u"同步结果").run(discover)


