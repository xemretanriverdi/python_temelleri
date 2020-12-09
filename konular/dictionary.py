sehirler =["kocaeli", "istanbul"]
plakalar = [41,34]

print(plakalar[sehirler.index("istanbul")])

plakalar = {"ankara" : 6, "izmir": 35}
print(plakalar["ankara"])
print(plakalar["izmir"])
plakalar["erzurum"] = 6
print(plakalar)
plakalar["izmir"]="new value"
print(plakalar)

#baska örnek

users={


    "emrebey" : 21,
    "ahmetbey": 20,

}

print(users["emrebey"])

users2={
"emrebey" : {
    "age" : 21,
    "roles":["admin","user"],
    " email" : "emrebey@gmail.com",
    "addres" : "pendik",
    "phone": 123212
},
"ahmetbey" : {
    "age" : 14,
    " email" : "ahmetbey@gmail.com",
    "addres" : "tuzla",
    "phone": 212312232
},
"ömerbey" : {
    "age" : 19,
    " email" : "ömerbey@gmail.com",
    "addres" : "kartal",
    "phone": 4124124
},

}
print(users2["emrebey"])
print(users2["ahmetbey"]["age"])
print(users2["ömerbey"]["addres"])

print(users2["emrebey"]["roles"][0])

