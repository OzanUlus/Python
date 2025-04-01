
# start = int(input("Başlangıç değeri: "))
# end = int(input("Bitiş değeri: "))

# while start <= end:
#     if(start % 2 == 0):
#         print(start)
#     start +=1

# print("--------------------------------------------")

# i=100
# while i >=1:
#     print(i)
#     i -= 1

# numbers = []
# number1 = int(input("1.Sayı: "))
# number2 = int(input("2.Sayı: "))
# number3 = int(input("3.Sayı: "))
# number4 = int(input("4.Sayı: "))
# number5 = int(input("5.Sayı: "))
# numbers.append(number1)
# numbers.append(number2)
# numbers.append(number3)
# numbers.append(number4)
# numbers.append(number5)

# i=0
# while( i < len(numbers)):
#     print(numbers[i])
#     i += 1

while True:
    username = input("Kullanıcı adını girin: ").strip()  # Başındaki ve sonundaki boşlukları temizler
    if " " in username:  # Eğer boşluk içeriyorsa
        print("Kullanıcı adı boşluk içeremez! Tekrar deneyin.")
        continue  # Başa döner
    break  # Geçerli bir username girildiğinde döngüden çıkar

print(f"Kullanıcı adı başarıyla kaydedildi: {username}")
        


