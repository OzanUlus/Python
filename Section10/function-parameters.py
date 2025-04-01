
def selamlama(isim):
    return f"Merhaba {isim}"

print(selamlama("Ozan"))
print(selamlama("Yaşar"))

def toplam (sayi1,sayi2):
    return sayi1 + sayi2

print(toplam(10 , 20))
print(toplam(30 , 20))

def yil():
    import datetime
    return datetime.datetime.now().year

def yasHesapla(doğumyili):
    return yil() - doğumyili

print(yasHesapla(1995))
print(yasHesapla(1986))
print(yasHesapla(1992))
print(yasHesapla(1996))

