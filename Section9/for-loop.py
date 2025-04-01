
#for => list
# numbers = [1,2,3,4,5,8,91,21]

# for number in numbers:
#     print(number)

numbers = [3,5,7,2,12,32,45]

for number in numbers:
    print(number)
print("-----------------------------------------------")
for number in numbers:
    x = number % 3 
    if(x == 0):
        print(number)
print("-----------------------------------------------")

total = 0
for number in numbers:
    total += number
print(total)    
print("-----------------------------------------------")

products = ["samsung s24","samsung s22","iphone 15","iphone 14"]

for product in products:
    if "iphone" in product.lower():
        print(product)

print("-----------------------------------------------")

count = 0
for product in products:
    if "samsung" in product.lower():
        count += 1
print(count)

print("-----------------------------------------------")

products = [
    {"productName" : "HP Victus", "price" : "32999"},
    {"productName" : "Lenovo ThinkPad", "price" : "25499"},
    {"productName" : "Apple Macbook", "price" : "49999"},
    {"productName" : "Huawei Matebook", "price" : "26999"},
    {"productName" : "Casper Niravana", "price" : "20000"},
]

for product in products:
    productsName = product["productName"]
    productsPrice = product["price"]

    print(f"{productsName}marka ürünün fiyatı {productsPrice} Türk Lirasıdır.")

print("-----------------------------------------------")

total = 0
for product in products:
    productsPrice = int(product["price"])
    total += productsPrice
print(f"Toplam ürün fiyatı {total} TL'dir.")

print("-----------------------------------------------")

for product in products:
    productsPrice = int(product["price"])
    if(productsPrice > 25000 and productsPrice < 40000):
        print(product["productName"])

print("-----------------------------------------------")

keys = input("Anahtar kelime giriniz: ")
for product in products:
    pro = product[keys]
    print(pro)


