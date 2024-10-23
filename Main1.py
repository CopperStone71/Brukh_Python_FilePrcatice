fileName = input("Введите имя файла: ")
print("Начните вводить строки: ")
with open(fileName, "a") as f:
    while True:
        fileInput = input()
        if fileInput == "":
            break
        f.write(fileInput + "\n")
print("Файл записан.")

