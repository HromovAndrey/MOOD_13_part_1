# Завдання 2
# При старті програми з’являється меню з наступними
# пунктами:
# 1. Завантаження даних;
# 2. Збереження даних;
# 3. Додавання даних;
# 4. Видалення даних.
# Використайте список цілих як сховища даних. Також
# застосуйте стиснення/розпакування даних.

import pickle
import gzip

def load_data(filename):
    try:
        with gzip.open(filename, 'rb') as f:
            data = pickle.load(f)
        print("Дані успішно завантажено з файлу.")
        return data
    except FileNotFoundError:
        print("Файл з даними не знайдено.")
        return []

def save_data(data, filename):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(data, f)
    print("Дані успішно збережено у файл.")

def add_data(data):
    try:
        number = int(input("Введіть ціле число для додавання до списку: "))
        data.append(number)
        print("Дані успішно додано до списку.")
    except ValueError:
        print("Введіть коректне ціле число.")

def remove_data(data):
    try:
        number = int(input("Введіть ціле число, яке потрібно видалити зі списку: "))
        if number in data:
            data.remove(number)
            print("Дані успішно видалено зі списку.")
        else:
            print("Вказане число не знайдено у списку.")
    except ValueError:
        print("Введіть коректне ціле число.")

def main():
    data = []
    while True:
        print("\nМеню:")
        print("1. Завантаження даних")
        print("2. Збереження даних")
        print("3. Додавання даних")
        print("4. Видалення даних")
        print("5. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            filename = input("Введіть ім'я файлу для завантаження даних: ")
            data = load_data(filename)
        elif choice == '2':
            filename = input("Введіть ім'я файлу для збереження даних: ")
            save_data(data, filename)
        elif choice == '3':
            add_data(data)
        elif choice == '4':
            remove_data(data)
        elif choice == '5':
            print("Програма завершує роботу.")
            break
        else:
            print("Некоректний вибір. Будь ласка, виберіть опцію зі списку.")


if __name__ == "__main__":
    main()
