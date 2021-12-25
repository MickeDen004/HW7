# Генераторы списков

# №1
years = [i for i in range(1206, 1227)] # Годы правления Чингисхана
print(years)
print()

# №2
a = [4, -4, 8, -8, 10, 13]
b = [i**2 for i in a]
print(b)
print()

# №3 Пример генератора со словарем
a1 = {1:15, 2:25, 3:35}
b1 = [i*a1[i] for i in a1]
print(b1)
print()

# №4 Прмер генератора словаря 2
a2 = {1:10, 2:20, 3:30}
b2 = [[i,a2[i]] for i in a2]
print(b1)
print()

d = dict(sun='태양', moon='달', universe='우주')
print(d)

e1 = [i for i in range(0, 250) if i%9==0 or i%15==0]
print(e1)

a3 = "rty36g4kx7*(I(Wj2-dcnuh)_ken0987301847rqfdbtdfns3rqofug19037gfujQGOW86DF1238RY8Y49P76wydfyhbdsicfk=e039r86y4379tfgvorsnfvhe4foqwgf87u9"
B3 = [int(i) for i in a3 if '0'<=i<='9']
print(B3)
print()

# №5 Сгенерировать список 1024 измерений случайной температуры (целое число ) в диапазоне от 0 до 255

from random import randint
temperature = [randint(0, 250) for i in range(1024)]
print(temperature)
print()






