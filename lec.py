# int-целое,float-дробное, boollean-логические, str-строки,list, None

#Value = None
#print (type(Value))
#a = 123
#b = 1.23
#print (type(a)) #tupe -показывает тип переменной
#print (type(b))
#Value =12334
#print (type(Value))
#s = 'hello world' #s-это string строка
#print(s) #вывод строки
#s = 'hello \nworld' #\n-с новой строки
#print(a,'-',b, s) #то что в одинарных ковычках выводит
#print('{} - {} - {}'.format(a, b, s))
#print(f'{a} - {b} - {s}') #интрополяция

#f = True
#f = False
# print(f)

#list = ['1', '2', '3', 'hello'] #вывод массива
#print(list)


#print('Введите a')
#a = input() # выводит строки
#print('Введите b')
#b = input()
#print(a, b)
#print('{} {}'.format(a, b)) вариант вывода печати
#print(f'{a} {b}') вариант вывода печати

#print('Введите a')
#a = int(input()) # выводит целые числа  int
#print('Введите b')
#b = int(input())
#print(a,' + ', b, ' = ', a+b)

#print('Введите a')
#a = float(input()) # выводитвещественные числа(через запятую) float
#print('Введите b')
#b = float(input())
#print(a,' + ', b, ' = ', a+b)

#арифметические операции +, -,*, /-вещественные, %-остаток от деления //-целые,**
#Приоритет операций
#**-возведение в степень, ⊕, ⊖,*, /, //, %, +, -
#( ) Скобки меняют приоритет
#a = 1.368
#b = 3
#c = round(a * b, 3)#round округляет числа после запятой, 3 указывает сколько знаков показать)
#print(c)

#a = 3
#a +=5
#print(a)

#логические операции
#>=, <, <=, ==, !=
#not, and, or – не путать с &, |,^
#Кое-что ещё: is, is not, in, not in

#a = 1 > 4 # на вывод выходит правда или ложь
#print (a)

#a = 1 > 4 and 5 > 2# на вывод выходит правда или ложь
#print (a)

#a = 1 == 4 # операция сравнения
#print (a)

#a = 1 != 4 # операция неравенства
#print (a)

#a = 'lena' # сравнение списков на вывод выходит правда или ложь
#b = 'lenaj'
#print (a == b)

#a = [1,2] # сравнение массива на вывод выходит правда или ложь
#b = [1,2]
#print (a == b)

#a = 1 < 3 < 4 # тройные сравнения правда или ложь
#print (a)

#f = 1 > 2 or 4 < 6 # or это или, вывод истина или ложь
#print(f)

#a = 1 == 4 # операция сравнения
#print (a)

#f = [1,2,3,4]
#print(f)
#print(not 2 in f)#проверяем not=нет 2 в массиве,если есть сразу 2

#is_odd = f[0] % 2 == 0 #0 это первая цифра в массиве, т.е 1,остаток от деления равен 0
#в пайтон 0=ложь, 1= это истина
#is_odd  = not f[0] % 2
#print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

# original = 23 #название переменной
# inverted = 0 #инвертированное число
# while original != 0:
#  inverted = inverted * 10 + (original % 10) #это переворачивает число
#  original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# else:
#  print('Пожалуй')
#  print('хватит )')
# print(inverted)

# for i in 1,2,3,4,5:
#     print(i**2)#возводит в квадрат

# list = [1,2,3,10,5]
# for i in list:
#     print(i)

# r = range(10)#выводит все числа до 10
# for i in r:
#     print(i)

#или
# for i in range(10):
#      print(i)

# for i in range(1, 10, 3):#последняя цифра,уменьшает список цифр на то число что указано
#       print(i)

# for i in 'hello - world':
#     print(i)

# r = range(5) # range(0, 5)
# r = range(2, 5) # range(2, 5)
# r = range(-5, 0) # range(-5, 0)
# r = range(1, 10, 2) # range(1, 10, 2)
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)

# line = "  "
# for i in range(2):#строки
#     line = " "
#     for j in range(4):#столбцы
#         line += "лол"#выводит значение на печать
#     print(line)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) #39 количество символов в строке
# print('ещё' in text) #проверяем есть ли слово еще в строке,ответ правда или ложь
# print(text.isdigit()) #проверям являются ли символы в строке числами
# print(text.islower()) #проверям являются ли символы нижним регистором
# print(text.replace('ещё','ЕЩЁ')) #меняем нижний регистр на верхний
# for c in text:
#  print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) #текст как массив 0=буква с и т.д
# print(text[len(text)-1]) #это последняя буква в строке,считаем сзади
# print(text[-5]) #5 буква с конца текста
# print(text[:]) #выводит на печать от 0 символа до последнего
# print(text[:2]) #выводит на печать от 0 символа до второго
# print(text[len(text)-2:]) #выводит на печть последние 2 символа
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# numbers = [1, 2, 3, 4, 5]#список
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))#приведение типо list к типу range
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# numbers = [1, 2, 3, 4, 5]#список
# print(numbers) # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran)) 
# numbers = list(ran)
# print(type(numbers))#type показывает какое значение,тут сменили лист на рандж

# numbers = [1, 2, 3, 4, 5]#список
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))#приведение типо list к типу range
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len') #выводит на печать какая последняя цифра в списке/массиве
# print(numbers)
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# #colors.remove('red') #del colors[0] # удалить элемент

#функции
#def function_name(x):

# def f(x): #def-функция
#  if x == 1:
#   return 'Целое'
#  elif x == 2:
#   return 23
#  else:
#   return
# arg = 2
# print(f(arg))
# print(type(f(arg)))

