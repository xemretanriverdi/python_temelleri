import requests

from bs4 import BeautifulSoup

imdburl = "https://www.imdb.com/chart/top/"

secaz = requests.get(imdburl) 

soup = BeautifulSoup(secaz.content,"html.parser")

gelen_veri = soup.find_all("table",{"class":"chart full-width"})
print(len(gelen_veri[0]))
gelen_veri2=
print("*******************************")
