#Задача 5
w = int(input("Введите число N: "))
n = w + 1
ses = 0.0
for x in range (n):
    z = x * 0.1 + 1
    ses += z
print(ses)