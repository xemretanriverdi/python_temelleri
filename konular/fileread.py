file = open("dosya.txt","r")#r okur
file.seek(10)  # 10 tane atla öyle oku
veri = file.read(2) #bastan 2 karakter
#  veri = file.read()  #veri okur

print(veri)



for satir in file: #satir satir olusturur
    print(satir)
file.close()

