def bvz(vhodnoe_znathchenie):
    a = vhodnoe_znathchenie*vhodnoe_znathchenie
    print("квадрат числа ", vhodnoe_znathchenie, " равен ", a)
    return a

bvz(17)

bvt = bvz(2)
print(bvt)
bvt = bvz(3)
print(bvt)
bvt = bvz(5)
print(bvt)


def summa(spisoghisel):
    znacheniye = 0
    for chislooooo in spisoghisel:
        znacheniye = znacheniye+chislooooo
    print("сумма чисел из списка ", spisoghisel, " равна ", znacheniye)
    return znacheniye

sp = [1, 2, 7]
result = summa(sp)
print(result)
result = summa([0, 0, 8])
print(result)
result = summa([1, 10, 12, 7, 2])
print(result)


def udvoit_chisla(spisoghisel):
    spisok = []
    for podarochek in spisoghisel:
        spisok.append(podarochek*2)
    print("исходный список(:", spisoghisel, " получился список: ", spisok)
    return spisok



spisok = []
result = udvoit_chisla(sp)
print(result)
result = udvoit_chisla([0, 0, 8])
print(result)
result = udvoit_chisla([1, 10, 12, 7, 2])
print(result)


def cvadratt(spisoghisel):
    spisok = []
    for podsarochek in spisoghisel:
            spisok.append(bvz(podsarochek))
    print("исходный список(:", spisoghisel, " получился список: ", spisok)
    return spisok

result = cvadratt(sp)
print(result)
result = cvadratt([0, 0, 8])
print(result)
result = cvadratt([1, 10, 12, 7, 2])
print(result)


def srednyaya(spisoghisel):
    per = summa(spisoghisel)/len(spisoghisel)
    print("среднее чисел из списка ", spisoghisel, " равна ", per)
    return per
# len(list1)


sp = [3, 2, 7]
result = srednyaya(sp)
print(result)
sp = [0, 0, 9]
result = srednyaya(sp)
print(result)
sp = [1, 10, 12, 7, 2]
result = srednyaya(sp)
print(result)


def prinyatiye(spisoghisel):
    if len(spisoghisel)>4:
        return srednyaya(spisoghisel)
    else:
        return summa(spisoghisel)

print("#################################################################")
sp = [1, 2, 7]
result = prinyatiye(sp)
print(result)
sp = [0, 0, 8, 0]
result = prinyatiye(sp)
print(result)
sp = [0, 0, 10, 0, 0]
result = prinyatiye(sp)
print(result)
sp = [1, 10, 12, 7, 2]
result = prinyatiye(sp)
print(result)