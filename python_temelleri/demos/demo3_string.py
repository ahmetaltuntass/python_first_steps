website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sonra Python Programlama Rehberiniz (40 Saat)"


print(len(course))

print(website[7:10])

print(website[-3:])  #Sondan başlarken 0 yerine -1'den başlanır.

print(course[0:15])

print(course[-15:])
print(course[::1]) #aynısını yazar
print(course[::-1]) #tersten yazar

name,surname,age,job = "Bora","Yılmaz",32,"Mühendis"

print("Benim adim {} {},Yaşim {} ve mesleğim {}".format(name,surname,age,job) )
print(f"Benim adim {name} {surname}, Yasim {age} ve mesleğim {job}")


a = "Hello world"
x = a.replace("w","W")
print(x)


d = "abc"
print(d*3)