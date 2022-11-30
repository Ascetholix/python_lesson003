# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
# ['sdf13', 'fds66', '34']
# -> 3
# 'sdf13', '34'

def func(a: str, list: list):
  for i in range(len(list)):
    if a in list[i]:
      print(list[i])

enterList = ['sdf13', 'fds66', '34']

n = '3'

func(n, enterList)