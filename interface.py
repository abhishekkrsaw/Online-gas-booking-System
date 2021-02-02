from tkinter import *
from tkinter import messagebox
def register1():
    window.destroy()
    import register
def about():
    msg['text']='This is the online LPG gas booking interface.\n\n Designed by:\n-Abhishek Kumar\n-Mayank Pratap\n-Shashwat Sood\n\nThanks to all of my friends and\n mentors for their support'
    msg['bg']='black'
    msg['fg']='white'
def exit():
    exi = messagebox.askyesno("Confirm! ", "Do you really want to exit")
    if (exi >0):
        window.destroy()
        return
def show():
    import show
def connection():
    window.destroy()
    import connection
window=Tk()
window.configure(background='violet')
window.title('INDIAN GAS')
window.geometry('1000x650')
frame1=Frame(window)
frame1.pack()
label1=Label(window,text='INDIAN GAS',font=('forte',30,'underline'),
             bg='yellow',fg='red')
label1.place(x=0,y=0,relwidth=1,height=120)
img=PhotoImage(file='8.png')
img=img.subsample(3)
label2=Label(window,image=img,bg='yellow')
label2.place(x=255,y=10)
label3=Label(window,image=img,bg='yellow')
label3.place(x=680,y=10)

msg=Label(window, text="Welcome to India's largest online gas booking platform !!",
          font=('times new roman',15,'bold'),fg='dark blue',bg='violet')
msg.place(x=0,y=130,relwidth=1)

button1=Button(window,text='Register for new lpg connection',command=register1,
               font=('arial',10),activebackground='light blue',cursor='hand2')
button1.place(x=30,y=180,height=40,width=200)

about=Button(window,text='About Us',font=('arial',10),activebackground='brown',
             cursor='hand2',command=about)
about.place(x=30,y=420,height=40,width=200)

exit1=Button(window,text='Exit',font=('arial',10),activebackground='light blue',
             cursor='hand2',command=exit)
exit1.place(x=30,y=500,height=40,width=200)

msg=Label(window,text='This is the place where you\n can book your LPG online !!!!',
            bg='white',fg='green',font=('arial',15),justify='left')
msg.place(x=520,y=170,height=480,width=480)

show1=Button(window,text='Show info',font=('arial',10),activebackground='red',
             cursor='hand2',command=show)
show1.place(x=30,y=340,height=40,width=200)

conn=Button(window,text='Add Connection',font=('arial',10),activebackground='red',
             cursor='hand2',command=connection)
conn.place(x=30,y=260,height=40,width=200)
