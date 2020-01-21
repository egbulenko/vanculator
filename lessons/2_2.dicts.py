# списки могут хранить похожие данные
my_list = ['apple', 'bread', 'sweets']

# списки могут хранить разные части (атрибуты) чего-то общего, например имя, фамилию, возраст человека
student = ['egor', 'bulenko', '11']

# print("имя: " + student[0] + "\n" + "фамилия: " + student[1] + "\n" + "возраст: " + student[2])

students = [
    ['egor', 'bulenko', '11'],
    ['ivan', 'bulenko', '8'],
    ['alexander', 'kim-kashmenskiy', '11'],
    ['olesya', 'kim-kashmenskaya', '9'],
]
# for student in students:
#     print("имя: " + student[0] + "\n" + "фамилия: " + student[1] + "\n" + "возраст: " + student[2])

# но хранить разные части чего-то общего в списках не очень удобно
students.append(['karmakulov', 'ivan', '10'])
students.append(['karmakulov', 'ilya', '7'])
#
# for student in students:
#     print("имя: " + student[0] + "\n" + "фамилия: " + student[1] + "\n" + "возраст: " + student[2])
#
#
# словари (dictionary) лучше годятся для но хранения частей чего-то общего: проще помнить, где что лежит
student = {
    'name': 'egor',
    'surname': 'bulenko',
    'age': '11'
}
print("имя: " + student['name'] + "\n" + "фамилия: " + student['surname'] + "\n" + "возраст: " + student['age'])
#
students = [
    {'name': 'egor', 'surname': 'bulenko', 'age': '11'},
    {'name': 'ivan', 'surname': 'bulenko', 'age': '8'},
    {'name': 'alexander', 'surname': 'kim-kashmenskiy', 'age': '11'},
    {'name': 'olesya', 'surname': 'kim-kashmenskaya', 'age': '9'},
]
#
# for student in students:
#     print("имя: " + student['name'] + "\n" + "фамилия: " + student['surname'] + "\n" + "возраст: " + student['age'])
#
students.append({'name': 'ivan', 'surname': 'karmakulov', 'age': '10'})
students.append({'name': 'ilya', 'surname': 'karmakulov', 'age': '7'})
#
for student in students:
    print("имя: " + student['name'] + "\n" + "фамилия: " + student['surname'] + "\n" + "возраст: " + student['age'])



book = {"name": "Гарри Поттер", "autor": "Joan Rowling"}
print("имя: " + book["name"] + "\n" + "автор: " + book["autor"] + "\n")

kniga = {
    'название': 'Гарри Поттер и Филосовский камень',
    'автор': 'Joan Rowling',
}
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
# for kniga in spisok_knik:
#     print("название: " + kniga['название'] + "\n" + "автор: " + kniga['автор'] + "\n")

for kniga in spisok_knik:
    if kniga["автор"] == "Котей":
        print("название: " + kniga['название'] + "\n" + "автор: " + kniga['автор'] + "\n")