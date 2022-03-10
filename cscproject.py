from tkinter import *
from tkinter import Frame
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
#1920x1080

#account deletion - done
#main page - done
#Add disclaimer - done
#delete req - done
#location code, areas should be close to each other


'''Disclaimer : If the service you are looking for is unavailable, no professionals are present at the moment in your vicinity providing that service. '''
#professional table status check before and after accepting ( should display only if status is 0 )
#***********************************************************************************************************************
'''
def profile_user():
    profile_user_window = Tk()
    profile_user_window.title('Profile')
    profile_user_window.geometry('150x170')
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute('select * from user where username="{}"'.format(v))
    res = cur.fetchall()
    l1=list()
    for j in range(len(res[0])):
        l1.append(res[0][j])
    print(l1)
    Label(profile_user_window, text='Username').grid(row=0, column=0)
    Label(profile_user_window, text='Password').grid(row=1, column=0)
    Label(profile_user_window, text='Name').grid(row=2, column=0)
    Label(profile_user_window, text='Age').grid(row=3, column=0)
    Label(profile_user_window, text='Address').grid(row=5, column=0)
    Label(profile_user_window, text='Pincode').grid(row=6, column=0)

    Label(profile_user_window, text=l1[0]).grid(row=0, column=1)
    Label(profile_user_window, text=l1[1]).grid(row=1, column=1)
    Label(profile_user_window, text=l1[2]).grid(row=2, column=1)
    Label(profile_user_window, text=l1[3]).grid(row=3, column=1)
    Label(profile_user_window, text=l1[4]).grid(row=4, column=1)
    Label(profile_user_window, text=l1[5]).grid(row=5, column=1)
def change_username_user():
    def change_username_user_submit_command(nu):
        global v
        import mysql.connector as sql
        con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
        cur = con.cursor()
        #
        cur.execute("select * from user where username='{}'".format(nu))
        res = cur.fetchall()
        if cur.rowcount == 0:
            cur.execute('update user set username="{}" where username="{}"'.format(nu, v))
            v = nu
            change_username_window_user.destroy()
        else:
            messagebox.showwarning(" ", "Username already exists!")

    change_username_window_user = Tk()
    change_username_window_user.geometry('240x67')
    change_username_window_user.title('Change Username')
    Label(change_username_window_user,text='Previous Username: ').grid(row=0,column=0)
    Label(change_username_window_user,text='{}'.format(v)).grid(row=0,column=1)
    Label(change_username_window_user,text='New Username').grid(row=1,column=0)
    new_username = Entry(change_username_window_user)
    new_username.grid(row=1, column=1)
    Button(change_username_window_user,text='Submit',command=lambda : change_username_user_submit_command(new_username.get())).grid(row=2,column=0,columnspan=2)
def change_password_user():
    global z
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute('select password from user where username = "{}"'.format(v))
    z = cur.fetchall()
    z = z[0][0]
    def change_password_user_submit_command(np):
        import mysql.connector as sql
        con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
        cur = con.cursor()
        cur.execute('update user set password = "{}" where username ="{}"'.format(np,v))
        change_password_window_user.destroy()
    change_password_window_user = Tk()
    change_password_window_user.title('Change Password')
    change_password_window_user.geometry('240x67')
    Label(change_password_window_user, text='Previous Password: ').grid(row=0, column=0)
    Label(change_password_window_user, text='{}'.format(z)).grid(row=0, column=1)
    Label(change_password_window_user, text='New Password').grid(row=1, column=0)
    new_password = Entry(change_password_window_user)
    new_password.grid(row=1, column=1)
    Button(change_password_window_user, text='Submit',command=lambda: change_password_user_submit_command(new_password.get())).grid(row=2, column=0,columnspan=2)

def sign_out():
    main_window.destroy()
    ls()
def mainwindow_user(u):
    global v
    global main_window
    v = u
    print(u)
    main_window = Tk()
    main_window.title('Main window')
    main_window.geometry('1920x1080')
    main_window.state('zoomed')
    # Frame
    frame1 = Frame(main_window, bg='PaleGreen1', highlightbackground="dark green", highlightthickness=1)
    frame1.pack(side=TOP, fill=X)
    Label(frame1, text='*Name*', bg='PaleGreen1', font=('TkDefaultFont', 16)).pack(side='left', padx=10, pady=5)
    #Menu
    dropmenu = Menubutton(frame1, text='  Menu  ', bg='Light blue', font=('TkDefaultFont', 16), relief=SOLID)
    dropmenu.menu = Menu(dropmenu)
    dropmenu['menu'] = dropmenu.menu

    dropmenu.menu.add_command(label='Profile',command=profile_user)
    dropmenu.menu.add_command(label='Username Reset',command=change_username_user)
    dropmenu.menu.add_command(label='Password Reset',command=change_password_user)
    dropmenu.menu.add_command(label='Sign Out',command=sign_out)

    dropmenu.pack(side=RIGHT, padx=10, pady=5)
    # Image
    bgimg = ImageTk.PhotoImage(Image.open('bgimage.jpg'))
    Label(main_window, image=bgimg).pack(side=TOP, fill=X)

    # Main window features
    main_window.mainloop()'''
def activity():
    activity_window = Toplevel()
    activity_window.title('Activity log')
    activity_window.geometry('1000x600')
    activity_window.resizable(0, 0)

    bg1 = ImageTk.PhotoImage(Image.open('NewImage2.jpeg').resize((1920, 1080), Image.ANTIALIAS))
    canvas12 = Canvas(activity_window, width=1920, height=1080)
    canvas12.pack(fill='both', expand=True)
    canvas12.create_image(960, 540, image=bg1, anchor="center")
    activity_window.mainloop()
