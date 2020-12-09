#birden 100 asal sayilar yazdir
def asalmi(sayi):
    a=True
    j=2
    while(j<sayi):
        if sayi%j==0:
            a=False
        j+=1
    return a

    

        


i = 2
while (i<100):
    if asalmi(i):
        print(i , "sayisi asaldir")
    i+=1
