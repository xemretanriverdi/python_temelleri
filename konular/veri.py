import requests

from bs4 import BeautifulSoup

imdburl = "https://www.imdb.com/chart/top/"

secaz = requests.get(imdburl) 

soup = BeautifulSoup(secaz.content,"html.parser")

gelenVeri = soup.find_all("table",{"class" : "chart full-width"})

filmTablosu=(gelenVeri[0].contents)[2]
print(gelenVeri)
print("*******************************")
print(filmTablosu)