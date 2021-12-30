def generating_sudoku(level):
###############################################################################    
    import time
    import Solver_for_generating_complete_sudoku
    import copy
    import random
###############################################################################    
    l=[]
    coors = [(i,j) for i in range(9) for j in range(9)]
    coors_copy=copy.deepcopy(coors)
    possible_solutions=[]
###############################################################################    
    def print_sudoku(x):
        for i in range(9):
            for j in range(9):
                print(x[i][j],end=' ')
            print()
    
    def internal_check_box(x1,x2,x3,y1,y2,y3,no1,no2,no):
        count_box=0
        for row in (x1,x2,x3):
            for col in (y1,y2,y3):
                if l[row][col]!=no and (row,col)!=(no1,no2):
                    count_box+=1    
        return count_box
    
    def check_box(i,j,x):
        count=0
        if ((i*i)+(j*j))%9==0:
            count=internal_check_box(i,i+1,i+2,j,j+1,j+2,i,j,x)          
        
        elif ((i*i)+((j-1)*(j-1)))%9==0:
            count=internal_check_box(i,i+1,i+2,j-1,j,j+1,i,j,x)
        
        elif ((i*i)+((j+1)*(j+1)))%9==0:
            count=internal_check_box(i,i+1,i+2,j-2,j-1,j,i,j,x)
        
        elif (((i-1)*(i-1))+((j)*(j)))%9==0:                             
            count=internal_check_box(i-1,i,i+1,j,j+1,j+2,i,j,x)
        
        elif (((i-1)*(i-1))+((j-1)*(j-1)))%9==0:                            
            count=internal_check_box(i-1,i,i+1,j-1,j,j+1,i,j,x)
        
        elif (((i-1)*(i-1))+((j+1)*(j+1)))%9==0:    
            count=internal_check_box(i-1,i,i+1,j-2,j-1,j,i,j,x)
        
        elif (((i+1)*(i+1))+((j)*(j))) % 9  == 0:
            count=internal_check_box(i-2,i-1,i,j,j+1,j+2,i,j,x)
        
        elif (((i+1)*(i+1))+((j-1)*(j-1)))%9==0:
            count=internal_check_box(i-2,i-1,i,j-1,j,j+1,i,j,x)
        
        elif (((i+1)*(i+1))+((j+1)*(j+1)))%9==0:                        
            count=internal_check_box(i-2,i-1,i,j-2,j-1,j,i,j,x)
        
        if count==8:
            return True
        return False
    def check_column(i,j,x):
        count_column=0
        for temp in range(i,-1,-1):
            if l[temp][j]!=x and (temp!=i) :
                count_column+=1
        if count_column==i:
            return True
        return False
    
    def generate_empty_sudoku():
        for i in range(9):
            l.append([])
            for j in range(9):
                l[i].append(0)
        return l
    
    def generate_complete_sudoku():
        global start_time
        start_time=time.time()
        for find_row_zero in range(9):
            for find_col_zero in range(9):
                if l[find_row_zero][find_col_zero]==0:
                    break
            if l[find_row_zero][find_col_zero]==0:
                break
        for i in range(find_row_zero,9):
            for j in range(9):
                l[i][j]=0
        for i in range(find_row_zero,4):
            while True:
                a=b=[1,2,3,4,5,6,7,8,9]
                for j in range(9):
                    current=random.choice(a)
                    b=copy.deepcopy(a)
                    while (l[i][j]==0):
                        if check_box(i,j,current) and check_column(i,j,current):
                            l[i][j]=(current)
                            a.remove(l[i][j]) 
                        else:
                            a.remove(current)
                            if len(a)==0:
                               break
                            current=random.choice(a)
                    if l[i][j]==0:         
                        l[i]=[0,0,0,0,0,0,0,0,0]
                        break
                    else: 
                        b.remove(l[i][j])
                        a=copy.deepcopy(b)
                if l[i]!=[0,0,0,0,0,0,0,0,0]:
                    break    
        return l
    
    def generate_main_sudoku(x):
        coors=copy.deepcopy(coors_copy)
        l=copy.deepcopy(l2)
        for check in range(x):
            possible_solutions.clear()
            while True:
                if len(coors)==0:
                    break
                (row_check1,column_check1)=random.choice(coors)
                coors.remove((row_check1,column_check1))
                l[row_check1][column_check1]=0
                temp_solved_lis=Solver_for_generating_complete_sudoku.solver(l)
                if len(temp_solved_lis)==1:
                    break
                l[row_check1][column_check1]=l2[row_check1][column_check1]
            if len(coors)==0:
                break
        return l
    
#############################################################################    
    l=generate_empty_sudoku()
    l=generate_complete_sudoku()
    l=Solver_for_generating_complete_sudoku.solver(l)
    l=copy.deepcopy(l[0])
    l2=copy.deepcopy(l)
##############################################################################    
    if level==1:
        x=38
        req=generate_main_sudoku(x)
    
    elif level==2:
        x=47
        req=generate_main_sudoku(x)
    
    elif level==3:
        x=66
        req=generate_main_sudoku(x)
    #print_sudoku(req)
    #print()
    #print_sudoku(l2)
###############################################################################    
    return req,l2

#lis1,lis2=generating_sudoku(1)
#print(lis1,lis2,sep='\n')
