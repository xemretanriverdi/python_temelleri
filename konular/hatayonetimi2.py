try:
    dosya = open("fener.txt","r")

except IOError: 
    print("Dosya bulunamadı...")

finally:
    dosya.close()