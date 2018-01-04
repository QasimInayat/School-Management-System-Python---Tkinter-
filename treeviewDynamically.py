from tkinter import  *
import sqlite3
import tkinter.ttk as ttk
from  PIL import *

class SampleApp(Tk):
    def __init__(self, *root, **master):
        Tk.__init__(self, *root, **master)
        self.geometry("600x500+350+100")
        self.title("LOGIN")
        self.config(bg="#4EC0A0")
        self.label = Label(background='#4EC0A0', foreground='black',font=(("Helvetica", "16") ))
        self.label.pack(padx=10, pady=10)


        self.label = Label(text="USERNAME", background='#4EC0A0', foreground='black')
        self.label.place(x=150,y=200)
        global LOGIN_USERNAME
        LOGIN_USERNAME = StringVar()

        self.uname = Entry(self,textvariable=LOGIN_USERNAME)
        self.uname.place(x=250,y=200)
        self.uname.focus()
        self.label = Label(text="PASSWORD", background='#4EC0A0', foreground='black')
        self.label.place(x=150,y=250)
        global LOGIN_PASSWORD
        LOGIN_PASSWORD = StringVar()
        self.password = Entry(self,textvariable=LOGIN_PASSWORD)
        self.password.place(x=250, y=250)



        self.btn = Button(text="LOGIN",command=showwin1,relief="raise")
        self.btn.place(x=330,y=300)


        self.lbl_showtext = Label( text="Please enter username and password",bg="#4EC0A0",fg="black")
        self.lbl_showtext.place(x=200,y=400)




def Database():
    global conn, cursor
    conn = sqlite3.connect('pythontut.db')
    cursor = conn.cursor()
    print("database connected")

    cursor.execute("CREATE TABLE IF NOT EXISTS `book` (book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, accession TEXT, entrydate TEXT, title TEXT, publisher TEXT, editor TEXT, subtitle TEXT,price TEXT,vendor TEXT)")


def showwin1():
    global win1
    users = LOGIN_USERNAME.get()
    passd = LOGIN_PASSWORD.get()
    Database()
    finduser = ("SELECT * FROM 'member' WHERE username= ? and password = ?")
    cursor.execute(finduser,[(users.lstrip()),(passd.lstrip())])
    results = cursor.fetchall()



    if results:
        root.destroy()
        win1 = MenuWindow()
    else:
        root.lbl_showtext.config(text="Uername and password is INVALID!!!",bg="#4EC0A0",fg="red")
        LOGIN_USERNAME.set("")
        LOGIN_PASSWORD.set("")

        print("SORRY")



def distroy_win1():
    global win1
    win1.destroy()


def show_add_recor_window():

    win1.destroy()
    win2 = insert_record()

class MenuWindow(Tk):
    def __init__(self, *win1, **win1master):
        Tk.__init__(self, *win1, **win1master)

        self.geometry("1000x600+180+70")
        self.title("Main-Menu")
        self.config(bg="#4EC0A0")
        self.label = Label(text="WELCOME TO THE LIBRARY MANAGEMENT SYSTEM", background='#4EC0A0', foreground='black',font=(("Helvetica", "16") ))
        self.label.pack(padx=10, pady=10)


        self.btn1 = Button( height=100, width=100, text="ADD+",bg="#99D7C9",compound="top",font=(("Helvetica", "10","bold")),relief="raised",command=show_add_recor_window)
       # keep a referernce variavble like that self.btn1.image = self.ph1
        self.btn1.place(x=150, y=150)

        self.btn1 = Button(height=100, width=100, text="UPDATE",compound="top",bg="#99D7C9",font=(("", "10","bold") ),command=show_update_window)
        self.btn1.place(x=350, y=150)

        self.btn1 = Button( height=100, width=100, text="DELETE ",bg="#99D7C9",command=show_delete_window,compound="top",font=(("Helvetica", "10","bold") ))
        self.btn1.place(x=150, y=300)

        self.btn1 = Button( height=100, width=100, text="SHOW",compound="top",bg="#99D7C9",font=(("Helvetica", "10","bold") ),command=show_records_window)
        self.btn1.place(x=350, y=300)


        self.btn_back = Button(text="LOGOUT",command=back_login_window)
        self.btn_back.place(x=500, y=450)
def back_login_window():
    win1.destroy()
    SampleApp()



