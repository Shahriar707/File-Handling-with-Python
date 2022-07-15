matrix = []

with open('input4.txt') as file:
    for i in file:
        lst = [x.strip() for x in i.split()]
        matrix.append(lst)
dimension = 0
for i in range(1):
    dimension = int(matrix[i][i])
matrix.pop(0)

first, second = [], []

for i in range(dimension):
    first.append(matrix[i])
for i in range(dimension, len(matrix)):
    second.append(matrix[i])

final = [[0] * dimension for i in range(dimension)]
dimension = len(first)
for i in range(len(first)):
    for j in range(len(second[0])):
        for k in range(len(second[0])):
            final[i][j] += int(first[i][k]) * int(second[k][j])

with open("output4.txt", "w") as output_file:
    for i in range(3):
        [output_file.write("{} ".format(final[i][j])) for j in range(3)]
        output_file.write("\n")