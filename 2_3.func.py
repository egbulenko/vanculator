# определить функцию print_student

spisok_knik = [
    { 'название': 'Гарри Поттер и Тайный ТЕЛЕВИЗОР',
      'автор': 'Joan Rowling'},
    { 'название': 'Гарри Поттер и вОЙСКА обезЬЯНЫ',
      'автор': 'Joan Rowling'},
    { 'название': 'Гарри Поттер и оСКАР',
      'автор': 'Joan Rowling'},
    { 'название': 'Гарри Поттер и Орден КаВалера',
      'автор': 'Joan Rowling'},
    { 'название': 'Гарри Поттер и Трудности общения с ПИТОНОМ',
      'автор': 'Joan Rowling'},
    { 'название': 'Гарри Поттер и Новогодние подарки',
      'автор': 'Joan Rowling'},
    { 'название': 'Гарри Поттер и Филосовский парень',
      'автор': 'Котей'}
]
# print(spisok_knik)


def print_book(book):
    # print("название: " + book['название'] + "\n" + "автор: " + book['автор'] + "\n")
    print("автор: " + book['автор'] + "\n" + "название: " + book['название'] + "\n")


def print_book1(book):
    print("название: " + book['название'] + "\n")





for kniga in spisok_knik:
    print_book1(kniga)

print("====")
for kniga in spisok_knik:
    if kniga["автор"] == "Котей":
        print_book1(kniga)



import random


def calc_sum(my_list):
    sum = 0
    for element in my_list:
        sum = sum + element
    return sum


list04 = [random.randrange(100) for x in range(20)]
sum = calc_sum(list04)
print(list04)
print(sum) 
