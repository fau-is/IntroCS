def is_matrix_symmetric(matrix):
    symmetric = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                symmetric = False
    return symmetric