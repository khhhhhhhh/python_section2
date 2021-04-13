from tkinter import *

def printHello() :
    print('Hi')

root=Tk()
w=Label(root, text='Python Test')
b=Button(root, text="Hellow Python", command=printHello)
c=Button(root, text='quit', command=root.quit)

b.pack()  #이건 뭐지?
c.pack()
w.pack()

root.mainloop()#이건 뭐지?
