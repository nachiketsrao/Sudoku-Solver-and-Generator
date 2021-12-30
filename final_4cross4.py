
#All imports and creation of root an canvas
import tkinter
from tkinter import messagebox
from PIL import ImageTk,Image
import time


def fourfour():
    root=tkinter.Tk()
    root.title("4x4 Sudoku Solver")
    root.resizable(height=None,width=None)
    root.geometry("1000x1000")
    root.configure(bg="SkyBlue2")
    root.attributes("-fullscreen",True)



    canvas=tkinter.Canvas(root,width=1300,height=1200,bg="SkyBlue2")
    canvas.pack()

    #function runtime that solves and returns the sudoku

    def runtime(grid):
        def print_sudoku(l):
            for i in range(4):
                for j in range(4):
                    print (l[i][j],end=" ")
                print("")

        def find_empty(l,empty):
            for row in range(4):
                for col in range(4):
                    if(l[row][col]==0):
                        empty[0]=row
                        empty[1]=col
                        return True
            return False

        def used_row(l,row,num):
            for i in range(4):
                if(l[row][i] == num):
                    return True
            return False

        def used_col(l,col,num):
            for i in range(4):
                if(l[i][col] == num):
                    return True
            return False


        def used_box(l,row,col,num):
            for i in range(2):
                for j in range(2):
                    if(l[i+row][j+col] == num):
                        return True
            return False


        def location_safe(l,row,col,num):
            return not used_row(l,row,num) and not used_col(l,col,num) and not used_box(l,row - row%2,col - col%2,num)

        def solve_sudoku(l):
            empty=[0,0]
            if(not find_empty(l,empty)):
                return True
            row=empty[0]
            col=empty[1]

            for num in range(1,5):
                if(location_safe(l,row,col,num)):
                    l[row][col]=num
                    if(solve_sudoku(l)):
                        return True
                    l[row][col] = 0

            #print_sudoku(l)        return False

        #maun starts here
        start_time=time.time()
        # if success print the grid
        if(solve_sudoku(grid)):
            #time.sleep(2)
            print(" The time elapsed is :",(time.time()-start_time))
            print("\n")
            return grid
        else:
            return False




    #reset function that clears the contents of the sudoku

    def reset():
        entry1.destroy()
        entry2.destroy()
        entry3.destroy()
        entry4.destroy()
        entry5.destroy()
        entry6.destroy()
        entry7.destroy()
        entry8.destroy()
        entry9.destroy()
        entry10.destroy()
        entry11.destroy()
        entry12.destroy()
        entry13.destroy()
        entry14.destroy()
        entry15.destroy()
        entry16.destroy()

        #root.clipboard_clear()
        print("Clip board cleared")
        global reset_btn
        reset_btn=tkinter.Button(canvas,text="Reset",font=("Times",30),bg="SteelBlue1",fg="Black",command=reset,state=tkinter.DISABLED).place(x=600,y=230)
        print("Entering reset")
        #global grid
        #grid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        #print(grid)
        show_all()


    #All null and all_full functions that check if there is no number or the entire sudoku is full of numbers
    def all_null(l):
        count=0
        for i in l:
            for j in i:
                if j==0:
                    count+=1
        if count==16:
            return False
        else:
            return True

    def all_full(l):
        count=0
        k=[1,2,3,4]
        for i in l:
            for j in i:
                if j in k:
                    count+=1
        if count==16:
            return False
        else:
            return True

    #function only_num that allows the inut of only  numbers

    def only_num(e):
        if e.isdigit() and (e=='0' or e=='9' or e=='8' or e=='7' or e=='6' or e=='5'):
            return False
        elif e.isdigit() and len(e)==1:
            return True
        elif e=="":
            return True
        else:
            return False



    # function that prints the solved the solved sudoku inside the entry boxes

    def print_solved(grid):
        entry1.destroy()
        entry2.destroy()
        entry3.destroy()
        entry4.destroy()
        entry5.destroy()
        entry6.destroy()
        entry7.destroy()
        entry8.destroy()
        entry9.destroy()
        entry10.destroy()
        entry11.destroy()
        entry12.destroy()
        entry13.destroy()
        entry14.destroy()
        entry15.destroy()
        entry16.destroy()

        print("final grid before printing",grid)


        o1=tkinter.Label(canvas,text=(grid[0][0]),font=("Times",35),bg="white")
        o1.place(x=210,y=174)


        o2=tkinter.Label(canvas,text=(grid[0][1]),font=("Times",35),bg="white")
        o2.place(x=280,y=174)

        o3=tkinter.Label(canvas,text=(grid[0][2]),font=("Times",35),bg="white")
        o3.place(x=365,y=174)

        o4=tkinter.Label(canvas,text=str(grid[0][3]),font=("Times",35),bg="white")
        o4.place(x=450,y=174)

        o5=tkinter.Label(canvas,text=str(grid[1][0]),font=("Times",35),bg="white")
        o5.place(x=210,y=244)

        o6=tkinter.Label(canvas,text=str(grid[1][1]),font=("Times",35),bg="white")
        o6.place(x=280,y=244)

        o7=tkinter.Label(canvas,text=str(grid[1][2]),font=("Times",35),bg="white")
        o7.place(x=365,y=244)

        o8=tkinter.Label(canvas,text=str(grid[1][3]),font=("Times",35),bg="white")
        o8.place(x=450,y=244)

        o9=tkinter.Label(canvas,text=str(grid[2][0]),font=("Times",35),bg="white")
        o9.place(x=210,y=317)

        o10=tkinter.Label(canvas,text=str(grid[2][1]),font=("Times",35),bg="white")
        o10.place(x=280,y=317)

        o11=tkinter.Label(canvas,text=str(grid[2][2]),font=("Times",35),bg="white")
        o11.place(x=365,y=317)

        o12=tkinter.Label(canvas,text=str(grid[2][3]),font=("Times",35),bg="white")
        o12.place(x=450,y=317)

        o13=tkinter.Label(canvas,text=str(grid[3][0]),font=("Times",35),bg="white")
        o13.place(x=210,y=385)

        o14=tkinter.Label(canvas,text=str(grid[3][1]),font=("Times",35),bg="white")
        o14.place(x=280,y=385)

        o15=tkinter.Label(canvas,text=str(grid[3][2]),font=("Times",35),bg="white")
        o15.place(x=365,y=385)

        o16=tkinter.Label(canvas,text=str(grid[3][3]),font=("Times",35),bg="white")
        o16.place(x=450,y=385)


        print("Grid has been cleared")
        messagebox.showinfo("Solver","The sudoku is solved!!",parent=root)
        print("End of porgram")
        global reset_btn
        reset_btn=tkinter.Button(canvas,text="Reset",font=("Times",30),bg="SteelBlue1",fg="Black",command=reset,state=tkinter.NORMAL).place(x=600,y=230)









    # void main part having function show_all that displays the sudoku from scratch and has an entry function that takes all the n=entries

    img=ImageTk.PhotoImage(Image.open(r".\four_cross_four.png"),master=root)
    canvas.create_image(338,305,anchor="center",image=img)

    def show_all():

        def entry():
            ##
            #global grid
            grid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

            if entry1.get()=='':
                i1=int(0)
            else:
                i1=int(entry1.get())


            if entry2.get()=='':
                i2=int(0)
            else:
                i2=int(entry2.get())


            if entry3.get()=='':
                i3=0
            else:
                i3=int(entry3.get())

            if entry4.get()=='':
                i4=0
            else:
                i4=int(entry4.get())

            if entry5.get()=='':
                i5=0
            else:
                i5=int(entry5.get())

            if entry6.get()=='':
                i6=0
            else:
                i6=int(entry6.get())

            if entry7.get()=='':
                i7=0
            else:
                i7=int(entry7.get())

            if entry8.get()=='':
                i8=0
            else:
                i8=int(entry8.get())

            if entry9.get()=='':
                i9=0
            else:
                i9=int(entry9.get())

            if entry10.get()=='':
                i10=0
            else:
                i10=int(entry10.get())

            if entry11.get()=='':
                i11=0
            else:
                i11=int(entry11.get())

            if entry12.get()=='':
                i12=0
            else:
                i12=int(entry12.get())

            if entry13.get()=='':
                i13=0
            else:
                i13=int(entry13.get())

            if entry14.get()=='':
                i14=0
            else:
                i14=int(entry14.get())

            if entry15.get()=='':
                i15=0
            else:
                i15=int(entry15.get())

            if entry16.get()=='':
                i16=0
            else:
                i16=int(entry16.get())


            #root.clipboard_clear()
            grid=[[i1,i2,i3,i4],[i5,i6,i7,i8],
            [i9,i10,i11,i12],[i13,i14,i15,i16]]
            print("The grid",grid)


            if all_null(grid)==True and all_full(grid)==True:
                x=runtime(grid)
                if x==False:
                    messagebox.showerror("Error","The sudoku is not solvable",parent=root)
                    root.lift()


                    print("Entering the wrong part")
                    #root.clipboard_clear()
                    grid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                    ##
                    global reset_btn
                    reset_btn=tkinter.Button(canvas,text="Reset",font=("Times",30),bg="SteelBlue1",fg="Black",command=reset,state=tkinter.NORMAL).place(x=600,y=230)

                    #show_all()
                else:
                    print_solved(x)
                    grid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

            elif all_null(grid)==False and all_full(grid)==True:

                messagebox.showerror("Error","No number in sudoku.",parent=root)
                ##

            elif all_null(grid)==True and all_full(grid)==False:

                messagebox.showerror("Error","The sudoku is filled with numbers.\n Please enter again.",parent=root)
                entry1.destroy()
                entry2.destroy()
                entry3.destroy()
                entry4.destroy()
                entry5.destroy()
                entry6.destroy()
                entry7.destroy()
                entry8.destroy()
                entry9.destroy()
                entry10.destroy()
                entry11.destroy()
                entry12.destroy()
                entry13.destroy()
                entry14.destroy()
                entry15.destroy()
                entry16.destroy()

                grid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                ##

                show_all()




        c=root.register(only_num)

        print("In main part of show_All")


        global entry1
        entry1 = tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(221, 200, window=entry1)
        entry1.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry2
        entry2 = tkinter.Entry (root, width=3,font=("Helvetica", 31))
        canvas.create_window(296, 198, window=entry2)
        entry2.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry3
        entry3 = tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(380, 200, window=entry3)
        entry3.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry4
        entry4 = tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(458, 200, window=entry4)
        entry4.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry5
        entry5 = tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(221, 270, window=entry5)
        entry5.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry6
        entry6 = tkinter.Entry (root, width=3,font=("Helvetica", 31))
        canvas.create_window(296, 268, window=entry6)
        entry6.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry7
        entry7 = tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(380, 270, window=entry7)
        entry7.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry8
        entry8 = tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(458, 270, window=entry8)
        entry8.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry9
        entry9 = tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(221, 345, window=entry9)
        entry9.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry10
        entry10 = tkinter.Entry (root, width=3,font=("Helvetica", 31))
        canvas.create_window(296, 343, window=entry10)
        entry10.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry11
        entry11= tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(380, 345, window=entry11)
        entry11.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry12
        entry12= tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(458, 345, window=entry12)
        entry12.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry13
        entry13= tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(221, 415, window=entry13)
        entry13.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry14
        entry14= tkinter.Entry (root, width=3,font=("Helvetica", 31))
        canvas.create_window(296, 413, window=entry14)
        entry14.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry15
        entry15= tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(380, 415, window=entry15)
        entry15.config(validate="key", validatecommand=(c,'%P'),justify="center")

        global entry16
        entry16= tkinter.Entry (root, width=3,font=("Helvetica", 33))
        canvas.create_window(458, 415, window=entry16)
        entry16.config(validate="key", validatecommand=(c,'%P'),justify="center")


        solve_btn=tkinter.Button(canvas,text="Solve",font=("Times",30),bg="SteelBlue1",fg="Black",command=entry).place(x=600,y=325)



    show_all()

    head_label=tkinter.Label(canvas,text="Welcome to 4x4 solver",font=("Times",60),fg="Black",bg="SteelBlue1").place(x=120,y=40)

    global reset_btn
    reset_btn=tkinter.Button(canvas,text="Reset",font=("Times",30),bg="gray50",command=reset,state=tkinter.DISABLED).place(x=600,y=230)

    head_instr=tkinter.Label(canvas,text="Instructions :",font=("Times",25),bg="SteelBlue1",fg="black").place(x=100,y=500)
    instr1=tkinter.Label(canvas,text="Please enter numbers between 1 and 4 only.",font=("Times",25)).place(x=100,y=550)
    #instr2=tkinter.Label(canvas,text="To view the solution, click the solve button.",font=("Times",25)).place(x=100,y=650)
    instr3=tkinter.Label(canvas,text="Each number can appear only once in every row, column and box.",font=("Times",25)).place(x=100,y=600)
    close_btn=tkinter.Button(canvas,text="Close",font=("Times",20),bg="gray50",command=root.destroy).place(x=1200,y=0)
    root.mainloop()

