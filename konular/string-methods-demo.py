website = "http://www.emretanriverdi.com"
course = "Python Kursu: Baştan Sona Python PRogramlama Reberiniz (40 saat)"

#1 " Hello World " baş ve son karakter silin
message= " Hello World "
message = message.strip()
print(message)

#2 websitede sadece emretanriverdi kalsın

#3 course de tüm karakterleri kücük yapın
course =course.lower()
course =course.upper()
course =course.title()


print(course)

#4 website içinde kaç a var?
result = website.count("a")
print(result)

#5 website www ile baslayıp com ile mi bitiyor
result1 = website.startswith("www")
result2 = website.endswith("com")
print("cevap" ,result1*result2)

#6 website içinde .com var mı

result =website.find(".com")
print(result)

#7 course icindekiler alfabetik mi ?

result = course.isalpha()
print(result)

#8 contents ifadesini 50 satıra yerleştirip sağına soluna * ekleyiniz

ifade = "contens"

ifade = ifade.center(50,"*")
print(ifade)

#9 course tüm bosluklara - değiştir

course = course.replace(" ","-")
print(course)

#10 hello word deki word u there olarak değiştir.
ifade2 = "Hello Word"
ifade2 = ifade2.replace("Word","There")
print(ifade2)
#11 course ifadesinibosluklardan ayır

course = course.split("-")
print(course)