
students = {
    101: ["Yiğit Bilgi", 2010, [40, 80, 90]],
    102: ["Ada Bilgi", 2012, [80, 80, 80]],
    103: ["Çınar Turam", 2010, [70, 70, 70]]
}

number = int(input("Lütfen öğrenci numarası giriniz: "))

student = students[number]

age = 2025- student[1]
avg = (student[2][0] + student[2][1] + student[2][2]) / 3

print(f"{number} numaralı {student[0]} adlı öğrenci yaşı {age} ve not ortalaması {avg}.")