def requests():
    def accept_request_submit(tree):
        if len(tree.selection()) ==0:
            messagebox.showwarning('',"You haven't selected a request to accept!")
            requests_window.destroy()
            requests()

        else:
            selected_item = tree.selection()[0]
            unuser = tree.item(selected_item)['values'][1]  #this is the username of the user, who has sent the request, that has been accepted
            date = tree.item(selected_item)['values'][6]
            jdsc = tree.item(selected_item)['values'][5]

            import mysql.connector as sql
            con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
            cur = con.cursor()
            cur.execute("update requests set status = 1 where unprofessional='{}' and unuser='{}' and date = '{}' and jd ='{}'".format(v,unuser,date,jdsc))

            messagebox.showinfo('','Request has been accepted.')
            requests_window.destroy()
            requests()



    requests_window = Toplevel()
    requests_window.title('Requests')
    requests_window.geometry('910x330')
    requests_window.resizable(0, 0)

    bg2 = ImageTk.PhotoImage(Image.open('NewImage2.jpeg').resize((1920, 1080), Image.ANTIALIAS))
    canvas11 = Canvas(requests_window, width=1000, height=600)
    canvas11.pack(fill='both', expand=True)
    canvas11.create_image(500, 300, image=bg2, anchor="center")
    #username(u)(r), address(u), locationcode(u), job desc(r), date(r), phoneno(u)(u)

    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    tree = ttk.Treeview(requests_window)
    tree['columns'] = ('no', 'name', 'address', 'locationcode','phno','job desc','date')
    tree.column('#0', width=0, stretch=NO)
    tree.column('no', width=120, minwidth=25)
    tree.column('name', width=120, minwidth=25)
    tree.column('address', width=120, minwidth=25)
    tree.column('locationcode', width=120, minwidth=25)
    tree.column('phno', width=120, minwidth=25)
    tree.column('job desc', width=120, minwidth=25)
    tree.column('date', width=120, minwidth=25)

    tree.heading('#0', text='', anchor=CENTER)
    tree.heading('no', text='SNo', anchor=CENTER)
    tree.heading('name', text='Name', anchor=CENTER)
    tree.heading('address', text='Address', anchor=CENTER)
    tree.heading('locationcode', text='Location Code', anchor=CENTER)
    tree.heading('phno', text='Phone Number', anchor=CENTER)
    tree.heading('job desc', text='Job Description', anchor=CENTER)
    tree.heading('date', text='Date', anchor=CENTER)
    canvas11.create_window(450,150,window=tree)
    cur.execute("select unuser,jd,date from requests where unprofessional = '{}' and status=0".format(v))
    res1 = cur.fetchall()
    L=[]
    for i in res1:
        cur.execute("select address, locationcode, phoneno from user where username = '{}'".format(i[0]))
        res2 = cur.fetchall()
        t = (i[0],) + res2[0] + (i[1],i[2])
        L.append(t)

    for i in range(len(L)):
        x = (i + 1,) + L[i]
        tree.insert(parent='', index='end', iid=i, values=x)
    butt = Button(requests_window, text='Accept Request',bg='light green', fg='blue',height=2,width=20,command = lambda: accept_request_submit(tree))
    canvas11.create_window(455,285,window = butt)











    requests_window.mainloop()
