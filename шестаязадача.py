#задача 4

x = int(input("Введите время в часах: "))



if 5 <= x <= 11:
   print ("Утро")
elif 12 <= x <= 17:
   print ("День")
elif 18 <= x <= 22:
   print ("Вечер")
elif 0 <= x <= 23:
   print ("Ночь")
else:
   print("Ошибка")



