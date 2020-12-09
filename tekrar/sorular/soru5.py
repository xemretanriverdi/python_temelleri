#iki isim isteyin ve bu kelimelerin ortak harflerini liste ekleyip yazdırın

isim1= input("Bir isim Giriniz :")
isim2= input("Bir isim Giriniz :")
harfler =[]
for harf in isim1:
    for harf2 in isim2:
        if harf==harf2:
            harfler.append(harf)


for harf in harfler:
    print(harf)