def search_service():
    global a
    def selection_record(tree):
        '''tree.selection will give us the list of all the data that has been selected.
        tree.item will give us a dictionary which has keys as column headings and values as record values of each row.'''
        # username(p), username(u),date ,job desc

        if len(tree.selection())==0:
            messagebox.showwarning('',"You haven't selected a service provider! Select one to continue.")
            search_service_submit_window.destroy()
            search_service()
        else:
            selected_item = tree.selection()[0]
            userprof = tree.item(selected_item)['values'][1] #this is the username of the professional that the user has selected
            import mysql.connector as sql
            con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
            cur = con.cursor()
            cur.execute("insert into requests values('{}','{}','{}','{}',{})".format(userprof,v,date.get(),jd.get(),0))

            messagebox.showinfo(" ", "Request successfully sent.")
            search_service_submit_window.destroy()
            search_service()




    def search_service_submit(k):
        global date, jd, search_service_submit_window

        if k == 'Select from the listed jobs/services':
            messagebox.showwarning(" ", "SELECT AN APPROPRIATE SERVICE!")
            search_service_window.destroy()
            search_service()
        else:
            search_service_window.destroy()
            search_service_submit_window = Toplevel()
            search_service_submit_window.geometry('700x580+200+100')
            search_service_submit_window.resizable(0, 0)
            canvasx = Canvas(search_service_submit_window, width=1000, height=600)
            canvasx.pack(fill='both', expand=True)
            #bg3 = ImageTk.PhotoImage(Image.open('NewImage2.jpeg').resize((1920, 1080), Image.ANTIALIAS))
            canvasx.create_image(500, 300, image=bg3, anchor="center")
            #username address locationcode date jobdesc sendreq
            import mysql.connector as sql
            con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
            cur = con.cursor()
            tree = ttk.Treeview(search_service_submit_window)
            tree['columns']= ('no','name','address','locationcode','phno')
            tree.column('#0',width=0,stretch=NO)
            tree.column('no', width=120, minwidth=25)
            tree.column('name', width=120, minwidth=25)
            tree.column('address', width=120, minwidth=25)
            tree.column('locationcode', width=120, minwidth=25)
            tree.column('phno', width=120, minwidth=25)

            tree.heading('#0',text='',anchor=CENTER)
            tree.heading('no', text='SNo', anchor=CENTER)
            tree.heading('name', text='Name', anchor=CENTER)
            tree.heading('address', text='Address', anchor=CENTER)
            tree.heading('locationcode', text='Location Code', anchor=CENTER)
            tree.heading('phno', text='Phone Number', anchor=CENTER)
            import mysql.connector as sql
            con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
            cur = con.cursor()
            cur.execute(' select username,address,locationcode,phoneno from professional where locationcode in ({},{},{},{},{}) and profession = "{}"'.format(a-2,a-1,a,a+1,a+2,k))
            res = cur.fetchall()
            for i in range(len(res)):
                x = (i+1,)+res[i]
                tree.insert(parent='', index='end', iid=i ,values=x)
            canvasx.create_window(350, 150, window = tree)
            canvasx.create_text(84,335,text ='Enter date :',font=('TkDefaultFont',11,'bold'))
            date = Entry(search_service_submit_window)
            date.insert(0,'Format : YYYY/MM/DD')
            date.place(x=130,y=320,width=150,height=30)
            canvasx.create_text(84, 370, text='Enter Job Description:', font=('TkDefaultFont', 11, 'bold'))
            jd = Entry(search_service_submit_window)
            jd.place(x=165, y=357, width=400, height=150)
            '''Taking data for further use'''
            # username(p), username(u),date ,job desc
            z = Button(search_service_submit_window, text='Send Request',bg='light green', fg='blue',height=2,width=20,command=lambda : selection_record(tree))
            z.place(x=260,y=530)


    search_service_window = Toplevel()
    search_service_window.title('Service search')
    search_service_window.geometry('520x240+410+230')
    search_service_window.resizable(0, 0)
    bg3 = ImageTk.PhotoImage(Image.open('NewImage2.jpeg').resize((1920, 1080), Image.ANTIALIAS))
    canvas12 = Canvas(search_service_window, width=1000, height=600)
    canvas12.pack(fill='both', expand=True)
    canvas12.create_image(500, 300, image=bg3, anchor="center")
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute("select locationcode from user where username = '{}'".format(v))
    a = cur.fetchall()
    a = int(a[0][0])
    cur.execute('select username,profession from professional where locationcode in ({},{},{},{},{})'.format(a-2,a-1,a,a+1,a+2))
    res = cur.fetchall()
    t = []
    for i in res:
        if i[1] not in t:
            t.append(i[1])
    canvas12.create_text(250, 35,text='Disclaimer : If the service you are looking for is unavailable,\n no professionals are present at the moment in your vicinity\n providing that service.',font=('TkDefaultFont', 11, 'bold'))
    if len(t)!=0:
        canvas12.create_text(250, 110,text='With the help of location code you provided,\n we have filtered all types of professions\n available in your location.',font=('TkDefaultFont', 15, 'bold'))
        n = StringVar()
        n.set('Select from the listed jobs/services')
        menu = OptionMenu(search_service_window, n, *t)
        menu.config(font=('TkDefaultFont',12))

        #menu1 = self.nametowidget(menu.menuname)
        #menu1.config(font=('TkDefaultFont',12))

        canvas12.create_window(250,175,window=menu)
        '''if n.get() != 'Select from the listed jobs/services':
            b = Button(search_service_window,text='Search',bg='light green', fg='blue',command=lambda: search_service_submit(n.get()))
            canvas12.create_window(250,200,window=b)
        else:
            messagebox.showwarning(" ", "SELECT AN APPROPRIATE SERVICE!")'''
        b = Button(search_service_window, text='Search', bg='light green', fg='blue',command=lambda: search_service_submit(n.get()))
        canvas12.create_window(250, 220, window=b)

    else:
        canvas12.create_text(295, 50,
                             text='With the help of location code you provided,\n we have filtered all types of professions\n available in your location.',
                             font=('TkDefaultFont', 15, 'bold'))
        search_service_window.geometry('580x225+410+230')
        canvas12.create_text(290, 150, text='Sorry! There are no professionals in your or near your location.\n Please try again.',font=('TkDefaultFont',14,"italic"),fill='red')

    search_service_window.mainloop()

def request_status():
    rs_window =Toplevel()
    rs_window.title('Location Code selection')
    rs_window.geometry('510x400')
    rs_window.resizable(0, 0)

    bg4 = ImageTk.PhotoImage(Image.open('NewImage2.jpeg').resize((1920, 1080), Image.ANTIALIAS))
    canvas12 = Canvas(rs_window, width=1000, height=600)
    canvas12.pack(fill='both', expand=True)
    canvas12.create_image(500, 300, image=bg4, anchor="center")
    # sno, name, date, status
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute('select unprofessional, date, status from requests where unuser = "{}"'.format(v))
    res = cur.fetchall()
    print(res)

    listBox = Text(rs_window, width=60)
    canvas12.create_window(250, 200, window=listBox)

    listBox.insert(END, "Sno | Name of professional      \t\t |Date      |Status\n")
    listBox.insert(END, "----------------------------------------------------------")
    listBox.insert(END, "\n")

    for i in range(len(res)):
        listBox.insert(END, (i + 1))
        listBox.insert(END, "    |")
        listBox.insert(END, res[i][0])
        listBox.insert(END, "                      \t \t |")
        listBox.insert(END, res[i][1])
        listBox.insert(END, "  \t|")
        if res[i][2]:
            listBox.insert(END, "Accepted")
        else:
            listBox.insert(END, "Not Accepted")
        listBox.insert(END, "\n")


    rs_window.mainloop()


