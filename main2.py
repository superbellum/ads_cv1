file = open('data.txt', 'r')

matrix_rows = int(file.readline())
matrix_columns = int(file.readline())

lines = file.readlines()
matrix = [[int(num) for num in line.split()] for line in lines]
file.close()

test_matrix = [[-2, 1, 3], [1, -2, 5], [1, -1, 6]]

SUM = 0
for line in matrix:
    min_number = min(line, key=lambda x: abs((x + SUM)))
    SUM += min_number

print(f'sum: {SUM}')
