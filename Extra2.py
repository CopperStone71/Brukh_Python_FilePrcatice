def print_last_n_lines(file_name, n):
  with open(file_name, 'r') as file:
    lines = file.readlines()
    # Выводим последние n строк
    for i in range(max(0, len(lines) - n), len(lines)):
      print(lines[i].strip())

file_name = input("Введите имя файла: ")
n = int(input("Введите количество строк для вывода: "))
print_last_n_lines(file_name, n)