from tkinter import *
def win():
    window.destroy()
f=open('show.txt','r')
l=f.read().split()
window=Tk()
window.title('Info')
window['bg']='sky blue'
window.geometry('320x320')
try:    
    l1=Label(window,text='Your Name:',bg='sky blue')
    e1=Label(window,text=l[0:2],bg='sky blue')
    l1.grid(row=1,column=1,padx=20,pady=10)
    e1.grid(row=1,column=2,padx=20)

    l2=Label(window,text='Your Mobile Number:',bg='sky blue')
    e2=Label(window,text=l[2],bg='sky blue')
    l2.grid(row=2,column=1,padx=20,pady=10)
    e2.grid(row=2,column=2,padx=20)

    l3=Label(window,text='Your Email Id:',bg='sky blue')
    e3=Label(window,text=l[3],bg='sky blue')
    l3.grid(row=3,column=1,padx=20,pady=10)
    e3.grid(row=3,column=2,padx=20)

    l3=Label(window,text='Your LPG weight:',bg='sky blue')
    e3=Label(window,text=l[4],bg='sky blue')
    l3.grid(row=4,column=1,padx=20,pady=10)
    e3.grid(row=4,column=2,padx=20)

    l3=Label(window,text='Your Delivery Date:',bg='sky blue')
    e3=Label(window,text=l[5],bg='sky blue')
    l3.grid(row=5,column=1,padx=20,pady=10)
    e3.grid(row=5,column=2,padx=20)

    l3=Label(window,text='Your Customer id:',bg='sky blue')
    e3=Label(window,text=l[6],bg='sky blue')
    l3.grid(row=6,column=1,padx=20,pady=10)
    e3.grid(row=6,column=2,padx=20)

    l3=Label(window,text='Your Delivery Address:',bg='sky blue')
    e3=Label(window,text=l[7:],bg='sky blue')
    l3.grid(row=7,column=1,padx=20,pady=10)
    e3.grid(row=7,column=2,padx=20)
    
except:
    pass

button1=Button(window,text='OK',command=win,bg='black',fg='white')
button1.place(x=135,y=290,width=50)
