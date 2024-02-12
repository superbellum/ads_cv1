data = []

data_file = open('data.txt', 'r')
num_rows = int(data_file.readline().strip())
num_cols = int(data_file.readline().strip())

for i in range(0, num_rows):
    line = data_file.readline()
    line_split = line.split()
    num_list = list(map(lambda st: int(st), line_split))
    data.append(num_list)
data_file.close()

data = data[:5]

SUM = 0

# data = [[-2, 1, 3], [1, -2, 5], [1, -1, 6]]
results = []

# iterate through first row
for i in range(0, len(data[0])):
    f = data[0][i]
    results.append([f])

    for j in range(1, len(data)):
        row = data[j]

        s = f + row[0]
        ni = row[0]

        for k in range(1, len(row)):
            n = row[k]

            if abs(f + n) < abs(s):
                s = f + n
                ni = n

        results[i].append(ni)
        f = s

    print(f'f[{i}] = {f}')
print(results)