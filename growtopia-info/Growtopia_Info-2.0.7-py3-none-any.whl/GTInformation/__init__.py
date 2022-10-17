import requests
from bs4 import BeautifulSoup

def GameData():
    try:
        from datetime import datetime
        from pytz import timezone
        Result = {
            "Online_User": "",
            "WOTDLink" : "",
            "WOTDName" : "",
            "GTTime" : "",
            "GTDate" : ""
        }        
        try:
            Website = requests.get(f"https://www.growtopiagame.com/detail").json()
            wotd = ((Website["world_day_images"]["full_size"].replace('https://www.growtopiagame.com/worlds/','')).replace('.png','')) 
            Result["Online_User"] = Website["online_user"]
            Result["WOTDLink"] = "https://s3.amazonaws.com/world.growtopiagame.com/"+wotd+".png"
            Result["WOTDName"] = wotd.upper()
            Result["GTTime"] = datetime.now(timezone('UTC')).astimezone(timezone('America/New_York')).strftime("%X")
            Result["GTDate"] = datetime.now(timezone('UTC')).astimezone(timezone('America/New_York')).strftime("%x")
            return Result
        except: 
            return({"Error":"It looks like we can't reach growtopiagame.com! Error code 2"})
    except:
        return({"Error":"pytz not detected! please install pytz! Error code 1"})

