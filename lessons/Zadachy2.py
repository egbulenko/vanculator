import random

my_list = [1, 2, 3, 4]
print(my_list)
random.shuffle(my_list)
print(my_list)



my_list = [1, 3, 7, 4, 5]

nomer_elementa = 1
for e in my_list:
    print("элемент", nomer_elementa, ": ", e)
    nomer_elementa = nomer_elementa+1