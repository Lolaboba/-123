#Задача 5
w = int(input("Введите число x: "))
n = w + 1
ses = 1
for i in range (1 , 100000000):
    q = 2 * i - 2
    for x in range(n):
        m = x ** q
        z = 1 / m
        ses += z
    print(ses)

