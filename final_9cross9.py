# -*- coding: utf-8 -*-
import time
import tkinter
from tkinter import messagebox
from PIL import ImageTk,Image


def ninenine():

    root=tkinter.Tk()
    root.title("9x9 Sudoku Solver")
    root.resizable(height=None,width=None)
    root.geometry("1000x1000")
    root.configure(bg="SkyBlue2")
    root.attributes("-fullscreen",True)

    canvas=tkinter.Canvas(root,width=1300,height=1200,bg="SkyBlue2")
    canvas.pack()

    global d
    d={}

    global uuu
    uuu=0
    def runtime(grid):


        starttime=time.time()
        def elimination(grid,empty):
            r=empty[0]
            c=empty[1]
            l=[1,2,3,4,5,6,7,8,9]

            for p in l:
                if used_row(grid,r,p):
                    l.remove(p)
                else:
                    if used_col(grid,c,p):
                        l.remove(p)
                    else:
                        if used_box(grid,r-r%3,c-c%3,p):
                            l.remove(p)

            if len(l)==1:
                grid[r][c]==l[0]

            d[(r,c)]=l
            #print(d,"\n")


        def d_creation(grid):
            for i in range(9):
                for j in range(9):
                    elimination(grid,[i,j])





        def print_sudoku(grid):
            for i in range(9):
                for j in range(9):
                    print (grid[i][j],end=" ")
                print("")


        def find_empty(grid,empty):

            for row in range(9):
                for col in range(9):
                    if(grid[row][col]==0):
                        empty[0]=row
                        empty[1]=col

                        return True
            return False


        def used_row(grid,row,num):
            for i in range(9):
                if(grid[row][i] == num):
                    return True
            return False


        def used_col(grid,col,num):
            for i in range(9):
                if(grid[i][col] == num):
                    return True
            return False



        def used_box(grid,row,col,num):
            for i in range(3):
                for j in range(3):
                    if(grid[i+row][j+col] == num):
                        return True
            return False



        def location_safe(grid,row,col,num):
            return not used_row(grid,row,num) and not used_col(grid,col,num) and not used_box(grid,row - row%3,col - col%3,num)


        def solve_sudoku(grid):
            #print("d",d)
            empty=[0,0]
            if(not find_empty(grid,empty)):
                return True
            row=empty[0]
            col=empty[1]


            if time.time()>(starttime+3):
                #uuu+=1
                return False
            for num in d[(row,col)]:
                if(location_safe(grid,row,col,num)):
                    grid[row][col]=num

                    if(solve_sudoku(grid)):
                        return True

                    grid[row][col] = 0



            #print_sudoku(l)


            return False

        d_creation(grid)



        # if success print the grid

        if(solve_sudoku(grid))==True:


            #print_sudoku(grid)
            #print(" The time elapsed is :",(time.time()-start_time))
            #print("\n")
            print("I am returning the grid and it ids",grid)
            return grid
        else:
            #print ("No solution exists")
            return False


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
        entry17.destroy()
        entry18.destroy()
        entry19.destroy()
        entry20.destroy()
        entry21.destroy()
        entry22.destroy()
        entry23.destroy()
        entry24.destroy()
        entry25.destroy()
        entry26.destroy()
        entry27.destroy()
        entry28.destroy()
        entry29.destroy()
        entry30.destroy()
        entry31.destroy()
        entry32.destroy()
        entry33.destroy()
        entry34.destroy()
        entry35.destroy()
        entry36.destroy()
        entry37.destroy()
        entry38.destroy()
        entry39.destroy()
        entry40.destroy()
        entry41.destroy()
        entry42.destroy()
        entry43.destroy()
        entry44.destroy()
        entry45.destroy()
        entry46.destroy()
        entry47.destroy()
        entry48.destroy()
        entry49.destroy()
        entry50.destroy()
        entry51.destroy()
        entry52.destroy()
        entry53.destroy()
        entry54.destroy()
        entry55.destroy()
        entry56.destroy()
        entry57.destroy()
        entry58.destroy()
        entry59.destroy()
        entry60.destroy()
        entry61.destroy()
        entry62.destroy()
        entry63.destroy()
        entry64.destroy()
        entry65.destroy()
        entry66.destroy()
        entry67.destroy()
        entry68.destroy()
        entry69.destroy()
        entry70.destroy()
        entry71.destroy()
        entry72.destroy()
        entry73.destroy()
        entry74.destroy()
        entry75.destroy()
        entry76.destroy()
        entry77.destroy()
        entry78.destroy()
        entry79.destroy()
        entry80.destroy()
        entry81.destroy()

        root.clipboard_clear()
        print("Clip board cleared")
        global reset_btn
        reset_btn=tkinter.Button(canvas,text="Reset",font=("Times",30),bg="SteelBlue1",fg="Black",command=reset,state=tkinter.DISABLED).place(x=900,y=230)
        print("Entering reset")
        show_all()






    def only_num(e):
        if e.isdigit() and e=='0':
            return False
        elif e.isdigit() and len(e)==1:
            return True
        elif e=="":
            return True
        else:
            return False

    def all_null(l):
        count=0
        for i in l:
            for j in i:
                if j==0:
                    count+=1
        if count==81:
            return False
        else:
            return True

    def all_full(l):
        count=0
        k=[1,2,3,4,5,6,7,8,9]
        for i in l:
            for j in i:
                if j in k:
                    count+=1
        if count==81:
            return False
        else:
            return True


    def print_solved(l):

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
        entry17.destroy()
        entry18.destroy()
        entry19.destroy()
        entry20.destroy()
        entry21.destroy()
        entry22.destroy()
        entry23.destroy()
        entry24.destroy()
        entry25.destroy()
        entry26.destroy()
        entry27.destroy()
        entry28.destroy()
        entry29.destroy()
        entry30.destroy()
        entry31.destroy()
        entry32.destroy()
        entry33.destroy()
        entry34.destroy()
        entry35.destroy()
        entry36.destroy()
        entry37.destroy()
        entry38.destroy()
        entry39.destroy()
        entry40.destroy()
        entry41.destroy()
        entry42.destroy()
        entry43.destroy()
        entry44.destroy()
        entry45.destroy()
        entry46.destroy()
        entry47.destroy()
        entry48.destroy()
        entry49.destroy()
        entry50.destroy()
        entry51.destroy()
        entry52.destroy()
        entry53.destroy()
        entry54.destroy()
        entry55.destroy()
        entry56.destroy()
        entry57.destroy()
        entry58.destroy()
        entry59.destroy()
        entry60.destroy()
        entry61.destroy()
        entry62.destroy()
        entry63.destroy()
        entry64.destroy()
        entry65.destroy()
        entry66.destroy()
        entry67.destroy()
        entry68.destroy()
        entry69.destroy()
        entry70.destroy()
        entry71.destroy()
        entry72.destroy()
        entry73.destroy()
        entry74.destroy()
        entry75.destroy()
        entry76.destroy()
        entry77.destroy()
        entry78.destroy()
        entry79.destroy()
        entry80.destroy()
        entry81.destroy()


        output1=tkinter.Label(canvas,text=str(l[0][0]),font=('Helvetica',30),bg='white')
        output1.place(x=363,y=104)

        output2=tkinter.Label(canvas,text=str(l[0][1]),font=('Helvetica',30),bg='white')
        output2.place(x=418,y=104)

        output3=tkinter.Label(canvas,text=str(l[0][2]),font=('Helvetica',30),bg='white')
        output3.place(x=473,y=104)

        output4=tkinter.Label(canvas,text=str(l[0][3]),font=('Helvetica',30),bg='white')
        output4.place(x=528,y=104)

        output5=tkinter.Label(canvas,text=str(l[0][4]),font=('Helvetica',30),bg='white')
        output5.place(x=583,y=104)

        output6=tkinter.Label(canvas,text=str(l[0][5]),font=('Helvetica',30),bg='white')
        output6.place(x=638,y=104)

        output7=tkinter.Label(canvas,text=str(l[0][6]),font=('Helvetica',30),bg='white')
        output7.place(x=693,y=104)

        output8=tkinter.Label(canvas,text=str(l[0][7]),font=('Helvetica',30),bg='white')
        output8.place(x=748,y=104)

        output9=tkinter.Label(canvas,text=str(l[0][8]),font=('Helvetica',30),bg='white')
        output9.place(x=803,y=104)

        output10=tkinter.Label(canvas,text=str(l[1][0]),font=('Helvetica',30),bg='white')
        output10.place(x=363,y=157)

        output11=tkinter.Label(canvas,text=str(l[1][1]),font=('Helvetica',30),bg='white')
        output11.place(x=418,y=157)

        output12=tkinter.Label(canvas,text=str(l[1][2]),font=('Helvetica',30),bg='white')
        output12.place(x=473,y=157)

        output13=tkinter.Label(canvas,text=str(l[1][3]),font=('Helvetica',30),bg='white')
        output13.place(x=528,y=157)

        output14=tkinter.Label(canvas,text=str(l[1][4]),font=('Helvetica',30),bg='white')
        output14.place(x=583,y=157)

        output15=tkinter.Label(canvas,text=str(l[1][5]),font=('Helvetica',30),bg='white')
        output15.place(x=638,y=157)

        output16=tkinter.Label(canvas,text=str(l[1][6]),font=('Helvetica',30),bg='white')
        output16.place(x=693,y=157)

        output17=tkinter.Label(canvas,text=str(l[1][7]),font=('Helvetica',30),bg='white')
        output17.place(x=748,y=157)

        output18=tkinter.Label(canvas,text=str(l[1][8]),font=('Helvetica',30),bg='white')
        output18.place(x=803,y=157)

        output19=tkinter.Label(canvas,text=str(l[2][0]),font=('Helvetica',30),bg='white')
        output19.place(x=363,y=212)

        output20=tkinter.Label(canvas,text=str(l[2][1]),font=('Helvetica',30),bg='white')
        output20.place(x=418,y=212)

        output21=tkinter.Label(canvas,text=str(l[2][2]),font=('Helvetica',30),bg='white')
        output21.place(x=473,y=212)

        output22=tkinter.Label(canvas,text=str(l[2][3]),font=('Helvetica',30),bg='white')
        output22.place(x=528,y=212)

        output23=tkinter.Label(canvas,text=str(l[2][4]),font=('Helvetica',30),bg='white')
        output23.place(x=583,y=212)

        output24=tkinter.Label(canvas,text=str(l[2][5]),font=('Helvetica',30),bg='white')
        output24.place(x=638,y=212)

        output25=tkinter.Label(canvas,text=str(l[2][6]),font=('Helvetica',30),bg='white')
        output25.place(x=693,y=212)

        output26=tkinter.Label(canvas,text=str(l[2][7]),font=('Helvetica',30),bg='white')
        output26.place(x=748,y=212)

        output27=tkinter.Label(canvas,text=str(l[2][8]),font=('Helvetica',30),bg='white')
        output27.place(x=803,y=212)

        output28=tkinter.Label(canvas,text=str(l[3][0]),font=('Helvetica',30),bg='white')
        output28.place(x=363,y=270)

        output29=tkinter.Label(canvas,text=str(l[3][1]),font=('Helvetica',30),bg='white')
        output29.place(x=418,y=270)

        output30=tkinter.Label(canvas,text=str(l[3][2]),font=('Helvetica',30),bg='white')
        output30.place(x=473,y=270)

        output31=tkinter.Label(canvas,text=str(l[3][3]),font=('Helvetica',30),bg='white')
        output31.place(x=528,y=270)

        output32=tkinter.Label(canvas,text=str(l[3][4]),font=('Helvetica',30),bg='white')
        output32.place(x=583,y=270)

        output33=tkinter.Label(canvas,text=str(l[3][5]),font=('Helvetica',30),bg='white')
        output33.place(x=638,y=270)

        output34=tkinter.Label(canvas,text=str(l[3][6]),font=('Helvetica',30),bg='white')
        output34.place(x=693,y=270)

        output35=tkinter.Label(canvas,text=str(l[3][7]),font=('Helvetica',30),bg='white')
        output35.place(x=748,y=270)

        output36=tkinter.Label(canvas,text=str(l[3][8]),font=('Helvetica',30),bg='white')
        output36.place(x=803,y=270)

        output37=tkinter.Label(canvas,text=str(l[4][0]),font=('Helvetica',30),bg='white')
        output37.place(x=363,y=323)

        output38=tkinter.Label(canvas,text=str(l[4][1]),font=('Helvetica',30),bg='white')
        output38.place(x=418,y=323)

        output39=tkinter.Label(canvas,text=str(l[4][2]),font=('Helvetica',30),bg='white')
        output39.place(x=473,y=323)

        output40=tkinter.Label(canvas,text=str(l[4][3]),font=('Helvetica',30),bg='white')
        output40.place(x=528,y=323)

        output41=tkinter.Label(canvas,text=str(l[4][4]),font=('Helvetica',30),bg='white')
        output41.place(x=583,y=323)

        output42=tkinter.Label(canvas,text=str(l[4][5]),font=('Helvetica',30),bg='white')
        output42.place(x=638,y=323)

        output43=tkinter.Label(canvas,text=str(l[4][6]),font=('Helvetica',30),bg='white')
        output43.place(x=693,y=323)

        output44=tkinter.Label(canvas,text=str(l[4][7]),font=('Helvetica',30),bg='white')
        output44.place(x=748,y=323)

        output45=tkinter.Label(canvas,text=str(l[4][8]),font=('Helvetica',30),bg='white')
        output45.place(x=803,y=323)

        output46=tkinter.Label(canvas,text=str(l[5][0]),font=('Helvetica',30),bg='white')
        output46.place(x=363,y=378)

        output47=tkinter.Label(canvas,text=str(l[5][1]),font=('Helvetica',30),bg='white')
        output47.place(x=418,y=378)

        output48=tkinter.Label(canvas,text=str(l[5][2]),font=('Helvetica',30),bg='white')
        output48.place(x=473,y=378)

        output49=tkinter.Label(canvas,text=str(l[5][3]),font=('Helvetica',30),bg='white')
        output49.place(x=528,y=378)

        output50=tkinter.Label(canvas,text=str(l[5][4]),font=('Helvetica',30),bg='white')
        output50.place(x=583,y=378)

        output51=tkinter.Label(canvas,text=str(l[5][5]),font=('Helvetica',30),bg='white')
        output51.place(x=638,y=378)

        output52=tkinter.Label(canvas,text=str(l[5][6]),font=('Helvetica',30),bg='white')
        output52.place(x=693,y=378)

        output53=tkinter.Label(canvas,text=str(l[5][7]),font=('Helvetica',30),bg='white')
        output53.place(x=748,y=378)

        output54=tkinter.Label(canvas,text=str(l[5][8]),font=('Helvetica',30),bg='white')
        output54.place(x=803,y=378)

        output55=tkinter.Label(canvas,text=str(l[6][0]),font=('Helvetica',30),bg='white')
        output55.place(x=363,y=436)

        output56=tkinter.Label(canvas,text=str(l[6][1]),font=('Helvetica',30),bg='white')
        output56.place(x=418,y=436)

        output57=tkinter.Label(canvas,text=str(l[6][2]),font=('Helvetica',30),bg='white')
        output57.place(x=473,y=436)

        output58=tkinter.Label(canvas,text=str(l[6][3]),font=('Helvetica',30),bg='white')
        output58.place(x=528,y=436)

        output59=tkinter.Label(canvas,text=str(l[6][4]),font=('Helvetica',30),bg='white')
        output59.place(x=583,y=436)

        output60=tkinter.Label(canvas,text=str(l[6][5]),font=('Helvetica',30),bg='white')
        output60.place(x=638,y=436)

        output61=tkinter.Label(canvas,text=str(l[6][6]),font=('Helvetica',30),bg='white')
        output61.place(x=693,y=436)

        output62=tkinter.Label(canvas,text=str(l[6][7]),font=('Helvetica',30),bg='white')
        output62.place(x=748,y=436)

        output63=tkinter.Label(canvas,text=str(l[6][8]),font=('Helvetica',30),bg='white')
        output63.place(x=803,y=436)

        output64=tkinter.Label(canvas,text=str(l[7][0]),font=('Helvetica',30),bg='white')
        output64.place(x=363,y=491)

        output65=tkinter.Label(canvas,text=str(l[7][1]),font=('Helvetica',30),bg='white')
        output65.place(x=418,y=491)

        output66=tkinter.Label(canvas,text=str(l[7][2]),font=('Helvetica',30),bg='white')
        output66.place(x=473,y=491)

        output67=tkinter.Label(canvas,text=str(l[7][3]),font=('Helvetica',30),bg='white')
        output67.place(x=528,y=491)

        output68=tkinter.Label(canvas,text=str(l[7][4]),font=('Helvetica',30),bg='white')
        output68.place(x=583,y=491)

        output69=tkinter.Label(canvas,text=str(l[7][5]),font=('Helvetica',30),bg='white')
        output69.place(x=638,y=491)

        output70=tkinter.Label(canvas,text=str(l[7][6]),font=('Helvetica',30),bg='white')
        output70.place(x=693,y=491)

        output71=tkinter.Label(canvas,text=str(l[7][7]),font=('Helvetica',30),bg='white')
        output71.place(x=748,y=491)

        output72=tkinter.Label(canvas,text=str(l[7][8]),font=('Helvetica',30),bg='white')
        output72.place(x=803,y=491)

        output73=tkinter.Label(canvas,text=str(l[8][0]),font=('Helvetica',30),bg='white')
        output73.place(x=363,y=545)

        output74=tkinter.Label(canvas,text=str(l[8][1]),font=('Helvetica',30),bg='white')
        output74.place(x=418,y=545)

        output75=tkinter.Label(canvas,text=str(l[8][2]),font=('Helvetica',30),bg='white')
        output75.place(x=473,y=545)

        output76=tkinter.Label(canvas,text=str(l[8][3]),font=('Helvetica',30),bg='white')
        output76.place(x=528,y=545)

        output77=tkinter.Label(canvas,text=str(l[8][4]),font=('Helvetica',30),bg='white')
        output77.place(x=583,y=545)

        output78=tkinter.Label(canvas,text=str(l[8][5]),font=('Helvetica',30),bg='white')
        output78.place(x=638,y=545)

        output79=tkinter.Label(canvas,text=str(l[8][6]),font=('Helvetica',30),bg='white')
        output79.place(x=693,y=545)

        output80=tkinter.Label(canvas,text=str(l[8][7]),font=('Helvetica',30),bg='white')
        output80.place(x=748,y=545)

        output81=tkinter.Label(canvas,text=str(l[8][8]),font=('Helvetica',30),bg='white')
        output81.place(x=803,y=545)

        messagebox.showinfo("Solver","The sudoku is solved!!",parent=root)
        global reset_btn
        reset_btn=tkinter.Button(canvas,text="Reset",font=("Times",30),bg="SteelBlue1",fg="Black",command=reset,state=tkinter.NORMAL).place(x=900,y=230)



    def show_all():
        def entry():

            if entry1.get()=='':
                input1=0
            else:
                input1=int(entry1.get())


            if entry2.get()=='':
                input2=0
            else:
                input2=int(entry2.get())


            if entry3.get()=='':

                input3=0
            else:
                input3=int(entry3.get())


            if entry4.get()=='':

                input4=0
            else:
                input4=int(entry4.get())


            if entry5.get()=='':

                input5=0
            else:
                input5=int(entry5.get())


            if entry6.get()=='':

                input6=0
            else:
                input6=int(entry6.get())


            if entry7.get()=='':

                input7=0
            else:
                input7=int(entry7.get())


            if entry8.get()=='':

                input8=0
            else:
                input8=int(entry8.get())


            if entry9.get()=='':

                input9=0
            else:
                input9=int(entry9.get())


            if entry10.get()=='':

                input10=0
            else:
                input10=int(entry10.get())


            if entry11.get()=='':

                input11=0
            else:
                input11=int(entry11.get())


            if entry12.get()=='':

                input12=0
            else:
                input12=int(entry12.get())


            if entry13.get()=='':

                input13=0
            else:
                input13=int(entry13.get())


            if entry14.get()=='':

                input14=0
            else:
                input14=int(entry14.get())


            if entry15.get()=='':

                input15=0
            else:
                input15=int(entry15.get())


            if entry16.get()=='':

                input16=0
            else:
                input16=int(entry16.get())


            if entry17.get()=='':

                input17=0
            else:
                input17=int(entry17.get())


            if entry18.get()=='':

                input18=0
            else:
                input18=int(entry18.get())


            if entry19.get()=='':

                input19=0
            else:
                input19=int(entry19.get())


            if entry20.get()=='':

                input20=0
            else:
                input20=int(entry20.get())


            if entry21.get()=='':

                input21=0
            else:
                input21=int(entry21.get())


            if entry22.get()=='':

                input22=0
            else:
                input22=int(entry22.get())


            if entry23.get()=='':

                input23=0
            else:
                input23=int(entry23.get())


            if entry24.get()=='':

                input24=0
            else:
                input24=int(entry24.get())


            if entry25.get()=='':

                input25=0
            else:
                input25=int(entry25.get())


            if entry26.get()=='':

                input26=0
            else:
                input26=int(entry26.get())


            if entry27.get()=='':

                input27=0
            else:
                input27=int(entry27.get())


            if entry28.get()=='':

                input28=0
            else:
                input28=int(entry28.get())


            if entry29.get()=='':

                input29=0
            else:
                input29=int(entry29.get())


            if entry30.get()=='':

                input30=0
            else:
                input30=int(entry30.get())


            if entry31.get()=='':

                input31=0
            else:
                input31=int(entry31.get())


            if entry32.get()=='':

                input32=0
            else:
                input32=int(entry32.get())


            if entry33.get()=='':

                input33=0
            else:
                input33=int(entry33.get())


            if entry34.get()=='':

                input34=0
            else:
                input34=int(entry34.get())


            if entry35.get()=='':

                input35=0
            else:
                input35=int(entry35.get())


            if entry36.get()=='':

                input36=0
            else:
                input36=int(entry36.get())


            if entry37.get()=='':

                input37=0
            else:
                input37=int(entry37.get())


            if entry38.get()=='':

                input38=0
            else:
                input38=int(entry38.get())


            if entry39.get()=='':

                input39=0
            else:
                input39=int(entry39.get())


            if entry40.get()=='':

                input40=0
            else:
                input40=int(entry40.get())


            if entry41.get()=='':

                input41=0
            else:
                input41=int(entry41.get())


            if entry42.get()=='':

                input42=0
            else:
                input42=int(entry42.get())


            if entry43.get()=='':

                input43=0
            else:
                input43=int(entry43.get())


            if entry44.get()=='':

                input44=0
            else:
                input44=int(entry44.get())


            if entry45.get()=='':

                input45=0
            else:
                input45=int(entry45.get())


            if entry46.get()=='':

                input46=0
            else:
                input46=int(entry46.get())


            if entry47.get()=='':

                input47=0
            else:
                input47=int(entry47.get())


            if entry48.get()=='':

                input48=0
            else:
                input48=int(entry48.get())


            if entry49.get()=='':

                input49=0
            else:
                input49=int(entry49.get())


            if entry50.get()=='':

                input50=0
            else:
                input50=int(entry50.get())


            if entry51.get()=='':

                input51=0
            else:
                input51=int(entry51.get())


            if entry52.get()=='':

                input52=0
            else:
                input52=int(entry52.get())


            if entry53.get()=='':

                input53=0
            else:
                input53=int(entry53.get())


            if entry54.get()=='':

                input54=0
            else:
                input54=int(entry54.get())


            if entry55.get()=='':

                input55=0
            else:
                input55=int(entry55.get())


            if entry56.get()=='':

                input56=0
            else:
                input56=int(entry56.get())


            if entry57.get()=='':

                input57=0
            else:
                input57=int(entry57.get())


            if entry58.get()=='':

                input58=0
            else:
                input58=int(entry58.get())


            if entry59.get()=='':

                input59=0
            else:
                input59=int(entry59.get())


            if entry60.get()=='':

                input60=0
            else:
                input60=int(entry60.get())


            if entry61.get()=='':

                input61=0
            else:
                input61=int(entry61.get())


            if entry62.get()=='':

                input62=0
            else:
                input62=int(entry62.get())


            if entry63.get()=='':

                input63=0
            else:
                input63=int(entry63.get())


            if entry64.get()=='':

                input64=0
            else:
                input64=int(entry64.get())


            if entry65.get()=='':

                input65=0
            else:
                input65=int(entry65.get())


            if entry66.get()=='':

                input66=0
            else:
                input66=int(entry66.get())


            if entry67.get()=='':

                input67=0
            else:
                input67=int(entry67.get())


            if entry68.get()=='':

                input68=0
            else:
                input68=int(entry68.get())


            if entry69.get()=='':

                input69=0
            else:
                input69=int(entry69.get())


            if entry70.get()=='':

                input70=0
            else:
                input70=int(entry70.get())


            if entry71.get()=='':

                input71=0
            else:
                input71=int(entry71.get())


            if entry72.get()=='':

                input72=0
            else:
                input72=int(entry72.get())


            if entry73.get()=='':

                input73=0
            else:
                input73=int(entry73.get())


            if entry74.get()=='':

                input74=0
            else:
                input74=int(entry74.get())


            if entry75.get()=='':

                input75=0
            else:
                input75=int(entry75.get())


            if entry76.get()=='':

                input76=0
            else:
                input76=int(entry76.get())


            if entry77.get()=='':

                input77=0
            else:
                input77=int(entry77.get())


            if entry78.get()=='':

                input78=0
            else:
                input78=int(entry78.get())


            if entry79.get()=='':

                input79=0
            else:
                input79=int(entry79.get())


            if entry80.get()=='':

                input80=0
            else:
                input80=int(entry80.get())


            if entry81.get()=='':

                input81=0
            else:
                input81=int(entry81.get())


            global grid ###

            grid=[[input1,input2,input3,input4,input5,input6,input7,input8,input9],
               [input10,input11,input12,input13,input14,input15,input16,input17,input18],
               [input19,input20,input21,input22,input23,input24,input25,input26,input27],
               [input28,input29,input30,input31,input32,input33,input34,input35,input36],
               [input37,input38,input39,input40,input41,input42,input43,input44,input45],
               [input46,input47,input48,input49,input50,input51,input52,input53,input54],
               [input55,input56,input57,input58,input59,input60,input61,input62,input63],
               [input64,input65,input66,input67,input68,input69,input70,input71,input72],
               [input73,input74,input75,input76,input77,input78,input79,input80,input81]]

            if all_null(grid)==False:
                messagebox.showerror("Error","No number has been given in the sudoku.",parent=root)
            else:
                x=(runtime(grid))
                if x==False:
                    messagebox.showerror("Error","Sudoku not solvable",parent=root)
                    global reset_btn
                    reset_btn=tkinter.Button(canvas,text="Reset",font=("Times",30),bg="SteelBlue1",fg="Black",command=reset,state=tkinter.NORMAL).place(x=900,y=230)

                else:
                    print_solved(grid)





        c=root.register(only_num)

        global entry1
        entry1 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify='center')
        canvas.create_window(378, 130, window=entry1)
        entry1.config(validate="key", validatecommand=(c,'%P'))

        global entry2
        entry2 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(432, 130, window=entry2)
        entry2.config(validate="key", validatecommand=(c,'%P'))

        global entry3
        entry3 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(486, 130, window=entry3)
        entry3.config(validate="key", validatecommand=(c,'%P'))

        global entry4
        entry4 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(544, 130, window=entry4)
        entry4.config(validate="key", validatecommand=(c,'%P'))

        global entry5
        entry5 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(598, 130, window=entry5)
        entry5.config(validate="key", validatecommand=(c,'%P'))

        global entry6
        entry6 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(652, 130, window=entry6)
        entry6.config(validate="key", validatecommand=(c,'%P'))

        global entry7
        entry7 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(712, 130, window=entry7)
        entry7.config(validate="key", validatecommand=(c,'%P'))

        global entry8
        entry8 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(766, 130, window=entry8)
        entry8.config(validate="key", validatecommand=(c,'%P'))

        global entry9
        entry9 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(820, 130, window=entry9)
        entry9.config(validate="key", validatecommand=(c,'%P'))

        #INPUT_ROW 2

        global entry10
        entry10 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(378, 185, window=entry10)#
        entry10.config(validate="key", validatecommand=(c,'%P'))

        global entry11
        entry11= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(432, 185, window=entry11)
        entry11.config(validate="key", validatecommand=(c,'%P'))

        global entry12
        entry12= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(486, 185, window=entry12)
        entry12.config(validate="key", validatecommand=(c,'%P'))

        global entry13
        entry13= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(544, 185, window=entry13)
        entry13.config(validate="key", validatecommand=(c,'%P'))

        global entry14
        entry14= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(598, 185, window=entry14)
        entry14.config(validate="key", validatecommand=(c,'%P'))

        global entry15
        entry15= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(652, 185, window=entry15)
        entry15.config(validate="key", validatecommand=(c,'%P'))

        global entry16
        entry16= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(712, 185, window=entry16)
        entry16.config(validate="key", validatecommand=(c,'%P'))

        global entry17
        entry17= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(766, 185, window=entry17)
        entry17.config(validate="key", validatecommand=(c,'%P'))

        global entry18
        entry18= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(820, 185, window=entry18)
        entry18.config(validate="key", validatecommand=(c,'%P'))

        #INPUT_ROW 3

        global entry19
        entry19 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(378, 240, window=entry19)
        entry19.config(validate="key", validatecommand=(c,'%P'))

        global entry20
        entry20= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(432, 240, window=entry20)
        entry20.config(validate="key", validatecommand=(c,'%P'))

        global entry21
        entry21= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(486, 240, window=entry21)
        entry21.config(validate="key", validatecommand=(c,'%P'))

        global entry22
        entry22= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(544, 240, window=entry22)
        entry22.config(validate="key", validatecommand=(c,'%P'))

        global entry23
        entry23= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(598, 240, window=entry23)
        entry23.config(validate="key", validatecommand=(c,'%P'))

        global entry24
        entry24= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(652, 240, window=entry24)
        entry24.config(validate="key", validatecommand=(c,'%P'))

        global entry25
        entry25= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(712, 240, window=entry25)
        entry25.config(validate="key", validatecommand=(c,'%P'))

        global entry26
        entry26= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(766, 240, window=entry26)
        entry26.config(validate="key", validatecommand=(c,'%P'))

        global entry27
        entry27= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(820, 240, window=entry27)
        entry27.config(validate="key", validatecommand=(c,'%P'))

        #INPUT_ROW 4

        global entry28
        entry28 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(378, 295, window=entry28)
        entry28.config(validate="key", validatecommand=(c,'%P'))

        global entry29
        entry29= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(432, 295, window=entry29)
        entry29.config(validate="key", validatecommand=(c,'%P'))

        global entry30
        entry30= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(486, 295, window=entry30)
        entry30.config(validate="key", validatecommand=(c,'%P'))

        global entry31
        entry31= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(544, 295, window=entry31)
        entry31.config(validate="key", validatecommand=(c,'%P'))

        global entry32
        entry32= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(598, 295, window=entry32)
        entry32.config(validate="key", validatecommand=(c,'%P'))

        global entry33
        entry33= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(652, 295, window=entry33)
        entry33.config(validate="key", validatecommand=(c,'%P'))

        global entry34
        entry34= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(712, 295, window=entry34)
        entry34.config(validate="key", validatecommand=(c,'%P'))

        global entry35
        entry35= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(766, 295, window=entry35)
        entry35.config(validate="key", validatecommand=(c,'%P'))

        global entry36
        entry36= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(820, 295, window=entry36)
        entry36.config(validate="key", validatecommand=(c,'%P'))

        #INPUT_ROW 5
        global entry37
        entry37 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(378, 350, window=entry37)
        entry37.config(validate="key", validatecommand=(c,'%P'))

        global entry38
        entry38= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(432, 350, window=entry38)
        entry38.config(validate="key", validatecommand=(c,'%P'))

        global entry39
        entry39= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(486,350, window=entry39)
        entry39.config(validate="key", validatecommand=(c,'%P'))

        global entry40
        entry40= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(544, 350, window=entry40)
        entry40.config(validate="key", validatecommand=(c,'%P'))

        global entry41
        entry41= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(598, 350, window=entry41)
        entry41.config(validate="key", validatecommand=(c,'%P'))

        global entry42
        entry42= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(652, 350, window=entry42)
        entry42.config(validate="key", validatecommand=(c,'%P'))

        global entry43
        entry43= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(712, 350, window=entry43)
        entry43.config(validate="key", validatecommand=(c,'%P'))

        global entry44
        entry44= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(766, 350, window=entry44)
        entry44.config(validate="key", validatecommand=(c,'%P'))

        global entry45
        entry45= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(820, 350, window=entry45)
        entry45.config(validate="key", validatecommand=(c,'%P'))

        #INPUT_ROW 6
        global entry46
        entry46 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(378, 405, window=entry46)
        entry46.config(validate="key", validatecommand=(c,'%P'))

        global entry47
        entry47= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(432, 405, window=entry47)
        entry47.config(validate="key", validatecommand=(c,'%P'))

        global entry48
        entry48= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(486, 405, window=entry48)
        entry48.config(validate="key", validatecommand=(c,'%P'))

        global entry49
        entry49= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(544, 405, window=entry49)
        entry49.config(validate="key", validatecommand=(c,'%P'))

        global entry50
        entry50= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(598, 405, window=entry50)
        entry50.config(validate="key", validatecommand=(c,'%P'))

        global entry51
        entry51= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(652, 405, window=entry51)
        entry51.config(validate="key", validatecommand=(c,'%P'))

        global entry52
        entry52= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(712, 405, window=entry52)
        entry52.config(validate="key", validatecommand=(c,'%P'))

        global entry53
        entry53= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(766, 405, window=entry53)
        entry53.config(validate="key", validatecommand=(c,'%P'))

        global entry54
        entry54= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(820, 405, window=entry54)
        entry54.config(validate="key", validatecommand=(c,'%P'))

        #INPUT_ROW 7

        global entry55
        entry55 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(378, 460, window=entry55)
        entry55.config(validate="key", validatecommand=(c,'%P'))

        global entry56
        entry56= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(432, 460, window=entry56)
        entry56.config(validate="key", validatecommand=(c,'%P'))

        global entry57
        entry57= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(486, 460, window=entry57)
        entry57.config(validate="key", validatecommand=(c,'%P'))

        global entry58
        entry58= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(544, 460, window=entry58)
        entry58.config(validate="key", validatecommand=(c,'%P'))

        global entry59
        entry59= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(598, 460, window=entry59)
        entry59.config(validate="key", validatecommand=(c,'%P'))

        global entry60
        entry60= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(652, 460, window=entry60)
        entry60.config(validate="key", validatecommand=(c,'%P'))

        global entry61
        entry61= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(712, 460, window=entry61)
        entry61.config(validate="key", validatecommand=(c,'%P'))

        global entry62
        entry62= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(766, 460, window=entry62)
        entry62.config(validate="key", validatecommand=(c,'%P'))

        global entry63
        entry63= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(820, 460, window=entry63)
        entry63.config(validate="key", validatecommand=(c,'%P'))

        #INPUT_ROW 8
        global entry64
        entry64 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(378, 515, window=entry64)
        entry64.config(validate="key", validatecommand=(c,'%P'))

        global entry65
        entry65= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(432, 515, window=entry65)
        entry65.config(validate="key", validatecommand=(c,'%P'))

        global entry66
        entry66= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(486, 515, window=entry66)
        entry66.config(validate="key", validatecommand=(c,'%P'))

        global entry67
        entry67= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(544, 515, window=entry67)
        entry67.config(validate="key", validatecommand=(c,'%P'))

        global entry68
        entry68= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(598, 515, window=entry68)
        entry68.config(validate="key", validatecommand=(c,'%P'))

        global entry69
        entry69= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(652, 515, window=entry69)
        entry69.config(validate="key", validatecommand=(c,'%P'))

        global entry70
        entry70= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(712, 515, window=entry70)
        entry70.config(validate="key", validatecommand=(c,'%P'))

        global entry71
        entry71= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(766, 515, window=entry71)
        entry71.config(validate="key", validatecommand=(c,'%P'))

        global entry72
        entry72= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(820, 515, window=entry72)
        entry72.config(validate="key", validatecommand=(c,'%P'))

        #INPUT_ROW 9
        global entry73
        entry73 = tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(378, 570, window=entry73)
        entry73.config(validate="key", validatecommand=(c,'%P'))

        global entry74
        entry74= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(432, 570, window=entry74)
        entry74.config(validate="key", validatecommand=(c,'%P'))

        global entry75
        entry75= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(486, 570, window=entry75)
        entry75.config(validate="key", validatecommand=(c,'%P'))

        global entry76
        entry76= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(544, 570, window=entry76)
        entry76.config(validate="key", validatecommand=(c,'%P'))

        global entry77
        entry77= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(598, 570, window=entry77)
        entry77.config(validate="key", validatecommand=(c,'%P'))

        global entry78
        entry78= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(652, 570, window=entry78)
        entry78.config(validate="key", validatecommand=(c,'%P'))

        global entry79
        entry79= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(712, 570, window=entry79)
        entry79.config(validate="key", validatecommand=(c,'%P'))

        global entry80
        entry80= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(766, 570, window=entry80)
        entry80.config(validate="key", validatecommand=(c,'%P'))

        global entry81
        entry81= tkinter.Entry (root, width=3,font=("Helvetica", 20),justify="center")
        canvas.create_window(820, 570, window=entry81)
        entry81.config(validate="key", validatecommand=(c,'%P'))

        solve_btn=tkinter.Button(canvas,text="Solve",font=("Times",30),bg="SteelBlue1",fg="Black",command=entry).place(x=900,y=350)





    img=ImageTk.PhotoImage(Image.open(r".\9x9 grid.png"),master=root)
    canvas.create_image(600,350,anchor="center",image=img)



    grid=[]

    show_all()

    head_label=tkinter.Label(canvas,text="Welcome to 9x9 solver",font=("Times",60),fg="Black",bg="SteelBlue2").place(x=210,y=0)

    global reset_btn
    reset_btn=tkinter.Button(canvas,text="Reset",font=("Times",30),bg="gray50",command=reset,state=tkinter.DISABLED).place(x=900,y=230)

    #head_instr=tkinter.Label(canvas,text="Instructions :",font=("Times",25),bg="SteelBlue2",fg="black").place(x=60,y=560)
    #instr1=tkinter.Label(canvas,text="Please enter numbers between 1 and 9 only.",font=("Times",25)).place(x=100,y=610)
    #instr2=tkinter.Label(canvas,text="To view the solution, click the solve button.",font=("Times",25)).place(x=100,y=650)
    #instr3=tkinter.Label(canvas,text="To clear all numbers in the sudoku, click the reset button.",font=("Times",25)).place(x=100,y=690)

    close_btn=tkinter.Button(canvas,text="Close",font=("Times",20),bg="gray50",command=root.destroy).place(x=1200,y=0)
    root.mainloop()

#ninenine()

