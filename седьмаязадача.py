# Задача № 7
x1 = int(input("Первая клетка координата x: "))
y1 = int(input("Первая клетка координата y: "))
x2 = int(input("Вторая клетка координата x: "))
y2 = int(input("Вторая клетка координата y: "))

d = y1 - y2
n = x1 - x2
m1 = y2 - y1
n1 = x1 - x2
m3 = y1 - y2
n3 = x2 - x1
m4 = y2 - y1
k4 = x2 - x1
if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
   if x1 > x2 and y1 > y2:
     if n  and d :
        if n == 2 and d == 1:
           print("Yes")
        elif n == 1 and d == 2:
           print("Yes")
        else:
           print("No")

   elif x1 > x2 and y1 < y2:
      if n1  and m1 :
         if n1 == 2 and m1 == 1:
            print("Yes")
         elif n1 == 1 and m1 == 2:
            print("Yes")
         else:
            print("No")

   elif x1 < x2 and y1 > y2:
      if n3 and m3:
         if n3 == 2 and m3 == 1:
            print("Yes")
         elif n3 == 1 and m3 == 2:
            print("Yes")
         else:
            print("No")

   else:
      if k4 and m4 :
         if k4 == 2 and m4 == 1:
            print("Yes")
         elif k4 == 1 and m4 == 2:
            print("Yes")
         else:
            print("No")

else:
   print("Ошибка")