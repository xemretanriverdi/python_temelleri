#bmw, mercedes,opel, mazda elamanlarına ait list oluştur
cars = ["Bmw","Mercedes","Opel","Mazda"]
print(cars)

#liste elemanları

print(len(cars))

#liste ilk ve son eleman
soneleman = len(cars)-1
print("ilk eleman : ", cars[0], " son eleman : " ,cars[len(cars)-1])

#mazda ile Porshe değiştirin

cars[-1]= "Porshe"
print(cars)

#mercedes listin bir elemanı mıdır 

result = "Mercedes" in cars #arama operatörü
print(result)

#listenin ilk üç elemanı ?

print(cars[:3])

#son iki elemana Bugatti ve Ferrari değiştir
 
cars[-2:]=["Bugatti","Ferrari"]
print(cars)

#son eleman silin

del cars[-1]
print(cars)


#arabaları tersten yazdır
print(cars[::-1])
