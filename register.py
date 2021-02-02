from tkinter import *
from tkinter import messagebox
def back():
    window.destroy()
    import interface
def validation():
    if v1.get()=='':
        messagebox.showwarning('Error!!','Please enter your First Name!!')

    elif v2.get()=='':
        messagebox.showwarning('Error!!','Please enter your Last Name!!')
        
    elif v3.get()=='':
        messagebox.showwarning('Error!!','Please enter your Mobile Number!!')  

    elif len(v3.get())!=10:
        messagebox.showwarning('Error!!','Please enter valid Mobile Number!!')

    elif v4.get()=='':
        messagebox.showwarning('Error!!','Please enter your Email Id!!')

    elif '@' not in v4.get() or '.com' not in v4.get():
        messagebox.showwarning('Error!!','Please enter valid Email Id!!')

    else:
        f=open('data.txt','a')
        f.write('\n')
        f.write(v1.get())
        f.write(' ')
        f.write(v2.get())
        f.write(' ')
        f.write(v3.get())
        f.write(' ')
        f.write(v4.get())
        f.close()

        f=open('show.txt','w')
        f.write('\n')
        f.write(v1.get())
        f.write(' ')
        f.write(v2.get())
        f.write(' ')
        f.write(v3.get())
        f.write(' ')
        f.write(v4.get())
        f.close()
        messagebox.showinfo('Thank You', 'You are now registered')
        window.destroy()
        import interface

window=Tk()
window['bg']='pink'
window.geometry('500x600')

frame=Frame(window,bg='pink')
frame.pack(pady=20)
head=Label(frame,text='New LPG Connection',font=('algerian',20,'underline','bold'),bg='pink',fg='dark blue')
head.grid()

frame0=Frame(window,bg='pink')
frame0.pack()
j=PhotoImage(file='LPG.png')
j=j.subsample(5)
image1=Label(frame0,image=j)
image1.grid(row=1)

frame1=Frame(window,bg='pink')
frame1.pack()
l1=Label(frame1,text="First Name",bg='pink',font=('calibri',12,'bold'))
l1.grid(row=2,pady=10)
v1=StringVar()
e1=Entry(frame1,textvariable=v1)
e1.grid(row=3,ipadx=20)

l2=Label(frame1,text="Last Name",bg='pink',font=('calibri',12,'bold'))
l2.grid(row=4,pady=10)
v2=StringVar()
e2=Entry(frame1,textvariable=v2)
e2.grid(row=5,ipadx=20)

l3=Label(frame1,text="Mobile Number",bg='pink',font=('calibri',12,'bold'))
l3.grid(row=6,pady=10)
v3=StringVar()
e3=Entry(frame1,textvariable=v3)
e3.grid(row=7,ipadx=20)

l4=Label(frame1,text="Email",bg='pink',font=('calibri',12,'bold'))
l4.grid(row=8,pady=10)
v4=StringVar()
e4=Entry(frame1,textvariable=v4)
e4.grid(row=9,ipadx=20)


frame5=Frame(window,bg='pink')
frame5.pack(ipady=10)
button=Button(frame5,text="Register",font=('arial',16,'bold'),activebackground='red',
              bg='light blue',command=validation,cursor='hand2')
button.grid(row=1,column=2,ipadx=30,ipady=8,pady=50,padx=10)
button1=Button(frame5,text="Back",font=('arial',16,'bold'),activebackground='red',
               bg='light blue',command=back,cursor='hand2')
button1.grid(row=1,column=1,ipadx=40,ipady=8,pady=50,padx=30)



