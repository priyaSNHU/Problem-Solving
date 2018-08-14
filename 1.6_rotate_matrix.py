# Problem Link: Problem: Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90degree. Can you do this in place?

def matrix_rotation(matrix , n):
    ## row
    for r in range(0, n//2):
        ##column
        for c in range(r , n-1-r):
            # store curr value in a variable
            temp = matrix[r][c]

            # now move left to top
            matrix[r][c] = matrix[n-1-c][r]

            #bottom to left
            matrix[n-1-c][r] = matrix[n-1-r][n-1-c]

            #right to bottom
            matrix[n-1-r][n-1-c] = matrix[c][n-1-r]

            # temp to right
            matrix[c][n-1-r] = temp

    for r in range(n):
        for c in range(n):
            print(matrix[r][c])
        print("")

n = 4
matrix = [[r+c for r in range(n)] for c in range(n)]
matrix_rotation(matrix, n)
