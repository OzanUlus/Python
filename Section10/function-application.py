
parameter = input("Parametre giriniz: ")
time = int(input("Tekrar sayısı: "))

def wordWrite(parameter):
  return parameter

def write(time):
  
  count = 0
  while(count < time):
    print(wordWrite(parameter))
    count += 1

write(time)
print("------------------------------------")
def dikdörtgenAlan(a,b):
    return a * b

def dikdörtgenCevre(a,b):
    return 2 * (a + b)

print(dikdörtgenAlan(10,15))
print(dikdörtgenCevre(10,15))
print("------------------------------------")

import random

def yazi_tura():
    result = random.choice(["yazi","tura"])
    return result

print(yazi_tura())

print("------------------------------------")
sayi1 = int(input("Sayi1: "))
sayi2 = int(input("Sayi2: "))

def asal_mi(sayi):
    if sayi <= 2:
        return False
    for i in range(2,int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

def asalBul(sayi1,sayi2):
    return [sayi for sayi in range(sayi1, sayi2 + 1) if asal_mi(sayi)]

print(asalBul(sayi1,sayi2))

print("------------------------------------")



def tamBölenler(sayi):
    return[i for i in range(1,sayi+1) if sayi % i == 0]

sayi = int(input("sayı giriniz: "))
print(f"{sayi} nın tam bölenleri: {tamBölenler(sayi)}")

  