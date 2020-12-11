def asal(list):
    asallist=list
    for sayi in asallist:
        temp = 2
        while(temp<sayi):
            if(sayi%temp==0):
                asallist.remove(sayi)
                temp+=1
            break
                
    return(asallist)


