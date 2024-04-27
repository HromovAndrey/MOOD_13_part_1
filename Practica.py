#import pickle

#data = {"login": "world", "passwork" : "123153" }# есть обьек

# print(data)
# serialized_data = pickle.dumps(data)# обьект переводиться в набір байтів
# print(serialized_data)
# read_data =  pickle.loads(serialized_data)# набір байтів перводится назад в обьект
#
# print(type(read_data), read_data)

# with open("data.pickle .pk .pk1") as file:
#     pickle.dump(data, file)
# dump значить що не має файла  dumps це з файлами
# with open("data.pickle", "rb") as file:#читаємо файл
#     read_data = pickle.load(file)
# print(type(read_data), read_data)

import pickle
import  gzip

data = {"login": "world", "password": "12345678"}

with gzip.open("data.gz", "wb") as file:
    serialized_data = pickle.dumps(data)
    file.write(serialized_data)