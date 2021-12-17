list_file = ['1.txt', '2.txt', '3.txt']  # список файлов в каталоге
dict_file_data = {}  # словарь {файл: содержание}
dict_file_count = {}  # словарь {файл: количество строк}


def get_count(file_name):
    count = 0

    with open(file_name) as file:
        for line in file:
            count += 1
    return count


def get_data(file_name):
    list_file_data = []

    with open(file_name) as file:
        for line in file:
            list_file_data.append(line.strip())
    return list_file_data


for i in list_file:
    dict_file_data[i] = get_data(i)


for i in list_file:
    dict_file_count[i] = get_count(i)


sorted_dict_count = {}
sorted_keys = sorted(dict_file_count, key=dict_file_count.get)

for w in sorted_keys:
    sorted_dict_count[w] = dict_file_count[w]

with open('result.txt', 'a') as document:
    for key, values in sorted_dict_count.items():
        document.write(f'{key}\n{values}\n')
        for value in dict_file_data[key]:
            document.write(f'{value}\n')

print('Приложение успешно отработало, итоговое решение смотрите в файле "result.txt"')