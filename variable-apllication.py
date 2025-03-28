
nameSurname = "Ozan Ulus"
phoneNumber = "0123456789"
mail = "info@ozanulus.com"
city = "Ankara"

soldProduct = "Mouse"
mousePrice = 550

soldProduct2 = "Keyboard"
keyboardPrice = 650

soldProduct3 = "Laptop"
laptopPrice = 55000

#--------------------------------------

totalPrice = mousePrice + keyboardPrice + laptopPrice
taxPrice = totalPrice * 0.18
taxlessPrice = totalPrice - taxPrice
print("Bill Information: " + nameSurname + "-" + phoneNumber + "-"  + mail + "-"  + city)
print("Taxless Price: " + str(taxlessPrice))
print("Tax Price: " + str(taxPrice))
print("Total Price: " + str(totalPrice))
