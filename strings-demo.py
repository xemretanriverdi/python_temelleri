website = "http://www.emretanriverdi.com"
course = "Python Kursu: Baştan sona Python Programlama Rehberiniz (40 saat)"

#1 course da bulunan karakter dizisi

courseLenght = len(course)
print("Course karakter sayısı : " + str(courseLenght) )

#2 website içinden www alın

website2 = website[:7] + website[10:]
print(website2)

#3 website içinden com karakterlerini alın

website3 = website[:-3]
print(website3)

#4 course içinden ilk 15 ve son 15 karakterleri alın
course2 = course[:16] + course[-14:]
print(course2)

#5 course tersten yazdırın
courseTers= course[::-1]
print("tersten  " , courseTers)


#benim adım bora yılmaz yaşım 32 ve mesleğim mühendis  
# ifadesini ekrana değişkenli yazır


name= "Emre"
surname= "Tanrıverdi"
age= 21
job= "Bilgisayar Mühendisi"

result = f" Benim adım {name} {surname} yaşım {age} mesleğim {job}."

print(result)

    #hello world kelimesindeki w  ile W değiş
selamla = "hello world"
print(selamla[0:6]+"W"+selamla[7:])

#abc ifatedesi yan yana üc defa yaz

karakter="abc"
print(3*karakter)