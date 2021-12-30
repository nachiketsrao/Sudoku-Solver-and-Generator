#from user import user

def new_user():
    from user import user
    import tkinter
    from tkinter import messagebox
    import pickle
    import os


    def check_valid(name):
        f=open("admin.dat","br")
        while True:
            try:
                x=pickle.load(f)
                if x.name==name.upper():
                    return False
            except:
                f.close()
                break
        return True    
        

    def entry():
        send_name=str(name.get())
        send_pass=str(password.get())

        if check_valid(send_name)==False:
            messagebox.showerror("Error","User name already taken !")
            root.destroy()
            return None
        print("The send name is ",send_name)
        print("The pass",send_pass)

        u=user()   # creating an object of the clas, object u has name, password and csv file
        
        u.name=send_name.upper()
        print()
        u.password=send_pass
        print("First input",u.first_input())

        if u.first_input()==False:
            messagebox.showerror("Error","Invalid input !!")
            root.destroy()
            return None
        elif u.first_input()==True:
            messagebox.showinfo("Done","Data has been added !")
            root.destroy()
            
            import csv
            f= open('points.csv','a+')
            w=csv.writer(f)
            w.writerow([u.name, 0, 0, 0 , 0])
            
            f.close()
            
            f=open("admin.dat","ba")
            pickle.dump(u,f)
            f.close()
            return None
        
        
                    #    print("The final pasword :",self.password)
                    #        name=str(self.name)+str(random.randint(1,1000))
                   
            
            
        

    root=tkinter.Tk()
    root.title("Signup page")
    root.geometry("1000x900")
    root.resizable(height=None,width=None)
    root.configure(bg="SkyBlue2")
    root.attributes("-fullscreen",True)

    head_label=tkinter.Label(root,font=("Times",50),text="Create your SUDOKU account ")
    head_label.place(x=250,y=100)

    
    user_name=tkinter.Label(root,font=("Times",30),text="User Name")
    user_name.place(x=300,y=300)

    global name
    name=tkinter.Entry(root,font=("Times",30))
    name.place(x=500,y=300)

    user_pass=tkinter.Label(root,font=("Times",30),text="Password")
    user_pass.place(x=300,y=400)


    global password
    password=tkinter.Entry(root,font=("Times",30),show="*")
    password.place(x=500,y=400)
    send_pass=str(password.get())

    info1=tkinter.Label(root,font=("Times",20),text="*User name and password should have minimum 4 characters")
    info1.place(x=300,y=500)

    info2=tkinter.Label(root,font=("Times",20),text="*User name can't have any special characters")
    info2.place(x=300,y=550)

    signup=tkinter.Button(root,font=("Times",25),text="Next",command=entry)
    signup.place(x=800,y=620)
    
    close_btn=tkinter.Button(root,font=("Times",20),text="Close",command=root.destroy)
    close_btn.place(x=1150,y=0)

    root.mainloop()


#new_user()
         

