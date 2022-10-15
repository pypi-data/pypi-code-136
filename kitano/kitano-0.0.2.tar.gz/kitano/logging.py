# ReinanBr 04/10/22
# lib: kitano
# LICENSE: MIT

from datetime import datetime
import time




#get date
def getDate(strfitTime:str='[%H:%M:%S %d/%m/%Y]') -> None:
	datePrint = datetime.now().strftime(strfitTime)
	return datePrint


showDate = True
#show date
def show_date(argument:bool) -> None:
	global showDate
	showDate = argument

#strft
strft = None
def strPrt(strf:str=None) -> None:
	global strft
	strft = strf



#lib for pritting
def puts(*txt,sep=' '):
	if len(txt) > 1:
		textShowing = (sep).join([str(text) for text in txt])
	if showDate:
		if strft:
			datePrt = getDate(strf)
		else:
			datePrt = getDate()
		prtTxt = f'{datePrt}: {textShowing}'
	else:
		prtTxt = f'{textShowing}'

	print(prtTxt)

