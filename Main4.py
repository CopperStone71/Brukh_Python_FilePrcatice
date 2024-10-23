def merge_files(input_files, output_file):
        with open(output_file, 'w') as out_file:
            for file_name in input_files:
                    with open(file_name, 'r') as in_file:
                        out_file.write(in_file.read() + '\n')
        print(f"Все файлы успешно объединены в {output_file}")

input_files = input("Введите имена файлов для объединения, разделенные пробелом: ").split()
output_file = input("Введите имя выходного файла: ")
merge_files(input_files, output_file)