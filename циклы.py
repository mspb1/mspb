# login_list = [ # Список
#    'root',
#    'username1'
#    ]
# password_list = { # Словарь
#    'root': '1q2w3e4r',
#    'username1': 'qwerty123'
# }
# username = input('Введите логин:\n')
# if not username:
#        print("Вы забыли ввести логин")
# else:
#     if username in login_list:
#        print("Угадал падонок",login_list[1])
#        password = input('Введите пароль:\n')
#        if password_list[username] == password:
#            print('Вы успешно вошли в систему')
#        else:
#             print('Отказано в доступе')
#     else:
#          print('Такого пользователя не существует')
""" Проверка вхождения числа символа """
a = 712332157
# if '5' in str(a):
#     print("5 есть в числе")
# else:
#     print("Облом с 5")
""" Проверка уникальности списка """
spisok = ['a', 'b', 'c', 'd','b']
print(len(spisok))
print(len(set(spisok)))#set Проверить, все ли элементы в списке уникальны
print("все уникальны в списке =",len(spisok) == len(set(spisok)))

for i in range(10):
    print(i)


