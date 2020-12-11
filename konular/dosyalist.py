with open("yazilim.txt","r+") as dosya:
    data = dosya.readlines()
    data.insert(1,"C++\n") #birinci satira ekledi
    dosya.seek(0)
    dosya.writelines(data)