from tkinter import *
from tkinter import messagebox

def submit():

   if email.get()=='':
        messagebox.showwarning('Error','Please enter your Email Id!!')

   elif Password.get()=='':
        messagebox.showwarning('Error','Please enter your Password!!')    
        
   elif email.get()!='aks@gmail.com' or Password.get()!='123456':
        messagebox.showerror('Error','Please enter valid Username or Password')

   else:
        window.destroy()
        import interface
        
window=Tk()
window.title("Login")
frame1=Frame(window,bg="pink")
frame1.pack(ipadx=100)
heading=Label(frame1, text="LOGIN", fg="blue",bg="pink", font="georgia 15 bold underline")
heading.pack()
frame2=Frame(window,bg='light blue')
frame2.pack(ipadx=50,pady=10,padx=10)
email=StringVar()
Password=StringVar()
a1=Label(frame2, text="Enter your Email Id: ",bg='light blue')
username=Entry(frame2,textvariable=email)
a2=Label(frame2, text="Enter Password: ",bg='light blue')
password=Entry(frame2,textvariable=Password,show='*')
a1.grid(row=1,column=1)
username.grid(row=1,column=2,ipadx=50,pady=10)
a2.grid(row=2,column=1,padx=100)
password.grid(row=2,column=2,ipadx=50,pady=10)
frame3=Frame(window)
frame3.pack()
button=Button(frame3, text="Login",command=submit,bg='white',cursor='hand2',activebackground='red')
button.pack(ipadx=10,pady=20)
      
