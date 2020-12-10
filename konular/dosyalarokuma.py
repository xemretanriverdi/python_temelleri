dosya=open("yazilim.txt","r")
#print(dosya.read()) #herseyi okur
#print(dosya.readline())#ilk satiri alır
print(dosya.readlines())#ilk satiri liste olarak alır
dosya.close()