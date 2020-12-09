name = "Emre "
surname = "Tanrıverdi"
birthday=1999
year = 2020
age=year-birthday
greeting = 'My name is ' + name + " " + surname + " and \nI am " +str(age)  + " years old."

print( greeting)
lenght = len(greeting) #karakter sayısını söyler
# \n ile altsatıra atarız ondan sonraki bosluğu sil hizalarsın

print(greeting[0]) #sıfırıncı karakter
print(greeting[3]) #üçüncü karakter
print(greeting[lenght-1]) #son karaker yada print(greeting[-1])
print(greeting[3:7]) #aradaki karakterleri söyler
print(greeting[3:]) #belirtilen yerden sona kadar
print(greeting[:14]) #baştan belirtilen yere kadar
print(greeting[2:40:2]) #adım sayısını belirtiyor



