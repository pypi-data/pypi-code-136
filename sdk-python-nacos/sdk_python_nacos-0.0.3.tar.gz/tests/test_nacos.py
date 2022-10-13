from  sdk_python_nacos import  NacosClient

host="http://nacos-config.smartfeng.com:28848"
username="dev"
password="wWwjiHp8cVzi%26cCt"
tenant="93d884d1-0bd5-4b31-a619-2e08cfabbc5e"

nacos=NacosClient(host,username,password,tenant)
config = nacos.getConfig("nacos-gateway-local.yaml")
print(config)
print(nacos.getConfig("nacos-gateway-local.yaml"))
print(nacos.getConfig("nacos-gateway-local.yaml"))
print(nacos.getConfig("nacos-gateway-local.yaml"))