def profile_user():
    global d11
    profile_user_window= Toplevel()
    profile_user_window.title('Profile')
    profile_user_window.geometry('225x270+165+65')
    profile_user_window.resizable(0, 0)
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute('select * from user where username="{}"'.format(v))
    res = cur.fetchall()
    l=list()
    for i in range(len(res[0])):
        l.append(res[0][i])
    print(l)
    Label(profile_user_window, text='Username', font=('TkDefaultFont', 11)).grid(row=0, column=0, padx=10, pady=5)
    Label(profile_user_window, text='Password',font=('TkDefaultFont',11)).grid(row=1, column=0,padx=10,pady=5)
    Label(profile_user_window, text='Name',font=('TkDefaultFont',11)).grid(row=2, column=0,padx=10,pady=5)
    Label(profile_user_window, text='Age',font=('TkDefaultFont',11)).grid(row=3, column=0,padx=10,pady=5)
    Label(profile_user_window, text='Address',font=('TkDefaultFont',11)).grid(row=4, column=0,padx=10,pady=5)
    Label(profile_user_window, text='Pincode',font=('TkDefaultFont',11)).grid(row=5, column=0,padx=10,pady=5)
    Label(profile_user_window, text='Phone Number', font=('TkDefaultFont', 11)).grid(row=6, column=0, padx=10, pady=5)

    Label(profile_user_window, text=l[0],font=('TkDefaultFont',11)).grid(row=0, column=1,padx=10,pady=5)
    Label(profile_user_window, text=l[1],font=('TkDefaultFont',11)).grid(row=1, column=1,padx=10,pady=5)
    Label(profile_user_window, text=l[2],font=('TkDefaultFont',11)).grid(row=2, column=1,padx=10,pady=5)
    Label(profile_user_window, text=l[3],font=('TkDefaultFont',11)).grid(row=3, column=1,padx=10,pady=5)
    Label(profile_user_window, text=l[4],font=('TkDefaultFont',11)).grid(row=4, column=1,padx=10,pady=5)
    Label(profile_user_window, text=l[5],font=('TkDefaultFont',11)).grid(row=5, column=1,padx=10,pady=5)
    Label(profile_user_window, text=l[6], font=('TkDefaultFont', 11)).grid(row=6, column=1, padx=10, pady=5)

def change_username_user():
    def change_username_user_submit_command(nu):
        global v
        import mysql.connector as sql
        con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
        cur = con.cursor()
        #
        cur.execute("select * from user where username='{}'".format(nu))
        res = cur.fetchall()
        if cur.rowcount == 0:
            cur.execute('update user set username="{}" where username="{}"'.format(nu, v))
            v = nu
            change_username_window_user.destroy()
        else:
            messagebox.showwarning(" ", "Username already exists!")

    change_username_window_user = Tk()
    change_username_window_user.geometry('240x67+165+65')
    change_username_window_user.title('Change Username')
    change_username_window_user.resizable(0, 0)
    Label(change_username_window_user,text='Previous Username: ').grid(row=0,column=0)
    Label(change_username_window_user,text='{}'.format(v)).grid(row=0,column=1)
    Label(change_username_window_user,text='New Username').grid(row=1,column=0)
    new_username = Entry(change_username_window_user)
    new_username.grid(row=1, column=1)
    Button(change_username_window_user,text='Submit',command=lambda : change_username_user_submit_command(new_username.get())).grid(row=2,column=0,columnspan=2)
def change_password_user():
    global w
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute('select password from user where username = "{}"'.format(v))
    w = cur.fetchall()
    print(v)
    w = w[0][0]

    def change_password_user_submit_command(np):
        import mysql.connector as sql
        con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
        cur = con.cursor()
        cur.execute('update user set password = "{}" where username ="{}"'.format(np,v))
        change_password_window_user.destroy()
    change_password_window_user = Tk()
    change_password_window_user.title('Change Password')
    change_password_window_user.geometry('240x67+165+65')
    change_password_window_user.resizable(0, 0)
    Label(change_password_window_user, text='Previous Password: ').grid(row=0, column=0)
    Label(change_password_window_user, text='{}'.format(w)).grid(row=0, column=1)
    Label(change_password_window_user, text='New Password').grid(row=1, column=0)
    new_password = Entry(change_password_window_user)
    new_password.grid(row=1, column=1)
    Button(change_password_window_user, text='Submit',command=lambda: change_password_user_submit_command(new_password.get())).grid(row=2, column=0,columnspan=2)
def remove_acc_():
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    def rem():
        o=messagebox.askquestion("Confirm", "Are you sure?")
        if o=='yes':
            cur.execute('delete from user where username="{}"'.format(v))
            main_window.destroy()
            ls()
        else:
            pass
    rem()
def sign_out():
    main_window.destroy()
    ls()
