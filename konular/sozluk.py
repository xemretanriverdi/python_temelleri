Fikstür = {"Fenerbahce": ["Erzurum","Trabzon","Kocaeli","Besiktas"],"Galatasaray": ["Eskişerhir","Trabzon","Besiktas","Malatya"],"Besiktas": ["Mersin","Amasya","Galatasaray","Fenerbahce"]}

takım = input("Takım ismi giriniz : ")

print("{} Kulübü Maçları : ".format(takım))
i=1
for mac in Fikstür[takım]:
   
    print("{}. Hafta: {}:{} ".format(i,takım,mac))
    
    i+=1


