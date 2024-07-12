#Словарь
print("Словари")
my_dict = {"Facebook" : 23429052, "GitHub" : 32824298222, "Google" : 4555329042}
print(my_dict)
print(my_dict["Facebook"])

my_dict["VK"] = 382265578
print(my_dict)
my_dict["4chan"] = 1004423315
print(my_dict)

del my_dict["Google"]
print(my_dict)

print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")#Множество
print("Множества")
my_set = {1, 1, 1, 2, 2, 2, 3, 3, 3}
print(my_set)

my_set.add("Гомер")
print(my_set)
my_set.add(1.2)
print(my_set)

my_set.discard(1)
print(my_set)