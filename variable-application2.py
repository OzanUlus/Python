"""
  Application 1 : Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız.
  Application 2 : Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
"""

print("-----Aplication1-----")

pi = 3.14
r =float(input("Yarıçap: "))

alan = pi * (r * r) # pi * (r ** 2) - pi * (r **3)
cevre = 2 * pi * r
print("Alan: " + str(alan))
print("Çevre: " + str(cevre))

print("-----Aplication2-----")

km = float(input("km: "))
mile = km * 1.609344
print("Mil: " + str(mile))
