#encoding='utf-8' 
import socket
import select,base64,collections,math
class Minecraft:
    def __init__(self):
        self.nickname='player'
        self.message=''
    def drain(self):
        while True:
            readable, _, _ = select.select([self._socket], [], [], 0.0)
            if not readable:
                break
            try:
                data = self._socket.recv(1500)
                e =  "Drained Data: <%s>\n"%data.strip()
                e += "Last Message: <%s>\n"%self.lastSent.strip()
                self._socket.close()
                print(e)
            except Exception as e:
                print('error!')
    def flatten(self,l):
        for e in l:
            if isinstance(e, collections.Iterable) and not isinstance(e, str):
                for ee in self.flatten(e): yield ee
            else: yield e
    def flatten_parameters_to_bytestring(self,l):
        return b",".join(map(_misc_to_bytes, self.flatten(l)))
    def _misc_to_bytes(self,m):
        return str(m).encode(encoding='UTF-8')
    def intFloor(self,*args):
        return [int(math.floor(x)) for x in self.flatten(args)]
    def _send(self,s):
        '''发送消息'''
        if self._socket==None:
            return None
        self.drain()
        self.lastSent = s
        #print(s)
        self._socket.sendall(base64.b64encode(base64.b64encode(bytes(s,'utf-8'))[::-1])+b'\n')
    def receive(self):
        if self._socket==None:
            return None
        '''接受消息'''
        return base64.b64decode(base64.b64decode(bytes(self._socket.makefile("r").readline().rstrip("\n"),encoding='utf-8'))[::-1]).decode('utf-8')
    def sendReceive(self,*data):
        '''发送并等待接受'''
        self._send(*data)
        return self.receive()
    def Close(self):
        '''断开连接'''
        self._socket=None
    def Connect(self,mc,guid):
        '''连接服务器'''
        self._socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect(('tk.makeblock.net.cn',4709))
        if self.sendReceive('????')=='?????':
            args=self.sendReceive('python|%s|%s'%(guid,mc)).split('`')
            if len(args)==2 and args[1]=='ok':
                self.nickname=args[0]
                return True
        self.Close()
        self.message=args[0]
        return False
    def toChat(self,msg):
        '''发送一句话到服务器中'''
        self._send('''tochat:%s说:%s''' % (self.nickname,msg))
    def getBlock(self,*args):
        '''获取指定位置的方块'''
        return self.sendReceive('''getblock:%s|%s|%s''' % tuple(self.intFloor(args)))
    
 

def setBlock(x,y,z,id,data):
    '''在指定位置放置指定方块'''
    pass
def setBlockByName(x,y,z,blockname,data,type):
    '''在指定位置放置指定方块'''
    pass
def drawLine(x,y,z,x1,y1,z1,id,data):
    '''画线'''
    pass
def setBlocks(x,y,z,x1,y1,z1,id,data):
    '''生成长方体'''
    pass
def setBlocksByName(x,y,z,x1,y1,z1,blockname,data,type):
    '''生成长方体'''
    pass
def drawCircle(x,y,z,radius,id,data,type):
    '''画圆'''
    pass
def drawSphere(x,y,z,radius,id,data,type):
    '''画球体'''
    pass
def getMyPos():
    '''获取我的位置'''
    pass
def openInventory(index):
    '''开启我的编程箱子'''
    pass

def setMyPos(x,y,z):
    '''将我传送到指定的位置'''
    pass
def setMyFly():
    '''设置飞行'''
    pass
def setLight(x,y,z):
    '''在指定坐标点设置雷电'''
    pass
