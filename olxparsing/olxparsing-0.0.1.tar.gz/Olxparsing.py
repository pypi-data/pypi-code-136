import requests
from bs4 import *

search=input("Qidiruv: ")
sayt=f"https://www.olx.uz/d/list/q-{search}"
olx=requests.get(sayt).text
soup=BeautifulSoup(olx, "lxml")
card_css=soup.find_all(class_="css-qfzx1y")

with open("Olx.txt","w",encoding="utf-8") as f:
    
  for card in card_css:
    try:
        tour=card.find(class_="css-1venxj6").find("img").get("src")
        title=card.find(class_="css-1venxj6").find("img").get("alt")
        f.write(f" Nomi: {title.strip()}, Rasm: {tour} \n \n")
    except:
        pass