class insert_record(Tk):
    def __init__(self, *win2, **win2master):
        Tk.__init__(self, *win2, **win2master)
        self.geometry("1000x600+180+70")

        self.bg ="#4EC0A0"
        self.config(bg=self.bg)

        self.lbl = Label(text="ADD A NEW BOOK RECORD",font=(("Helvetica", "16") ))
        self.lbl.place(x=100,y=20)
        global ACCESSION
        global ENTRYDATE
        global TITLE
        global PUBLISHER
        global EDITOR
        global SUBTITLE
        global PRICE
        global VENDOR
        # ==========variables#==================
        ACCESSION = StringVar()
        ENTRYDATE = StringVar()
        TITLE = StringVar()
        PUBLISHER = StringVar()
        EDITOR = StringVar()
        SUBTITLE = StringVar()
        PRICE = StringVar()
        VENDOR = StringVar()
        self.lbl_Accession_number = Label( text="Accession No", font=("Helvetica", 16)).place(x=30, y=50)
        self.lbl_Entry_data = Label( text="Entry Date", font=("Helvetica", 16)).place(x=30, y=100)
        self.lbl_Title = Label( text="Title", font=("Helvetica", 16)).place(x=30, y=150)
        self.lbl_Publisher = Label( text="Publisher", font=("Helvetica", 16)).place(x=30, y=200)
        self.lbl_Editor = Label( text="Editor", font=("Helvetica", 16)).place(x=30, y=250)
        self.lbl_Subtitle = Label( text="Sub-Title", font=("Helvetica", 16)).place(x=30, y=300)
        self.lbl_Price = Label( text="Price", font=("Helvetica", 16)).place(x=30, y=350)
        self.lbl_Vendor = Label( text="Vendor", font=("Helvetica", 16)).place(x=30, y=400)

        # ===================Entry===================================#
        self.ent_Accession_number = Entry( textvariable=ACCESSION).place(x=200, y=55)
        self.ent_Entry_data = Entry( textvariable=ENTRYDATE).place(x=200, y=110)
        self.ent_Title = Entry( textvariable=TITLE).place(x=200, y=150)
        self.ent_Publisher = Entry( textvariable=PUBLISHER).place(x=200, y=200)
        self.ent_Editor = Entry( textvariable=EDITOR).place(x=200, y=250)
        self.ent_Subtitle = Entry( textvariable=SUBTITLE).place(x=200, y=300)
        self.ent_Price = Entry( textvariable=PRICE).place(x=200, y=350)
        self.ent_Vendor = Entry( textvariable=VENDOR).place(x=200, y=400)
        self.btn_add = Button( text="Add+", font=("Helvetica", 16), command=add_book).place(x=350,y=450)
        self.lbl_add = Label(text="Complete",fg="red").place(x=250,y=450)
        self.btn_back_home=Button(text="BACK",font=("Helvetica", 16),command=back_to_home).place(x=450,y=450)
def add_book():

    if  ACCESSION.get() == "" or ENTRYDATE.get() == "" or TITLE.get() == "" or PUBLISHER.get() == "" or EDITOR.get() == "" or SUBTITLE.get() == "" or PRICE.get() == "" or VENDOR.get() == "":

        print("PLEASE INSERT ALL BOOK DATA")

    else:

        Database()
    #bad ma configure karna hoga
        cursor.execute("INSERT INTO 'book' (accession, entrydate, title, publisher, editor, subtitle,price,vendor) VALUES(?, ?, ?, ?, ?, ?,?,?)",  (str(ACCESSION.get()), str(ENTRYDATE.get()), str(TITLE.get()), str(PUBLISHER.get()), str(EDITOR.get()), str(SUBTITLE.get()), str(PRICE.get()), str(VENDOR.get())))
        print("query runnning")
        conn.commit()
        print("BOOK RECORD INSERTED")
        ACCESSION.set("yes me running")
        ENTRYDATE.set("")
        TITLE.set("")
        PUBLISHER.set("")
        EDITOR.set("")
        SUBTITLE.set("")
        PRICE.set("")
        VENDOR.set("")
        cursor.close()
        conn.close()
def back_to_home():
    win1.destroy()

    print("sabar")

class update_record(Tk):
    def __init__(self, *win3, **win3master):
        Tk.__init__(self, *win3, **win3master)

        self.geometry("1000x600+180+70")
