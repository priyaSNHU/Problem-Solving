# Problem:  Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def set_matrix_zero(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    row = [0 for i in range(row_len)]
    col = [0 for i in range(col_len)]

    for r in range(row_len):
        for c in range(col_len):
            if not matrix[r][c]:
                row[r] = True
                col[c] = True
    for r in range(row_len):
        for c in range(col_len):
            if row[r] or col[c]:
                matrix[r][c] = 0
            print(matrix[r][c])
        print("")
                


matrix = [[r+c for r in range(4)] for c in range(3)]
set_matrix_zero(matrix)
