# Завдання 1
# Користувач заповнює з клавіатури список цілих.
# Стисніть отримані дані та збережіть їх у файл. Після цього
# завантажте дані з файлу в новий список.
import pickle

number = (int(input("Заповніть з клавіатури список цілих чисел")))
print(number)

serialized_data = pickle.dumps(number)
print(f"Serialized data:\n{serialized_data}\n")

deserialized_data = pickle.loads(serialized_data)
print(f"Deserialized data:\n{deserialized_data}\n")



