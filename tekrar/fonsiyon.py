def selamla(isim):
    print("Merhaba ",isim)
    print("Nasilsin")


selamla("Emre ")

def kullaniciBilgi(isim="Belirtilmemis",soyisim="Belirtlilmemis"):
    print("Kullanicinin ismi {}".format(isim))
    print("Kullanicinin soyismi {}".format(soyisim))

kullaniciBilgi("Emre")


def topla(a,b):
    return a+b

print(topla(3,4))
