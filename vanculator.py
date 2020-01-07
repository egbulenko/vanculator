# 2. Задавать определённое количество вопросов (например, 3) и после этого останавливаться

def bvz(vopros, otvet):
    print(vopros)
    print("Введите ответ:")
    perremmeennaayya = input()
    if perremmeennaayya == otvet:
        print("Верно!")
    else:
        print("НЕ ТАК!!!")

spisok_voprosov_i_otvetov = [
    {'вопрос': '5 + 10 = ?',
     'ответ': '15'},
    {'вопрос': '12 + 45 = ?',
     'ответ': '57'},
    {'вопрос': '0 + 0 = ?',
     'ответ': '0'},
    ]

for element in spisok_voprosov_i_otvetov:
    vopros = element['вопрос']
    otvet = element['ответ']
    bvz(vopros, otvet)
