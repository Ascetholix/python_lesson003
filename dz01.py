# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

def SumOdd(list: list):
  sumOdd = 0
  for i in range(len(list)):
    if i%2==1:
      sumOdd += list[i]
  return sumOdd

my_list = list(map(int, input('Введите числа через пробел: ').split()))

print(SumOdd(my_list))

