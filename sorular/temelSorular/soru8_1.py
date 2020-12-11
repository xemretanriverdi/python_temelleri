def fakt(list):
    list4=[]
    for sayi in list:
        a=sayi-1
        while(a>=1):
            sayi=a*sayi
            a=a-1
        list4.append(sayi)
        
    return list4