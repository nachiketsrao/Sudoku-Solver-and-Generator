##################################  Import Modules   ##########################
from tkinter import *
from tkinter import messagebox
from final_9cross9 import run9cross9
from generator import GenerateSudokuToSolve
from final_4cross4 import run4cross4

###############################################################################

def tab2():
    
    root=Tk()
    root.geometry("1350x730")
    root.title("PROJECT SUDOKU")
    root.configure(bg='yellow')
    root.attributes('-fullscreen',True)
    options=[("Level : 1"),("Level : 2"),("Level : 3")]
    global v
    v=0
    
    def level():
        global v
        y1=500
        text=Label(root,text="Please choose the level of the Sudoku ",font=('Times',20),fg='Black',bg='yellow')
        text.place(x=50,y=450)
        for val,option in enumerate(options):
            
            radbut=Radiobutton(root,text=option,indicatoron=0,width=20,padx=20,pady=3,variable=v,command=showchoice,value=val,fg='blue',font=('Times',15))
            radbut.place(x=250,y=y1)
            y1=y1+35
            
    def showchoice():
        
        global v
        print(v)
        level=v+1
        #print("Level : ",level)
        v=0
        GenerateSudokuToSolve(level)
    
    def close_window3():
         root.destroy()    
    
    welcome=Label(root,text="SUDOKU SOLVER",font=('Times',55),fg='darkblue',bg='yellow')
    welcome.place(x=400,y=10)
    
    fourtext=Label(root,text="Click here to solve 4 into 4 sudoku --",font=('Times',20),fg='green',bg='yellow')
    fourtext.place(x=50,y=150)
    
    fourbutton=Button(root,text="Solve 4 X 4",font=('Times',14),fg='blue',command=run4cross4)
    fourbutton.place(x=500,y=150)
    
    ninetext=Label(root,text="Click here to solve 9 into 9 sudoku --",font=('Times',20),fg='green',bg='yellow')
    ninetext.place(x=50,y=250)
    
    ninebutton=Button(root,text="Solve 9 X 9",font=('Times',14),fg="blue",command=run9cross9)
    ninebutton.place(x=500,y=250)
    
    generatetext=Label(root,text="Click here to generate and solve a 9 X 9 sudoku --",font=('Times',20),fg='green',bg='yellow')
    generatetext.place(x=50,y=350)
    
    generatebutton=Button(root,text="Generate and Solve",font=('Times',14),fg="blue",command=level)
    generatebutton.place(x=630,y=350)
    
    exitbutton=Button(root,text="Exit",font=('Times',14),fg="blue",command=close_window3).place(x=650,y=690)
    root.mainloop()    