## Problem: Find the largest length of connected grid 



EMPTY = 0   # empty cell
FILLED = 1  # filled cell
VISITED = 2    # visited cell (not empty and not filled)

# visits any conncected cells (all 8 directions)
def visit(index):
    global rows, columns, matrix, size
    matrix[index] = VISITED    # change to represent current region
    size += 1               # add to current region size

    # if not first column
    if (index % columns != 0):
        
        # check left
        if (matrix[index - 1] == FILLED):
            visit(index - 1)
        
        # if not first row, check upper left
        if (int(index / columns) != 0):
            if (matrix[index - columns - 1] == FILLED):
                visit(index - columns - 1)
        
        # if not last row, check lower left
        if (int(index / columns) != rows - 1):
            if (matrix[index + columns - 1] == FILLED):
                visit(index + columns - 1)
    # end if not first column
    
    # if not last column
    if (index % columns != columns - 1):
        
        # check right
        if (matrix[index + 1] == FILLED):
            visit(index + 1)
        
        # if not first row, check upper right
        if (int(index / columns) != 0):
            if (matrix[index - columns + 1] == FILLED):
                visit(index - columns + 1)
    
        # if not last row, check lower right
        if (int(index / columns) != rows - 1):
            if (matrix[index + columns + 1] == FILLED):
                visit(index + columns + 1)
    # end if not last column
    
    # if not first row, check up
    if (int(index / columns) != 0):
        if (matrix[index - columns] == FILLED):
            visit(index - columns)
    
    # if not last row, check down
    if (int(index / columns) != rows - 1):
        if (matrix[index + columns] == FILLED):
            visit(index + columns)
#end def visit

# get row and column numbers
rows = int(input())    # m
columns = int(input()) # n

# create matrix
# internally represented as a single dimensional list
# max 81 elements -- by pre-condition
# Note: The index [row][col] is [4*row + col]
matrix = []
for i in range(rows):
    matrix.append(input().split()) # split entry line
matrix = [int(j) for j in matrix]     # convert to int

# find biggest region
biggest = 0     # size of the biggest region

# while there are still unfound filled's
while 1 in matrix:
    size = 0    # size of the current region
    visit(matrix.index(1))
    if (size > biggest):
        biggest = size
# end while

# print
print (biggest)
