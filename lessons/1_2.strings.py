
a = "first string"
b = "b"

print(a)
print(b)
print(a + b)
print(a + " " + b)

print(3)
print(a + " " + str(3))

list0 = ["Молоко", "печенье"]
# Длина списка: 3. Содержимое: [0, 1, 3]
print(len(list0))
print(list0)
print("Длина списка: " + str(len(list0)) + ". Содержимое: " + str(list0))

print("Длина списка: %s. Содержимое списка: %s" % (len(list0), list0))

a = input("Введи число")
print(int(a) + 1)