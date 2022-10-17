import urllib .parse
from urllib .request import urlopen
import json
import time
import sys
import os
def Time_1 ():
    for OO0OO0000O0O0O0O0 in range (1 ,51 ):
        sys .stdout .write ('\r')
        sys .stdout .write ('{0}% |{1}'.format (int (OO0OO0000O0O0O0O0 %51 )*2 ,int (OO0OO0000O0O0O0O0 %51 )*'■'))
        sys .stdout .flush ()
        time .sleep (0.125 )
    sys .stdout .write ('\n')
def KuGou_music ():
    print ("注：下载的是酷狗网页中的歌曲，下载到：D:\kugou音乐")
    OOOO00OOOOO0O0000 =urllib .parse .urlencode ({'keyword':input ('请输入歌名:')})
    OOOO00OOOOO0O0000 =OOOO00OOOOO0O0000 [OOOO00OOOOO0O0000 .find ('=')+1 :]
    O00O00O0O0O0OO00O ='https://songsearch.kugou.com/song_search_v2?callback=jQuery1124042761514747027074_1580194546707&keyword='+OOOO00OOOOO0O0000 +'&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1580194546709'
    OO0OOO00OOO000O0O =urlopen (url =O00O00O0O0O0OO00O )
    OO0OOO00OOO000O0O =OO0OOO00OOO000O0O .read ().decode ('utf-8')
    O0O00O000O0O00O00 =OO0OOO00OOO000O0O [OO0OOO00OOO000O0O .find ('(')+1 :-2 ]
    O0OO000OOOOO0000O =json .loads (O0O00O000O0O00O00 )
    OO0OO0000OO000O00 ={}
    OOO00O0OO000OOO0O ={}
    for O000OO0O0O0O0O0OO in O0OO000OOOOO0000O ['data']['lists']:
        OO0OO0000OO000O00 [O000OO0O0O0O0O0OO ['FileName']]=O000OO0O0O0O0O0OO ['FileHash']
        OOO00O0OO000OOO0O [O000OO0O0O0O0O0OO ['FileName']]=O000OO0O0O0O0O0OO ['AlbumID']
    O00OO0O0OO00000O0 =[OOO000OO0O0O0OOOO for OOO000OO0O0O0OOOO in OO0OO0000OO000O00 ]
    O000O0OO0OOO00000 =[OO0OO0OO000OOO0OO for OO0OO0OO000OOO0OO in OO0OO0000OO000O00 ]
    for O0OOOOOOO0OO0O00O in range (len (O000O0OO0OOO00000 )):
        if '- <em>'in O000O0OO0OOO00000 [O0OOOOOOO0OO0O00O ]:
            O000O0OO0OOO00000 [O0OOOOOOO0OO0O00O ]=O000O0OO0OOO00000 [O0OOOOOOO0OO0O00O ].replace ('- <em>','-')
        if '</em>'in O000O0OO0OOO00000 [O0OOOOOOO0OO0O00O ]:
            O000O0OO0OOO00000 [O0OOOOOOO0OO0O00O ]=O000O0OO0OOO00000 [O0OOOOOOO0OO0O00O ].replace ('</em>','')
        if '<em>'in O000O0OO0OOO00000 [O0OOOOOOO0OO0O00O ]:
            O000O0OO0OOO00000 [O0OOOOOOO0OO0O00O ]=O000O0OO0OOO00000 [O0OOOOOOO0OO0O00O ].replace ('<em>','')
    for O0OOOOOOO0OO0O00O in range (len (O000O0OO0OOO00000 )):
        print ("{}-:{}".format (O0OOOOOOO0OO0O00O +1 ,O000O0OO0OOO00000 [O0OOOOOOO0OO0O00O ]))
    OOO0OOOO00O0O00OO =int (input ('请输入你想下载的歌曲序号:'))
    O00O00O0O0O0OO00O ='https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash='+OO0OO0000OO000O00 [O00OO0O0OO00000O0 [OOO0OOOO00O0O00OO -1 ]]+'&album_id='+OOO00O0OO000OOO0O [O00OO0O0OO00000O0 [OOO0OOOO00O0O00OO -1 ]]+'&dfid=2SSV0x4LWcsx0iylej1F6w7P&mid=44328d3dc4bfce21cf2b95cf9e76b968&platid=4'
    O0OOOO00O0OO0OO0O =urlopen (url =O00O00O0O0O0OO00O )
    O00O0000O0O00OO0O =O0OOOO00O0OO0OO0O .read ().decode ('utf-8')
    O000OO00000O0000O =json .loads (O00O0000O0O00OO0O )
    try :
        O0OO0OOO00000OOO0 =O000OO00000O0000O ['data']['play_backup_url']
        OO0OO000OOOO000O0 =urlopen (url =O0OO0OOO00000OOO0 ).read ()
        try :
            os .mkdir ('D:\kugou音乐')
        except Exception as OOOOOO0O0O0O0OOOO :
            print (OOOOOO0O0O0O0OOOO ,'稍等,程序仍然执行')
        finally :
            O0000000O0OOO0000 ='D:\kugou音乐'+O000O0OO0OOO00000 [OOO0OOOO00O0O00OO -1 ]+'.mp3'
            with open (O0000000O0OOO0000 ,'wb')as O0O00000O0OOO0000 :
                print ('正在下载当中...')
                O0O00000O0OOO0000 .write (OO0OO000OOOO000O0 )
                Time_1 ()
                print ('{}.mp3下载成功！'.format (O000O0OO0OOO00000 [OOO0OOOO00O0O00OO -1 ]))
    except :
        print ('对不起，没有该歌曲的版权！')

if __name__ =='__main__':
    KuGou_music ()
