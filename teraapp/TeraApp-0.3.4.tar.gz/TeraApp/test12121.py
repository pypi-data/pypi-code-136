from TeraApp.TeraApp.Functions.functions import *

app = TeraAppWIcon('a',1200,800,'','','True')

app.textarea(100,100,'blue',200,200,'white',15)

#app.input(100,600,'blue')
app.inputr2(400,400,'white',100,100)

app.gif('r.gif',5,5,400,400)

app.sound('song.mp3')

mute1 = False
def mute():
    global mute1
    if mute1 is False:
        print('mute')
        app.sound_name.stop()
        mute1 = True
    else:
        print('unmute')
        v = app.sound_name.play()
        mute1 = False

app.buttonf('gdf',500,500,'blue',mute)
app.buttonfri(500,700,'logo.png',mute,500,500,0)
app.buttonf_name.setStyleSheet("""
        QPushButton:hover {
            color: yellow;
        }
    """)

app.app.exec()