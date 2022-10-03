import csv

f = open('Py_Lab1_res3.txt', 'w')
with open("books.csv", 'r') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=";")
    print('Введите ФИО искомого Автора')
    autor = input() #Вводим ФИО автора с клавиатуры
    print("  ID", "    Автор (ФИО)", "  Название", "               ", "  Жанр книги")
    for t in file_reader: #Проверяем таблицу на совпадения с запросом
          if autor==t["Автор (ФИО)"]:
            #print("  ID", "   Автор (ФИО)", "   Название", "                ", "  Жанр книги")
            print(t["ID"],  t["Автор (ФИО)"], t["Название"], "  ", t["Жанр книги"])
f.close()
