def ortalama(sayilar):
    ort=len(sayilar)
    toplam =0
    for sayi in sayilar:
        toplam=toplam+sayi
    sonuc = toplam/ort

    return sonuc


sayilar = []
sayi= int(input("Sayi giriniz: "))
sayilar.append(sayi)


while (ortalama(sayilar)<10):
    sayi= int(input("Sayi giriniz: "))
    sayilar.append(sayi)
    print("ortalama = ",ortalama(sayilar))

print("Sayilar ortalması {} olduğu için problem tamamlanmıstır",ortalama(sayilar))



    







