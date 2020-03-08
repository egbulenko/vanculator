import random


spisok_voprosov_i_otvetov = [
    {'вопрос': '5 + 10 = ?',
     'ответ': '15'},
    {'вопрос': '12 + 45 = ?',
     'ответ': '57'},
    {'вопрос': '0 + 0 = ?',
     'ответ': '0'},

    ]


def bvz(otvet):
    print("Введите ответ:")
    perremmeennaayya = input()
    if perremmeennaayya == otvet:
        print("Верно!")
        return True
    else:
        print("НЕ ТАК!!!")
        print("Правильный ответ: ", otvet)
        return False


random.shuffle(spisok_voprosov_i_otvetov)
SKOLKO_VOPROSOV_ZADAVAT = 3
shetchik_nomera_voprosa = 1
shetchic_voprosov = 0
kol_vo_pravilnyh_otvetov = 0
for element in spisok_voprosov_i_otvetov:
    vopros = element['вопрос']
    otvet = element['ответ']
    print("Вопрос", shetchik_nomera_voprosa)
    print(vopros)
    rezultat_proverki = bvz(otvet)
    shetchik_nomera_voprosa = shetchik_nomera_voprosa+1
    if rezultat_proverki == True:
        kol_vo_pravilnyh_otvetov = kol_vo_pravilnyh_otvetov + 1
    shetchic_voprosov = shetchic_voprosov + 1
    if shetchic_voprosov == SKOLKO_VOPROSOV_ZADAVAT:
        break

print("правильных ответов: " + str(kol_vo_pravilnyh_otvetov) + " из " + str(SKOLKO_VOPROSOV_ZADAVAT))
rezultat_proverki = True