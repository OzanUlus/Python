
title = "Python Programing Lessons"

time = len(title)
print(time)

print(title[:6])

print(title[:6] + " " + title[18:25])

print(title[::-1])

student = input("Student name and surname: ")
degree1 = float(input("Degree1: "))
degree2 = float(input("Degree2: "))
avg = (degree1+degree2) / 2

msg = f"{student} isimli öğrencinin 1.notu {degree1}, 2.notu {degree2} ve not ortalması {avg} olarak hesaplanmıştır"
print(msg)