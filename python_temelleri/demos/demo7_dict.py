"""
ögrenciler = {

"120" :{
"ad" : "Ali",
   "soyad" : "Yilmaz",
   "telefon" : "532 000 00 01"
},

"125": {
           "ad" : "Can",
                 "soyad" : "Korkmaz",
                   "telefon" : "532 000 00 02"
},

"128" : {
"ad" : "Volkan",
"soyad" : "Yükselen",
"telefon" : "532 000 00 03"

},

}
"""
ögrenciler = {}
yourNumber = input("Numaranizi giriniz: ")
name = input("Adinizi giriniz: ")
surname = input("Soyadinizi giriniz: ")
phone = input("Ögrenci telefon: ")

ögrenciler[yourNumber] = {
    "ad" : name,
    "soyad" : surname,
    "telefon" : phone
}

yourNumber = input("Numaranizi giriniz: ")
name = input("Adinizi giriniz: ")
surname = input("Soyadinizi giriniz: ")
phone = input("Ögrenci telefon: ")

ögrenciler[yourNumber] = {
    "ad" : name,
    "soyad" : surname,
    "telefon" : phone
}

yourNumber = input("Numaranizi giriniz: ")
name = input("Adinizi giriniz: ")
surname = input("Soyadinizi giriniz: ")
phone = input("Ögrenci telefon: ")

ögrenciler[yourNumber] = {
    "ad" : name,
    "soyad" : surname,
    "telefon" : phone
}

ogrNo = (input("Ögrenci No: "))

ögrenci = ogrNo[yourNumber]
print(ögrenci)