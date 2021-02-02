from tkinter import *
from tkinter import messagebox
def back():
    window.destroy()
    import interface
def validation():

    if v2.get()=='':
        messagebox.showwarning('Error!!','Please enter your Delivery date Name!!')
        
    elif v3.get()=='':
        messagebox.showwarning('Error!!','Please enter your Customer id!!')  

    elif v4.get()=='':
        messagebox.showwarning('Error!!','Please enter your Address!!')

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

        f=open('show.txt','a')
        f.write(' ')
        f.write(v1.get())
        f.write(' ')
        f.write(v2.get())
        f.write(' ')
        f.write(v3.get())
        f.write(' ')
        f.write(v4.get())
        f.close()
        messagebox.showinfo('Thank You', 'Your connection is added')
        window.destroy()
        import interface

window=Tk()
window['bg']='light blue'
window.geometry('500x600')

frame=Frame(window,bg='light blue')
frame.pack(pady=20)
head=Label(frame,text='Add Connection',font=('algerian',20,'underline','bold'),bg='light blue',fg='dark blue')
head.grid()

frame0=Frame(window,bg='light blue')
frame0.pack()
j=PhotoImage(file='1.png')
j=j.subsample(2)
image1=Label(frame0,image=j)
image1.grid(row=1)

frame1=Frame(window,bg='light blue')
frame1.pack()
l1=Label(frame1,text="Choose the LPG weight",bg='light blue',font=('calibri',12,'bold'))
l1.grid(row=2,pady=10)
v1=StringVar()
v1.set("25kg") # default value
e1= OptionMenu(frame1,v1, "8kg", "12kg", "25kg","30kg")
e1['relief']='groove'
e1.grid(row=3,ipadx=20)

l2=Label(frame1,text="Enter Delivery Date",bg='light blue',font=('calibri',12,'bold'))
l2.grid(row=4,pady=10)
v2=StringVar()
e2=Entry(frame1,textvariable=v2)
e2.grid(row=5,ipadx=20)

l3=Label(frame1,text="Customer Id",bg='light blue',font=('calibri',12,'bold'))
l3.grid(row=6,pady=10)
v3=StringVar()
e3=Entry(frame1,textvariable=v3)
e3.grid(row=7,ipadx=20)

l4=Label(frame1,text="Address",bg='light blue',font=('calibri',12,'bold'))
l4.grid(row=8,pady=10)
v4=StringVar()
e4=Entry(frame1,textvariable=v4)
e4.grid(row=9,ipadx=20,ipady=20)


frame5=Frame(window,bg='light blue')
frame5.pack(ipady=10)
button=Button(frame5,text="Add",font=('arial',16,'bold'),activebackground='red',
              bg='gold',command=validation,cursor='hand2')
button.grid(ipadx=25,ipady=6,pady=50,padx=10)




