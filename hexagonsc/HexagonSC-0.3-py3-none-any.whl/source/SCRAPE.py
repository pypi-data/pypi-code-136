
#gonna scrape RSI for citizen data
#outputs pilotname, primary org, affiliate orgs, the rank within those orgs and the year the pilot made his account
#%% Request
from xml.etree.ElementTree import tostring
from bs4 import BeautifulSoup
import requests
#%%
#if (r.status_code == 404):
#format this
def usrScrape(username):
    orgurl="https://robertsspaceindustries.com/citizens/{FORMAT}/organizations"
    orgurl=orgurl.format(FORMAT=username)
    userurl="https://robertsspaceindustries.com/citizens/{FORMAT}"
    userurl=userurl.format(FORMAT=username)
    r = requests.get(orgurl)
    soup = BeautifulSoup(r.content, 'html5lib')
    r2 = requests.get(userurl)
    soup2 = BeautifulSoup(r2.content, 'html5lib')
   
    if (r.status_code == 404): #detect if the ocr failed to produce a searchable name
        orgdict={                #dict declare
        "Name":["OCR FAIL"],
        "Rank":["OCR FAIL"],
    }
        return "OCR FAIL", orgdict
    table = soup.findAll('div', attrs = {'class':'info'})
    orgNumb=len(table)

    nValue=list(())          #list init
    rValue=list(())
    for i in range (orgNumb):#list size init for iterator
        nValue.append("")
        rValue.append("")
    orgdict={                #dict init
    "Name":nValue,
    "Rank":rValue,
    }
    
    for i in range (orgNumb): #sort the data into the dicitonary
        
        orgname=table[i].find('a').text
        if (orgname.find("\xa0")==0):#redacted org case
            nValue[i]="REDACTED"
        else:
            nValue[i]=orgname
        orgrank=len(table[i].findAll("span", attrs = {'class':'active'}))
        rValue[i]=orgrank 

    orgdict.update({"Rank" : rValue})
    orgdict.update({"Name" : nValue})#update

    table2= soup2.find_all('strong', attrs = {'class':'value'})# get the date the person joined
    if (orgdict.get("Name")==[]):
        date=table2[3].text
    else:
        date=table2[5].text
    return date, orgdict
# %%
# Debug deez nuts
#dates,diction=usrScrape("SUNRABBIT")
#print(dates)
#print(diction)
# %%
