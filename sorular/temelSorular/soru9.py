#arac sınıfı olusturun ve arac sınıfından tır üretin


class Vasita():
    def __init__(self,id,sınıf,marka,model,fiyat,yil):

        self.id=id
        self.sınıf="Vasıta"
        self.marka=marka
        self.model=model
        self.fiyat=fiyat
        self.yil=yil

    def bilgiGoster(self):
        
        print(self.sınıf," Bilgileri")
        print(self.sınıf," ID         :   ",self.id)
        print(self.sınıf," Kasa Tipi  :   ",self.sınıf)
        print(self.sınıf," Marka      :   ",self.marka)
        print(self.sınıf," Modeli     :   ",self.model)
        print(self.sınıf," Cıkıs Yılı :   ",self.yil)
        print(self.sınıf," Fiyatı     :   ",self.fiyat)


    def zamYap(self,zamMiktari):
        self.fiyat=fiyat+zamMiktari
        print("Zam Yapildi")

    def indirimYap(self,indirimMiktari):
        self.fiyat=fiyat-indirimMiktari
        print("İndirim Yapildi")



class Kamyon(Vasita):
    def __init__(self, id, sınıf, marka, model, fiyat, yil,uzunluk):
        super().__init__(id,sınıf, marka, model, fiyat, yil)
        self.sınıf="Kamyon"
        self.uzunluk=uzunluk
    
    def bilgiGoster(self):
        
        return super().bilgiGoster()


volvo =Kamyon(1," ","Volvo","FH 540",1320000,2015,3000)

Kamyon.bilgiGoster(volvo)

        

    



        