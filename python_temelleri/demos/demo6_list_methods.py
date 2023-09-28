
names = ["Ali","Yagmur","Hakan","Deniz"]
years = ["1998","2000","1998","1987"]

names.append("Cenk")
print(names)

names.insert(0,"Sena")
print(names)             #names.insert(len(names),"Mehmet") #Listenin sonuna length ile ekleme

names.remove("Deniz")
#names.pop(1)
print(names)

names = ["Ali","Yagmur","Hakan","Deniz"]
print(names.index("Deniz"))

result = "Ali" in names
print(result)

names.reverse()
print(names)

names.sort()
print(names)




years = ["1998","2000","1998","1987"]
years.sort()
print(years)

a = ["Chevrolet,Dacia"]
#str = "Chevrolet, Dacia"
# result= str.split(",")

b = max(years)
c = min(years)
print("Max value is :  ",b + " Min value is  ",c)

print(years.count("1998"))

years.clear()
print(years)


list1 = []

marka = input("Marka:  ")
list1.append(marka)

marka = input("Marka:  ")
list1.append(marka)

marka = input("Marka:  ")
list1.append(marka)

print(list1)