def mainwindow_user(u):
    global v
    global main_window
    v = u
    print(v)
    main_window = Tk()
    main_window.title('Main window')
    main_window.geometry('1000x600+150+50')
    main_window.resizable(0, 0)
    #main_window.state('zoomed')
    # Frame
    frame1 = Frame(main_window, bg='PaleGreen1', highlightbackground="dark green", highlightthickness=1)
    frame1.pack(side=TOP, fill=X)
    Label(frame1, text='*Name*', bg='PaleGreen1', font=('TkDefaultFont', 16)).pack(side='left', padx=10, pady=5)
    #Menu
    dropmenu = Menubutton(frame1, text='  Menu  ', bg='Light blue', font=('TkDefaultFont', 16), relief=SOLID)
    dropmenu.menu = Menu(dropmenu)
    dropmenu['menu'] = dropmenu.menu

    dropmenu.menu.add_command(label='Profile',command=profile_user)
    dropmenu.menu.add_command(label='Username Reset',command=change_username_user)
    dropmenu.menu.add_command(label='Password Reset',command=change_password_user)
    dropmenu.menu.add_command(label='Remove Account', command=remove_acc_)
    dropmenu.menu.add_command(label='Sign Out',command=sign_out)

    dropmenu.pack(side=RIGHT, padx=10, pady=5)
    # Image
    '''
    bg = ImageTk.PhotoImage(Image.open('NewImage1.jpeg').resize((1920, 1080), Image.ANTIALIAS))
    x=Label(main_window,image=bg)
    x.place(x=0,y=45)
    Label(main_window,text='he').pack()
    '''
    bg = ImageTk.PhotoImage(Image.open('NewImage1.jpeg').resize((1920, 1080), Image.ANTIALIAS))
    canvas = Canvas(main_window, width=1920,height=1080)
    canvas.pack(fill='both', expand=True)
    canvas.create_image(960, 540, image=bg, anchor="center")
    #
    homepage = ImageTk.PhotoImage(Image.open('Homepage.png').resize((1010, 390), Image.ANTIALIAS))
    canvas.create_image(510,20,image=homepage, anchor="n")
    button2 = Button(main_window, text="Request Status",font=('arial',12,'bold'),height=3,width=30, bg='light green', fg='blue',command=request_status)
    button1 = Button(main_window, text="Search For Services",font=('arial',12,'bold'),height=3,width=30, bg='light green', fg='blue',command=search_service)
    canvas.create_window(150, 430,anchor='nw',window=button1)
    canvas.create_window(550, 430,anchor='nw', window=button2)


    # Main window features
    main_window.mainloop()


#***********************************************************************************************************************

def profile_professional():
    global c11
    profile_professional_window= Toplevel()
    profile_professional_window.title('Profile')
    profile_professional_window.geometry('225x270+165+65')
    profile_professional_window.resizable(0, 0)
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute('select * from professional where username="{}"'.format(v))
    res = cur.fetchall()
    l=list()
    for i in range(len(res[0])):
        l.append(res[0][i])
    print(l)
    Label(profile_professional_window, text='Username',font=('TkDefaultFont',11)).grid(row=0, column=0,padx=10,pady=5)
    Label(profile_professional_window, text='Password',font=('TkDefaultFont',11)).grid(row=1, column=0,padx=10,pady=5)
    Label(profile_professional_window, text='Name',font=('TkDefaultFont',11)).grid(row=2, column=0,padx=10,pady=5)
    Label(profile_professional_window, text='Age',font=('TkDefaultFont',11)).grid(row=3, column=0,padx=10,pady=5)
    Label(profile_professional_window, text='Profession',font=('TkDefaultFont',11)).grid(row=4, column=0,padx=10,pady=5)
    Label(profile_professional_window, text='Address',font=('TkDefaultFont',11)).grid(row=5, column=0,padx=10,pady=5)
    Label(profile_professional_window, text='Pincode',font=('TkDefaultFont',11)).grid(row=6, column=0,padx=10,pady=5)
    Label(profile_professional_window, text='Phone Number', font=('TkDefaultFont', 11)).grid(row=7, column=0, padx=10,pady=5)

    Label(profile_professional_window, text=l[0],font=('TkDefaultFont',11)).grid(row=0, column=1,padx=10,pady=5)
    Label(profile_professional_window, text=l[1],font=('TkDefaultFont',11)).grid(row=1, column=1,padx=10,pady=5)
    Label(profile_professional_window, text=l[2],font=('TkDefaultFont',11)).grid(row=2, column=1,padx=10,pady=5)
    Label(profile_professional_window, text=l[3],font=('TkDefaultFont',11)).grid(row=3, column=1,padx=10,pady=5)
    Label(profile_professional_window, text=l[4],font=('TkDefaultFont',11)).grid(row=4, column=1,padx=10,pady=5)
    Label(profile_professional_window, text=l[5],font=('TkDefaultFont',11)).grid(row=5, column=1,padx=10,pady=5)
    Label(profile_professional_window, text=l[6],font=('TkDefaultFont',11)).grid(row=6, column=1,padx=10,pady=5)
    Label(profile_professional_window, text=l[7], font=('TkDefaultFont', 11)).grid(row=7, column=1, padx=10, pady=5)

def change_username_professional():
    def change_username_professional_submit_command(nu):
        global v
        import mysql.connector as sql
        con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
        cur = con.cursor()
        #
        cur.execute("select * from professional where username='{}'".format(nu))
        res = cur.fetchall()
        if cur.rowcount == 0:
            cur.execute('update professional set username="{}" where username="{}"'.format(nu, v))
            v = nu
            change_username_window_professional.destroy()
        else:
            messagebox.showwarning(" ", "Username already exists!")

    change_username_window_professional = Tk()
    change_username_window_professional.geometry('240x67+165+65')
    change_username_window_professional.title('Change Username')
    change_username_window_professional.resizable(0, 0)
    Label(change_username_window_professional,text='Previous Username: ').grid(row=0,column=0)
    Label(change_username_window_professional,text='{}'.format(v)).grid(row=0,column=1)
    Label(change_username_window_professional,text='New Username').grid(row=1,column=0)
    new_username = Entry(change_username_window_professional)
    new_username.grid(row=1, column=1)
    Button(change_username_window_professional,text='Submit',command=lambda : change_username_professional_submit_command(new_username.get())).grid(row=2,column=0,columnspan=2)
