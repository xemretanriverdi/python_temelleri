
# iki modul olustur biri verilen listi asal list biri de fakt list yapsın. 1 den 40 a kadar  sayilarin asal olanlarının faktoriyelleri

from soru8_1 import *
from soru8_2 import *
list=[]
for sayi in range(1,41):
    list.append(sayi)

print("Asal olanları saklanacak sayilar")
print(list)
list2=asal(list)
print("Asal olanlari")
print(list2)
list3=fakt(list2[:5])
print("Asal olan ilk 5 faktoriyel:")
print(list3)





