# -*- coding: utf-8 -*-
# fix all issues with load_previous, need to store previous time, level and hints taken
import original_control_room
import os.path
from os import path
import os
from tkinter import *
from tkinter import messagebox
import random
import copy

from user import user

def check_IsAnySaved(CurrentUserObject):
    
    file_name = str(CurrentUserObject.name) + ".csv"      # Name of the peron is the name of the csv file
        
    if path.exists(file_name):
        return( True )
    else:
        return( False )
    
    
def solve_previous(CurrentUserObject):
    
    arr = CurrentUserObject.get_csv()
    
    l = copy.deepcopy(arr)
    
    for lis in l:
        for i in range (len(lis)):
            lis[i] = int(lis[i])
            
    print("l   : ",l)
    
    copy_l = list ( CurrentUserObject.get_fullSolved() )
    
    for lis in copy_l:
        for i in range (len(lis)):
            lis[i] = int(lis[i])
            
    print()
    print("copy_l : ",copy_l)
    
    # removing empty lists in l and copy_l :
    
    for i in range (len(l)-1,-1,-1):
        if len(l[i]) == 0:
            del l[i]
            
    for i in range (len(copy_l)-1,-1,-1):
        if len(copy_l[i]) == 0:
            del copy_l[i]
            
    
    def GenerateSudokuToSolve(CurrentUserObject, l, copy_l): 
    #######################################################################    
    
        
        global root #,copy_l # ,l
        
        print("recheceking l : ", l)
        
        root = Tk()
        root.geometry("1350x800")
        root.configure(height=500,width=500,bg="blue2",padx=390,pady=120)
        root.attributes('-fullscreen',True)
    ##########################################################################    # copy_l solved sudoku
    ######################################################################3### 
        def click(event):
            global coordinates_of_click,info_l,button_guess_state,button_real_state,main_coors,store_coors
            x = event.x_root - root.winfo_rootx() 
            y = event.y_root - root.winfo_rooty() 
            coordinates_of_click = root.grid_location(x, y) 
            (x,y)=coordinates_of_click
            if button_guess_state:
                if info_l[y][x].get()=='':
                    info_l[y][x].config(fg="Yellow")
                    store_coors.append(coordinates_of_click)
                    main_coors.append(coordinates_of_click)
            if button_real_state:
                info_l[y][x].config(fg="Black")
                main_coors.append(coordinates_of_click)
            
        def disable_buttons(a,b,c,d):
            button_guess['state']=a
            button_real['state']=b
            button_guess_to_real['state']=c
            button_clear_guesses['state']=d
        
        def button_guess_func():
            disable_buttons('disabled','active','active','active')
            global colour,button_guess_state,button_real_state
            button_guess_state=True
            button_real_state=False
            
          
        def button_real_func():
            disable_buttons('active','disabled','active','active')
            global colour,button_real_state,button_guess_state
            button_real_state=True
            button_guess_state=False
            #clear(store_coors)
            
        def button_guess_to_real_func():
            disable_buttons('active','disabled','disabled','active')
            global store_coors,info_l,button_guess_state,button_real_state
            for i in store_coors:
                (c,r)=i
                info_l[r][c].config(fg="Black")
            store_coors=[]
            button_guess_state=False
            button_real_state=True
        
        def clear(lis):
            global store_coors,info_l,button_guess_state,button_real_state,main_coors
            for i in lis:
                (c,r)=i
                info_l[r][c].delete(0,'end')
            #button_clear_guesses['state']='disabled'
            if lis==main_coors:
                store_coors=[]
                main_coors=[]
            else:
                store_coors=[]
        
        def hint():
            global empty_list, state, hints_taken
        
            hints_taken = hints_taken + 1
            
            while len(empty_list)!=0:
                
                hint_pos=random.choice(empty_list)
                info=hint_pos.grid_info()
                (r,c)=(info['row'],info['column'])
                (new_r,new_c)=modify_row_and_col(r,c)
                if info_l[r][c].get()=='':
                    info_l[r][c].destroy()
                    info_l[r][c]=(Label (root,width=2,text=copy_l[new_r][new_c],font=("Helvetica",32),bg="white",fg="Red",padx=1,pady=2))
                    info_l[r][c].grid(row=r,column=c)
                    empty_list.remove(hint_pos)
                    break       
                else:
                    empty_list.remove(hint_pos)
                    
            if len(empty_list)==0:
                button_hint['state']='disabled'
                disable_buttons('disabled','disabled','disabled','disabled')
                button_check['state']='disabled'
                button_clear_all['state']="disabled"
                button_pause['state']='disabled'
                state=False
                #type2=Label(root,text="YOU COULDN'T SOLVE THE SUDOKU",bg="blue2",fg="White",font="Helvetica 30 bold").place(x=-90,y=575)
                process_data()
                preparing_for_exit()
            print(hints_taken)
                    
        def instruction():
            global root
            messagebox.showinfo("Instructions","""
Each box contains 1-9
Each row contains 1-9
Each row contains 1-9
Each digit is unique to a row,column and box.

Points:
For every level, few points are assigned initially:
level 1: 100 points
level 2: 300 points
level 3: 500 points
For every 12 seconds, 1 point is deducted
For every hint taken , 10 points are deducted

Colour coding:
Black - entered digit
Red - Hint
Yellow - guessed digit

*Please note that the entered digits cannot be changed in the loaded sudoku.""",parent=root)
        #refer = hints_taken
            root.lift()
            
        def pause():        
            def play():
                global state,pause_window,init_time
                pause_window.destroy()
                state=True
                time_control(init_time)
            
            global state,pause_window
            state=False
            pause_window=Tk()
            pause_window.configure(height=500,width=500,bg="blue2")
            pause_window.attributes('-fullscreen',True)
            pause_text=Label(pause_window,text="THE GAME IS PAUSED",font=("Helvetica 40 bold"),fg="White",bg="blue2").place(x=400,y=100)
            
            string =return_time(init_time)
            time= Label(pause_window,text="TIME COMPLETED : ",font=("Helvetica",35),fg="White",bg="blue2").place(x=470,y=200)
            curr_time=Label(pause_window,text=string,font=("Helvetica",40),fg="White",bg="medium blue",relief="sunken",bd=5,highlightthickness=5)
            curr_time.place(x=560,y=300)
            play_button=Button(pause_window,command=play,text="Resume",font=('Times',15),width=20,height=3)
            play_button.place(x=560,y=420)
        
        def return_time(time):
            sec=str(time%60).zfill(2)
            temp=time//60
            minute=str(temp%60).zfill(2)
            hour=str(temp//60).zfill(2)
            return (hour+':'+minute+':'+sec)    
        
        def time_control(init_time):
            def timer():
                global state
                if state:
                    global init_time
                    string=return_time(init_time)
                    main_time.config(text=string)
                    init_time+=1
                    main_time.after(1000,timer)
            timer()
            
        def correct (inp):
            if inp.isdigit() and len(str(inp))<2:         
                return True                                
            elif inp =="" and len(str(inp))<2:
                return True
            else:
                return False
        
        reg=root.register(correct)
    ###############################################################################    
        def modify_row_and_col(x,y):
            if x>=1 and x<=3:
                row1=x-1
            elif x>=5 and x<=7:
                row1=x-2
            elif x>=9 and x<=11:
                row1=x-3
           
            if y>=1 and y<=3:
                col1=y-1
            elif y>=5 and y<=7:
                col1=y-2
            elif y>=9 and y<=11:
                col1=y-3
            return row1,col1
        
        def decorate_grid(lis,i,j):
            if i in (0,4,8,12) and j in (0,4,8,12):
                lis[i].append(Label (root,text='',font=("Helvetica",1),bg="Black",fg="Black",justify='center'))
            if i in (0,4,8,12) and j not in (0,4,8,12):
                lis[i].append(Label (root,text='                                                    ',font=("Helvetica", 1),bg="Black",fg="Black",justify='center'))
            if i not in (0,4,8,12) and j in (0,4,8,12):
                lis[i].append(Label (root,text='',font=("Helvetica",35),bg="Black",fg="Black",justify='center'))    
                
    ###################################################################################
        global time_latest
    
        def process_data():
            
            button_check['state']='disabled'
            global state
            state=False
            main_lis=[]
            main_lis,empty_boxes=get_data(info_l)
            check_all_inputs(empty_boxes,main_lis)
        
            
        def get_data(lis):  # gives a list of all generated and user entered values in sudoku
            global info_l  # lis takes vales from the tkinter objects
            count_empty=0
            sub,main=[],[]
            for i in range(13):
                if i not in (0,4,8,12):
                    for j in range(13):
                        if j not in (0,4,8,12):
                            row,col=modify_row_and_col(i,j)
                            if type(info_l[i][j]) == type(demo_entry):
                                curr=info_l[i][j].get()
                                if curr=='':
                                    curr=0
                                    count_empty+=1
                                else:
                                    curr=int(curr)
                            else:
                                curr=copy_l[row][col]
                            sub.append(curr)
                            
                    main.append(sub)
                    sub=[]
    
            return main,count_empty
            
        def check_all_inputs(count,final):
            if count>0:
                global root1
                
                MsgBox = messagebox.askquestion ('Choose option','Number of empty boxes : '+str(count)+'\nDo you want to continue solving ?',icon = 'warning', parent = root)
                if MsgBox == 'yes':
                   yes_button()
                else:
                    no_button()
                    
            
            else:
                #global copy_l
                global init_time,hints_taken
                preparing_for_exit()
                button_clear_all['state']="disabled"
                button_pause['state']='disabled'
                if final==copy_l:
                    button_solution['state']='disabled'
                    type1=Label(root,text="Hurray! YOU SOLVED THE SUDOKU",bg="blue2",fg="White",font="Helvetica 30 bold").place(x=-90,y=575)
                    #--------------- To take all factors and calculate new score and put it into the csv :
                    # CurrentUserObject.calculate_points( level, time )
                    #time_list = time_latest
                    
                    # time in seconds :
                    print(init_time)
                    #seconds_taken = int(time_list[0] + time_list[1]) * 3600 + int(time_list[3] + time_list[4]) * 60 + int(time_list[6] + time_list[7])
                    #print(seconds_taken)
                    print("hints taken : ", hints_taken)
                    
                    #---------------------------------------------------------------------------------
                    
                    # to get the level
                    import csv
                    f=open('points.csv','r')
                    w=csv.reader(f)
                    lis=list(w)
                    #print('lis test :',lis)
                    f.close()
                    
                    #print(lis)
                    
                    for i in lis:
                        if len(i)>0:
                            if i[0] == CurrentUserObject.name :
                                
                                level = i[4]
                                break
                    
                    current_score = int(float(calculate_points(level, init_time, hints_taken)))
                    print("Score achieved now : ", current_score )
                
                    original_control_room.num_score.config(text=original_control_room.points+current_score)
                    CurrentUserObject.calculate_points(level, init_time, hints_taken)
            #---------------------------------------------------------------------------------
                    #current_score = int(float(calculate_points(level, seconds_taken, hints_taken)))
                    #print("Score achieved now : ", current_score )
                    
                    #-------Search for user and add the new score:
                    #import copy
                    
                else:
                    type1=Label(root,text="YOU COULDN'T SOLVE THE SUDOKU",bg="blue2",fg="White",font="Helvetica 30 bold").place(x=-90,y=575)
        
        def calculate_points(level, time, hints_taken) :   
        
            # takes time in seconds
            # level 1: 100 points
            # level 2: 300 points
            # level 3: 500 points
            # 1/12 of no. of seconds taken to be subtracted from the initial number
            # multiply number of hints taken by 10 and subtract the product from the initial points.
            # display rank, name, points
            print(level, time, hints_taken)
            initial = 0
            
            if level=='1':
                initial = 100
            elif level=='2':
                initial = 300
            else:
                initial = 500
            
            print(initial)    
            score = initial - time * (1/12)
            
            score = score - hints_taken * 10
            print(score)
            return( score )
        
        def yes_button():
            global state,root1
            button_check['state']='active'
            state=True
            time_control(init_time)
            #root1.destroy()    
                
        def no_button():
            global root1
            button_check['state']="disabled"
            button_clear_all['state']="disabled"
            disable_buttons("disabled",'disabled','disabled','disabled')
            button_pause['state']='disabled'
            button_hint['state']='disabled'
            #root1.destroy()
            preparing_for_exit()
            type1=Label(root,text="YOU COULDN'T SOLVE THE SUDOKU",bg="blue2",fg="White",font="Helvetica 30 bold").place(x=-90,y=575)
        
        def preparing_for_exit():
            global condition
            condition=False
            for i in range(13):
                for j in range(13):
                    if type(info_l[i][j]) == type(demo_entry):
                        curr=info_l[i][j].get()
                        info_l[i][j].destroy()
                        info_l[i][j]=Label (root,width=2,text=curr,font=("Helvetica",32),bg="white",fg="Black",pady=2)                
                        info_l[i][j].grid(row=i,column=j)
                        
    ###############################################################################
        def destroy_window():
            global saving_window,state,info_l#, time_latest
            #time_latest = time_control(init_time)
            #print('Time now :  ',time_latest)
            state=False
            main_list,main_count=get_data(info_l)
            if main_count>0:
                print("yeh magga")
                
                MsgBox = messagebox.askquestion ('save option','Do you want to save this sudoku ?\nClick yes for save \nclick no for discarding',icon = 'warning', parent = root)
                if MsgBox == 'yes':
                   save_button()
                else:
                    import csv
                    f=open('points.csv','r')
                    w=csv.reader(f)
                    lis=list(w)
                    #print('lis test :',lis)
                    f.close()
                    
                    #print(lis)
                    
                    for i in lis:
                        if len(i)>0:
                            if i[0] == CurrentUserObject.name :
                               
                                i[2]=i[3]=i[4]='0'
                                break
                    
                    for i in range(len(lis)-1,-1,-1):
                        if len(lis[i])==0:
                            del(lis[i])
                            
                    f = open('points.csv','w')
                    wr=csv.writer(f)    # check this function, it is clearing the whole thing
                    wr.writerows(lis)
                    f.close()
                    root.destroy()
                    print(str(CurrentUserObject.name)+'.csv')
                    if path.exists(str(CurrentUserObject.name)+'.csv'):
                        os.remove(str(CurrentUserObject.name)+'.csv')
                    
            else:
                root.destroy()
                if path.exists(str(CurrentUserObject.name)+'.csv'):
                    os.remove(str(CurrentUserObject.name)+'.csv')
                
        def discard_button():
            global saving_window
            saving_window.destroy()
            root.destroy()
            
            
        def save_button(): 
            global info_l,init_time #, time_latest
            print("initial copy_l  :", copy_l)
            #time_latest = time_control(init_time)
            #time_list = time_latest
                    
                    # time in seconds :
            print(init_time)
            #seconds_taken = int(time_list[0] + time_list[1]) * 3600 + int(time_list[3] + time_list[4]) * 60 + int(time_list[6] + time_list[7])
            #print(seconds_taken)
            # take this time in seconds, push it into csv, access in calculate points function for object
            #---------------------------------------------------------------------------------
            # to get the level
            import csv
            f=open('points.csv','r')
            w=csv.reader(f)
            lis=list(w)
            #print('lis test :',lis)
            f.close()
            
            #print(lis)
            
            for i in lis:
                if len(i)>0:
                    if i[0] == CurrentUserObject.name :
                        
                        level = i[4]
                        break
                    
            #---------------------------------------------------------------------------------
            CurrentUserObject.edit_csv(get_data(info_l)[0] , copy_l, init_time, hints_taken, level)
                
            global saving_window    # refer to the user object of current person,
            #saving_window.destroy() # check whether object.number==1, if yes, then ask if old sudoku should be replaced with new one
            root.destroy()          # else call create_csv from user object and store accordingly
            
    ###############################################################################    
        def solution():
            disable_buttons('disabled','disabled','disabled','disabled')
            button_check['state']='disabled'
            button_solution['state']='disabled'
            button_clear_all['state']="disabled"
            button_hint['state']='disabled'
            button_pause['state']='disabled'
            global state #,copy_l
            state=False
            type2=Label(root,text="YOU COULDN'T SOLVE THE SUDOKU",bg="blue2",fg="White",font="Helvetica 30 bold").place(x=-90,y=575)
            output_data()
            
        def output_data():
            global info_l # ,copy_l,l
            for i in range(13):
                for j in range(13):
                    if i not in (0,4,8,12) and j not in (0,4,8,12):
                        row,col=modify_row_and_col(i,j)
                        if l[row][col]==0:
                            info_l[i][j].destroy()
                            info_l[i][j]=Label (root,width=2,text=copy_l[row][col],font=("Helvetica",32),bg="white",fg="red",pady=2)                
                            info_l[i][j].grid(row=i,column=j)
    ###############################################################################    
        global init_time,state,info_l,demo_entry,guess_state,store_coors,colour,main_coors,coordinates_of_click,button_guess_state,button_real_state,empty_list, hints_taken
    #########################################################    
        import csv
        f=open('points.csv','r')
        w=csv.reader(f)
        lis=list(w)
        #print('lis test :',lis)
        f.close()
        
        #print(lis)
        
        for i in lis:
            if len(i)>0:
                if i[0] == CurrentUserObject.name :
                    
                    init_time = int(i[2])
                    hints_taken=int(i[3])
                    break
    #########################################################    
        #hints_taken=0
        #init_time=0
        state=True
        pause_window=None
        guess_state=False
        demo_entry=Entry (root,width=2,font=("Helvetica", 35),justify='center')
        info_l,store_coors,main_coors,empty_list=[],[],[],[]
        colour='Black'
        coordinates_of_click=(0,0)
        button_guess_state= False
        button_real_state= True
    #######################################################################
        
        print("rechecking l  :  ",l)
        for i in range(13):
            info_l.append([])
            for j in range(13):
                if i not in (0,4,8,12) and j not in (0,4,8,12):
                    row,col=modify_row_and_col(i,j)
                    #print()
                    #print("rechecking l  :  ",l)
                    #print( row,'   ',col)
                    if l[row][col]==0:
                        print("empty box")
                        info_l[i].append(Entry (root,width=2,font=("Helvetica", 35),fg=colour,justify='center',relief='flat',cursor=''))
                        info_l[i][j].config(validate="key", validatecommand=(reg,'%P'))
                        info_l[i][j].bind("<Button-1>", click)
                        empty_list.append(info_l[i][j])
                    else:
                        info_l[i].append(Label (root,width=2,text=l[row][col],font=("Helvetica",32),bg="white",fg="blue2",padx=1,pady=2))
                else:
                    decorate_grid(info_l,i,j)    
    
                info_l[i][j].grid(row=i , column=j,pady=0,padx=0)
                
        #print(info_l)
    ###############################################################################
        #draw_lines_in_grid()
        button_check = Button(root,text = 'Check',width=15,height=2,command =process_data)
        button_check.place(x=-170,y=150)
        
        button_solution= Button(root,text="View Solution",width=15,height=2,command=solution)
        button_solution.place(x=-170,y=200)
        
        button_clear_all=Button(root,command=lambda :clear(main_coors),text="Clear all entries",width=15,height=2)
        button_clear_all.place(x=-170,y=250)
        
        button_hint=Button(root,command=hint,text="Hint",width=15,height=2)
        button_hint.place(x=-170,y=300)
        
        button_pause=Button(root,command=pause,text="Pause",width=15,height=2)
        button_pause.place(x=-170,y=350)
        
        button_exit = Button(root,text="Exit",width=15,height=2,command=destroy_window)
        button_exit.place(x=870,y=-120)
        ####################################
        button_guess= Button(root,text="Start Guessing",width=22,height=2,command= button_guess_func)
        button_guess.place(x=600,y=150)
        
        button_guess_to_real= Button(root,text="Convert guessed text to real",state='disabled',width=22,height=2,command= button_guess_to_real_func)
        button_guess_to_real.place(x=600,y=200)
        
        button_real= Button(root,text=("Stop Guessing"),state='disabled',width=22,height=2,command=button_real_func)
        button_real.place(x=600,y=250)
        
        button_clear_guesses=Button(root,command=lambda :clear(store_coors),state='disabled',width=22,height=2,text="Clear all guesses")
        button_clear_guesses.place(x=600,y=300)
        
        button_instructions=Button(root,width=22,height=2,text="Instructions",command=instruction)
        button_instructions.place(x=600,y=350)
        
        main_time=Label(root,text='00:00:00',font=("Helvetica",40),fg="White",bg="medium blue",relief="sunken",bd=5,highlightthickness=5)
        main_time.place(x=162,y=-120)
            
        time_control(init_time)
        root.mainloop()
        
    GenerateSudokuToSolve(CurrentUserObject, l, copy_l)