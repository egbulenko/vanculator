# # определить функцию print_student
#
# spisok_knik = [
#     { 'название': 'Гарри Поттер и Тайный ТЕЛЕВИЗОР',
#       'автор': 'Joan Rowling'},
#     { 'название': 'Гарри Поттер и вОЙСКА обезЬЯНЫ',
#       'автор': 'Joan Rowling'},
#     { 'название': 'Гарри Поттер и оСКАР',
#       'автор': 'Joan Rowling'},
#     { 'название': 'Гарри Поттер и Орден КаВалера',
#       'автор': 'Joan Rowling'},
#     { 'название': 'Гарри Поттер и Трудности общения с ПИТОНОМ',
#       'автор': 'Joan Rowling'},
#     { 'название': 'Гарри Поттер и Новогодние подарки',
#       'автор': 'Joan Rowling'},
#     { 'название': 'Гарри Поттер и Филосовский парень',
#       'автор': 'Котей'}
# ]
# # print(spisok_knik)
#
#
# def print_book(book, smth):
#     # print("название: " + book['название'] + "\n" + "автор: " + book['автор'] + "\n")
#     print("автор: " + book['автор'] + "\n" + "название: " + book['название'] + "\n")
#
#
# def print_book1(book):
#     print("название: " + book['название'] + "\n")
#
#
#
#
#
# for kniga in spisok_knik:
#     print_book1(kniga)
#
# print_book1[spisok_knik[0]]
# print_book1[spisok_knik[1]]
# kniga = spisok_knik[2]
# kizhechka = spisok_knik[1]
# print_book1(kniga)
# print_book1(kizhechka)
#
# print("====")
# for kniga in spisok_knik:
#     if kniga["автор"] == "Котей":
#         print_book1(kniga)
#
#
#
# import random
#
#
# def calc_sum(my_list):
#     sum = 0
#     for element in my_list:
#         sum = sum + element
#     return sum
#
#
# list04 = [random.randrange(100) for x in range(20)]
# sum = calc_sum(list04)
# print(list04)
# print(sum)


def function(tekst_voprosa, proschalniy_tekst):
    # пишет текст вопроса
    # читает ответ который ввёл пользователь
    # пишет прощальный текст + ответ пользователя
    print(tekst_voprosa)
    bvz = input()
    print(proschalniy_tekst, bvz)

# vopros = "как тебя зовут?"
# pro_text = "пока"
# function(vopros, pro_text)
#
# vopros = "сколько тебе лет?"
# pro_text = "всего"
# function(vopros, pro_text)
#
# function("какой сегодня день?", "уже")

def bolshe_desyati(nmb):
    if nmb > 10:
        print("Bigger!")
        return True
    else:
        print("NOT bigger!")
        return False


if bolshe_desyati(12):
    print("BIG BIG NUMBER")

if not bolshe_desyati(1):
    print("SMALL number")

bb = bolshe_desyati(17)
nn = bolshe_desyati(7)

print(bb)
print(nn)