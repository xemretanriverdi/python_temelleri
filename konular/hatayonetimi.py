say1 = input("Sayi1 :")
say2 = input("Sayi2 :")
try:
    say1 = int(say1)
    say2 = int(say2)
    print(say1/say2)

except ValueError: #int e str atama
    print("Lütfen sayi giriniz")

except ZeroDivisionError:# 0 bolen
    print("0 a bolunmez")

# except (ValueError,ZeroDivisionError):
  #  print("ortak kullanım alanı")
