import random
import time

num = random.randint(1, 100)
a = 1
print (num)
while True:
    answer = int(input('Какое число я загадал? '))

    if answer < num:
        print('Моё число больше!')
    elif answer > num:
        print('Моё число меньше!')
    else:
        print('Ураган! Ты угадал!')
        break

    if a == 10:
        print('Попытки кончились.')
        break
    a += 1