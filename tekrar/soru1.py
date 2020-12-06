#birden yüze kadar yedi yada 3 katlari değilse yazdir yazdır

i = 1
while(i<100):
    if i%3==0 or i%7==0 :
        i+=1
        continue
    print("i :",i)
    i+=1
