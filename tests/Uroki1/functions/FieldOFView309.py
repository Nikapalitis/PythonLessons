# Как передать из одной функции в другую - надо правильно структурировать функции

import math

PI = math.pi

def radius():
    n = float(input('Enter Диаметр цилиндра в см: '))
    n /= 2
    return n

def height():
    m = float(input('Enter Высота цилиндра в см: '))
    return m




def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s*h

    return v

print('Объем цилиндра предмета', volume(), 'см3')