import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

# cursor.execute("select * from customers where city = 'Oslo'")
# customers = cursor.fetchall()

# for customer in customers:
#     print(customer[1] + " " + customer[2])

sql = "INSERT INTO genres(name) VALUES('Macera')"
cursor.execute(sql)
connection.commit()

connection.close()
print("Db is ready")