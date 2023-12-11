import os

dic_file = {}

directory = r'C:\Users\Polina_Malina\Desktop\Открытие и чтение файла, запись в файл\3'

for file_name in os.listdir(directory):
    f = os.path.join(directory, file_name)
    with open(f, 'r', encoding='utf-8') as file:
        count = sum(1 for line in file if line.rstrip('\n'))
    with open(f, 'r', encoding='utf-8') as file:
        list = file.read()
        dic_file[file_name] = count, list

dic_file_sort = sorted(dic_file.items(), key=lambda x: x[1])

for file_list in dic_file_sort:
    with open('united.txt', 'a', encoding='utf-8') as file:
        file.write(str(file_list[0]))
        file.write('\n')
        for i in file_list[1]:
            file.write(str(i))
            file.write('\n')