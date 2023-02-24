perimetr = input("Введите ширину и высоту через пробел\n")
list_of_strings = perimetr.split()
s = list(map(int, list_of_strings))
st_mat = s[0]*s[1]*2926
dl_freza = (s[0]*2+s[1]*2)*56

neon = int(input("long neon \n"))
kol = int(input("kolichestvo neon \n"))
neon = neon*912 + kol*22+neon*202+kol*155
print("Стоимость материала",st_mat)
print("Стоимость фрезеровки",dl_freza)
print("Стоимость неона",neon)
def sum(a,b):
     procent=a*b/100
     return procent
sebest = st_mat+dl_freza+neon
itog50 = sum(sebest,50)
itog43 = sum(sebest,43)
itog = sebest + itog50 +itog43
print("Себестоимоссть",sebest)
print("Конечная стоимость изделия",itog)