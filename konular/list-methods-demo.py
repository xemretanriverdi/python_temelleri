names=["Emre","Ahmet","Ömer","Emircan"]
years=[1999,1999,133,23,2000,2001]

#1 Cenk ismini ekleyin
names.append("Cenk")
print(names)
#2 Sena ismini başa ekle
names.insert(0,"Sena")
print(names)

#3 Cenki siliniz
names.remove("Cenk")
print(names)

#4 Ahmet indexi kaç
print(names.index("Ahmet"))
#5 Emre bir eleman mıdır
bool= "Emre" in names
print(bool)

#6 Liste elemanlarını ters cevir
print(names)
print(names[::-1])

#7 Elemanları alfabetik

names.sort()
print(names)

#8 yearsı büyüükten kücüğe
years.reverse()
print(years)

#9 str ="Chevrolet,Dacia" diziye çevir

str ="Chevrolet,Dacia"
str.split(',')
print(str)

#10 years en büyük ve enn kücük
years.sort()
print(years[0],years[-1])
#11 years tüm elemanlar silin
years.clear()
print(years)


#12 kullanıcdan alacağımız üç marka listesini listte saklayınn
markalar=[]
marka =input("marka :")
markalar.append(marka)
marka =input("marka :")
markalar.append(marka)
marka =input("marka :")
markalar.append(marka)
print(markalar)


#13
#9


