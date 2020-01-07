# 2. Задавать определённое количество вопросов (например, 3) и после этого останавливаться

def bvz(vopros, otvet):
    print(vopros)
    print("Введите ответ:")
    perremmeennaayya = input()
    if perremmeennaayya == otvet:
        print("Верно!")
    else:
        print("НЕ ТАК!!!")


вопрос = "5 + 10 = ?"
ответ = '15'
bvz(вопрос, ответ)

vopros = "12 + 45 = ?"
otvet = '57'
bvz(vopros, otvet)

voprosik = "0 + 0 = ?"
otvetik = '0'
bvz(voprosik, otvetik)
