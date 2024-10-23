fileName = input("Введите имя файла: ")
with open(fileName, 'r') as file:
    lines = file.readline()
    in_num = [f"{i+1}: {line.rstrip()}" for i, line in enumerate(lines)]
    for line in in_num:
        print((line))