
list1 = ["Bmw","Mercedes","Opel","Mazda"]
print(len(list1))
print(list1[0]+" , " +list1[3])

list1[3] = "Toyota"
print(list1)

print("Mercedes" in list1)

list1 = ["Bmw","Mercedes","Opel","Mazda"]
print(list1[-2])

print(list1[0:3])

list1[-2:] = ["Toyota","Renault"]
print(list1)



list1 = ["Bmw","Mercedes","Opel","Mazda"]
list1 = list1 + ["Audi"] + ["Nissan"]
print(list1)

"""
10. soru
"""

del list1[-1]
print(list1)




#10. soru sonu

print(list1[::-1])

studentA = ["Yigit","Bilgi","2010",[70,60,70]]
studentB = ["Sena","Turan","1999",[80,80,70]]
studentC = ["Ahmet","Turan","1998",[80,70,90]]

print(studentA[0]+" "+studentA[1]+" "+studentA[2])

result = print("Ögrencinin adi {} Soyadi {} Dogum Tarihi {}".format(studentA[0],studentA[1],studentA[2]))
result1 = print(f"Ögrencinin Adi Yigit Soyadi Bilgi Dogum Tarihi 2010")