a="Python"
b="Programlama "
c="dili "

print(a*3) 
print(a[4])  

d = a + b + c
print(d)
print(len(a))
print(a[len(a)-1]) #son eleman

print(a[0:2]) # ilk iki terim
x = "Konusamadıklarımız"
print(x[:5:2]) #baslanic:soneelamn:atlamamiktari
print(x.upper)
isim =" Mevlüt Emre Tanrıverdi"

isim = isim.upper()
isim = isim.replace(" ","  ") #karakter değiştirme
isim = isim.replace("EMRE","Secaz") #karakter değiştirme
isim = isim.replace("Secaz","Emre") #karakter değiştirme


print(type(isim))

isim = isim.split() # her kelime karakter dizis oldu

print(type(isim)) 
print(isim[1])

print(isim)


metin=("Merhaba arkadaslar. Benim adım Emre, İstanbulda yaşıyorum. Yaklasık 3 senedir yazılımla uğrasıyorum")
metin =metin.split(".")
print(type(metin))
print("Metinde {} adet cümle vardır".format(len(metin)))

a = "araba"

sonuc=(a.endswith("sba"))
print(sonuc)
