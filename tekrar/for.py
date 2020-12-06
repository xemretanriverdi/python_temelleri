i=0

while i<10:
    print("i:",i)
    i= i+1 # i+=1

#faktoriyel alma

sayi = int(input("Bir sayi giriniz : "))

i=1
fakt=1
while(i<=sayi):
    fakt=fakt*i
    i+=1
print("{} sayisinin faktoriyeki {} dir".format(sayi,fakt))

x={1,2,3,5,6}

for sayi in x:
    print(sayi)

for sayi in range (1,30):
    print(sayi)

for sayi in range (1,100,2):
    print(sayi)