
brands = ["Toyota","Bmw","Renault","Mercedes"]

count = len(brands)
print(count)

firstBrand = brands[0]
lastBrand = brands[-1]
print(f"First: {firstBrand} Last: {lastBrand}")

brands[2] = "DS"
print(brands)

result = "DS" in brands
print(result)

print(brands[:2])

ressult2 = brands + ["Citreon","Ford"]
print(ressult2)

del ressult2[5]
print(ressult2)

students = [["Yiğit Bilgi", 2010 ,[70, 80, 90]], ["Ada Bilgi", 2011 ,[70, 70, 80]],["Çınar Bilgi", 2017 ,[60, 60, 90]]]

student1 = students[0][0]
student1Age = 2025-students[0][1]
print(f"{student1} yas = {student1Age}")

student2 = students[1][0]
student2Age = 2025-students[1][1]
print(f"{student2} yas = {student2Age}")

student3 = students[2][0]
student3Age = 2025-students[2][1]
print(f"{student3} yas = {student3Age}")

student1Avg = (students[0][2][0] + students[0][2][1] +students[0][2][2]) / 3
print(f"{student1} ortalama = {student1Avg}")

student2Avg = (students[1][2][0] + students[1][2][1] +students[1][2][2]) / 3
print(f"{student2} ortalama = {student2Avg}")

student3Avg = (students[2][2][0] + students[2][2][1] +students[2][2][2]) / 3
print(f"{student1} ortalama = {student3Avg}")
