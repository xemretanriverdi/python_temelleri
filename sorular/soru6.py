
import random
#verilen sayi tahmin oyunu

sayi1=random.randint(1,100)



sayi2=0
puan=100
while(sayi2!=sayi1):
    sayi2 = int(input("2. Yarismaci bir sayi girsin : "))
    if(sayi1>sayi2):
        print("Daha yüksek bir sayi giriniz")
            
    if(sayi1<sayi2):
        print("Daha düşük bir sayi giriniz")
            
    puan=puan-10
    if puan==0:
         print("G A M E  O V E R")
         break
    
if(sayi2==sayi1):
    print("Doğru tahmin ettiniz yarısmacının tuttuğu sayi = {} \n puanınınız: {}".format(sayi1,puan))


