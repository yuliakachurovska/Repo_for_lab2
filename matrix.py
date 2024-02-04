n_rows = int(input("Введіть кількість рядків матриці: "))
n_columns = int(input("Введіть кількість стовпців матриці: "))

matrix = []
row = []
for i in range(n_rows):
    row = []
    for j in range(n_columns):
        el = int(input(f"Введіть елемент матриці: "))
        row.append(el)
    matrix.append(row)

# Виведення матриці стовпцями
for col in range(n_columns):
    for row in matrix:
        print(row[col], end=' ')
    print()

tar_el = int(input("Введіть шуканий елемент: "))

found = False
for i in range(n_rows):
    for j in range(n_columns):
        if matrix[i][j] == tar_el:
            print(f"Знайдено шуканий елемент {tar_el} у рядку {i} і стовпці {j}.")
            found = True
            break

if not found:
    print(f"Елемент {tar_el} не знайдено в матриці.")