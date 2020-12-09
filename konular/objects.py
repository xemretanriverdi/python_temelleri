
class Account:

    def __init__(self,isim,numara,bakiye):
        self.isim= isim
        self.numara = numara
        self.bakiye = bakiye

    def hesapBilgileri(self):
        print("Hesap bilgilerii:")
        print("Kullanici adi: ",self.isim)
        print("Hesap no: ",self.numara)
        print("Bakiye : ",self.bakiye)

    def paraCek(self,miktar):
        if miktar<self.bakiye:

            self.bakiye -=miktar
            print(self.isim," isimli Müşterinin Bakiyesi = ",self.bakiye)
        else:
            print("Bakiyeniz yetersiz")

account1=Account("Emre Tanrıverdi",1,23323)
account2=Account("Ahmet Tanrıverdi",2,13232)
account3=Account("Emircan Alioğlu",3,3421)
account4=Account("Ömer Sofi",4,123124)




account1.hesapBilgileri()
account1.paraCek(30000)
