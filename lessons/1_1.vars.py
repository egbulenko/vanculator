
# создать переменную с пустым значением (None)
a = None

# создать переменные для числовых значением - нулём, положительным, отрицательным
n1 = 1
t0 = 0
y2 = 2
g_5 = -5
print(n1, t0, y2, g_5)

# создать переменные для текстовых значением - пустая строка, непустая строка, несколько строк
text_90 = "loschad"
text = 'Some Text'
text02 = "Some Text"
text3 = ""
text4 = "kjsdfkja sdfwsd" \
        " dsfsdfs ewdwer" \
        "ewq ewrfewr"
text5 = """lksjfwlkfe
ldfnlkf jtow efem; loerj
          gdf ndkjhr m
ml; rgo
"""
print(text_90, text, text02, text3, text4, text5)

print("text4: " + text4)
print("text5: " + text5)

# создать переменные для списка - пустой список, непустой список
list0 = ["Молоко", "печенье"]
list1 = [0, 1, 3]
list2 = ["zero", "one", "dodo"]
list3 = [0, "one", "dodo"]
list4 = [n1, text, list1]
list5 = []

len(list1)
# Длина списка: 3. Содержимое: [0, 1, 3]
print(len(list0))
print(list0)
print(len(list1))
print(list1)
print(len(list2))
print(list2)
print(len(list3))
print(list3)
print(len(list4))
print(list4)
print(len(list5))
print(list5)

# добавить значение в список (list.append(v)), удалить значение из списка (list.remove(v))
print("###############################################")
print(len(list1))
print(list1)

list1.append(4)
print(len(list1))
print(list1)

list1 = list1 + [6, 3]
print(len(list1))
print(list1)

list1.remove(3)
print(len(list1))
print(list1)

list0.append("Мандарины")
print(len(list0))
print(list0)
list0 = list0 + ["Шоколад", "Орешки"]
print(len(list0))
print(list0)

list0.remove("печенье")
print(len(list0))
print(list0)

# сравнить равенство переменных
#   - пустое значение и 0
#   - пустое значение и пустая строка
#   - пустое значение и пустой список
#   - пустая строка и 0
#   - пустая строка и список
#   - разные переменные, строки и числа
print("##################################")
print(0 == 0)
print(0 == 5)
print(0 < 5)
print(5 < 5)
print(5 <= 5)
print(5 > 5)
print(5 >= 5)
a = 5
print(a == 0)
print("A" == "a")
print("A" > "a")
print("A" < "a")
print("Ab" < "ab")
print("aab" < "abb")

print("# COMPARE LISTS #############################")
list1 = [0, 1, 3]
print(list1 == [0, 1, 3])
print(list1 == [0, 3, 1])
a = 1
l2 = [0, a, 3]
print(list1 == l2)
print(list1 != l2)
print(l2)
a = 2
print(list1 == l2)
print(l2)

a = None
print(a == "")
print(a == 0)
print(a == [])
print(a == None)

# взять элемент из списка
print("# LIST ELEMENT #########################")
print(len(list0))
print(list0)

milk = list0[0]
print(milk)
print(len(list0))
print(list0)

list0[3] = milk
print(len(list0))
print(list0)

list0[0] = "Орешки"
print(len(list0))
print(list0)

list0[2] = "Мандарины"
print(len(list0))
print(list0)
list0[1] = "Шоколад"
print(len(list0))
print(list0)

c = list0[2]
list0[2] = list0[1]
list0[1] = c
print(len(list0))
print(list0)
