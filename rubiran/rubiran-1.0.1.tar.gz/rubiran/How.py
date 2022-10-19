#Copyright (C) 2022 X CODER
from time import sleep

class color:
      red = '\033[91m'
      green = '\033[92m'
      blue = '\033[94m'
      yellow = '\033[93m'
      magenta = '\033[95m'
      cyan = '\033[96m'
      white = '\033[97m'
      bold = '\033[1m'
      underline = '\033[4m'
      black='\033[30m'

class chup:
      x_coder = f"""{color.bold}
{color.white} [⏦] - {color.cyan} 𝐑𝐔𝐁𝐈𝐑𝐀𝐍 {color.yellow} 𝐕𝐄𝐑𝐒𝐈𝐎𝐍  {color.red}1.0.1    

{color.white} [⏦] - {color.cyan} 𝐑𝐔𝐁𝐈𝐑𝐀𝐍 {color.yellow} 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 (𝐂) {color.red} 2022 {color.green}𝐌𝐀𝐌𝐀𝐃 𝐂𝐎𝐃𝐄𝐑   

{color.white} [⏦] - {color.cyan} 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑  {color.yellow} 𝐑𝐔𝐁𝐈𝐊𝐀 {color.red} 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 : {color.green} @python_java_source

{color.white}╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾
"""
      print(x_coder)
      
for x in range(3):
    for i in ("⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"):
        sleep(0.1)
        if x == 10:
            print('',end='')
            break
        else:
            print( color.blue+'   𝐋𝐈𝐁𝐑𝐀𝐑𝐘 𝐑𝐔𝐁𝐈𝐑𝐀𝐍 𝐑𝐔𝐍𝐈𝐍𝐆 𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓   ',color.green+i,end='\r')
print(color.white+"\n")