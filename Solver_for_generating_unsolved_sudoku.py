def solver(l):
    import time
    import copy
    start_solver=time.time()
    def print_sudoku(x): 
        for i in range(9): 
            for j in range(9): 
                print (x[i][j],end=" ")
            print("")
        print()
    def find_empty(x,empty): 
        for row in range(9): 
            for col in range(9): 
                if(x[row][col]==0): 
                    empty[0]=row 
                    empty[1]=col 
                    return True
        return False
    def used_row(x,row,num): 
        for i in range(9): 
            if(x[row][i] == num): 
                return True
        return False
    def used_col(x,col,num): 
        for i in range(9): 
            if(x[i][col] == num): 
                return True
        return False
    def used_box(x,row,col,num): 
        for i in range(3): 
            for j in range(3): 
                if(x[i+row][j+col] == num): 
                    return True
        return False
    def location_safe(x,row,col,num):   
        return not used_row(x,row,num) and not used_col(x,col,num) and not used_box(x,row - row%3,col - col%3,num)
    def solve_sudoku(x): 
        if len(possible_solutions)>1:
            return True
        if time.time()-start_solver>1:
            possible_solutions.append(5)
            return True
        empty=[0,0] 
        if(not find_empty(x,empty)): 
            return True
        row=empty[0] 
        col=empty[1] 
        for num in range(1,10): 
            if(location_safe(x,row,col,num)): 
                x[row][col]=num 
                if(solve_sudoku(x)): 
                    #print_sudoku(x)
                    possible_solutions.append(copy.deepcopy(grid))
                    if len(possible_solutions)>1:
                        return True
                x[row][col] = 0
        return False
    global grid #Amendments made
    grid=[]
    grid=copy.deepcopy(l)
    possible_solutions=[]
    for loc in range(9):
        for wor in range(9):
            grid[wor][loc]=int(grid[wor][loc])
    solve_sudoku(grid) 
    if len(possible_solutions)==1: 
        return True
    return False