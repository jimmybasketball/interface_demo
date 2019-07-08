# -*- coding:utf-8 -*-
#author by hujiuanji http post 方法总结
####定义
# import requests
# url='http://mallapi.dev.epet.com/v3/content/Tools/Eat.html?do=Suggest'
# data={'keyword':'菜'}
# # def requestWithCookie():
# #     try:
# #         ssrequest = requests.session()
# #         requests.utils.add_dict_to_cookiejar(ssrequest.cookies, BCOOKIES)
# #         response = ssrequest.get(url, headers=headers, params=params, timeout=float(30),verify=False)
# #         # response.raise_for_status()
# #         return response
# #     except Exception,e:
# #         raise e
# #
# #         return None
# r=requests.post(url,data)
# print r
# print r.url
# print r.text
# print r.content
# post方法 json发送数据
import  requests
import  json
import traceback
class m_post():
    def __init__(self,url,data):
        self.url=url
        self.data=data
        self.headers={}
        self.file={}
        self.cookie={}

    def post(self):
        try:
            response=requests.post(url=self.url,headers=self.headers,data=self.data,timeout=30)
            return response
        except Exception,e:
            raise e

    def postwithJson(self):
        try:
            response=requests.post(url=self.url,headers=self.headers,json=self.data,timeout=30)
            return response
        except Exception,e:
            raise e

    def postwithFile(self):
        try:
            response=requests.post(url=self.urf,headers=self.headers,data=self.data,file=self.file,timeout=30)
            return response
        except Exception,e:
            raise e

    def postwithCookie(self):
        try:
            get_cookie=requests.post(url='http://mall.api.epet.com/v3/login.html?do=postSubmit',data={'postsubmit':'r9b8s7m4','username':'epet','password':'epetbar'})
            m_cookie=get_cookie.cookies
            print get_cookie._content
            response=requests.post(url='http://mallapi.dev.epet.com/v3/content/opgc/Index.html?do=GetList',data={'pid':'2000027','param':'0'},cookies=m_cookie)
            return response
        except Exception,e:
            raise e





class m_get():
    def __init__(self):
        url={}
        headers={}
        data={}
        file={}
        cookie={}

    def get(self):
        try:
            response=requests.get(url=self.url, headers=self.headers, params=self.params, timeout=30,verify=False)
            return response
        except Exception,e:
            raise e

    def getwithCookie(self):
        try:
            serequest=requests.session()
            requests.utils.add_dict_to_cookiejar(serequest.cookies, self.cookie)
            response=requests.post(url=self.url,headers=self.headers,json=self.data,timeout=30)
            return response
        except Exception,e:
            raise e






if __name__=='__main__':
    a=m_post('www.baidu.com',{})
    print a.postwithCookie().content





