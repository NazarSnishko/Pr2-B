def dict_to_tuple_list(dictionary):
    return list(dictionary.items())

# Отримання словника від користувача
user_dict = {}
while True:
    key = input("Введіть ключ (або натисніть Enter, щоб завершити введення): ")
    if not key:
        break
    value = input("Введіть значення для ключа '{}': ".format(key))
    user_dict[key] = value

# Перетворення словника у список кортежів
tuple_list = dict_to_tuple_list(user_dict)

# Виведення результату
print("Список кортежів:")
print(tuple_list)
