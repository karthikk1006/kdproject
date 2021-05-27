from tkinter import *
from tkinter import Frame
from PIL import Image, ImageTk
main_window=Tk()
main_window.geometry('1920x1080')
main_window.state('zoomed')

#TITLEBAR
#Frame
frame1=Frame(main_window,bg='PaleGreen1', highlightbackground="dark green",highlightthickness=1)
frame1.grid(row=0,column=0,columnspan=1000,rowspan=1,sticky=NSEW)
Label(frame1,text='Button',bg='PaleGreen1',font=('TkDefaultFont',16),padx=10,pady=5,justify='right').grid(row=0,column=1,sticky=E)
Label(frame1,text='*Name*',bg='PaleGreen1',font=('TkDefaultFont',16),padx=10,pady=5).grid(row=0,column=0,sticky=W)

#Image
bgimg=ImageTk.PhotoImage(Image.open('bgimage.jpg'))
Label(main_window,image=bgimg ,borderwidth=1).grid(row=1,column=0)



main_window.mainloop()
