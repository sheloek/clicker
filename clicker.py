from tkinter import *

root = Tk()

root['bg'] = '#fafafa'
root.title('Кликер')
root.geometry('300x500')
root.resizable(width=False, height=False)

n = 0

def nplus():
    global n
    n = n + 1
    label['text'] = '$ ' + str(n)

frame = Frame(root, bg='#fafafa', bd=5)
frame.place(relx=0.1, rely=0.025, relwidth=0.8, relheight=0.075)

title = Label(frame, text='Ваш баланс:', bg='#fafafa', font='Helvetica 25')
title.pack()

frame1 = Frame(root, bg='#fafafa', bd=5)
frame1.place(relx=0, rely=0.12, relwidth=1, relheight=0.15)

label = Label(frame1, text='$ ' + str(n), font=('Helvetica 50'), bg='#fafafa')
label.pack()


frame3 = Frame(root, bg='#fafafa', bd=5)
frame3.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.3)

button = Button(frame3, text='+$1', width=30, height=10, background="#c0c0c0", font='Helvetica 50', command=nplus)
button.pack()

frame3 = Frame(root, bg='blue', bd=5)
frame3.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

title33 = Label(frame3, text='Скоро', bg='blue', font='Helvetica 25')
title33.pack()

root.mainloop()