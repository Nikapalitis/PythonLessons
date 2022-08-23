import os
import time
('C://Users/Nikoloz Tsekvava/Desktop/for exmpl/', ['folder 1', 'folder 2'], ['file 1.txt', 'file 2.txt', 'Screenshot_1.png'])

spisok = []


for adress, dirs, files in os.walk('C://Users/Nikoloz Tsekvava/Desktop/for exmpl/'):
    for file in files:
        # .path.join автоматически добовляет слешы / для файлов
        full = os.path.join(adress, file)
        # if '.txt' in full: - сортировка по названию или типу файла , папки итд
        if time.time() - os.path.getctime(full) < 386400:
            spisok.append(full)



print(spisok)
