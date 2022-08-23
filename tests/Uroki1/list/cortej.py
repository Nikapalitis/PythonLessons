# x = (9, 8, 7, 6) - cortaje это не измиеняеммый тип данных
# print(type(x))
# ----------

# # Cortaje text
# x = tuple('string text')
# print(x)

# Cortaje elements
# print (x.count(9))
# .count сколько одинаковых елементов есть в кортедже
# print(x.index(9)) выводит индекс елемента
# .index
x = (9, 8, 7, 6, 5, 4, 3)
y = []



for i in range(len(x)):
    y.append(x[i] + 3)

print(x)

t = list(x)
t[0] = 10
x = tuple(t)

print(x)

r = 5
u = 7

r, u = (u, r)

print(x[1:5])
print(y)