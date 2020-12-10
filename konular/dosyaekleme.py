with open("yazilim.txt","r+") as dosya: #r+ hem okur hem ekler
    data=dosya.read()
    dosya.seek(0)
    
    data ="Flutter\n" +data #sona ekler
    # eger basına eklemek istiyorsak tüm veriyi kesip sonra ekleyip sonra yapıstırcaz ex:
    dosya.write(data)

