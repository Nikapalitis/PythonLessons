#Параметры

# def count_list(par, count = 0) # параметр по умолчанию (изначально уже есть значение)

# parametr которым можно добавить argument для дальнейшей работы
# -----------------
# def count_list(par):
#     count = 0
#     for i in par:
#         count += 1
#     return count
# _________________

def count_list(par, par2 = False, count = 0):
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count

a = True

j = [9, 8, 7, 6, 5, 4,]

print(count_list(j, a)) #argument в котором можно использовать параметр из функции

h = ['a', 'b', 'c', 'g']

print(count_list(h))


k = [9, 8, 7]

print(count_list(k))

