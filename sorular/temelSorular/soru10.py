#coklu kalıtım ornegı

class Ogrenci():
    def ogrenciCalis(self):
        print("Ogrenci ders calısıyor")



class Calisan():
    def calis(self):
        print("Personeller suan calısıyor")


class Yazilimci (Ogrenci,Calisan):
    pass


yazilimci =Yazilimci()
yazilimci.ogrenciCalis()
yazilimci.calis()
