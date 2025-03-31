
fuelType = input("Yakıt tipi: ")
fuelCount = float(input("100 km ne kadar yakıyor: "))

if(fuelType == "benzin"):
    price = (fuelCount * 39.95) / 100
    print(f"Km başına ücret: {price}")
elif(fuelType =="dizel"):
    price = (fuelCount * 41.71) / 100
    print(f"Km başına ücret: {price}")
else:
    price = (fuelCount * 20.28) / 100
    print(f"Km başına ücret: {price}")
#--------------------------------------------------------------------

note1 = float(input("1.Not: "))
note2 = float(input("2.Not: "))
note3 = float(input("3.Not: "))

avg = (note1 + note2 + note3) / 3

if(avg < 25):
    print(0)
elif(avg >= 25 and avg < 45):
    print(1)
elif(avg >= 45 and avg < 55):
    print(2)
elif(avg >= 55 and avg < 70):
    print(3)
elif(avg >= 70 and avg < 85):
    print(4)
else:
    print(5)
