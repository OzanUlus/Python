
def toplam():
    return 10 + 20

sonuc = toplam()
print(sonuc)

def yil():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    return yil() - 1995

print(yasHesapla())

def saat():
    import datetime
    return datetime.datetime.now().hour

def selamlama():
    if(saat() < 12):
        return("Günaydın")
    else:
        return("Merhaba iyi çalışmalar.")

print(selamlama())