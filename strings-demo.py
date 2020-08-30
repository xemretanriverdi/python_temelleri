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

#benim adım bora yılmaz yaşım 32 ve mesleğim mühendis  ifadesini ekrana değişkenli yazır

result = f"/benim adım" {name}