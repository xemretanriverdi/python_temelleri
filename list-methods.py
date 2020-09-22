numbers = [1,10,4,52,23,4]
letters = ['a','s','f','r']
val= min(numbers)
val= max(numbers)
val= max(letters)
print(val)

val2 = numbers[3:6]
val2 = numbers[3:6]

val2 = numbers[::2] #ritim
numbers[2]=99
val2 = numbers[2]
numbers.append(49) #eleman ekler
numbers.append(59)
numbers.insert(3, 77) #indexe ekler
numbers.insert(-1, 31) #indexe ekler
numbers.pop() #son rakamı siler 
numbers.pop(2)
numbers.remove(4) #karakter varsa siler

numbers.sort() #liste kücükten b düzelir
numbers.reverse() #liste büyükten k düzelir

letters.sort()
letters.reverse() #liste büyükten k düzelir

print(len(numbers))
print(len(letters))

print(numbers)
print(letters)

print(numbers.count(10))
