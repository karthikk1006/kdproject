from tkinter import *
main_window=Tk()
main_window.geometry('1920x1080')
main_window.state('zoomed')
frame1=Frame(main_window,bg='PaleGreen1')
frame1.pack(side=TOP,fill=X)
Label(frame1,text='fenk').pack()

main_window.mainloop()
