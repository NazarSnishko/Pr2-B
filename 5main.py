matrix = [list(map(int, input().split())) for _ in range(int(input("Введіть кількість рядків: ")))]
min_index = min(((i, row.index(min(row))) for i, row in enumerate(matrix)), key=lambda x: x[1])
max_index = max(((i, row.index(max(row))) for i, row in enumerate(matrix)), key=lambda x: x[1])
print("Найменший елемент:", matrix[min_index[0]][min_index[1]], "рядок:", min_index[0] + 1, "стовпець:", min_index[1] + 1)
print("Найбільший елемент:", matrix[max_index[0]][max_index[1]], "рядок:", max_index[0] + 1, "стовпець:", max_index[1] + 1)
