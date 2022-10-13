

import requests,json

DEFAULT_GROUP_NAME = "DEFAULT_GROUP"

class NacosClient:
    ACCESS_TOKEN=None
    '''
    host = nacos服务地址
    username = 用户
    password = 密码
    namespace = 命名空间
    group = 组，默认为：DEFAULT_GROUP
    '''
    def __init__(self, host, username, password,namespace,group=None):
        self.host = host
        self.namespace = namespace
        self.username = username
        self.password = password
        self.group = group or DEFAULT_GROUP_NAME
    # 登录
    def _doLogin(self):
        response = requests.request("post", self.host+"/nacos/v1/auth/users/login?username="+self.username+"&password="+self.password,headers={'Content-Type':'application/x-www-form-urlencoded'})
        self.ACCESS_TOKEN=json.loads(response.text).get("accessToken")
        
    # 获取指定配置
    def getConfig(self,dataId,tenant=None,group=None):
        if self.ACCESS_TOKEN == None:
            print("Nacos登录")
            self._doLogin()
        data={"dataId":dataId,"tenant":tenant or self.namespace,"group":group or self.group,"accessToken":self.ACCESS_TOKEN}
        response = requests.request("get", self.host+"/nacos/v1/cs/configs",params=data)
        if 403==response.status_code:
            self.ACCESS_TOKEN == None
            print("Nacos Token失效")
            return self.getConfig(dataId,tenant,group)
        return response.text

