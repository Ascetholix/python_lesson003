# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def Binary(number: int):
  binary = ''
  while number != 0:
    num = number%2
    number//=2
    binary = str(num)+binary
  return int(binary)

enterNamber = int(input('Введите число: '))

print(Binary(enterNamber))