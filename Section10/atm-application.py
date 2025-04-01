
bankAccountInfo = {"Name-Surname" : "Ozan Ulus","Balance" : 125000, "Ex-Balance" : 50000}

def menu(number):
    if(number == 1):
        accountInformation()
    elif(number == 2):
        moneyAmount = float(input("Çekmek istediğiniz miktarı giriniz: "))
        drawMoney(moneyAmount)
    elif(number == 3):
        moneyAmount = float(input("Yatırmak istediğiniz miktarı giriniz: "))
        sendMoney(moneyAmount)
    else:
        print("YAnlış seçim yaptınız.")

        



def drawMoney(moneyAmount):
    if moneyAmount <= 0:
        print("Geçersiz tutar! Pozitif bir miktar giriniz.")
        return

    if moneyAmount > bankAccountInfo["Balance"]:
        choice = int(input("Çekmek istediğiniz miktar hesabınızda yoktur. "
                           "Ek hesaptan çekmek ister misiniz?\n"
                           "Ek hesap kullanmak için 1, çıkış için 2 basınız: "))

        if choice == 1:
            toplamBakiye = bankAccountInfo["Balance"] + bankAccountInfo["Ex-Balance"]
            
            if toplamBakiye >= moneyAmount:
                difference = moneyAmount - bankAccountInfo["Balance"]
                bankAccountInfo["Ex-Balance"] -= difference
                bankAccountInfo["Balance"] = 0
                print(f"{moneyAmount} TL çekildi.  Ek hesap bakiyesi: {bankAccountInfo['Ex-Balance']} TL")
            else:
                print("Bu miktar için işlem yapamıyoruz. Yetersiz ek hesap!")
        else:
            print("İşlem iptal edildi.")
    else:
        bankAccountInfo["Balance"] -= moneyAmount
        print(f"{moneyAmount} TL çekildi. Yeni bakiye: {bankAccountInfo['Balance']} TL")

def sendMoney(moneyAmount):
    if moneyAmount < 0:
        print("Geçersiz tutar. Pozitif bir miktar giriniz.")
        return
    
    bankAccountInfo["Balance"] += moneyAmount
    print(f"Para yatırma işleminiz gerçekleşmiştir. Yeni bakiye {bankAccountInfo['Balance']} Tl ")

def accountInformation():
    print(f"Hesabınızda {bankAccountInfo['Balance']} Tl vardır ve Ek hesap limitiniz {bankAccountInfo['Ex-Balance']} ")


print("Yapmak istediğiniz işlemi seçiniz. Sorgu için 1 , para çekmek için 2 , para yatırmak için 3")
number = int(input("Seçiminiz: "))
menu(number)