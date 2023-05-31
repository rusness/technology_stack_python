import random

def add_matrices(matrix_1, matrix_2):
    n = len(matrix_1)
    m = len(matrix_1[0])
    result = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = matrix_1[i][j] + matrix_2[i][j]
    return result

def generate_matrix(n, m, a, b):
    matrix = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = random.randint(a, b)
    return matrix


matrix_1 = generate_matrix(3, 3, 0, 10)
matrix_2 = generate_matrix(3, 3, 0, 10)
print(matrix_1)
print(matrix_2)
result = add_matrices(matrix_1, matrix_2)
print(result)
