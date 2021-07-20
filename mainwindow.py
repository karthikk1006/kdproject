from tkinter import *
from tkinter import Frame
from PIL import Image, ImageTk
main_window=Tk()
main_window.geometry('1920x1080')
main_window.state('zoomed')
'''
#TITLEBAR
#Frame
frame1=Frame(main_window,bg='PaleGreen1', highlightbackground="dark green",highlightthickness=1)
frame1.grid(row=0,column=0,sticky=NSEW)
Label(frame1,text='*Name*',bg='PaleGreen1',font=('TkDefaultFont',16),padx=10,pady=5).grid(row=0,column=0)
Label(frame1,text='*Button*',bg='PaleGreen1',font=('TkDefaultFont',16),padx=10,pady=5,justify='right').grid(row=0,column=1,columnspan=10)

#Image
bgimg=ImageTk.PhotoImage(Image.open('bgimage.jpg'))
Label(main_window,image=bgimg ,borderwidth=1).grid(row=1,column=0)'''
'''What to add in menu:
1. Account
2. Change Password
3. Sign out( destroy current page and start from first )
4. Change Username
'''
def menu_option1():
    pass
def menu_option2():
def menu_option3():
def menu_option4():
#Frame
frame1=Frame(main_window,bg='PaleGreen1', highlightbackground="dark green",highlightthickness=1)
frame1.pack(side=TOP,fill=X)
Label(frame1,text='*Name*',bg='PaleGreen1',font=('TkDefaultFont',16)).pack(side='left',padx=10,pady=5)

dropmenu =Menubutton(frame1 , text='  Menu  ',bg='Light blue',font=('TkDefaultFont',16),relief=SOLID)
dropmenu.menu= Menu(dropmenu)
dropmenu['menu'] = dropmenu.menu

dropmenu.menu.add_command(label='Profile',command= menu_option1)
dropmenu.menu.add_command(label='Username Reset',command= menu_option2)
dropmenu.menu.add_command(label='Password Reset',command= menu_option3)
dropmenu.menu.add_command(label='Sign Out',command= menu_option4)

dropmenu.pack(side=RIGHT,padx=10,pady=5)
#Image
bgimg=ImageTk.PhotoImage(Image.open('bgimage.jpg'))
Label(main_window,image=bgimg).pack(side=TOP,fill=X)

#Main window features
main_window.mainloop()
