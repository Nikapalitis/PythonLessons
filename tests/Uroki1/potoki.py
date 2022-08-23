x = 5.5

if x == 0:
    x = 1
    print('x был равен нулю и переписан на 1')

elif type(x) == type(5) or type(x) == type(5.5):
     print('x допутсимое значение')

else:
    print('B x не допустимый тип данных')
    x = 1



print(100/x)