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