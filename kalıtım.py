class Calisan():
    def __init__(self,isim,maas,departman):
        print("Çalısan sınıfnın yapıcı fonksiyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman

    def bilgileriGoster(self):
        print("Adi : ",self.isim)
        print("Maas : ",self.maas)
        print("Departman : ",self.departman)

    def maasZam(self,zamMiktari):
        print("Maasa zam yapıldı")
        self.maas+=zamMiktari
    

    def departmanDegis(self,yeniDepartman):
        self.departman=yeniDepartman


calisan = Calisan("Emre Tanriverdi",34700,"Mühendis")
Calisan.departmanDegis(calisan,"CEO")
Calisan.bilgileriGoster(calisan)


class Yönetici(Calisan): #annesi calısan
    def __init__(self, isim, maas, departman,eleman):
        super().__init__(isim,maas,departman)#onları tekrar self diyetanıtmamak icin

        self.eleman = eleman
    def bilgileriGoster(self):
        print("Calisan Sayisi:",self.eleman)
        return super().bilgileriGoster()
       #override
    def kisiSayisiArttir(self,arttı):
        self.eleman=self.eleman+arttı
yönetici = Yönetici("Cem",50000,"Patron",1000)
Yönetici.kisiSayisiArttir(yönetici,3000)

Yönetici.bilgileriGoster(yönetici)
