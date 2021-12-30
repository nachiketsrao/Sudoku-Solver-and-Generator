from user import user
import tkinter
from tkinter import messagebox
import pickle
from new_user import new_user

def hosa_user():
    move=tkinter.Button(root,font=("Times",20),text="Sign Up",command=hosa_user,state=tkinter.DISABLED)
    new_user()
  

def entry():
    f=open("admin.dat","br")
    send_name=str(name.get())
    send_pass=str(password.get())
    flag=False
    while True:
        try:
            x=pickle.load(f)
            if x.name==send_name.upper() and x.password==send_pass:
                messagebox.showinfo("Success","The login has been successful")
                Flag=True
                return None
        except:
            f.close()
            break
    if flag==False:
        messagebox.showerror("Error","Wrong User Name/Password, Please try again!!")
        flag=False
        return None  
            
    
global root
root=tkinter.Tk()
root.title("Old user page")
root.geometry("1000x900")
root.resizable(height=None,width=None)
root.configure(bg="light sky blue")
root.attributes("-fullscreen",True)

head_label=tkinter.Label(root,font=("Times",50),text="WELCOME TO SUDOKU ")
head_label.place(x=250,y=90)

plz_sign=tkinter.Label(root,font=("Times",30),text="Please sign in.")
plz_sign.place(x=100,y=260)

user_name=tkinter.Label(root,font=("Times",30),text="User Name")
user_name.place(x=100,y=350)

global name
name=tkinter.Entry(root,font=("Times",30))
name.place(x=320,y=350)

user_pass=tkinter.Label(root,font=("Times",30),text="Password")
user_pass.place(x=100,y=420)

global password
password=tkinter.Entry(root,font=("Times",30),show="*")
password.place(x=320,y=420)
send_pass=str(password.get())

signin=tkinter.Button(root,font=("Times",25),text="Sign In",command=entry)
signin.place(x=320,y=500)

new_lbl=tkinter.Label(root,font=("Times",20),text="Don't have an account?")
new_lbl.place(x=970,y=350)

global move
move=tkinter.Button(root,font=("Times",20),text="Register",command=hosa_user)
move.place(x=1050,y=400)

close_btn=tkinter.Button(root,font=("Times",20),text="Close",command=root.destroy)
close_btn.place(x=1170,y=30)

root.mainloop()

