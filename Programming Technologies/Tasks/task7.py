""""
Программа запрашивает у пользователя возраст, логин, пароль и выводит сообщение
Если 18 лет и больше и логин и пароль правильный
Если меньше 18 или логин и пароль не правильный
Если admin admin вернет роль администратор
Если user 12345 вернется роль пользователь
Если ошибка в данных доступ запрещен
"""
#константы
ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "admin"
USER_LOGIN = "user"
USER_PASSWORD = "12345"

try:
    age = int(input("Введите ваш возраст: "))
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    
    if age >= 18:
        if login == ADMIN_LOGIN and password == ADMIN_PASSWORD:
            print("Доступ разрешен \nВаша роль: Администратор")
        elif login == USER_LOGIN and password == USER_PASSWORD:
            print("Доступ разрешен \nВаша роль: Пользователь")
        else:
            print("Доступ запрещен")
    else:
        print("Доступ запрещен")
        
except ValueError:
    print("Ошибка ввода. Возраст должен быть целым числом")