##################################  Import Modules   ##########################
from tkinter import *
from tkinter import messagebox
from final_9cross9 import ninenine
from generator import GenerateSudokuToSolve
from final_4cross4 import fourfour
from LoadPrevious import check_IsAnySaved, solve_previous
###############################################################################

def tab2(CurrentUserObject):
    print('big time success')
    global variable1,points,num_score,wait_window,your_rank,rank1,rank2,rank3
    wait_window=''
    variable1=0
    root1=Tk()
    root1.geometry("1350x730")
    root1.title("PROJECT SUDOKU")
    root1.configure(bg='yellow')
    root1.attributes('-fullscreen',True)
    
    
    def CheckAndLoad():
        print("Entered load")
        print()
        if check_IsAnySaved(CurrentUserObject):
            print("loading saved")
            solve_previous(CurrentUserObject)
        else:
            messagebox.showinfo("Error","No sudokus saved",parent= root1) 
            print("no sudokus")
    
    def LevelButtons():
        text=Label(root1,text="Please choose the level of the Sudoku ",font=('Times',20),fg='green',bg='yellow')
        text.place(x=70,y=550)
        
        radbut1=Radiobutton(root1,text="Level :1",indicatoron=0,width=20,padx=20,pady=3,command=showchoice1,fg='blue',font=('Times',15)).place(x=170,y=600)
        radbut2=Radiobutton(root1,text="Level :2",indicatoron=0,width=20,padx=20,pady=3,command=showchoice2,fg='blue',font=('Times',15)).place(x=170,y=650)
        radbut3=Radiobutton(root1,text="Level :3",indicatoron=0,width=20,padx=20,pady=3,command=showchoice3,fg='blue',font=('Times',15)).place(x=170,y=700)
    
    
    def level():
        loadPrevious=Label(root1,text="Click here to load previously saved sudoku -- ",font=('Times',20),fg='green',bg='yellow')
        loadPrevious.place(x=70,y=425)  # for loading the saved sudoku, if any
        
        loadPreviousButton=Button(root1,text="Load",font=('Times',14),fg='blue',command= CheckAndLoad)
        loadPreviousButton.place(x=570,y=425)  # for loading the saved sudoku, if any
        
        loadnew=Label(root1,text="Click here to generate a new sudoku -- ",font=('Times',20),fg='green',bg='yellow')
        loadnew.place(x=70,y=475)
        
        loadNewButton=Button(root1,text="Generate",font=('Times',14),fg='blue',command= LevelButtons)
        loadNewButton.place(x=570,y=475)
    
        
    def showchoice1():
        GenerateSudokuToSolve(1, CurrentUserObject)
        
        
    def showchoice2():
        GenerateSudokuToSolve(2, CurrentUserObject)
        
    
    def showchoice3():
        GenerateSudokuToSolve(3, CurrentUserObject)
        
        
    def close_window3():
         root1.destroy()   
         
    import csv
    f=open('points.csv','r')
    w=csv.reader(f)
    
    #w=list(w)''
    lis =list(w)
    f.close()
    print(lis)
    
    for i in lis:
        print(i)
        
        if len(i)>0:
            if i[0] == CurrentUserObject.name :
                
                points = i[1]
                break
    
    
    def leaderboard():
        
        import csv
        f=open('points.csv','r')
        w=csv.reader(f)
        lis=list(w)
        #print('lis test :',lis)
        f.close()
        
        leaders=[]
        
        lis = [i for i in lis if len(i) != 0]
        total_rank=len(lis)
        leaders = sorted(lis, key=lambda x: int(x[1]))
        leaders.reverse()
        print()
        print(leaders)
        print()
        for i in range (len(leaders)):
            if leaders[i][0]==CurrentUserObject.name:
                rank=i+1
                break
        
        leaders=leaders[:4]
        
        
        print("Leaders : ",leaders)
        
        lead = Label(root1,text='LEADERBOARD',font=('Times',27),fg='Black',bg='yellow')
        lead.place(x=900,y=200)
        
        rank1 =Label(root1,text='1) '+str(leaders[0][0])+' -- '+str(leaders[0][1]),font=('Times',20),fg='Black',bg='yellow')
        rank1.place(x=925,y=270)
        
        rank2 =Label(root1,text='2) '+str(leaders[1][0])+' -- '+str(leaders[1][1]),font=('Times',20),fg='Black',bg='yellow')
        rank2.place(x=925,y=340)
        
        rank3 =Label(root1,text='3) '+str(leaders[2][0])+' -- '+str(leaders[2][1]),font=('Times',20),fg='Black',bg='yellow')
        rank3.place(x=925,y=410)
        
        return rank,total_rank
        
    user_rank,total_players=leaderboard()
    points = int(points)
    print(CurrentUserObject.points)
    score=Label(root1,text="Your total score is  :  ",font=('Times',20),fg='Black',bg='yellow')
    score.place(x=900,y=480)  # for loading the saved sudoku, if any
    
    num_score=Label(root1,text=points,font=('Times',20),fg='Black',bg='yellow')
    num_score.place(x=1125,y=480)
    
    rank=Label(root1,text="Your rank is : ",font=('Times',20),fg='Black',bg='yellow').place(x=900,y=530)
    
    your_rank=Label(root1,text=user_rank,font=('Times',20),fg='Black',bg='yellow')
    your_rank.place(x=1050,y=530)
    
    total_rank=Label(root1,text="Total number of players : "+str(total_players),font=('Times',20),fg='Black',bg='yellow').place(x=900,y=580)
    warning=Label(root1,text="* If your rank has changed, it will be updated the \nnext time you login",font=('Times',13),fg='Black',bg='yellow').place(x=900,y=630)
    
    welcome=Label(root1,text="SUDOKU SOLVER",font=('Times',55),fg='darkblue',bg='yellow')
    welcome.place(x=400,y=10)
    
    fourtext=Label(root1,text="Click here to solve 4 into 4 sudoku --",font=('Times',20),fg='green',bg='yellow')
    fourtext.place(x=50,y=150)
    
    fourbutton=Button(root1,text="Solve 4 X 4",font=('Times',14),fg='blue',command=fourfour)
    fourbutton.place(x=500,y=150)
    
    ninetext=Label(root1,text="Click here to solve 9 into 9 sudoku --",font=('Times',20),fg='green',bg='yellow')
    ninetext.place(x=50,y=250)
    
    ninebutton=Button(root1,text="Solve 9 X 9",font=('Times',14),fg="blue",command=ninenine)
    ninebutton.place(x=500,y=250)
    
    generatetext=Label(root1,text="Click here to generate and solve a 9 X 9 sudoku --",font=('Times',20),fg='green',bg='yellow')
    generatetext.place(x=50,y=350)
    
    generatebutton=Button(root1,text="Generate and Solve",font=('Times',14),fg="blue",command=level)
    generatebutton.place(x=630,y=350)
    
    exitbutton=Button(root1,text="Exit",font=('Times',20),fg="blue",command=close_window3).place(x=1270,y=20)
    root1.mainloop()
    
#tab2()