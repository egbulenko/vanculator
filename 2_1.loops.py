# цикл по списку  (for .. in)
list1000 = ["dgegidy","bloopersy","konfetki"]
# print(list1000[0])
# print(list1000[1])
# print(list1000[2])

for element in list1000:
    print(element)


# просто N итераций (range)

# for i in range(5):
#     print(i)
#
# for i in range(2, 5):
#     print(i)
for lalala in range(0,6):
    print("очистить кожуру")
    print("съесть мандарин")

print("выбросить кожуру")


# while .. do

age = 2

while age < 12:
    print("дождаться нового года")
    print("принести подарок с работы: тебе уже", age)
    age = age + 1
print("а всё, подарков больше нет: ты слишком взрослый, тебе уже", age)

# прерываение выполнения цикла (break, continue)
print("===BREAK==========================================================================")
age = 8
want_present = False
while age < 12:
    print("дождаться нового года")
    print("принести подарок с работы: тебе уже", age)
    if not want_present:
        print("мне не нравятся такие подарки, не приноси их больше")
        break
    age = age + 1

if age >= 12:
    print("а всё, подарков больше нет: ты слишком взрослый, тебе уже", age)
else:
    print("а всё, подарков больше нет: ты сам от них отказался, тебе уже", age)



print("===CONTINUE==========================================================================")
age = 8
want_present = False
while age < 12:
    print("дождаться нового года")
    print("принести подарок с работы: тебе уже", age)
    if not want_present:
        print("мне не нравятся такие подарки, не приноси их на следующий год")
        age = age + 2
        continue
    print("+1")
    age = age + 1

if age >= 12:
    print("а всё, подарков больше нет: ты слишком взрослый, тебе уже", age)
else:
    print("а всё, подарков больше нет: ты сам от них отказался, тебе уже", age)


print("===SUM==========================================================================")

# list03 = [12, 32, 45, 5, 5, 3, 6, 78, 58, 3]
# print(12+32+45+5+5+3+6+78+58+3)

a = 7
b = 8

print(a + b)
a = a + b
print(a)


import random

list04 = [random.randrange(100) for x in range(20)]
print(len(list04))
print(list04)

sum = 0
print("sum: ", sum)
for element in list04:
    sum = sum + element
    print("element: ", element)
    print("sum: ", sum)


print("===SUM TILL 100==========================================================================")

# list03 = [12, 32, 45, 5, 5, 3, 6, 78, 58, 3]
# print(12+32+45+5+5+3+6+78+58+3)

a = 7
b = 8

print(a + b)
a = a + b
print(a)

list04 = [random.randrange(100) for x in range(20)]
print(len(list04))
print(list04)

sum = 0
print("sum: ", sum)
idx = 0
while sum < 100:
    sum = sum + list04[idx]
    idx = idx + 1
    print(sum)

sum = 0
print("sum: ", sum)
for element in list04:
    sum = sum + element
    print("element: ", element)
    print("sum: ", sum)
    if sum >= 100:
        break



