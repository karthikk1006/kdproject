from tkinter import *
import importlib
from tkinter import Frame
from PIL import ImageTk, Image
from tkinter import messagebox

def mainwindow_professional(u):
    main_window = Tk()
    main_window.title('Main window')
    main_window.geometry('1920x1080')
    main_window.state('zoomed')
    # Frame
    frame1 = Frame(main_window, bg='PaleGreen1', highlightbackground="dark green", highlightthickness=1)
    frame1.pack(side=TOP, fill=X)
    Label(frame1, text='*Name*', bg='PaleGreen1', font=('TkDefaultFont', 16)).pack(side='left', padx=10, pady=5)

    dropmenu = Menubutton(frame1, text='  Menu  ', bg='Light blue', font=('TkDefaultFont', 16), relief=SOLID)
    dropmenu.menu = Menu(dropmenu)
    dropmenu['menu'] = dropmenu.menu

    dropmenu.menu.add_command(label='Profile')
    dropmenu.menu.add_command(label='Username Reset')
    dropmenu.menu.add_command(label='Password Reset')
    dropmenu.menu.add_command(label='Sign Out')

    dropmenu.pack(side=RIGHT, padx=10, pady=5)
    # Image
    bgimg = ImageTk.PhotoImage(Image.open('bgimage.jpg'))
    Label(main_window, image=bgimg).pack(side=TOP, fill=X)

    # Main window features
    main_window.mainloop()







# adding details to table after entry for signup and checking wheteher username is unique or not
def signup_professional_submit():
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute("select * from professional where username='{}'".format(a1.get()))
    res = cur.fetchall()
    if cur.rowcount == 0:
        cur.execute("insert into professional values('{}','{}','{}',{},'{}','{}','{}')".format(a1.get(), a2.get(), a3.get(), a4.get(), a5.get(), a6.get(), a7.get()))
        messagebox.showinfo(" ", "ACCOUNT CREATION SUCCESSFUL")
        root_sp.destroy()
        root_s.destroy()
    else:
        messagebox.showwarning(" ", "Username already exists!")
def signup_user_submit():
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute("select * from professional where username='{}'".format(b1.get()))
    res = cur.fetchall()
    if cur.rowcount == 0:
        cur.execute("insert into user values('{}','{}','{}',{},'{}','{}')".format(b1.get(), b2.get(), b3.get(), b4.get(), b5.get(), b6.get()))
        messagebox.showinfo(" ", "ACCOUNT CREATION SUCCESSFUL")
        root_su.destroy()
        root_s.destroy()

    else:
        messagebox.showwarning(" ", "Username already exists!")
# signup professional and user
def signup_professional():
    global a1, a2, a3, a4, a5, a6, a7, root_sp
    root_sp = Toplevel()
    root_sp.geometry('220x170')
    root_sp.title('Create a professional account')
    # details

    Label(root_sp, text='Enter Username').grid(row=0, column=0)
    a1 = Entry(root_sp)
    a1.grid(row=0, column=1, columnspan=1)
    Label(root_sp, text='Enter Password').grid(row=1, column=0)
    a2 = Entry(root_sp)
    a2.grid(row=1, column=1, columnspan=1)
    Label(root_sp, text='Enter Name').grid(row=2, column=0)
    a3 = Entry(root_sp)
    a3.grid(row=2, column=1, columnspan=1)
    Label(root_sp, text='Enter Age').grid(row=3, column=0)
    a4 = Entry(root_sp)
    a4.grid(row=3, column=1, columnspan=1)
    Label(root_sp, text='Enter Profession').grid(row=4, column=0)
    a5 = Entry(root_sp)
    a5.grid(row=4, column=1, columnspan=1)
    Label(root_sp, text='Enter Address').grid(row=5, column=0)
    a6 = Entry(root_sp)
    a6.grid(row=5, column=1, columnspan=1)
    Label(root_sp, text='Enter Pincode').grid(row=6, column=0)
    a7 = Entry(root_sp)
    a7.grid(row=6, column=1, columnspan=1)

    Button(root_sp, text='Submit', command=signup_professional_submit, bg='light green', fg='blue').grid(row=7,
                                                                                                         column=0,
                                                                                                         columnspan=2)
def signup_user():
    global b1, b2, b3, b4, b5, b6, root_su
    root_su = Toplevel()
    root_su.geometry('220x150')
    root_su.title('Create a user account')
    # details

    Label(root_su, text='Enter Username').grid(row=0, column=0)
    b1 = Entry(root_su)
    b1.grid(row=0, column=1, columnspan=1)
    Label(root_su, text='Enter Password').grid(row=1, column=0)
    b2 = Entry(root_su)
    b2.grid(row=1, column=1, columnspan=1)
    Label(root_su, text='Enter Name').grid(row=2, column=0)
    b3 = Entry(root_su)
    b3.grid(row=2, column=1, columnspan=1)
    Label(root_su, text='Enter Age').grid(row=3, column=0)
    b4 = Entry(root_su)
    b4.grid(row=3, column=1, columnspan=1)
    Label(root_su, text='Enter Address').grid(row=4, column=0)
    b5 = Entry(root_su)
    b5.grid(row=4, column=1, columnspan=1)
    Label(root_su, text='Enter Pincode').grid(row=5, column=0)
    b6 = Entry(root_su)
    b6.grid(row=5, column=1, columnspan=1)

    Button(root_su, text='Submit', command=signup_user_submit, bg='light green', fg='blue').grid(row=6, column=0,
                                                                                                 columnspan=2)
