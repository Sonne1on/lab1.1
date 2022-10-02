import csv
f = open('Py_Lab1_res.txt', 'w')
with open("books.csv", 'r') as file:
    csvDictReader = csv.DictReader(file, delimiter=";")

    # Делаем счетчик
    i = 1 # подсчитаем кол-во записей
    j = 0 # подсчитаем кол-во строк, где в поле "Название" более 30 символов
    for r in csvDictReader:
          i += 1
          if len(r["Название"]) > 30:
            j += 1
    print(f'В файле {i} строк.')
    print(f'Из них {j} строк, где в поле "Название" более 30 символов.')
f.close()
