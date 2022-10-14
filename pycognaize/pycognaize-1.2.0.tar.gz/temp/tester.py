import os
# from collections import defaultdict
#
# import pycognaize
from pycognaize.document import Snapshot
from pycognaize.document.field import TextField, field

os.environ['SNAPSHOT_PATH'] = "/home/atlantx/Documents/cognaize/pycognaize/pycognaize/tests/resources"
os.environ['SNAPSHOT_ID'] = "snapshots"

# snapshot = Snapshot.get()
# snapshot.download("/home/atlantx/Documents/cognaize/pycognaize/pycognaize/temp/")
# print(snapshot.documents)
# document = snapshot.documents['632c61fc86d52800197d03f3']
# for key, value in document.y.items():
#     print(key)
#
# print(document.y.groups, '--------')

# # print(document.x)
# import os
#
from pycognaize.common.enums import EnvConfigEnum
from pycognaize.login import Login
#
if __name__ == '__main__':
    os.environ[EnvConfigEnum.HOST.value] = 'https://uat-api.cognaize.com'

    from pycognaize import Snapshot, Login
    # log = Login()
    # log.login("hovhannes.zohrabyan@cognaize.com", "Format/Cognaize_dat")

    # os.environ[EnvConfigEnum.SNAPSHOT_ID.value] = '60ef38b12957f4000060b44a'
    Snapshot.download('123123', '/home/atlantx/Documents/cognaize/pycognaize/temp/')
