file = open('data.txt', 'r')

matrix_rows = int(file.readline())
matrix_columns = int(file.readline())

lines = file.readlines()
matrix = [[{'num': int(num), 'sel': False} for num in line.split()] for line in lines]
file.close()

test_matrix = [[-2, 1, 3], [1, -2, 5], [1, -1, 6]]
ITERS = 1
while ITERS < 1_000_000:
    SUM = 0

    for i in range(0, len(matrix)):
        row = matrix[i]

        # select not-selected numbers
        not_sel_nums = [n for n in row if not n['sel']]

        if len(not_sel_nums) == 0:
            continue

        min_number = min(not_sel_nums, key=lambda x: abs((x['num'] + SUM)))
        min_number['sel'] = True

        SUM += min_number['num']

    if SUM == 0:
        break

    ITERS += 1

print(f'iters: {ITERS}')