# ********************************************************
def login_professional_submit():
    global c11
    import mysql.connector as sql
    con = sql.connect(host="localhost", user="root", password="2810", database="kdproject", autocommit=True)
    cur = con.cursor()
    c11=c1.get()
    cur.execute('select * from professional where username="{}"'.format(c1.get()))
    res = cur.fetchall()
    if cur.rowcount == 0:
        messagebox.showwarning(" ", "Username does not exist!")
    else:
        for i in res:
            if i[1] != c2.get():
                messagebox.showwarning(" ", "Incorrect password")
            else:
                root_lp.destroy()
                root_l.destroy()
                root.destroy()
                mainwindow_professional(c11)
def login_user_submit():
    import mysql.connector as sql
    con = sql.connect(host="localhost", user="root", password="2810", database="kdproject", autocommit=True)
    cur = con.cursor()
    cur.execute('select * from user where username="{}"'.format(d1.get()))
    res = cur.fetchall()
    if cur.rowcount == 0:
        messagebox.showwarning(" ", "Username does not exist!")
    else:
        for i in res:
            if i[1] != d2.get():
                messagebox.showwarning(" ", "Incorrect password")
            else:
                root_lu.destroy()
                root_l.destroy()
                root.destroy()
# login professional and user
def login_professional():
    global root_lp
    global c1, c2
    root_lp = Toplevel()
    root_lp.geometry("200x150")
    root_lp.title("Professional Login")
    # details
    Label(root_lp, text="Enter Username").grid(row=0, column=0)
    c1 = Entry(root_lp)
    c1.grid(row=0, column=1)
    Label(root_lp, text="Enter Password").grid(row=1, column=0)
    c2 = Entry(root_lp, show="*")
    c2.grid(row=1, column=1)

    Button(root_lp, text="Login", command=login_professional_submit, bg='light green', fg='blue').grid(row=3, column=0,
                                                                                                       columnspan=2)
def login_user():
    global root_lu
    global d1, d2
    root_lu = Toplevel()
    root_lu.geometry("200x150")
    root_lu.title("Professional Login")
    # details
    Label(root_lu, text="Enter Username").grid(row=0, column=0)
    d1 = Entry(root_lu)
    d1.grid(row=0, column=1)
    Label(root_lu, text="Enter Password").grid(row=1, column=0)
    d2 = Entry(root_lu, show="*")
    d2.grid(row=1, column=1)

    Button(root_lu, text="Login", command=login_user_submit, bg='light green', fg='blue').grid(row=3, column=0,
                                                                                               columnspan=2)
# ********************************************************
def signup():
    global root_s
    root_s = Toplevel()
    root_s.geometry('400x250')
    root_s.title('Sign Up')
    Label(root_s, text='What kind of an account do you want to create?', font=('arial', 10, 'bold')).grid(row=0,
                                                                                                          column=0,
                                                                                                          columnspan=2)

    # Buttons
    Button(root_s, text='Professional Account', command=signup_professional, bg='light green', fg='blue').grid(row=2,
                                                                                                               column=0,
                                                                                                               pady=10,
                                                                                                               padx=50)
    Button(root_s, text='User Account', command=signup_user, bg='light green', fg='blue').grid(row=2, column=1, pady=10,
                                                                                               padx=20)
def login():
    global root_l
    root_l = Toplevel()
    root_l.geometry('400x250')
    root_l.title('Login')
    Label(root_l, text='With which account do you want to login with?', font=('arial', 10, 'bold')).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=2)

    Button(root_l, text='Professional Account', command=login_professional, bg='light green', fg='blue').grid(row=2,
                                                                                                              column=0,
                                                                                                              pady=10,
                                                                                                              padx=50)
    Button(root_l, text='User Account', command=login_user, bg='light green', fg='blue').grid(row=2, column=1, pady=10,
                                                                                              padx=20)






#Entrypage
#mainroot
root = Tk()
root.geometry('200x100')
root.title('EntryPage')
Label(root, text='Create a new account?', font=('arial', 10, 'bold')).pack()
b_signup = Button(root, text='Sign Up', command=signup, bg='light green', fg='blue').pack()
Label(root, text='Account exists already?', font=('arial', 10, 'bold')).pack()
b_login = Button(root, text='Login', command=login, bg='light green', fg='blue').pack()

root.mainloop()



