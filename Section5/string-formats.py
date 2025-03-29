# string concat
name = "Ozan"
surname = "Ulus"
age = 30

# msg = "My name is " + name + " " + surname + "." + " I'm " + str(age) + " years old."

#string format

# msg = "My name is {} {}. I'm {} years old.".format(name, surname, age)
# msg = "My name is {1} {0}. I'm {2} years old.".format(name, surname, age)
# msg = "My name is {n} {s}. I'm {a} years old.".format(n=name, s=surname, a=age)

#f-string

msg = f"My name is {name} {surname}. I'm {age} years old."
print(msg)