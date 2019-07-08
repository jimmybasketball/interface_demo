# encoding=utf-8
from interface_demo.common import comm
import unittest
import json
import requests
import paramunittest

getRequestInfo_xls= comm.Common().get_xls("data.xlsx","user")

@paramunittest.parametrized(*getRequestInfo_xls)
class GoodsListBiaoQian(unittest.TestCase):

    def setParameters(self,case_name,method,gids,biaoqian):
        self.case_name = str(case_name)
        # self.url = str(requestUrl)
        self.method = str(method)
        self.gids=str(gids)
        self.biaoqian = biaoqian
        self.url="https://mall.api.epet.com/v3/goods/list/list.html?" \
                 "do=dynamic&appname=epetmall&distinct_id=22990222799145077&duuid=947BF6F5BAF24F009D9AACD774BC8072" \                
                 "&hash=&id_param=&iphone_model=iPhone7%2C2&page=1&postsubmit=r9b8s7m4&system=ios&version=446&debug=1"

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        print(self.case_name+"测试开始前准备")

    def testBiaoQian(self):
        #set URL
        print("第一步：设置url  "+self.url)

        print(self.url)

        # self.url = "https://mall.api.epet.com/v3/user/sign/UserSign.html"

        # set headers
        # header = {"Content-Type": "application/json"}
        # configHttp.set_headers(header)
        # print("第二步：设置header(token等)")
        #
        content={'gids':self.gids}
        self.return_json =requests.post(self.url,data=content)
        # method = str(self.return_json.request)[
        #          int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法：" + self.method)

        # check result
        # self.tearDown()
        print("第五步：检查结果")
        print(self.return_json.text)
        self.checkResult()

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.return_Info = self.return_json.json()

        # return_data = (json.loads(self.return_json.text))['data']

        #获取商品列表页的商品的标签信息
        aa = json.loads(self.return_Info.text)
        dict_gid = {}
        for i in aa['data']['lists']:
            gid = i['data']['gid']
            print(i['data']['gid'])
            label = []
            try:
                if i['data']['activity']:
                    for j in i['data']['activity']:
                        print(j['label'])
                        label.append(j['label'])
                        dict_gid[gid]=label
            except KeyError:
                print('gid have not activity')
        if dict_gid:
            pass
