numbers = [1,10,5,16,4,9,10]
letters = ["a","g","s","b","y","a","s"]

val = max(numbers)
print(val)

val= max(letters)
print(val)

numbers[4] = 40
numbers.append(49)        #listeye ekleme
numbers.insert(3,78)      # istedigimiz indexe ekleme (indexteki eleman kaybolmaz saga kayar)
numbers.insert(-1,52)


numbers.pop(0)               #index vererek çıkarma

numbers.pop(-1)
numbers.remove(40)              #listedeki degeri silme

numbers.sort()               #sıralama

numbers.reverse()           #listeyi ters çevirme

 
print(letters.count("a"))


numbers.clear()
print(numbers)