################# FRAMES
        self.Top = Frame(self, width=900, height=50, bd=8, relief="raise")
        self.Top.pack(side=TOP)
        self.Left = Frame(self, width=300, height=500, bd=8, relief="raise")
        self.Left.pack(side=LEFT)
        self.Right = Frame(self, width=600, height=500, bd=8, relief="raise")
        self.Right.pack(side=RIGHT)
        self.Forms = Frame(self, width=300, height=450)
        self.Forms.pack(side=TOP)
        self.Buttons = Frame(self.Right, width=300, height=100, bd=8, relief="raise")
        self.Buttons.pack(side=BOTTOM)
        global ACCESSION_UP
        global ENTRYDATE_UP
        global TITLE_UP
        global PUBLISHER_UP
        global EDITOR_UP
        global SUBTITLE_UP
        global PRICE_UP
        global VENDOR_UP
        ACCESSION_UP = StringVar()
        ENTRYDATE_UP = StringVar()
        TITLE_UP = StringVar()
        PUBLISHER_UP = StringVar()
        EDITOR_UP = StringVar()
        SUBTITLE_UP = StringVar()
        PRICE_UP = StringVar()
        VENDOR_UP = StringVar()

        self.lbl_Accession_number = Label(self.Left,text="Accession No",bg="White", font=("Helvetica", 8)).place(x=30, y=50)
        self.lbl_Entry_data = Label(self.Left,text="Entry Date", font=("Helvetica", 8)).place(x=30, y=100)
        self.lbl_Title = Label(self.Left,text="Title", font=("Helvetica", 8)).place(x=30, y=150)
        self.lbl_Publisher = Label(self.Left,text="Publisher", font=("Helvetica", 8)).place(x=30, y=200)
        self.lbl_Editor = Label(self.Left,text="Editor", font=("Helvetica", 8)).place(x=30, y=250)
        self.lbl_Subtitle = Label(self.Left,text="Sub-Title", font=("Helvetica", 8)).place(x=30, y=300)
        self.lbl_Price = Label(self.Left,text="Price", font=("Helvetica", 8)).place(x=30, y=350)
        self.lbl_Vendor = Label(self.Left,text="Vendor", font=("Helvetica", 8)).place(x=30, y=400)
