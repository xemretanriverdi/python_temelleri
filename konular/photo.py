import urllib.request

url1="https://upload.wikimedia.org/wikipedia/tr/8/85/200px-Fenerbah%C3%A7e.png"
url2="https://upload.wikimedia.org/wikipedia/commons/2/20/Galatasaray_Sports_Club_Logo.svg"
url3="https://upload.wikimedia.org/wikipedia/commons/0/08/Be%C5%9Fikta%C5%9F_Logo_Be%C5%9Fikta%C5%9F_Amblem_Be%C5%9Fikta%C5%9F_Arma.png"

urllist=[url1,url2,url3]

say=1

for url in urllist:
    urllib.request.urlretrieve(url,"Resim" + str(say))
    say +=1    