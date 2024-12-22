#1
a = list(range(1,1001))
for i in a:
    print(i)
#2
[print(i) for i  in range(3,31) if i % 3 == 0 ]
#Другой вариант
numbs = list(range(3,31,3))
for num in numbs:
    print(num)
#3
[print(i**3) for i in range(1,11)]
#Другой вариант
a = list(range(1,11))
for i in a:
    print(i**3)
#4
namesforobed = ['Сергей', 'Максим', 'Евгений']
for name in namesforobed:
    print(f'Приглашаю тебя на обед, {name}')
#5
age = int(input("Введите возраст: ")) #Или age = 13(Любое число)
print('Младенец' if age <2 else "Малыш" if 2<= age < 4 else 'Подросток' if 4 <= age < 13 else 'Подросток' if 13<= age < 20 else 'Взрослый' if 20<= age < 65 else 'Пожилой ' ) #Через тернарный оператор
##Можно тупо через обычной if-elif-else

#6
users = ['admin', 'abobus', 'biba', 'vadim', 'ssx']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
#7
numb = list(range(1,10))
for num in numb:
    if num == 1:
        suff = "st"
    if num == 2:
        suff = "nd"
    if num == 3:
        suff = "rd"
    else:
        suff = "th"
        print(f"{num}{suff}")
#8
info = {
    'first_name' : "SerGey"
    ,'last_name' : "Fed"
    ,'age' :18
    ,'city' : "Tuymen"
}
print(f"First Name: {info['first_name']}")
print(f"Last Name: {info['last_name']}")
print(f"Age: {info['age']}")
print(f"City: {info['city']}")
#9
favorite_num = {
    "SerGey":18,
    "Vadim":27,
    "Sx":34,
    "erx":43,
}
for name, num in favorite_num.items():
    print(f"Favorite number {name}: {num}")
#10
number_of_guests = int(input("Сколько мест вы хотите забронировать в ресторане? "))
a = "Вам придется подождать." if number_of_guests > 8 else "Ваш стол готов!"
print(a)
#11
# while True:
#     age = int(input("Введите возраст: "))
#     if age < 3:
#         print("Билет бесплатный")
#     if 3 <= age <= 12:
#         print("10$")
#     if age > 12:
#         print("15$")
#12
def pizza_dobavki():
    while True:
        dobavka = input("Введите дополнение для пиццы или quit(для выхода)")
        if dobavka == "quit":
            break
        yield dobavka
for dobavvk in pizza_dobavki():
    print(f"Дополнение '{dobavvk}' включено в заказ ")
#13
opros = []
while True:
    useropros = input("Где бы вы хотели провести отпуск? или quit(для выхода)")
    if useropros == "quit":
        break
    opros.append(useropros)
print('Результаты опроса:')

for i, opr in enumerate(opros, start=1):
    print(f"От {i} пользователя: {opr}")
#14
def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Бебрусс")
#15
print(f"Сложение - {70+2}, Вычитание -  {74-2}, Умножение - {36*2}, Деление -  {int(144/2)}")
#16
a,b,c,d = 100,12,2,3
print((a+b)/c**d)
#17
names = ['name1', 'name2', 'name3']
for name in names:
    print(name)
#18
moto = ['Kawasaki', 'Suzuki', 'Ducati', 'Honda']
for motiki in moto:
    print(f"Я хотел бы купить мотоцикл {motiki}")
#19
names = ['name1', 'name2', 'name3']
citata  = 'Счастье — это довольство собою'
for name in names:
    print(f'{name.lower()} сказал: "{citata}" ')
    print(f'{name.upper()} сказал: "{citata}" ')
    print(f'{name.capitalize()} сказал: "{citata}" ')
    print("---")
#20
messages  = ['Первое слово', 'Второе слово', 'Третье слово', 'Дальше заебался']
def show_messages(messages):
    for message in messages:
        print(message)

show_messages(messages)
#21
def city_country(city, country):
    print(f"{city}, {country}")
city_country("Казань", "Россия")
city_country("Сантиаго", "Чили")
city_country("Астана", "Казахстан")
#22
color = input("Введите цвет:")
if color == "green":
    print(color)
#23
favorite_fruits =['apple', 'pineapple', 'strawberry']
if 'strawberry' in favorite_fruits:
    print(f"{favorite_fruits[2].capitalize()} - есть в списке") # можно просто f"strawbery - есть в списке"
if 'apple' in favorite_fruits:
    print(f"{favorite_fruits[0].capitalize()} - есть в списке") # тут также
if 'pineapple' in favorite_fruits:
    print(f"{favorite_fruits[1].capitalize()} - есть в списке") # и тут
if 'kiwi' in favorite_fruits:
    print("Kiwi - есть в списке")
if 'dragon fruit' in favorite_fruits:
    print("Dragon Fruit - есть в списке ")
#24
a,b,c = 5,3,4
V = a*b*c
Sp = 2*(a*b+b*c+a*c)
print(f"Обьем - {V},а площадь поверхности  - {Sp}")
#25
a,b = 10,20
print(f"Среднее арифмет  - {(a+b)/2}")
#26
x  = int(input("Введите x: "))
y = 3*x*6-6*x*2-7
print(y)
#27
x  = int(input("Введите x: "))
y = 4 * (x-3) * 6 - 7 *(x-3) * 2 + 2
print(y)
#28 - Одно и тоже 24 задание
#29
num1,num2 = int(input("Первое число: ")), int(input("Второе число: "))
print(f"Сумма - {num1+ num2}, Разность - {num1-num2}, Произведение  - {num1*num2}, Частное - {num1%num2}")
#30
[print(i) for i in range(1,101) if i % 5 == 0]
#31
massiv = [2,5,10]
print(sum(massiv))

# #32
import math as m
N = 5
print(f"Факториал числа N - {m.factorial(N)}")
#33
sigma = [583,910, 14, 'sigma', 101, 'mt']
print(sigma[:4] , sigma[1:-1] , sigma[-2:] )
# #34
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
if A < B:
    nmb_between = list(filter(lambda x: A < x < B, range(A + 1, B)))
    print("Числа между A и B:", nmb_between)
    N = len(nmb_between)
    print("Количество чисел N:", N)
#35
a,b = int(input("Первое число:")),int(input("Второе число:"))
if a > b:
    print(a+b)
else:
    print(a*b)