def ItemData(NameItem, Region = "en"):
    def body(HTMLResult,NameItem):
        def checking(Result):
            check = 0
            for fix in Result.keys():
                theresult = Result[fix]
                if check == 3:
                    Result[fix] = theresult.split(" - ")
                if check == 8:
                    Result[fix] = theresult.split(" ")
                if check == 7:
                    restore = []
                    for number in theresult.split(" "):
                        input = ""
                        for number2 in number:
                            if number2.isdigit():
                                input = input+number2
                        if input != "":
                            restore.append(input)
                    Result[fix] = {
                            "Fist":restore[0],
                            "Pickaxe":restore[1],
                            "Restore":restore[2]
                    }
                if check == 9:
                    time = []
                    growtime = {}
                    for number in theresult.split(" "):
                        input = ""
                        for number2 in number:
                            if number2.isdigit():
                                input = input+number2
                        if input != "":
                            time.append(input)
                    format = ["Month","Week","Day","Hour","Minute","Second"]
                    i = 0
                    while i != len(time):
                        growtime[format[((len(format))-1)-i]] = time[((len(time))-1)-i]
                        i+=1
                    Result[fix] = growtime

                if check == 10:
                    gems = []
                    if len(theresult.split(" - ")) == 1:
                        gems.append(theresult.split(" - ")[0])
                        gems.append(theresult.split(" - ")[0])
                    else:
                        gems.append(theresult.split(" - ")[0])
                        gems.append(theresult.split(" - ")[1])                        
                    Result[fix] = {
                            "Max":gems[1],
                            "Min":gems[0]
                        }                                
                check +=1
        wordcheck = None
        Result = {}
        if len(HTMLResult.select(".gtw-card")) == 1:
            Properties = HTMLResult.find_all('div',  class_= "card-text")
            Data = HTMLResult.select(".card-field")
            Rarity = BeautifulSoup((str((HTMLResult.find('small'))).replace("(Rarity: ", "")).replace(")", ""), "html.parser").text
            PropertiesResult = []
            for add in Properties:
                hum = BeautifulSoup(str(add).replace("<br/>", "--split--"), "html.parser")
                PropertiesResult.append(hum.text)
            Result.update({"Description": PropertiesResult[0].strip()})
            Result.update({"Properties": (PropertiesResult[1].strip()).split("--split--")})
            try:
                Result.update({"Rarity": int(Rarity)})
            except:
                Result.update({"Rarity": "None"})
            DataResult = []
            for typ in Data:
                mus = BeautifulSoup((str(typ).replace("</tr>", ",")).replace("</th>", ","), "html.parser")
                DataResult = (((mus.text).split(",")))
            res = 0 
            while res <= (len(DataResult)-3):
                Result.update({DataResult[res].strip(): DataResult[res+1].strip()})
                res = res+2
            checking(Result)
            try:
                ItemTitle = ((((HTMLResult.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
            except:    
                ItemTitle = (HTMLResult.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
            Result["Title"] = ItemTitle
            wordcheck = True
        elif len(HTMLResult.select(".gtw-card")) > 1:
            for HTMLResultTabber in HTMLResult.select(".gtw-card"):   
                Result2 = {}   
                PropertiesResult = []
                Properties = HTMLResultTabber.find_all('div',  class_= "card-text")
                Data = HTMLResultTabber.select(".card-field")
                Rarity = BeautifulSoup((str((HTMLResultTabber.find('small'))).replace("(Rarity: ","")).replace(")", ""), "html.parser").text
                for add in Properties:
                    hum = BeautifulSoup(str(add).replace("<br/>", "--split--"), "html.parser")
                    PropertiesResult.append(hum.text)
                Result2.update({"Description": PropertiesResult[0].strip()})
                Result2.update({"Properties": (PropertiesResult[1].strip()).split("--split--")})
                try:
                    Result2.update({"Rarity": int(Rarity)})
                except:
                    Result2.update({"Rarity": "None"})
                DataResult = []
                for typ in Data:
                    mus = BeautifulSoup((str(typ).replace("</tr>", ",")).replace("</th>", ","), "html.parser")
                    DataResult = (mus.get_text(" ",strip=True)).split(",")
                res = 0 
                while res <= (len(DataResult)-3):
                    Result2.update({DataResult[res].strip(): DataResult[res+1].strip()})
                    res = res+2  
                checking(Result2)
                try:
                    ItemTitle = ((((HTMLResultTabber.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                except:    
                    ItemTitle = (HTMLResultTabber.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                Result[ItemTitle] = Result2
                Result[ItemTitle]["Title"] = ItemTitle
                wordcheck = False
        if wordcheck == False:
            NameItem = NameItem.lower()
            word = []
            Result2 = {}
            for item in Result.keys():
                if NameItem in item.lower():
                    word.append(item)
            for item2 in word:
                Result2[item2] = Result[item2]
            if len(Result2) == 1:
                for item3 in Result2.keys():
                    return Result2[item3]
            else:
                return Result2
        elif wordcheck == True:
            return Result
        else:
            return {"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region,"Error Code": "2"}
    #====================================================================Main Program=============================================================================
    try:
        ItemPage = BeautifulSoup(requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+NameItem).text, "html.parser")
        if ItemPage.select(".gtw-card") == []:
            ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
            try:
                ItemPage = BeautifulSoup(requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"]).text, "html.parser")
            except:
                return {"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region,"Error Code": "2"}
        return body(ItemPage,NameItem)
    except:
        return({"Error": "It looks like we can't reach fandom.com "+Region+"! Try again later","Error Code": "1"})


def ItemRecipe(NameItem, Region = "en"):
    def body(HTMLResult,NameItem):
        def Insert(this,Recipe):
            if this in Recipe.keys():
                Recipe[this].append([])
                for meh in item.select('td'):
                    meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                    Recipe[this][1].append(meh.replace(u'\xa0', u''))                 
            else:
                Recipe[this] = [[]]
                for meh in item.select('td'):
                    meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                    Recipe[this][0].append(meh.replace(u'\xa0', u'')) 

        def Insert2(this,Recipe):
            if this in Recipe[meh].keys():
                Recipe[meh][this].append([])
                for the in mes.select('td'):
                    the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                    Recipe[meh][this][1].append(the.replace(u'\xa0', u''))                    
            else:
                Recipe[meh][this] = [[]]
                for the in mes.select('td'):
                    the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                    Recipe[meh][this][0].append(the.replace(u'\xa0', u'')) 

        def Title(itemish):
            try:
                ItemTitle = ((((itemish.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
            except:    
                ItemTitle = (itemish.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
            return ItemTitle
        fortabber = HTMLResult.select_one(".tabber.wds-tabber")
        require = []
        Result = {}
        wordcheck = None
        if len(HTMLResult.select(".gtw-card")) == 1:
            ws = 0
            count = 0
            Recipe = {}
            for item in HTMLResult.select(".content"):
                if item.select(".content") == []:
                    if not count in require:
                        Insert(((item.find('th')).text).strip(), Recipe)
                    ws += 1
                else:
                    meh = ((item.find('th')).text).strip()
                    Recipe[meh] = {}
                    for mes in item.select(".content"):
                        Insert2(((mes.find('th')).text).strip(), Recipe)
                        ws += 1
                        require.append(ws)
                count +=1
            Result= Recipe
            Result["Title"] = Title(HTMLResult)
            wordcheck = True
        else:
            for itemish in fortabber.select(".wds-tab__content"):
                ws = 0
                count = 0
                Recipe = {}
                if itemish.select(".content") == []:
                    for item in itemish.select(".content"):
                        if item.select(".content") == []:
                            if not count in require: 
                                Insert(((item.find('th')).text).strip(), Recipe)
                            ws += 1
                        else:
                            meh = ((item.find('th')).text).strip()
                            Recipe[meh] = {}
                            for mes in item.select(".content"):
                                Insert2(((mes.find('th')).text).strip(), Recipe)
                                ws += 1
                                require.append(ws)
                        count +=1
                    Result[Title(itemish)] = Recipe
                    Result[Title(itemish)]["Title"] = Title(itemish)
                else:
                    for item in itemish.select(".content"):
                        if item.select(".content") == []:
                            if not count in require: 
                                Insert(((item.find('th')).text).strip(), Recipe) 
                            ws += 1
                        else:
                            meh = ((item.find('th')).text).strip()
                            Recipe[meh] = {}
                            for mes in item.select(".content"):
                                Insert2(((mes.find('th')).text).strip(), Recipe) 
                                ws += 1
                                require.append(ws)
                        count +=1
                    Result[Title(itemish)] = Recipe
                    Result[Title(itemish)]["Title"] = Title(itemish)
            wordcheck = False
        if wordcheck == False:
            NameItem = NameItem.lower()
            word = []
            Result2 = {}
            for item in Result.keys():
                if NameItem in item.lower():
                    word.append(item)
            for item2 in word:
                Result2[item2] = Result[item2]
            if len(Result2) == 1:
                for item3 in Result2.keys():
                    return Result2[item3]
            else:
                return Result2
        elif wordcheck == True:
            return Result
        else:
            return {"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region,"Error Code": "2"}
    #====================================================================Main Program=============================================================================
    try:
        ItemPage = BeautifulSoup(requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+NameItem).text, "html.parser")
        if ItemPage.select(".gtw-card") == []:
            ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
            try:
                ItemPage = BeautifulSoup(requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"]).text, "html.parser")
            except:
                return {"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region,"Error Code": "2"}
        return body(ItemPage,NameItem)
    except:
        return({"Error": "It looks like we can't reach fandom.com "+Region+"! Try again later","Error Code": "1"})

def ItemSprite(NameItem, Region = "en"):
    def body(HTMLResult,NameItem):
        wordcheck = None
        Result = {}  
        if len(HTMLResult.select(".gtw-card")) == 1:
            Data = {
                "Item" :"",
                "Tree" :"",
                "Seed" :""
            }  
            images = HTMLResult.find('div', {"class": "gtw-card"})
            Data["Item"]= (images.find('div', {"class": "card-header"})).img['src']
            Data["Tree"] = (((((((images.find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).img['src']
            Data["Seed"] = (images.find('td', {"class": "seedColor"})).img['src']
            try:
                ItemTitle = ((((HTMLResult.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
            except:    
                ItemTitle = (HTMLResult.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
            Result = Data
            Result["Title"] = ItemTitle
            wordcheck = True
        else:
            for HTMLResultTabber in HTMLResult.select(".wds-tab__content"):
                Data = {
                    "Item" :"",
                    "Tree" :"",
                    "Seed" :""
                }  
                images = HTMLResultTabber.find('div', {"class": "gtw-card"})
                Data["Item"]= (images.find('div', {"class": "card-header"})).img['src']
                Data["Tree"] = (((((((images.find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).img['src']
                Data["Seed"] = (images.find('td', {"class": "seedColor"})).img['src']
                try:
                    ItemTitle = ((((HTMLResultTabber.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                except:    
                    ItemTitle = (HTMLResultTabber.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                Result[ItemTitle] = Data
                Result[ItemTitle]["Title"] = ItemTitle
            wordcheck = False
        if wordcheck == False:
            NameItem = NameItem.lower()
            word = []
            Result2 = {}
            for item in Result.keys():
                if NameItem in item.lower():
                    word.append(item)
            for item2 in word:
                Result2[item2] = Result[item2]
            if len(Result2) == 1:
                for item3 in Result2.keys():
                    return Result2[item3]
            else:
                return Result2
        elif wordcheck == True:
            return Result
        else:
            return {"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region,"Error Code": "2"}
    #====================================================================Main Program=============================================================================
    try:
        ItemPage = BeautifulSoup(requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+NameItem).text, "html.parser")
        if ItemPage.select(".gtw-card") == []:
            ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
            try:
                ItemPage = BeautifulSoup(requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"]).text, "html.parser")
            except:
                return {"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region,"Error Code": "2"}
        return body(ItemPage,NameItem)
    except:
        return({"Error": "It looks like we can't reach fandom.com "+Region+"! Try again later","Error Code": "1"})  