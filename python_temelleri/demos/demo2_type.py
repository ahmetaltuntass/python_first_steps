"""

Daire Alani : pi r^2
Daire cevresi : 2 pi r

* Yari çapi verilen dairenin alan ve çevresini hesaplayiniz.
r 3.14
"""
pi = 3.14

yariCap = float(input("Yaricapi giriniz: "))


alan = pi * (yariCap**2)
cevre = 2* pi *(yariCap)

print("alan: ",str(alan) +  " Cevre: ",str(cevre))
