def split_file(input_file, lines_per_file):
        with open(input_file, 'r') as file:
            lines = file.readlines()
            total_lines = len(lines)
            file_count = 0

            for i in range(0, total_lines, lines_per_file):
                file_count += 1
                output_file = f"{input_file}_part{file_count}.txt"

                with open(output_file, 'w') as out_file:
                    out_file.writelines(lines[i:i + lines_per_file])

                print(f"Создан файл: {output_file}")

input_file = input("Введите имя файла: ")
lines_per_file = int(input("Введите количество строк: "))
split_file(input_file, lines_per_file)