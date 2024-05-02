# Завдання 3
# Маємо певний словник з логінами і паролями користувачів. Логін використовується як ключ, пароль —
# як значення. Реалізуйте: додавання, видалення, пошук,
# редагування, збереження та завантаження даних (використовуючи стиснення та розпакування).

import pickle
import gzip

def add_user(users, login, password):
    if login not in users:
        users[login] = password
        print("Користувача успішно додано.")
    else:
        print("Користувач з таким логіном вже існує.")

def remove_user(users, login):
    if login in users:
        del users[login]
        print("Користувача успішно видалено.")
    else:
        print("Користувач з таким логіном не існує.")

def find_user(users, login):
    if login in users:
        print("Користувач з логіном '{}' знайдений. Пароль: '{}'".format(login, users[login]))
    else:
        print("Користувач з логіном '{}' не знайдений.".format(login))

def edit_user(users, login, new_password):
    if login in users:
        users[login] = new_password
        print("Пароль користувача успішно змінено.")
    else:
        print("Користувач з таким логіном не існує.")

def save_data(users, filename):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(users, f)
    print("Дані успішно збережені у файлі.")

def load_data(filename):
    try:
        with gzip.open(filename, 'rb') as f:
            users = pickle.load(f)
        print("Дані успішно завантажено з файлу.")
        return users
    except FileNotFoundError:
        print("Файл з даними не знайдено.")
        return {}

def main():
    users = {}
    while True:
        print("\nМеню:")
        print("1. Додавання користувача")
        print("2. Видалення користувача")
        print("3. Пошук користувача")
        print("4. Редагування пароля користувача")
        print("5. Збереження даних у файл")
        print("6. Завантаження даних з файлу")
        print("7. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            login = input("Введіть логін користувача: ")
            password = input("Введіть пароль користувача: ")
            add_user(users, login, password)
        elif choice == '2':
            login = input("Введіть логін користувача, якого потрібно видалити: ")
            remove_user(users, login)
        elif choice == '3':
            login = input("Введіть логін користувача, якого потрібно знайти: ")
            find_user(users, login)
        elif choice == '4':
            login = input("Введіть логін користувача, пароль якого потрібно змінити: ")
            new_password = input("Введіть новий пароль: ")
            edit_user(users, login, new_password)
        elif choice == '5':
            filename = input("Введіть ім'я файлу для збереження даних: ")
            save_data(users, filename)
        elif choice == '6':
            filename = input("Введіть ім'я файлу для завантаження даних: ")
            users = load_data(filename)
        elif choice == '7':
            print("Програма завершує роботу.")
            break
        else:
            print("Некоректний вибір. Будь ласка, виберіть опцію зі списку.")


if __name__ == "__main__":
    main()
