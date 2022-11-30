# 1. Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора псевдослучайных чисел.
import time

def my_random(ranMin: int, ranMax: int):
    a = (time.time())*100000

    temp = (round(a) % ranMax)+ranMin
    return temp

mini = int(input('Введите от: '))
maxi = int(input('Введите до: '))

print(my_random(mini,maxi))
