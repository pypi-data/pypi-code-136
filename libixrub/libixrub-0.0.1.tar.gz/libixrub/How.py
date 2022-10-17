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
{color.white} [⏦] - {color.cyan} 𝐋𝐈𝐁𝐈𝐗𝐑𝐔𝐁 {color.yellow}𝐕𝐄𝐑𝐒𝐈𝐎𝐍  {color.white}1.1    

{color.white} [⏦] - {color.cyan} 𝐋𝐈𝐁𝐈𝐗 {color.yellow}𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 (𝐂) {color.white} 2022 {color.red}𝐗 𝐂𝐎𝐃𝐄𝐑    

{color.white} [⏦] - {color.cyan} 𝐎𝐖𝐍𝐄𝐑  {color.yellow} 𝐑𝐔𝐁𝐈𝐊𝐀 {color.white} 𝐈𝐃 : {color.red}@X_CODER

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
            print( color.blue+'   𝐋𝐈𝐁𝐑𝐀𝐑𝐘 𝐋𝐈𝐁𝐈𝐗 𝐑𝐔𝐍𝐈𝐍𝐆 𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓  ',color.green+i,end='\r')
print(color.white+"\n")