#################ENTRIES OF UPDATE WINDOW
        self.ent_Accession_number = Entry(self.Left,textvariable=ACCESSION_UP).place(x=150, y=50)
        self.ent_Entry_data = Entry(self.Left,textvariable=ENTRYDATE_UP).place(x=150, y=100)
        self.ent_Title = Entry(self.Left,textvariable=TITLE_UP).place(x=150, y=150)
        self.ent_Publisher = Entry(self.Left,textvariable=PUBLISHER_UP).place(x=150, y=200)
        self.ent_Editor = Entry(self.Left,textvariable=EDITOR_UP).place(x=150, y=250)
        self.ent_Subtitle = Entry(self.Left,textvariable=SUBTITLE_UP).place(x=150, y=300)
        self.ent_Price = Entry(self.Left,textvariable=PRICE_UP).place(x=150, y=350)
        self.ent_Vendor = Entry(self.Left,textvariable=VENDOR_UP).place(x=150, y=400)


        self.btn_show = Button(self.Buttons, text="SHOW RECORD", command=update_show)
        self.btn_show.pack(side=LEFT)

        self.btn_back = Button(self.Buttons, text="BACK", command=back_win3_to_menu)
        self.btn_back.pack(side=RIGHT)
        self.btn_update = Button(self.Buttons, text="Update",command=update_Data)
        self.btn_update.pack(side=RIGHT)

        # ==================================LIST WIDGET========================================
        # ==================================LIST WIDGET========================================
        global tree
        scrollbary = Scrollbar(self.Right, orient=VERTICAL)
        scrollbarx = Scrollbar(self.Right, orient=HORIZONTAL)
        tree = ttk.Treeview(self.Right, columns=(
        "id", "accession", "entrydate", "title", "publisher", "editor", "sub-title", "price", "vendor"),
                            selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('id', text="ID", anchor=W)
        tree.heading('accession', text="ACCESSION.NO", anchor=W)
        tree.heading('entrydate', text="ENTRYDATE", anchor=W)
        tree.heading('title', text="TITLE", anchor=W)
        tree.heading('publisher', text="PUBLISHER", anchor=W)
        tree.heading('editor', text="EDITOR", anchor=W)
        tree.heading('sub-title', text="SUB-TITLE", anchor=W)
        tree.heading('price', text="PRICE", anchor=W)
        tree.heading('vendor', text="VENDOR", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=80)
        tree.column('#2', stretch=NO, minwidth=0, width=120)
        tree.column('#3', stretch=NO, minwidth=0, width=80)
        tree.column('#4', stretch=NO, minwidth=0, width=150)
        tree.column('#5', stretch=NO, minwidth=0, width=120)
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        tree.column('#7', stretch=NO, minwidth=0, width=120)
        tree.column('#8', stretch=NO, minwidth=0, width=120)
        tree.bind('<ButtonRelease-1>', select_data)
        tree.pack()
def select_data(a):

    tst_data = tree.item(tree.selection())
    print("THE VALUES",type(tst_data),tst_data)
    item = tree.selection()[0]
    print(item)
    global update_tree_id


    update_tree_id = tree.item(item)['values'][0]
    print(update_tree_id)
    ACCESSION_UP.set(tree.item(item)['values'][1])
    ENTRYDATE_UP.set(tree.item(item)['values'][2])
    TITLE_UP.set(tree.item(item)['values'][3])
    PUBLISHER_UP.set(tree.item(item)['values'][4])
    EDITOR_UP.set(tree.item(item)['values'][5])
    SUBTITLE_UP.set(tree.item(item)['values'][6])
    PRICE_UP.set(tree.item(item)['values'][7])
    VENDOR_UP.set(tree.item(item)['values'][8])
def back_win3_to_menu():
    win3.withdraw()

#####ye function values set karaega text field pe upadte k form ma
def update_Data():

    accessionno = ACCESSION_UP.get()
    entrydate =ENTRYDATE_UP.get()
    title = TITLE_UP.get()
    publisher =PUBLISHER_UP.get()
    editor =EDITOR_UP.get()
    subtitle=SUBTITLE_UP.get()
    price = PRICE_UP.get()
    vendor = VENDOR_UP.get()
    try:
        Database()
        upd_query = (" UPDATE 'book' SET accession = ?, entrydate = ?, title = ?, publisher = ?, editor = ?, subtitle = ?,price =?,vendor =? WHERE book_id = ? ")
        result_update = cursor.execute(upd_query,[(accessionno),(entrydate),(title),(publisher),(editor),(subtitle),(price),(vendor),(update_tree_id)])
        conn.commit()
        cursor.close()
        conn.close()
        print("UPDATED")
    except sqlite3.OperationalError:
        print("SOMETHING WRONG WITH UPDATING")
def update_show():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `book` ORDER BY `book_id` ASC")
    fetch = cursor.fetchall()
    global data
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
    cursor.close()
    conn.close()

def show_update_window():
    global win3
    distroy_win1()
    win3 = update_record()

class show_records(Tk):
    def __init__(self, *win4, **win4master):
        Tk.__init__(self, *win4, **win4master)
        self.geometry("800x600+350+50")

        self.bg ="black"
        self.config(bg=self.bg)
        self.Left = Frame(self, width=300, height=500, bd=8, relief="raise")
        self.Left.pack(side=LEFT)
        self.btn_show = Button(self.Left,text="SHOW RECORD",command=Read)
        self.btn_show.pack(side=TOP)
        self.btn_back = Button(self.Left, text="BACK", command=back_to_menu)
        self.btn_back.pack(side=RIGHT)
        self.Right = Frame(self, width=600, height=500, bd=8, relief="raise")
        self.Right.pack(side=TOP)
        # ==================================LIST WIDGET========================================
        # ==================================LIST WIDGET========================================
        global tree
        scrollbary = Scrollbar(self.Right, orient=VERTICAL)
        scrollbarx = Scrollbar(self.Right, orient=HORIZONTAL)
        tree = ttk.Treeview(self.Right, columns=("id", "accession", "entrydate", "title", "publisher", "editor","sub-title","price","vendor"),
                selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('id', text="ID", anchor=W)
        tree.heading('accession', text="Accession.NO", anchor=W)
        tree.heading('entrydate', text="entrydate", anchor=W)
        tree.heading('title', text="title", anchor=W)
        tree.heading('publisher', text="publisher", anchor=W)
        tree.heading('editor', text="editor", anchor=W)
        tree.heading('sub-title', text="sub-title", anchor=W)
        tree.heading('price', text="price", anchor=W)
        tree.heading('vendor', text="vendor", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=80)
        tree.column('#2', stretch=NO, minwidth=0, width=120)
        tree.column('#3', stretch=NO, minwidth=0, width=80)
        tree.column('#4', stretch=NO, minwidth=0, width=150)
        tree.column('#5', stretch=NO, minwidth=0, width=120)
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        tree.column('#7', stretch=NO, minwidth=0, width=120)
        tree.column('#8', stretch=NO, minwidth=0, width=120)
        tree.pack()
def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `book` ORDER BY `book_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5],data[6],data[7],data[8]))
    cursor.close()
    conn.close()


print("woriking")



def show_records_window():
        global win4
        win1.destroy()
        win4 = show_records()

def back_to_menu():
        win4.destroy()
        win1 = MenuWindow()



class delete_window(Tk):
    def __init__(self, *win5, **win5master):
        Tk.__init__(self, *win5, **win5master)
        self.geometry("600x500")

        self.bg ="black"
        self.config(bg=self.bg)
        self.geometry("1000x600+100+20")
        ################# FRAMES
        self.Top = Frame(self, width=900, height=50, bd=8, relief="raise")
        self.Top.pack(side=TOP)

        self.Right = Frame(self, width=600, height=500, bd=8, relief="raise")
        self.Right.pack(side=RIGHT)
        self.Forms = Frame(self, width=300, height=450)
        self.Forms.pack(side=TOP)
        self.Buttons = Frame(self.Right, width=300, height=100, bd=8, relief="raise")
        self.Buttons.pack(side=BOTTOM)
        global ACCESSION_UP
        global ENTRYDATE_UP
        global TITLE_UP
        global PUBLISHER_UP
        global EDITOR_UP
        global SUBTITLE_UP
        global PRICE_UP
        global VENDOR_UP
        ACCESSION_UP = StringVar()
        ENTRYDATE_UP = StringVar()
        TITLE_UP = StringVar()
        PUBLISHER_UP = StringVar()
        EDITOR_UP = StringVar()
        SUBTITLE_UP = StringVar()
        PRICE_UP = StringVar()
        VENDOR_UP = StringVar()




        self.btn_show = Button(self.Buttons, text="SHOW RECORD", command=update_show)
        self.btn_show.pack(side=LEFT)

        self.btn_back = Button(self.Buttons, text="BACK", command=back_win3_to_menu)
        self.btn_back.pack(side=RIGHT)
        self.btn_update = Button(self.Buttons, text="DELETE", command=delete_data)
        self.btn_update.pack(side=RIGHT)

        # ==================================LIST WIDGET========================================
        # ==================================LIST WIDGET========================================
        global tree
        scrollbary = Scrollbar(self.Right, orient=VERTICAL)
        scrollbarx = Scrollbar(self.Right, orient=HORIZONTAL)
        tree = ttk.Treeview(self.Right, columns=(
            "id", "accession", "entrydate", "title", "publisher", "editor", "sub-title", "price", "vendor"),
                            selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('id', text="ID", anchor=W)
        tree.heading('accession', text="ACCESSION.NO", anchor=W)
        tree.heading('entrydate', text="ENTRYDATE", anchor=W)
        tree.heading('title', text="TITLE", anchor=W)
        tree.heading('publisher', text="PUBLISHER", anchor=W)
        tree.heading('editor', text="EDITOR", anchor=W)
        tree.heading('sub-title', text="SUB-TITLE", anchor=W)
        tree.heading('price', text="PRICE", anchor=W)
        tree.heading('vendor', text="VENDOR", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=80)
        tree.column('#2', stretch=NO, minwidth=0, width=120)
        tree.column('#3', stretch=NO, minwidth=0, width=80)
        tree.column('#4', stretch=NO, minwidth=0, width=150)
        tree.column('#5', stretch=NO, minwidth=0, width=120)
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        tree.column('#7', stretch=NO, minwidth=0, width=120)
        tree.column('#8', stretch=NO, minwidth=0, width=120)
        tree.bind('<ButtonRelease-1>', select_data)
        tree.pack()
def show_delete_window():
    win1.withdraw()
    win5=delete_window()

def delete_data():
    Database()
    deletes =  ("DELETE FROM 'book' WHERE book_id = ?")
    cursor.execute(deletes,[(update_tree_id)])
    conn.commit()
    cursor.close()
    conn.close()
    print("deleted")





root = SampleApp()
root.mainloop()