def change_password_professional():
    global w
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute('select password from professional where username ="{}"'.format(v))
    w = cur.fetchall()
    w = w[0][0]
    def change_password_professional_submit_command(np):
        import mysql.connector as sql
        con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
        cur = con.cursor()
        cur.execute('update professional set password = "{}" where username ="{}"'.format(np,v))
        change_password_window_professional.destroy()
    change_password_window_professional = Tk()
    change_password_window_professional.title('Change Password')
    change_password_window_professional.geometry('240x67+165+65')
    change_password_window_professional.resizable(0, 0)
    Label(change_password_window_professional, text='Previous Password: ').grid(row=0, column=0)
    Label(change_password_window_professional, text='{}'.format(w)).grid(row=0, column=1)
    Label(change_password_window_professional, text='New Password').grid(row=1, column=0)
    new_password = Entry(change_password_window_professional)
    new_password.grid(row=1, column=1)
    Button(change_password_window_professional, text='Submit',command=lambda: change_password_professional_submit_command(new_password.get())).grid(row=2, column=0,columnspan=2)
'''def change_address_professional():
    global w
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    cur.execute('select address from professional where username ="{}"'.format(v))
    w = cur.fetchall()
    w = w[0][0]
    def change_address_professional_submit_command(np):
        import mysql.connector as sql
        con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
        cur = con.cursor()
        cur.execute('update professional set address = "{}" where username ="{}"'.format(np,v))
        change_address_window_professional.destroy()
    change_address_window_professional = Tk()
    change_address_window_professional.title('Change Address')
    change_address_window_professional.geometry('300x100+165+65')
    change_address_window_professional.resizable(0, 0)
    Label(change_address_window_professional, text='Previous Address: ').grid(row=0, column=0)
    Label(change_address_window_professional, text='{}'.format(w)).grid(row=0, column=1)
    Label(change_address_window_professional, text='New Address').grid(row=1, column=0)
    new_address = Entry(change_address_window_professional)
    new_address.grid(row=1, column=1)
    Button(change_address_window_professional, text='Submit',command=lambda: change_address_professional_submit_command(new_address.get())).grid(row=2, column=0,columnspan=2)'''
def remove_acc():
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    def rem():
        o=messagebox.askquestion("Confirm", "Are you sure?")
        if o=='yes':
            cur.execute('delete from professional where username="{}"'.format(v))
            main_window.destroy()
            ls()
        else:
            pass
    rem()

def sign_out():
    main_window.destroy()
    ls()
def mainwindow_professional(u):
    global v
    global main_window
    v = u
    main_window = Tk()
    main_window.title('Main window')
    main_window.geometry('1000x600+150+50')
    main_window.resizable(0, 0)
    #main_window.state('zoomed')
    # Frame
    frame1 = Frame(main_window, bg='PaleGreen1', highlightbackground="dark green", highlightthickness=1)
    frame1.pack(side=TOP, fill=X)
    Label(frame1, text='*Name*', bg='PaleGreen1', font=('TkDefaultFont', 16)).pack(side='left', padx=10, pady=5)
    #Menu
    dropmenu = Menubutton(frame1, text='  Menu  ', bg='Light blue', font=('TkDefaultFont', 16), relief=SOLID)
    dropmenu.menu = Menu(dropmenu)
    dropmenu['menu'] = dropmenu.menu

    dropmenu.menu.add_command(label='Profile',command=profile_professional)
    dropmenu.menu.add_command(label='Username Reset',command=change_username_professional)
    dropmenu.menu.add_command(label='Password Reset',command=change_password_professional)
    dropmenu.menu.add_command(label='Remove Account', command=remove_acc)
    dropmenu.menu.add_command(label='Sign Out', command=sign_out)
    #A one stop platform for Reliable and Prompt service in installation, maintenance and repair for all your home gadgets, appliances, items and products. This covers plumbing, electrical, white goods, carpentry, painting and similar home and utility services.
    #One click and get a quote!
    dropmenu.pack(side=RIGHT, padx=10, pady=5)
    # Image
    bg = ImageTk.PhotoImage(Image.open('NewImage1.jpeg').resize((1920, 1080), Image.ANTIALIAS))
    canvas = Canvas(main_window, width=1920, height=1080)
    canvas.pack(fill='both', expand=True)
    canvas.create_image(960, 540, image=bg, anchor="center")
    homepage = ImageTk.PhotoImage(Image.open('Homepage prof.png').resize((1010, 390), Image.ANTIALIAS))
    canvas.create_image(510, 20, image=homepage, anchor="n")
    button1 = Button(main_window, text="View requests", font=('arial', 12, 'bold'), height=3, width=30,bg='light green', fg='blue', command=requests)
    canvas.create_window(350, 430, anchor='nw', window=button1)

    # Main window features
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
    cur = con.cursor()
    main_window.mainloop()


lc = [('Adyar', 20),
         ('Ambattur', 21),
         ('Anna Nagar', 22),
         ('Ashok Nagar', 23),
         ('Avadi', 24),
         ('Ayanavaram', 25),
         ('Egmore', 26),
         ('Ennore', 27),
         ('Flower Bazaar', 28),
         ('Guindy', 29),
         ('Harbour', 30),
         ('High Court', 31),
         ('Kilpauk', 32),
         ('Kotturpuram', 33),
         ('Koyambedu', 34),
         ('Madhavaram', 35),
         ('Madipakkam', 36),
         ('Meenambakkam', 37),
         ('Mylapore', 38),
         ('Neelankarai', 39),
         ('Nungambakkam', 40),
         ('Pallavaram', 41),
         ('Pattabiram', 42),
         ('Poonamallee', 43),
         ('Port Marine', 44),
         ('Puliyanthope', 45),
         ('Puzhal', 46),
         ('Royapettah', 47),
         ('Royapuram', 48),
         ('Saidapet', 49),
         ('Selaiyur', 50),
         ('Sembium', 51),
         ('SRMC', 52),
         ('St.Thomas Mount', 53),
         ('T.Nagar', 54),
         ('Tambaram', 55),
         ('Taramani', 56),
         ('Teynampet', 57),
         ('Thirumangalam', 58),
         ('Thiruvottiyur', 59),
         ('Thuraipakkam', 60),
         ('Triplicane', 61),
         ('Vadapalani', 62),
         ('Valasaravakkam', 63),
         ('Vepery', 64),
         ('Villivakkam', 65),
         ('Washermenpet', 66)
         ]
