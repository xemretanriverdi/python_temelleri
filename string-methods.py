message = "Hello There. My name is Emre Tanrıverdi"

message = message.upper() #karakterleri büyütür
message = message.lower() #karakterleri küçültür
message = message.title() # Her kelimenin baş harfi büyük harfe cevrilir
message = message.capitalize() #sadece en baş harf büyür
message = message.strip() #baştaki boşluk gider
message = message.split() #her kelimeyi karakter dizisi yapar message dizi oldu 
#message = message.split(",") #her kelimeyi karakter dizisi yapar noktalardan itibaren ayırır
message=" ".join(message) #" araya boşluğu koyarak birleştirir"
print(message)
index = message.find("emre")
print(str(index) +". index te mevcut") #-1 verirse mevcut değil
isFound = message.startswith("H") #ne ile basladığını söyler
print(isFound)
isFound = message.endswith("i") #ne ile bittiğini söyler
print(isFound)
message= message.replace("emre","Mevlüt Emre") #karakterleri değiştirir
print(message)
message = message.center(50,'*') #adedince karakter olusturur
print(message)
#fazlası için Python String methodlarının ayrıntıları internette mevcut

