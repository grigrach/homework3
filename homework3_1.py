import os

def merge_files(source_files):
    # Получаем список файлов в папке

    # Создаем словарь, где ключ - количество строк в файле, значение - список файлов с таким количеством строк
    file_counts = {}
    for file_name in source_files:
        print(file_name)
        with open(file_name, 'r',encoding='utf-8') as file:
            lines = file.readlines()
            file_counts.setdefault(len(lines), []).append(file_name)

    # Сортируем файлы по количеству строк и записываем их в результирующий файл
    with open('merged_file.txt', 'w', encoding='utf-8') as merged_file:
        for num_lines, file_names in sorted(file_counts.items()):
            for file_name in file_names:
                with open(file_name, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                merged_file.write(f"\n{file_name}\n{num_lines}\n")
                merged_file.writelines(lines)

# Вызов функции с указанием директории, в которой находятся файлы
source_files = ['1.txt','2.txt','3.txt']
merge_files(source_files)