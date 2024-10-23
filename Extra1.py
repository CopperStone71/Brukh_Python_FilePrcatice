def print_first_n_lines(file_name, n):
        with open(file_name, 'r') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line.strip())

file_name = input("Введите имя файла: ")
n = int(input("Введите количество строк для вывода: "))
print_first_n_lines(file_name, n)