def ls():
    # adding details to table after entry for signup and checking wheteher username is unique or not
    def signup_professional_submit():
        count = 0
        import mysql.connector as sql
        con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
        cur = con.cursor()
        cur.execute("select * from professional where username='{}'".format(a1.get()))
        res = cur.fetchall()
        #Username existence check
        if cur.rowcount == 0:
            for i in str(a4.get()):
                if i not in '0123456789':
                    count += 1
            if count != 0:
                messagebox.showwarning(' ', "Age entered is not a number!")
            else:
                cur.execute("insert into professional values('{}','{}','{}',{},'{}','{}','{}',{})".format(a1.get(), a2.get(), a3.get(), a4.get(), a5.get(), a6.get(), a7.get(),a8.get()))
                messagebox.showinfo(" ", "ACCOUNT CREATION SUCCESSFUL")
                root_sp.destroy()
                root_s.destroy()
        else:
            messagebox.showwarning(" ", "Username already exists!")
        #Age should be a number



    def signup_user_submit():
        count=0
        import mysql.connector as sql
        con = sql.connect(host='localhost', user='root', password='2810', database='kdproject', autocommit=True)
        cur = con.cursor()
        cur.execute("select * from professional where username='{}'".format(b1.get()))
        res = cur.fetchall()
        if cur.rowcount == 0:
            for i in str(b4.get()):
                if i not in '0123456789':
                    count+=1
            if count != 0:
                messagebox.showwarning(' ', "Age entered is not a number!")
            else:
                cur.execute("insert into user values('{}','{}','{}',{},'{}','{}',{})".format(b1.get(), b2.get(), b3.get(), b4.get(), b5.get(), b6.get(), b7.get()))
                messagebox.showinfo(" ", "ACCOUNT CREATION SUCCESSFUL")
                root_su.destroy()
                root_s.destroy()

        else:
            messagebox.showwarning(" ", "Username already exists!")
    # signup professional and user

    def lc_refer():
        '''lc_refer_window = Tk()
        lc_refer_window.title('Location Codes')
        lc_refer_window.geometry('290x300+460+260')
        lc_refer_window.resizable(0, 0)
        lc_frame1 = Frame(lc_refer_window, width=600, height=600)
        lc_frame1.pack(fill=BOTH,expand=1)'''

        lc_frame1 = Tk()
        lc_frame1.geometry('90x250+460+260')
        scrollbar = Scrollbar(lc_frame1)
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox(lc_frame1, yscrollcommand=scrollbar.set)
        for i in range(46):
            mylist.insert(END, "{}       {}".format(lc[i][0], lc[i][1]))

        mylist.pack(side=LEFT, fill=BOTH,expand=True)


        scrollbar.config(command=mylist.yview)
        lc_frame1.mainloop()

        '''lc_canvas = Canvas(lc_frame1)
        lc_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        scrollbar = ttk.Scrollbar(lc_frame1, orient=VERTICAL,command= lc_canvas.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        lc_canvas.configure(yscrollcommand=scrollbar.set)
        lc_canvas.bind('<Configure>',lambda e: lc_canvas.configure(scrollregion = lc_canvas.bbox('all')))
        lc_frame2 = Frame(lc_canvas)

        lc_canvas.create_window(0,0,window =lc_frame2)
        Label(lc_frame2,text='WHAT IS LOCATION CODE',font=('TkDefaultFont',12 ,'bold')).grid(row=0,column=0,columnspan=2)
        Label(lc_frame2, text='Every area has a particular numeric location code,\n which helps us reach to you at the earliest', font=('TkDefaultFont', 10)).grid(row=1, column=0,columnspan=2)

        for i in range(len(lc)):
            Label(lc_frame2, text=lc[i][0]).grid(row=i+2, column=0)
            Label(lc_frame2, text=lc[i][1]).grid(row=i+2, column=1)'''
        '''for i in range(len(lc)):
            Label(lc_refer_window,text=lc[i][0]).grid(row=2+i,column=0)
            Label(lc_refer_window, text=lc[i][1]).grid(row=2+i, column=1)
        scrollbar = Scrollbar(lc_refer_window,orient=VERTICAL)
        scrollbar.grid(row=0,column=2,sticky='ns')

        lc_refer_window.mainloop()'''
    def signup_professional():
        global a1, a2, a3, a4, a5, a6, a7, a8, root_sp
        root_sp = Toplevel()
        root_sp.geometry('280x240+440+240')
        root_sp.title('Create a professional account')
        root_sp.resizable(0, 0)
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
        Label(root_sp, text='Enter *Location Code').grid(row=6, column=0)
        a7 = Entry(root_sp)
        a7.grid(row=6, column=1, columnspan=1)
        Label(root_sp, text='Enter Phone Number').grid(row=7, column=0)
        a8 = Entry(root_sp)
        a8.grid(row=7, column=1, columnspan=1)
        Label(root_sp,text='* Refer for Location Codes').grid(row=8,column=0,pady=10)
        Button(root_sp, text='Click here', command=lc_refer, bg='light green', fg='blue').grid(row=8,column=1,columnspan=2)


        Button(root_sp, text='Submit', command=signup_professional_submit, bg='light green', fg='blue').grid(row=9, column=0,columnspan=2)
    def signup_user():
        global b1, b2, b3, b4, b5, b6,b7, root_su
        root_su = Toplevel()
        root_su.geometry('280x240+440+240')
        root_su.title('Create a user account')
        root_su.resizable(0, 0)
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
        Label(root_su, text='Enter *Location Code').grid(row=5, column=0)
        b6 = Entry(root_su)
        b6.grid(row=5, column=1, columnspan=1)
        Label(root_su, text='Enter Phone Number').grid(row=6, column=0)
        b7 = Entry(root_su)
        b7.grid(row=6, column=1, columnspan=1)
        Label(root_su, text='* Refer for Location Codes').grid(row=7, column=0, pady=10)
        Button(root_su, text='Click here', command=lc_refer, bg='light green', fg='blue').grid(row=7, column=1,columnspan=2)

        Button(root_su, text='Submit', command=signup_user_submit, bg='light green', fg='blue').grid(row=8, column=0,
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
            root_lp.destroy()
            root_l.destroy()
            messagebox.showwarning(" ", "Username does not exist!")
        else:
            for i in res:
                if i[1] != c2.get():
                    root_lp.destroy()
                    root_l.destroy()
                    messagebox.showwarning(" ", "Incorrect password")

                else:
                    root_lp.destroy()
                    root_l.destroy()
                    root.destroy()
                    mainwindow_professional(c11)
    def login_user_submit():
        global d11
        import mysql.connector as sql
        con = sql.connect(host="localhost", user="root", password="2810", database="kdproject", autocommit=True)
        cur = con.cursor()
        cur.execute('select * from user where username="{}"'.format(d1.get()))
        res = cur.fetchall()
        d11= d1.get()
        if cur.rowcount == 0:
            root_lu.destroy()
            root_l.destroy()
            messagebox.showwarning(" ", "Username does not exist!")
        else:
            for i in res:
                if i[1] != d2.get():
                    root_lu.destroy()
                    root_l.destroy()
                    messagebox.showwarning(" ", "Incorrect password")

                else:
                    root_lu.destroy()
                    root_l.destroy()
                    root.destroy()
                    print(d11)
                    mainwindow_user(d11)

    # login professional and user
    def login_professional():
        global root_lp
        global c1, c2, c11, c22
        root_lp = Toplevel()
        root_lp.geometry("220x75+440+240")
        root_lp.resizable(0, 0)
        root_lp.title("Professional Login")
        # details
        Label(root_lp, text="Enter Username").grid(row=0, column=0)
        c1 = Entry(root_lp)
        c1.grid(row=0, column=1)
        Label(root_lp, text="Enter Password").grid(row=1, column=0)
        c2 = Entry(root_lp, show="*")
        c2.grid(row=1, column=1)
        c11=c1.get()
        c22=c2.get()
        Button(root_lp, text="Login", command=login_professional_submit, bg='light green', fg='blue').grid(row=3, column=0,columnspan=2)
        print(c11)
    def login_user():
        global root_lu
        global d1, d2, d11, d22
        root_lu = Toplevel()
        root_lu.geometry("220x75+440+240")
        root_lu.resizable(0, 0)
        root_lu.title("User Login")
        # details
        Label(root_lu, text="Enter Username").grid(row=0, column=0)
        d1 = Entry(root_lu)
        d1.grid(row=0, column=1)
        Label(root_lu, text="Enter Password").grid(row=1, column=0)
        d2 = Entry(root_lu, show="*")
        d2.grid(row=1, column=1)
        d11 = StringVar()
        d11 = d1.get()
        d22 = d2.get()
        Button(root_lu, text="Login", command=login_user_submit, bg='light green', fg='blue').grid(row=3, column=0,columnspan=2)
        print(d11)
    # ********************************************************
    def signup():
        global root_s
        root_s = Toplevel()
        root_s.geometry('400x250+420+220')
        root_s.resizable(0, 0)
        root_s.title('Sign Up')
        Label(root_s, text='What kind of an account do you want to create?', font=('arial', 10, 'bold')).grid(row=0,column=0,columnspan=2)

        # Buttons
        Button(root_s, text='Professional Account', command=signup_professional, bg='light green', fg='blue').grid(row=2,column=0,pady=1,padx=50)
        Button(root_s, text='User Account', command=signup_user, bg='light green', fg='blue').grid(row=2, column=1, pady=10,padx=20)
    def login():
        global root_l
        root_l = Toplevel()
        root_l.geometry('400x250+420+220')
        root_l.resizable(0, 0)
        root_l.title('Login')
        Label(root_l, text='With which account do you want to login with?', font=('arial', 10, 'bold')).grid(row=0,column=0,columnspan=2)

        Button(root_l, text='Professional Account', command=login_professional, bg='light green', fg='blue').grid(row=2,column=0,pady=10,padx=50)
        Button(root_l, text='User Account', command=login_user, bg='light green', fg='blue').grid(row=2, column=1, pady=10,padx=20)

    #MAINROOT(askinf for signup or login)
    root = Tk()
    #sw=root.winfo_screenwidth(); sh=root.winfo_screenheight()
    #root.geometry('300x105+{}+{}'.format(int((sw / 2) - 150), int((sh / 2) - 52.5)))
    root.geometry('300x105+400+200')
    root.resizable(0, 0)
    root.title('EntryPage')
    root.configure(bg='#C5FFFA')
    Label(root, text='Create a new account?', font=('arial', 12, 'bold'),bg='#C5FFFA').pack()
    b_signup = Button(root, text='Sign Up', command=signup, bg='light green', fg='blue').pack()
    Label(root, text='Account exists already?', font=('arial', 12, 'bold'),bg='#C5FFFA').pack()
    b_login = Button(root, text='Login', command=login, bg='light green', fg='blue').pack()
    root.mainloop()
ls()





