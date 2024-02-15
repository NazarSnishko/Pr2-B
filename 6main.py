input_string = input("Введіть рядок: ")
result = {char: input_string.count(char) for char in set(input_string)}
print("Унікальні символи та їх кількість в рядку:")
for char, count in result.items():
    print(f"'{char}': {count}")