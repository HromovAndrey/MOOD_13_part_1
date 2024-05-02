# Завдання 1
# Користувач заповнює з клавіатури список цілих.
# Стисніть отримані дані та збережіть їх у файл. Після цього
# завантажте дані з файлу в новий список.

import pickle
import gzip


def save_list_to_file(data, filename):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_list_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        loaded_data = pickle.load(f)
    return loaded_data

input_list = []
while True:
    try:
        number = int(input("Введіть ціле число (або 'q' для завершення): "))
        input_list.append(number)
    except ValueError:
        if input("Ви впевнені, що хочете завершити введення? (y/n): ").lower() == 'y':
            break

save_list_to_file(input_list, "compressed_list.pklz")
print("Список успішно збережено у файл.")

loaded_list = load_list_from_file("compressed_list.pklz")
print("Дані успішно завантажено з файлу:", loaded_list)
