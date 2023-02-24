""" объявили функцию для подсчёта количества символов в тексте"""
# def char_frequency(text):
#     text = """
#     У лукоморья дуб зелёный;
#     Златая цепь на дубе том:
#     """
#    text = input("Введите ваш текст \n")
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#    count = {}  # для подсчёта символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")
## # вызвали функцию в любом месте программы
# char_frequency("dsdf")

""" функция, которая возводит любое число в степень n один аргумент по умолчанию"""
# def pow_func(base, n=2):
#    print(base ** n)
#    return base # Возврат из функции
# print(pow_func(5, 3))

""" функцию, которая проверяет, является ли число n делителем числа a"""
# def pow_func(a,n):
#  if a % n == 0:
#    print(f"Число {n} делитель ")
#  else:
#   print(f" {n} не является делителем")
# pow_func(301, 3)

"""возвращать количество делителей числа а"""
# def get_multipliers(a):
#    count = 1
#    for n in range(1, a // 2 + 1):
#        if a % n == 0:
#            count += 1
#    return count
# delitel = get_multipliers(100)
# print(delitel)
#функцию, которая печатает обратную лесенку
# def lesenka (strok):
#     for i in range(strok,0,-1):  #range(START, END, STEP).
#         print("*"*i)
# lesenka(5)
"""Проверка строк на палиндро"""
# def palindrome(text): #является ли эта строка палиндромом
#     text = input("введите слово или текст")
#     text = text.lower()
#     text = text.replace(" ","")
#     if text == text[::-1]:
#          print("Палиндром")
#          result = True
#     else:
#          print("No palindrom")
# palindrome("qwertyytrewq1")
"""рекурсивный вызов"""
# def factorial(fact):
#     if fact == 0:
#         return 1
#     print(fact)
#     return factorial(fact-1) * fact # рекурсивный вызов выведет факториал числа
# print(factorial(5)) # Выведет число 55

"""Передача в функцию множественного значения 1.2 2. 3."""
# def proizv(*nums):
#     sum_ = 1
#     for n in nums:
#         sum_ *= n
#     return sum_
# def proizv(*all_num):
#     nums = 1
#     # all_num = all_num.replace(" ", "")
#     # all_num = all_num.replace(", ", "")
#     # all_num = all_num.replace("\n", "")
#     List_num = list(map(int, all_num))
#     print(List_num)
#     for n in List_num:
#         nums *=n
#     return nums
# print("произведение чисел = ", proizv(2, 2, 2))

"""Вфвод чисел Фибаначе"""
# def rec_fibb(n):
#    if n == 1:
#        return 1
#    if n == 2:
#       return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
# print(rec_fibb(10)) # 55
"""перевернуть текст функцией рекурсивной"""
def revers(text):
    if len(text) == 0:
         print("Пустое выражение")
         return text
    else:
        return text[-1] + revers(text[:-1])
print(revers("абырвылг"))
# """Дано натуральное число N. Вычислите сумму его цифр"""
# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        print("", n)
#        return n % 10 + sum_digit(n // 10)
# print(sum_digit(211))

"""генератор Фебаначи"""
# def gen_febanache():
#     a, b = 0, 1
#     yield a
#     yield b
#     while True:
#         a, b =b, b+a
#         yield b
# for num in gen_febanache():
#    print("  ",num)
"""
import time
N = 100
def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       print(f"Функция выполнилась. Время: {dt:.10f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper
def pow_2():
   return 10000000 ** 2
def in_build_pow():
   return pow(10000000, 2)
pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)
pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921
in_build_pow()
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458
"""
""" Пример подсчёта выполнения 
def counter(func):
   count = 0
   def wrapper(*args, **kwargs):
       nonlocal count
       func(*args, **kwargs)
       count += 1
       print(f"Функция {func} была вызвана {count} раз")
   return wrapper
@counter
def say_word(word):
   print(word)
say_word("Oo!!!")
say_word("Oo!!!"
"""
"""работа с кешем"""
# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кеш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кеша: {cache_dict[num]}")
#        print(f"кеш {cache_dict}")
#        return cache_dict[num]
#    return wrapper
# @cache
# def f(n):
#    return n * 123456789
# print(f(12))

def Desk(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        print("Нет корней ")
        return D
    else:
        if D == 0:
           x1 = -b/(2*a)
           print("D=0 ")
           return x1
        else:
            x1 = (-b-D**0.5)/(2*a)
            x2 = (-b + D**0.5/(2*a))
            print(x1, x2)
        return x1
print(Desk(1, 1, 1))

def D(a, b, c):
    return  b**2 - 4*a*c
def d_otr(D):
     if D(a, b, c) < 0:
         return "Нет корней "
     elif D(a, b, c) == 0:
         x1 = -b/(2*a)
         return print(f"корень один x1={x1}")
     else:
         x1 = (-b - D ** 0.5) / (2 * a)
         x2 = (-b + D ** 0.5 / (2 * a))
         return print(f"корнb x1={x1}, x2={x2}")
D(2, 4, 10)