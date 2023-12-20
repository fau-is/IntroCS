def is_matrix_symmetric(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    else:
        for i in range len(matrix):
            for j in range len(matrix[i]):
                if matrix[i] != matrix[j]:
                    return False

    return True
