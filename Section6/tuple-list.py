
my_list = [1,2,3]
my_tuple = (1,2,3)          #değiştirlemez add,delete and update

print(type(my_list))
print(type(my_tuple))

result = my_list[0]
result = my_tuple[0]

my_list.append(3)
# my_tuple.append(3)
result = my_list
result = my_tuple


print(result)

my_tuple2 = tuple(my_list)
my_list2 = list(my_tuple)

print(type(my_tuple2))
print(type(my_list2))


