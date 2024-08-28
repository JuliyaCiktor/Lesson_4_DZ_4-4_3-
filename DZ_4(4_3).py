import random
list1 = random.randint(3, 10)
r_list = []
for i in range(list1):
    r_list.append(random.randint(0, 100))
new_list = [r_list[0], r_list[2], r_list[-2]]
print("начальный список", r_list)
print("Новий список:", new_list)