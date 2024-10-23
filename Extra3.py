fileName = input("Введите имя файла: ")

def get_user_data(fileName):
    while True:
        try:
            user_input = input("Введите ФИО и год рождения через пробел: ")
            surname, name, patronymic, birth_year = user_input.split()

            if not surname.isalpha() or not name.isalpha() or not patronymic.isalpha():
                raise ValueError("ФИО должны содержать только буквы.")
            if not birth_year.isdigit() or len(birth_year) != 4:
                raise ValueError("Год рождения должен быть 4-значным числом.")
            if not surname[0].isupper() or not name[0].isupper() or not patronymic[0].isupper():
                raise ValueError("Каждый элемент ФИО должен начитаться с заглавной буквы")

            with open(fileName, "a") as file:
                file.write(f"{surname}\t{name}\t{patronymic}\t{birth_year}\n")

            print("Данные успешно записаны.")
            break

        except ValueError as e:
            print(f"Ошибка: {e}. Пожалуйста, попробуйте снова.")

        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

def read_data(fileName):
    try:
        with open(fileName, "r") as file:
            print("Фамилия\tИмя\tОтчество\tГод рождения")
            print("------------------------------------------------")
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print(f"Файл {fileName} не найден.")
    except Exception as e:
        print(f"Неизвестная ошибка при чтении файла: {e}")

get_user_data(fileName)
read_data(fileName)
