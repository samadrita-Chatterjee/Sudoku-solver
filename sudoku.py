backtracks=0
def findempty_celltofill(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                return r,c
    return -1,-1    #if no cells in the grid are empty
# checks whether the guess is  valid guess to the given row,col,3*3 matrix
def is_valid(grid,guess,row,col):
    for i in range(0,9):
        if grid[row][i]==guess:
            return False 
    for i in range(0,9):
        if grid[i][col]==guess:
            return False
    start_row,start_col=3*(row//3),3*(col//3)
    for i in range(0,3):
        for j in range(0,3):
            if grid[i+start_row][j+start_col]==guess:
                return False
    return True
# solve sudoku using backtracking
def Solve_Sudoku(grid): 
    global backtracks
    row,col=findempty_celltofill(grid)
    if row == -1:
        return True
    for guess in range(1,10):
        # check is this a valid guess
        if is_valid(grid,guess,row,col):
            #if this is avalid guess then place it at that cell on the grid
            grid[row][col]=guess
            # then recursively call the solve_sudoku function
            if Solve_Sudoku(grid):
                return True
        backtracks+=1 
        # removing the assigned guess since it is not valid then we need to backtrack        
        grid[row][col]=0 
    return False 
#0 means empty cells
grid=[[0,0,2,7,8,0,0,0,3],
      [0,0,0,0,0,9,8,0,1],
      [4,0,0,0,0,3,0,7,0],
      [9,0,5,0,0,8,0,0,0],
      [0,0,0,0,7,0,0,0,0],
      [0,0,0,5,0,0,4,0,8],
      [0,6,0,4,0,0,0,0,7],
      [3,0,9,8,0,0,0,0,0],
      [8,0,0,0,3,1,6,0,0]]
if Solve_Sudoku(grid):
    print(grid)
else:
    print("This puzzle has no solution")
#To count how many wrong guesses this program did 
print('\n')
print(backtracks)


    