# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def Composition(list: list):
  compos = []
  lenList = len(list)-1
  if lenList%2==1:
    for i in range(len(list)//2):
      compos.append(list[i]*list[lenList-i])
  else:
    for i in range(len(list)//2+1):
      compos.append(list[i]*list[lenList-i])
  return compos

myList = list(map(int, input('Введите числа через пробел: ').split()))

print(Composition(myList))