from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox
signup=Tk()
Background=ImageTk.PhotoImage(file='BG1.png')
BLabel=Label(signup,image=Background,width=600,height=400)
BLabel.grid()
signup.geometry('500x600')
signup.title('signup page...')
signup.iconbitmap('icon.ico')

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    c1.set(0)

def to_login():
    signup.destroy()
    import main
def to_database():
    if e1.get()=='' or e2=='' or e3=='' or e4=='':
        messagebox.showerror('error','All value is required')
    elif e1.get() == '':
        messagebox.showerror('email', 'Please enter Email')
    elif e2.get() == '':
        messagebox.showerror('username', 'Please enter Username')
    elif e3.get() == '':
        messagebox.showerror('password', 'Please enter Password')
    elif e4.get() == '':
        messagebox.showerror('password', 'Please enter conform Password')

    elif e3.get() != e4.get():
        messagebox.showerror('error','unmatch password')
    elif c1.get()==0:
        messagebox.showerror('erre','please accept terms and condition')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='')
            mycursor = con.cursor()
        except:
            messagebox.showerror('error','database connectivity issue,please try again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50),username varchar(50),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute("use userdata")
        query='select * from data where username=%s'
        mycursor.execute(query,(e1.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('error','username Alredy exists')
        else:
            query = 'insert into data(email,username,password)values(%s,%s,%s)'
            mycursor.execute(query, (e1.get(), e2.get(), e3.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is Successful')
            clear()
            signup.destroy()
            import main








title=Label(signup,text='CREATE AN ACCOUNT',font=('times',16,'underline'),bd=0,fg='green')
title.place(x=150,y=10)

l1=Label(signup,text='Email',font=('times',16,'bold'),fg='blue')
l1.place(x=50,y=80)
e1=Entry(signup,width=25,font=('times',16,'bold'))
e1.place(x=180,y=80)

l2=Label(signup,text='Username',font=('times',16,'bold'),fg='blue')
l2.place(x=50,y=130)
e2=Entry(signup,width=25,font=('times',16,'bold'))
e2.place(x=180,y=130)

l3=Label(signup,text='Password',font=('times',16,'bold'),fg='blue')
l3.place(x=50,y=180)
e3=Entry(signup,width=25,font=('times',16,'bold'),show='*')
e3.place(x=180,y=180)

l4=Label(signup,text='C_Password',font=('times',16,'bold'),fg='blue')
l4.place(x=50,y=230)
e4=Entry(signup,width=25,font=('times',16,'bold'),show='*')
e4.place(x=180,y=230)

c1=IntVar()

check=Checkbutton(signup,text='I agree to the Terms & Conditions',font=('time',10,'bold'),fg='green',cursor='hand2',variable=c1)
check.place(x=50,y=300)

sub=Button(signup,text='Submit',pady=10,padx=10,bg='green',fg='white',activeforeground='white',activebackground='blue',width=60,command=to_database)
sub.place(x=30,y=350)

singuplabel=Label(signup,text='you have a account?',font=('tamil',10,'bold'),fg='blue')
singuplabel.place(x=50,y=450)

signinButton=Button(signup,text='Login',font=('time',10,'underline'),fg='green',bd=0,cursor="hand2",command=to_login)
signinButton.place(x=200,y=450)




signup.mainloop()