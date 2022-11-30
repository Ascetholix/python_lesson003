# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
#   [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def Fibo(num):
  fib = [0,1,1]              
  fib1 = [0,1,-1]

  for i  in range(num-2):
    fib.append(fib[i+1]+fib[i+2])          
    fib1.append(fib1[i+1]-fib1[i+2])
  for j in range(1, num+1):
    fib.insert(0,fib1[j])
  return fib
  
fiboNum = int(input('Введите число: '))

print(Fibo(fiboNum))
