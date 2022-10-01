# Связать файловую переменную с файлом, определив модификатор работы
# a – открытие для добавления данных(дозапись)
# r – открытие для чтения данных
# w – открытие для записи данных(перезапись)
# w+, r+

# > Важно! Все данные в файле хранятся в текстовом формате, если нужно использовать цифры, нужно перед этим произвести конвертацию.


# Добавление в файл вариант 1
# colors = ["red", "green", "белый"]
# data = open('file.txt', 'a')  # создаем переменную и связываем ее с текстовым файлом а - дозапись в файл
# data = open('file.txt', 'w')  # создаем переменную и связываем ее с текстовым файлом w - перезапись данных в файле
# data.writelines(colors) # разделителей не будет
# data.write(colors[0])  # Только str
# data.write('\nLENE 2\n')
# data.write('LENE 3\n')
# data.close()  # закрыть файл, разорвать подключение.

# Добавление в файл вариант 2
# with open('file.txt', 'a') as data:
#      data.write('LENE 12\n')
#      data.write('LENE 13\n')  # разрыв связи происходит автоматически

# Чтение файла
# path = 'file.txt'  # путь к папке
# data = open(path, 'r')  # откроем в режиме чтения
# for line in data:
#     print(line, end='')
# data.close()

# exit() -закрывает работу программы если над кодом написать

# вытаскиваем из другого файла данные
# import lec #lec - имя файла
# print(lec.f(1))

#тоже самое сокращенно
# import lec as l #lec - имя файла
# print(l.f(1))

#Функции
# def new_string(symbol, count = 3): #если count не написан, то счетчик в скобках
#  return symbol * count 
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12 умножае на каунт 3

#функция позволяет выводить неограниченное количество аргументов
# def concatenatio(*params):
#   res: str = ""
#   for item in params:
#    res += item
#   return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2

#для работы с цифрами в этой строке использовать тип данных int.работает как сложение всех чисел

# def concatenatio(*params):
#   res: int = 0
#   for item in params:
#     res += item
#   return res
# print(concatenatio(1, 2, 3, 4))

# рекурсия-функция которая вызывает сама себя
#пример с фибаначи
# def fib(n):
#   if n in [1, 2]:
#    return 1
#   else:
#    return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#  list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

#Кортеж-это неизменяемый список
# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')


# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support
# item assignment


# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

#кортеж
# a = (2, 4)
# print(a)
# print(a[0])#показывает [] индекс обязательно надо запятую

#перебираем кортеж циклом for
# a = (3, 4, 5)
# for item in a:
#     print(item)

#словари-Неупорядоченные коллекции произвольных
# объектов с доступом по ключу
# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# типы ключей могут отличаться

# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# down: ↓
# right: →

# Множества
# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}


# Неизменяемое множество
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})