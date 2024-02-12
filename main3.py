import random

file = open('data.txt', 'r')

matrix_rows = int(file.readline())
matrix_columns = int(file.readline())

lines = file.readlines()
matrix = [[int(num) for num in line.split()] for line in lines]
file.close()


# greedy algo
def calc_sum(mat):
    s = 0
    for line in mat:
        min_number = min(line, key=lambda x: abs((x + s)))
        s += min_number
    return s


ITERS = 0
while ITERS < 1_000_000:
    n1 = random.randint(10, 30)
    n2 = random.randint(30, 70)
    n3 = random.randint(70, 90)
    s1 = calc_sum(matrix[:n1])
    s2 = calc_sum(matrix[n1:n2])
    s3 = calc_sum(matrix[n2:n3])
    s4 = calc_sum(matrix[n3:])

    if s1 + s2 + s3 + s4 == 0:
        print(f'i: {ITERS}, sum = 0')
        break

    ITERS += 1
