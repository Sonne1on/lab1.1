import csv
import random

with open('books.csv') as r_file:
    tab_r = list(csv.reader(r_file, delimiter=';'))

with open('bib_links.txt' ,'w') as faile_bl:
    for N in range(1 ,21):   # Задаем кол-во 20 строк
        row = random.randint(1, len(tab_r))   # Произвольный выбор
        autor = tab_r[row][4]
        books = tab_r[row][1]
        date = tab_r[row][6][6:10]
        bl = f'{N}. {autor}.   {books}  :  {date}'
        faile_bl.write(bl + '\n')
print()
print('Результат можно увидеть в файле bib_links.txt')