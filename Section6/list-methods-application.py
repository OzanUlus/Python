
customers = ["ozanulus","ahmettaştekin","yaşaryıldırım","berkalpdirem"]
order_totals = [12000,13000,5000,15000]

# customers.append("ozanulus")
# order_totals.append(5000)
# customers.pop()
# order_totals.pop()

# result = customers
# result2 = order_totals

# print(result)
# print(result2)

# customer1 = customers[0]
# customer1Total = order_totals[0]
# print(f"{customer1} isimli müşterinin sipariş toplamı {customer1Total} liradır.")

# customer2 = customers[1]
# customer2Total = order_totals[1]
# print(f"{customer2} isimli müşterinin sipariş toplamı {customer2Total} liradır.")

# customer3 = customers[2]
# customer3Total = order_totals[2]
# print(f"{customer3} isimli müşterinin sipariş toplamı {customer3Total} liradır.")

# customer4 = customers[3]
# customer4Total = order_totals[3]
# print(f"{customer4} isimli müşterinin sipariş toplamı {customer4Total} liradır.")

customers.sort()
print(customers)

order_totals.sort(reverse=True)
print(order_totals)

minOrder = min(order_totals)
print(minOrder)

count = customers.count("ozanulus")
print(count)

customers.remove("ahmettaştekin")
print(customers)

customers.clear()
order_totals.clear()
print(customers)
print(order_totals)

customer1 = input("Customer1 Name-Surname: ")
customer1Total = input("Customer1 Total: ")
customers.append(customer1)
order_totals.append(customer1Total)

customer2 = input("customer2 Name-Surname: ")
customer2Total = input("customer2 Total: ")
customers.append(customer2)
order_totals.append(customer2Total)

customer3 = input("customer3 Name-Surname: ")
customer3Total = input("customer3 Total: ")
customers.append(customer3)
order_totals.append(customer3Total)

print(customers)
print(order_totals)





