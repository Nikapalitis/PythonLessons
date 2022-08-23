print('Before Function ')

def show():
    print('Function')

def show2():
    x = 7
    return x
    # return - что бы использовать значение из функций. return возвращает значение в точку запуска функции

y = show2()
print(y)

z = show2() + 9

print(z)

show()
print('AFTer Function')
