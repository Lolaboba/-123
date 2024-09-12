# Задача № 2
x = int(input("Введите 1 сторону треугольника: "))
n = int(input("Введите 2 сторону треагольника: "))
m = int(input("Введите 3 сторону треугольника: "))


if x > n + m:
   print ("NO")
elif  x + m < n:
   print ("NO")
elif m > n + x:
   print ("NO")
else:
   print ("YES")





