# first_name = input("Введите ваше имя:")
#last_name = input("Введите вашу фамилию:")
#age = input("Введите ваш возраст:")
#city = input("Введите город проживания:")

# Выводим приветствие, подставляя имя и фамилию пользователя,
# которые он ввел с клавиатуры
#print("Привет,", first_name, last_name, "!")

# Выводим фиксированный текст для удобства просмотра
#print("Ваш профиль:")
# Выводим возраст и город, которые указал пользователь
#print("Возраст:", age, "лет")
#print("Город:", city)

# biblio = {'book':'-', 'avtor':'-', 'year':'-'}
# (biblio['book']) =input("Введите название книги:")
# (biblio['avtor']) =input("Введите автора:")
# (biblio['year']) =input("Введите год написания:")
# print(biblio)

L = input("Введите числа через пробел:")
list_of_strings = L.split() # список строковых представлений чисел split Результат работы этого метода — список строк
List_num = list(map(int, list_of_strings)) # cписок чисел LIST Любой непустой список
List_num[0], List_num[-1] = List_num[-1], List_num[0] # Смена  крайних позиций в списке
List_num.append(sum(List_num)) # Добавление ceevs s список
print((List_num[:]))
print((List_num[::-1])) # вывод задом наперёд