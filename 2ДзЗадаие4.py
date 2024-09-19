# Задача 4
q = int(input("Введите число K: "))
w = int(input("Введите число N: "))
ses = w + 1
b1 = 0
for x in range (q , ses):
   if x % 2 == 0:
    b1 += x
print(b1)

