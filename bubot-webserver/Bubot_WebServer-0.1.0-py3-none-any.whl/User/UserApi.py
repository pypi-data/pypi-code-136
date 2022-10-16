from Bubot.Core.ObjApi import ObjApi
# from bubot.Helpers.Сryptography.SignedData import SignedData
from BubotObj.User.User import User


class UserApi(ObjApi):
    name = "User"
    handler = User

