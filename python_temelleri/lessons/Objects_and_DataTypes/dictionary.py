#key - value


#liste yöntemiyle birebir indextekini bulma
# sehirler = ["kocaeli","istanbul"]

# plakalar = [41,34]

# print(plakalar[sehirler.index("istanbul")])



#print(plakalar["kocaeli"]) => 41 

# plakalar = {"Kocaeli" : 41,"İstanbul" : 34}

# print(plakalar["Kocaeli"])


# plakalar["ankara"] = 6
# print(plakalar)

# plakalar["Kocaeli"] = "new value"
# print(plakalar)

users = {
    "sadikturan" : {
        "age": 36,
        "roles" : ["user"],
        "email" : "sadik@gmail.com",
        "phone" : "1231233"
    },
    "cinarturan" : {
     "age" : 2,
     "roles" : ["admin","user"],
        "email" : "cinar@gmail.com",
        "phone" : "123123"

    }


}

print(users["cinarturan"])
