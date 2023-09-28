website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sonra Python Programlama Rehberiniz (40 Saat)"

a = " Hello World "
a = a.strip()
print(a)


b = website.split(".")           #website.split("http://w.com")
print(b[1])

course = course.lower()
print(course)

print(website.count("a"))  #website.count("www",0,10) #0 ile 10. index arasinda ne kadar var?


result = website.startswith("www")
print(result)

isExist = website.count(".com")
print(bool(isExist))

print(course.isdigit())

x = "Contents"
print(x.center(50,"*"))

print(course.replace(" ","-"))

print(a.replace("World","There"))

print(course.split(" "))