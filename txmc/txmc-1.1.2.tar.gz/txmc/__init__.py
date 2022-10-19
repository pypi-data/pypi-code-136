#encoding='utf-8' 
import socket
import select,base64,collections,math
class Minecraft:
    def __init__(self,server,guid):
        '''连接服务器'''
        self.nickname='player'
        self.message=''
        self.status=False
        self.__socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect(('tk.makeblock.net.cn',4709))
        if self.__sendReceive('????')=='?????':
            args=self.__sendReceive('python|%s|%s'%(guid,server)).split('`')
            if len(args)==2 and args[1]=='ok':
                self.nickname=args[0]
                self.status=True
            else:
                self.message=args[0]
        else:
            self.Close()
    def __drain(self):
        while True:
            readable, _, _ = select.select([self.__socket], [], [], 0.0)
            if not readable:
                break
            try:
                data = self.__socket.recv(1500)
                e =  "Drained Data: <%s>\n"%data.strip()
                e += "Last Message: <%s>\n"%self.lastSent.strip()
                self.__socket.close()
                print(e)
            except Exception as e:
                print('error!',e)
    def __flatten(self,l):
        for e in l:
            if isinstance(e, collections.Iterable) and not isinstance(e, str):
                for ee in self.__flatten(e): yield ee
            else: yield e
    def __flatten_parameters_to_bytestring(self,l):
        return b",".join(map(_misc_to_bytes, self.__flatten(l)))
    def _misc_to_bytes(self,m):
        return str(m).encode(encoding='UTF-8')
    def __intFloor(self,*args):
        return [int(math.floor(x)) for x in self.__flatten(args)]
    def __send(self,s):
        '''发送消息'''
        if self.__socket==None:
            return None
        self.__drain()
        self.lastSent = s
        #print(s)
        self.__socket.sendall(base64.b64encode(base64.b64encode(bytes(s,'utf-8'))[::-1])+b'\n')
    def __receive(self):
        if self.__socket==None:
            return None
        '''接受消息'''
        return base64.b64decode(base64.b64decode(bytes(self.__socket.makefile("r").readline().rstrip("\n"),encoding='utf-8'))[::-1]).decode('utf-8')
    def __sendReceive(self,*data):
        '''发送并等待接受'''
        self.__send(*data)
        return self.__receive()
    def Close(self):
        '''断开连接'''
        self.__socket=None
        self.status=False
    @staticmethod
    def Connect(server,guid):
        '''连接服务器'''
        return Minecraft(server,guid)
    def toChat(self,msg):
        '''发送一句话到服务器中'''
        self.__send('''tochat:%s说:%s''' % (self.nickname,msg))
    def getBlock(self,*args):
        '''获取指定位置的方块'''
        return self.__sendReceive('''getblock:%s|%s|%s''' % tuple(self.__intFloor(args)))
    def setBlock(self,*args):
        '''在指定位置放置指定方块'''
        self.__send('''setblock:%d|%d|%d|%d|%d''' % tuple(self.__intFloor(args)))
    def setBlockByName(self,x,y,z,blockname,data,type='replace'):
        '''在指定位置放置指定方块'''
        return self.__sendReceive('''setblocknew:{_x}|{_y}|{_z}|{_block}|{_data}|{_type}'''
        .format(_x=x,_y=y,_z=z,_block=blockname,_data=data,_type='keep' if type=='keep' else 'replace'))
    def drawLine(self,*args):
        '''画线'''
        return self.__send('''drawLine:%s|%s|%s|%s|%s|%s|%s|%s''' % tuple(self.__intFloor(args)))
    def setBlocks(self,*args):
        '''生成长方体''' 
        return self.__send('''setblocks:%s|%s|%s|%s|%s|%s|%s|%s''' % tuple(self.__intFloor(args)))
    def setBlocksByName(self,x,y,z,x1,y1,z1,blockname,data=0,type='replace'):
        '''生成长方体'''
        return self.__sendReceive('''setblocksnew:{_x}|{_y}|{_z}|{_x1}|{_y1}|{_z1}|{_block}|{_data}|{_type}'''
        .format(_x=x,_y=y,_z=z,_x1=x1,_y1=y1,_z1=z1,_block=blockname,_data=data,_type=type))
    def getMyPos(self):
        '''获取我的位置'''
        return self.__sendReceive('''getplaypos:%s'''%(self.nickname))
    def setMyFly(self):
        '''设置飞行'''
        self.__send('''playfly:%s|1'''%(self.nickname))
    def openInventory(self,index=1):
        '''开启我的编程箱子'''
        return self.__sendReceive('''openmyinventory:%s''' % (index))
    def setMyPos(self,x,y,z):
        '''将我传送到指定的位置'''
        return self.__sendReceive('''setplayerpos:%s|%d|%d|%d'''%(self.nickname,x,y,z))
    def setLight(self,*args):
        '''在指定坐标点设置雷电'''
        return self.__sendReceive('''light:%d|%d|%d'''% tuple(self.__intFloor(args)))
    def drawCircle(self,x,y,z,radius,id,data,type='x'):
        '''画圆'''
        self.__send('''drawCircle:%d|%d|%d|%d|%d|%d|%d'''% (1 if type=='x' else 0 ,x,y,z,radius,id,data))
    def drawSphere(self,x,y,z,radius,id,data,type=0):
        '''画球体
        type=0 空心 1实心
        '''
        self.__send('''drawSphere:%d|%d|%d|%d|%d|%d|%d'''% (type,x,y,z,radius,id,data))