from tkinter import *

import pymysql
from PIL import ImageTk
from tkinter import messagebox
import mysql

login_window=Tk()
bgImage=ImageTk.PhotoImage(file='bg3.jpeg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.grid(row=0,column=0)
login_window.geometry('840x360')
login_window.title('Login Page...')
login_window.iconbitmap('icon.ico')
def login_main():
    if usernameentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror('error','All field are Required')
    else:
        try:
            com = pymysql.Connect(host='localhost', user='root', password='')
            mycursor = com.cursor()
        except:
            messagebox.showerror('error','Connection is not established try again')
            return

        query ='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameentry.get(),passwordentry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('error','Invalid username or password')
        else:
            messagebox.showinfo('Success','Login successful')


def user_enter(event):
    if usernameentry.get()=='Username':
        usernameentry.delete(0,END)

def password_enter(event):
    if passwordentry.get()=='Password':
        passwordentry.delete(0,END)

def to_signup():
    login_window.destroy()
    import signup





heading=Label(login_window,text='User Login',font=('times',20,'bold'),fg='green',bg='white')
heading.place(x=600,y=5)

usernameentry=Entry(login_window,width=35,bd=3,font=('tamil',12,'bold'))
usernameentry.place(x=500,y=60)
usernameentry.insert(0,'Username')
usernameentry.bind('<FocusIn>',user_enter)



passwordentry=Entry(login_window,width=35,bd=3,show='*',font=('tamil',12,'bold'))
passwordentry.place(x=500,y=100)
passwordentry.insert(0,'Password')
passwordentry.bind('<FocusIn>',password_enter)



forgetButton=Button(login_window,text='forgot password?',bd=0,bg='white',activebackground='white',cursor='hand2',fg='green',activeforeground='firebrick1',font=('tamil',10,'bold'))
forgetButton.place(x=700,y=130)

login_b=Button(login_window,text='Login',font=('times',15,'bold'),fg='white',bg='blue',width=26,command=login_main)
login_b.place(x=500,y=160)

orlabel=Label(login_window,text='****************************** OR ****************************',font=('tamil',10,'bold'),fg='blue',bg='white')
orlabel.place(x=500,y=230)

singuplabel=Label(login_window,text='Don\'t have a account?',font=('tamil',10,'bold'),fg='red',bg='white')
singuplabel.place(x=500,y=250)

signinButton=Button(login_window,text='Create New Account',font=('time',10,'underline'),fg='green',bd=0,bg='white',cursor="hand2",command=to_signup)
signinButton.place(x=650,y=250)



login_window.mainloop()