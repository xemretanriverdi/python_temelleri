with open ("yazilim.txt","r") as dosya: #otomatik close yapar
  #  print(dosya.read())

    dosya.seek(10) #10 dan sonra alır
    print(dosya.read(5))#5 karakter okur




