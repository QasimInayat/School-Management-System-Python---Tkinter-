from tkinter import  *
import sqlite3
import tkinter.ttk as ttk
from tkinter import messagebox

def Database():
    global conn, cursor
    conn = sqlite3.connect('pythonn.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `result` (st_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, st_name TEXT, c_name TEXT, c_code TEXT, f_name TEXT, quizes TEXT, midterm TEXT,finals TEXT,total TEXT)")


#--------------------- TEACHER'S LOGIN APPROVAL ----------------------------#
def Login_Approval():
    if (USERNAME.get() == '') or (PASSWORD.get() == '   '):
        goto_TeacherHome()
        obj_TeacherLogin.withdraw()

def goto_TeacherLogin():
    global  obj_TeacherLogin
    obj_TeacherLogin = TchrLoginForm()
#--------------------- STUDENT'S LOGIN APPROVAL ----------------------------#
def Login_Approval2():
    if (USERNAME.get() == '') or (PASSWORD.get() == '   '):
        goto_StudentHome()
        objStudentLogin.withdraw()
def goto_StudentLogin():
    global  objStudentLogin
    objStudentLogin = StLoginForm()


#--------------------- HOME MAIN FORM ----------------------------#
class HomeWindow(Tk):
    def __init__(self, *main, **master):
        Tk.__init__(self, *main, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Student Login')
        self.config(bg='white')

        global USERNAME
        global PASSWORD
        USERNAME = StringVar()
        PASSWORD = StringVar()

        self._Header = PhotoImage(file='Header.gif')
        self._HeaderLabel = Label(self, image=self._Header, height=300, width=300).place(x=500, y=2000)

        self._Footer = PhotoImage(file="FOOTER.gif")

        self._HeadLabel = Label(self, text='abc', width=100, height=100, bg='#3C6739').place(x=-5500, y=1000)
        self._background = PhotoImage(file='Background.gif')
        self._image = PhotoImage(file='HomeBackground.gif')

        self._IconTeacherButton = PhotoImage(file="TeacherIcon.gif")
        self._IconStudentButton = PhotoImage(file='StudentIcon.gif')

        self._Label1 = Label(self, image=self._background).place(x=0, y=0)
        self._Label2 = Label(self, image=self._image).place(relx=0.5, rely=0.5, anchor='center', height=450, width=920)

        self._TeacherButton = Button(self, image=self._IconTeacherButton, text='Teacher', width=200, height=235,
                                     bg='#3C6739', command = goto_TeacherLogin).place(x=350, rely=0.5, anchor='center')
        self._TeacherLabel = Label(self, text='Teacher Login', font=('arial', 20, 'bold')).place(x=251, y=480)

        self._StudentButton = Button(self, image=self._IconStudentButton, text='Teacher', width=200, height=235,
                                     bg='#3C6739',command =goto_StudentLogin).place(x=920, rely=0.5, anchor='center')
        self._StudentButton = Label(self, text='Student Login', font=('arial', 20, 'bold')).place(x=822, y=480)

        self._HeaderLabel = Label(self, image=self._Header, text='Teacher', width=1277, height=80, bg='#3C6739').place(
            x=0, rely=0)
        self._FooterLabel = Label(self, image=self._Footer, height=40, width=1277, bg='#3C6739').place(x=0.5, y=677)

#--------------------- HOME MAIN FORM (END)----------------------------#


#--------------------- STUDENT'S LOGIN FORM ----------------------------#
class StLoginForm(Tk):
    def __init__(self, *StudentLoginForm, **master):
        Tk.__init__(self, *StudentLoginForm, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Student Login')
        self.config(bg='white')

        self.frameH2 = Frame(self, height=50, width=1277, bg='#3C6739').place(relx=0, y=30)
        self.frameC2 = Frame(self, height=80, width=1277, bg='#F0F0F0').place(x=0, y=90)
        self.LStudentLogin = Label(self, font=('impact', 30, 'bold'), text="STUDENT'S LOGIN").place(relx=0.4,
                                                                                                    y=100)
        self.frameF = Frame(self, height=50, width=1277, bg='#3C6739').place(relx=0, y=180)

        self.SLusername = Label(self, text='username', bg='white', font=('arial', 20)).place(x=490, y=356)
        self.SEusername = ttk.Entry(self, font=('arial', 20), textvariable=USERNAME).place(relx=0.5, rely=0.5)
        self.SLPassword = Label(self, text='password', bg='white', font=('arial', 20)).place(x=490, y=410)
        self.SEPassword = ttk.Entry(self, font=('arial', 20), textvariable=PASSWORD, show='*').place(x=639,
                                                                                                     y=410)
        self.SBLogin = Button(self, text='LOGIN', padx=190, pady=5, font=('arial', 12, 'bold'), bg='#3C6739',
                              fg='white', command = Login_Approval2).place(relx=0.39, y=470)
        self.SLMessage = Label(self, text='', fg='red', bg='white', font=('arial', 15)).place(relx=0.43,
                                                                                              rely=0.72)


def goto_Student_Home():
    global StudentHome
    StudentHome = StLoginForm()
    main.withdraw()



#--------------------- STUDENT'S LOGIN FORM (END) ----------------------------#


#--------------------- TEACHER'S LOGIN FORM  ----------------------------#
class TchrLoginForm(Tk):
    def __init__(self, *TeacherLoginForm, **master):
        Tk.__init__(self, *TeacherLoginForm, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Teacher Login')
        self.config(bg='white')

        self.frameH = Frame(self, height=50, width=1277, bg='#3C6739').place(relx=0, y=30)
        self.frameC = Frame(self, height=80, width=1277, bg='#F0F0F0').place(x=0, y=90)
        self.LTeacherLogin = Label(self, font=('impact', 30, 'bold'), text="TEACHER'S LOGIN").place(relx=0.4,
                                                                                                    y=100)
        self.frameF = Frame(self, height=50, width=1277, bg='#3C6739').place(relx=0, y=180)

        self.TLusername = Label(self, text='username', bg='white', font=('arial', 20)).place(x=490, y=356)
        self.TEusername = ttk.Entry(self, textvariable=USERNAME, font=('arial', 20)).place(relx=0.5, rely=0.5)
        self.TLPassword = Label(self, text='password', bg='white', font=('arial', 20)).place(x=490, y=410)
        self.TEPassword = ttk.Entry(self, textvariable=PASSWORD, font=('arial', 20), show='*').place(x=639,
                                                                                                     y=410)
        self.TBLogin = Button(self, text='LOGIN', padx=190, pady=5, font=('arial', 12, 'bold'), bg='#3C6739',
                              fg='white', command=Login_Approval).place(relx=0.39, y=470)
        self.TLMessage = Label(self, text='', fg='red', bg='white', font=('arial', 15)).place(relx=0.43,
                                                                                              rely=0.72)


#--------------------- TEACHER'S LOGIN FORM (END) ----------------------------#

#--------------------- TEACHER'S STUFF (START) ----------------------------#
#--------------------- TEACHER'S HOME (START) ----------------------------#
class TeacherHome(Tk):
    def __init__(self, *TeacherHomeWindow, **master):
        Tk.__init__(self, *TeacherHomeWindow, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Teacher Login')
        self.config(bg='white')

        self.AHframe = Frame(self, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)

        self.LStudentLogin = Label(self, font=('impact', 30, 'bold'), text="TEACHER'S HOME", bg='white').place(relx=0.4,
                                                                                                               y=150)

        self.B_AttendanceReg = Button(self, text='Attendance Register', width=25, height=13, bg='#3C6739', fg='white',
                                      font=('arial black', 10), bd=6).place(x=120, rely=0.4)
        self.B_ReportCard = Button(self, text='Report Card', width=25, height=13, bg='#3C6739', fg='white',
                                   font=('arial black', 10), bd=6, command= open_show_records).place(x=520, rely=0.4)
        self.B_EvaloutionForm = Button(self, text='General Application', width=25, height=13, bg='#3C6739', fg='white',
                                       font=('arial black', 10), bd=6, command = goto_GeneralApplicationFaculty).place(x=930, rely=0.4)

        self.AFframe = Frame(self, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)



def goto_TeacherHome():

    ojbTeacherHome = TeacherHome()
#--------------------- TEACHER'S HOME (END) ----------------------------#


#--------------------- REPORT CARD (MODULE # 2) ----------------------------#
class show_records(Tk):
    def __init__(self, *win4, **win4master):
        Tk.__init__(self, *win4, **win4master)
        self.geometry("800x600+350+50")

        self.geometry("1280x720")

        self.bg = "white"
        self.config(bg=self.bg)
        self.AHframe = Frame(self, height=40, width=1280, bg='#3C6739').place(relx=0, y=0)
        self.AHHeading = Label(self, text='REPORT CARD', font=('impact', 18), bg='#3C6739', fg='white').place(
            relx=0.5, rely=0)
        self.Left = ttk.Frame(self, width=300, height=1000, relief="raise")
        self.Left.place(x=65, y=420)
        self.btn_show = ttk.Button(self.Left, text="LOAD", command=Read)
        self.btn_show.pack()
        self.btn_add = ttk.Button(self.Left, text="ADD" ,command=add_book)
        self.btn_add.pack()
        self.btn_exit = ttk.Button(self.Left, text="EXIT", command = Exit_show_records)
        self.btn_exit.pack()


        #goto_TeacherHome

        self.Right = ttk.Frame(self, width=600, height=500, relief="raise")
        self.Right.place(x=200, y=45)
        global tree

        scrollbary = Scrollbar(self.Right, orient=VERTICAL)
        scrollbarx = Scrollbar(self.Right, orient=HORIZONTAL)
        tree = ttk.Treeview(self.Right, columns=(
            "st_id", "st_name", "c_name", "c_code", "f_name", "quizes", "midterm", "finals", "total"),
                            selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('st_id', text="ID", anchor=W)
        tree.heading('st_name', text="Name", anchor=W)
        tree.heading('c_name', text="Course Name", anchor=W)
        tree.heading('c_code', text="Course Code", anchor=W)
        tree.heading('f_name', text="Faculty Name", anchor=W)
        tree.heading('quizes', text="Quizes", anchor=W)
        tree.heading('midterm', text="Midterm", anchor=W)
        tree.heading('finals', text="Fianls", anchor=W)
        tree.heading('total', text="Total Marks", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=120)
        tree.column('#2', stretch=NO, minwidth=0, width=120)
        tree.column('#3', stretch=NO, minwidth=0, width=120)
        tree.column('#4', stretch=NO, minwidth=0, width=120)
        tree.column('#5', stretch=NO, minwidth=0, width=120)
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        tree.column('#7', stretch=NO, minwidth=0, width=120)
        tree.column('#8', stretch=NO, minwidth=0, width=120)
        tree.pack()

        # %%%%%%%%%%%%%%%%%%%%%%%%%% ADDING RESULT  %%%%%%%%%%%%%%%%%%%%%%%%%%
        self.lbl = Label(self, text="ADD A NEW RESULT", font=("Arial Black", 10, 'bold'), bg='white')
        self.lbl.place(x=25, y=68)
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
        self.lbl_Accession_number = Label(self, text="Name", font=("Helvetica", 8, 'bold'), bg='white').place(x=2,
                                                                                                              y=100)
        self.lbl_Entry_data = Label(self, text="Course Name", font=("Helvetica", 8, 'bold'), bg='white').place(x=2,
                                                                                                               y=135)
        self.lbl_Title = Label(self, text="Title", font=("Helvetica", 8, 'bold'), bg='white').place(x=2, y=170)
        self.lbl_Publisher = Label(self, text="Faculty Name", font=("Helvetica", 8, 'bold'), bg='white').place(x=2,
                                                                                                               y=205)
        self.lbl_Editor = Label(self, text="Quizes", font=("Helvetica", 8, 'bold'), bg='white').place(x=2, y=240)
        self.lbl_Subtitle = Label(self, text="Midterm", font=("Helvetica", 8, 'bold'), bg='white').place(x=2, y=275)
        self.lbl_Price = Label(self, text="Finals", font=("Helvetica", 8, 'bold'), bg='white').place(x=2, y=310)
        self.lbl_Vendor = Label(self, text="Total Marks", font=("Helvetica", 8, 'bold'), bg='white').place(x=2, y=345)


        self.ent_Accession_number = ttk.Entry(textvariable=ACCESSION, width=13).place(x=100, y=100)
        self.ent_Entry_data = ttk.Entry( textvariable=ENTRYDATE, width=13).place(x=100, y=135)
        self.ent_Title = ttk.Entry( textvariable=TITLE, width=13).place(x=100, y=170)
        self.ent_Publisher = ttk.Entry(textvariable=PUBLISHER, width=13).place(x=100, y=205)
        self.ent_Editor = ttk.Entry(textvariable=EDITOR, width=13).place(x=100, y=240)
        self.ent_Subtitle = ttk.Entry(textvariable=SUBTITLE, width=13).place(x=100, y=275)
        self.ent_Price = ttk.Entry(textvariable=PRICE, width=13).place(x=100, y=310)
        self.ent_Vendor = ttk.Entry(textvariable=VENDOR, width=13).place(x=100, y=345)

        Read()
        self.AFframe = Frame(self, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)

def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `result` ORDER BY `st_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5],data[6],data[7],data[8]))
    cursor.close()
    conn.close()

def Exit_home():
    StudentHome.withdraw()


def open_show_records():
    global goto_show_records
    goto_show_records = show_records()

def Exit_show_records():
    goto_show_records.destroy()

class insert_record(Tk):
    def __init__(self, *win2, **win2master):
        Tk.__init__(self, *win2, **win2master)
        self.geometry("1000x600+180+70")

        self.bg ="#4EC0A0"
        self.config(bg=self.bg)

def add_book():
    if ACCESSION.get() == "" or ENTRYDATE.get() == "" or TITLE.get() == "" or PUBLISHER.get() == "" or EDITOR.get() == "" or SUBTITLE.get() == "" or PRICE.get() == "" or VENDOR.get() == "":
        #tkMessageBox.showinfo("Say Hello", "Hello World")
        #messagebox.showerror("Error", "Error message")
        #messagebox.showwarning("Warning", "Warning message")
        messagebox.showinfo("Requirment!", "Please fill all the fields")
    else:
        Database()

        cursor.execute("INSERT INTO 'result' (st_name, c_name, c_code, f_name, quizes, midterm,finals,total) VALUES(?, ?, ?, ?, ?, ?,?,?)",  (str(ACCESSION.get()), str(ENTRYDATE.get()), str(TITLE.get()), str(PUBLISHER.get()), str(EDITOR.get()), str(SUBTITLE.get()), str(PRICE.get()), str(VENDOR.get())))
        print("query runnning")
        conn.commit()



def open_insert_record():
    objinsert_record = insert_record()
        # %%%%%%%%%%%%%%%%%%%%%%%%%% ENDING (LOAD AND ADD STUDENT'S RESULT) %%%%%%%%%%%%%%%%%%%%%%%%%%


class GeneralApplicationFaculty(Tk):
    def __init__(self, *GeneralApplicationFacultyWindow, **master):
        Tk.__init__(self, *GeneralApplicationFacultyWindow, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Teacher Login')
        self.config(bg='white')

        self.AHframe = Frame(self, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)


        self.LStudentLogin = Label(self, font=('impact', 30, 'bold'), text="GENERAL APPLICATION", bg='white').place(relx=0.36,
                                                                                                            y=100)
        self.HeadingMessage = Label(self, font=('arial', 15, 'bold'),text='Please fill a Query in a appropriate manner',bg='white').place(relx=0.34, y=150)


        global PhoneNumber
        global Program
        global Query
        global Subject

        PhoneNumber = StringVar()
        Program = StringVar()
        Query = StringVar()
        Subject = StringVar()
        self.Body = Frame(self, bg='#F0F0F0', height = 375, width= 1100).place(relx=0.07, rely=0.35)
        self.LPhoneNumber = Label( text='Contact Number', font= ('arial', 10, 'bold')).place(relx=0.14 , rely=0.36)
        self.EPhoneNumber = ttk.Entry(textvariable = PhoneNumber, width = 40, font= ('arial', 14)).place(relx=0.14, rely=0.39)

        self.LProgram = Label( text='Program', font= ('arial', 10, 'bold')).place(relx=0.52, rely=0.36)
        self.EProgram = ttk.Entry(textvariable = Program, width = 40, font = ('arial', 14)).place(relx=0.52, rely=0.39)

        self.LSubject = Label( text='Subject', font = ('arial', 10, 'bold')).place(relx=0.14, rely=0.45)
        self.ESubject = ttk.Entry( width=84, font=('arial', 14), textvariable = Subject).place(relx=0.14, rely=0.48)

        self.LQuery = Label( text = 'Query', font = ('arial', 10, 'bold')).place(relx=0.14, rely=0.54)
        self.EQuery = ttk.Entry( textvariable = Query, width = 18, font = ('arial', 70)).place(relx=0.14, rely=0.57)

        self.BSubmit = ttk.Button(text='Submit', command = add_query).place(relx=0.82, rely=0.79)
        self.BReset = ttk.Button( text='Reset', command = reset_query).place(relx=0.74, rely=0.79)
        self.BHome = ttk.Button(text='Home').place(relx=0.5, rely=0.79)




def add_query():
    if PhoneNumber.get() == "" or Program.get() == "" or Query.get() == "" or Subject.get() == "":
        #tkMessageBox.showinfo("Say Hello", "Hello World")
        #messagebox.showerror("Error", "Error message")
        #messagebox.showwarning("Warning", "Warning message")
        messagebox.showinfo("Requirment!", "Please fill all the fields")
    else:
        Database()
        cursor.execute("INSERT INTO 'queries' (phone_number, program, subject, query) VALUES(?, ?, ?, ?)",  (str(PhoneNumber.get()), str(Program.get()), str(Subject.get()), str(Query.get())))
        conn.commit()

def reset_query():
    Program.set("")
    PhoneNumber.set("")
    Subject.set("")
    Query.set("")

def goto_GeneralApplicationFaculty():
    global  objGeneralApplicationFaculty
    objGeneralApplicationFaculty = GeneralApplicationFaculty()
#--------------------- TEACHER'S STUFF (END) ----------------------------#


#--------------------- STUDENT'S HOME ----------------------------#
class StudentHome(Tk):
    def __init__(self, *StudentHomeWindow, **master):
        Tk.__init__(self, *StudentHomeWindow, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Student Login')
        self.config(bg='white')

        self.AHframe = Frame(self, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)

        self.LStudentLogin = Label(self, font=('impact', 30, 'bold'), text="STUDENTS'S HOME", bg='white').place(relx=0.4,
                                                                                                               y=150)

        self.B_ViewResult = Button(self, text='View Result', width=25, height=13, bg='#3C6739', fg='white',
                                      font=('arial black', 10), bd=6, command = ViewResult).place(x=120, rely=0.4)
        self.B_GeneralAppliation = Button(self, text='General Application', width=25, height=13, bg='#3C6739', fg='white',
                                   font=('arial black', 10), bd=6, command = goto_GeneralApplication).place(x=520, rely=0.4)
        self.B_GradeCalculator = Button(self, text='Grade Calculator', width=25, height=13, bg='#3C6739', fg='white',
                                       font=('arial black', 10), bd=6, command = goto_GradeCalculator).place(x=930, rely=0.4)

        self.AFframe = Frame(self, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)

def goto_StudentHome():
    objStudentHome = StudentHome()
    #--------------------- STUDENT'S HOME (END)----------------------------#

#--------------------- STUDENT'S STUFF ----------------------------#

    #--------------------- VIEW RESULT (MODULE # 1)----------------------------#
class ViewResult(Tk):
    def __init__(self, *ViewResultWindow, **master):
        Tk.__init__(self, *ViewResultWindow, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Teacher Login')
        self.config(bg='white')

        self.AHframe = Frame(self, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)

        global tree
        global IDNO
        IDNO = StringVar()
        self.LStudentLogin = Label(self, font=('impact', 30, 'bold'), text="FALL 2017", bg='white').place(relx=0.43,y=100)
        self.HeadingMessage = Label(self, font= ('arial', 15, 'bold'),text='Please view your Result of Fall 2017 by Entering your ID Number', bg='white').place(relx=0.26, y=150)
        self.L_IDNO = Label(self, text='ID No.', font = ('arial', 15, 'bold'), bg='white').place(relx=0.36, y=240)
        self.E_IDNO = ttk.Entry(textvariable=IDNO, font= ('arial', 15)).place(relx=0.43, y=240)
        self.B_CheckResult = Button(text='CHECK YOUR RESULT', bg='#3C6739', fg='white', font=('arial black', 10), command= Result).place(relx=0.43, y= 280)

        scrollbary = Scrollbar(self, orient=VERTICAL)
        scrollbarx = Scrollbar(self, orient=HORIZONTAL)
        tree = ttk.Treeview(self, columns=(
            "st_id", "st_name", "c_name", "c_code", "f_name", "quizes", "midterm", "finals", "total"),
                            selectmode="extended", height=10, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('st_id', text="ID", anchor=W)
        tree.heading('st_name', text="Name", anchor=W)
        tree.heading('c_name', text="Course Name", anchor=W)
        tree.heading('c_code', text="Course Code", anchor=W)
        tree.heading('f_name', text="Faculty Name", anchor=W)
        tree.heading('quizes', text="Quizes", anchor=W)
        tree.heading('midterm', text="Midterm", anchor=W)
        tree.heading('finals', text="Fianls", anchor=W)
        tree.heading('total', text="Total Marks", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=120)
        tree.column('#2', stretch=NO, minwidth=0, width=120)
        tree.column('#3', stretch=NO, minwidth=0, width=120)
        tree.column('#4', stretch=NO, minwidth=0, width=120)
        tree.column('#5', stretch=NO, minwidth=0, width=120)
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        tree.column('#7', stretch=NO, minwidth=0, width=120)
        tree.column('#8', stretch=NO, minwidth=0, width=120)
        tree.place(x=50, rely=0.5)

        self.AFframe = Frame(self, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)


def goto_ViewResult():
    obj_ViewResult = ViewResult()

def Result():


    if (IDNO.get()== ""):
        messagebox.showinfo("Requirment!", "Please enter a Valid ID NO")

    try:
        tree.delete(*tree.get_children())
        Database()
        sql = "SELECT * FROM RESULT WHERE st_id = '%s'"%IDNO.get()
        cursor.execute(sql)
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
        cursor.close()
        conn.close()
    except:
        IndexError
    #--------------------- VIEW RESULT (MODULE # 1) END----------------------------#

    # --------------------- GENERAL APPLICATION (MODULE # 2) START----------------------------#
class GeneralApplication(Tk):
    def __init__(self, *GeneralApplicationWindow, **master):
        Tk.__init__(self, *GeneralApplicationWindow, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Teacher Login')
        self.config(bg='white')

        self.AHframe = Frame(self, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)


        self.LStudentLogin = Label(self, font=('impact', 30, 'bold'), text="GENERAL APPLICATION", bg='white').place(relx=0.36,
                                                                                                            y=100)
        self.HeadingMessage = Label(self, font=('arial', 15, 'bold'),text='Please fill a Query in a appropriate manner',bg='white').place(relx=0.34, y=150)


        global PhoneNumber
        global Program
        global Query
        global Subject

        PhoneNumber = StringVar()
        Program = StringVar()
        Query = StringVar()
        Subject = StringVar()
        self.Body = Frame(self, bg='#F0F0F0', height = 375, width= 1100).place(relx=0.07, rely=0.35)
        self.LPhoneNumber = Label( text='Contact Number', font= ('arial', 10, 'bold')).place(relx=0.14 , rely=0.36)
        self.EPhoneNumber = ttk.Entry(textvariable = PhoneNumber, width = 40, font= ('arial', 14)).place(relx=0.14, rely=0.39)

        self.LProgram = Label( text='Program', font= ('arial', 10, 'bold')).place(relx=0.52, rely=0.36)
        self.EProgram = ttk.Entry(textvariable = Program, width = 40, font = ('arial', 14)).place(relx=0.52, rely=0.39)

        self.LSubject = Label( text='Subject', font = ('arial', 10, 'bold')).place(relx=0.14, rely=0.45)
        self.ESubject = ttk.Entry( width=84, font=('arial', 14), textvariable = Subject).place(relx=0.14, rely=0.48)

        self.LQuery = Label( text = 'Query', font = ('arial', 10, 'bold')).place(relx=0.14, rely=0.54)
        self.EQuery = ttk.Entry( textvariable = Query, width = 18, font = ('arial', 70)).place(relx=0.14, rely=0.57)

        self.BSubmit = ttk.Button(text='Submit', command = add_query).place(relx=0.82, rely=0.79)
        self.BReset = ttk.Button( text='Reset', command = reset_query).place(relx=0.74, rely=0.79)



def add_query():
    if PhoneNumber.get() == "" or Program.get() == "" or Query.get() == "" or Subject.get() == "":
        #tkMessageBox.showinfo("Say Hello", "Hello World")
        #messagebox.showerror("Error", "Error message")
        #messagebox.showwarning("Warning", "Warning message")
        messagebox.showinfo("Requirment!", "Please fill all the fields")
    else:
        Database()
        #bad ma configure karna hoga
        cursor.execute("INSERT INTO 'queries' (phone_number, program, subject, query) VALUES(?, ?, ?, ?)",  (str(PhoneNumber.get()), str(Program.get()), str(Subject.get()), str(Query.get())))
        print("query runnning")
        conn.commit()
        print("BOOK RECORD INSERTED")
def reset_query():
    Program.set("")
    PhoneNumber.set("")
    Subject.set("")
    Query.set("")

def goto_GeneralApplication():
    objGeneralApplication = GeneralApplication()
    # --------------------- GENERAL APPLICATION (MODULE # 2) END----------------------------#

    # --------------------- GRADE CALCULATOR (MODULE # 3) START----------------------------#
class GradeCalculator(Tk):
    def __init__(self, *GradeCalculatorWindow, **master):
        Tk.__init__(self, *GradeCalculatorWindow, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Teacher Login')
        self.config(bg='white')

        self.AHframe = Frame(self, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)

        self.LStudentLogin = Label(self, font=('impact', 30, 'bold'), text="GRADE CALCULATOR", bg='white').place(
                relx=0.36,
                y=100)
        self.HeadingMessage = Label(self, font=('arial', 15, 'bold'),
                                        text='Enter your marks to calculate your Grade', bg='white').place(relx=0.34,y=150)

        global sub1Sessional
        global sub1MidTerm
        global sub1Finals
        global sub1Total

        global TPercentage
        TPercentage = StringVar()

        sub1Sessional = StringVar()
        sub1MidTerm = StringVar()
        sub1Finals = StringVar()
        sub1Total = StringVar()



        global sub2Sessional
        global sub2MidTerm
        global sub2Finals
        global sub2Total


        sub2Sessional = StringVar()
        sub2MidTerm = StringVar()
        sub2Finals = StringVar()
        sub2Total = StringVar()


        global sub3Sessional
        global sub3MidTerm
        global sub3Finals
        global sub3Total

        sub3Sessional = StringVar()
        sub3MidTerm = StringVar()
        sub3Finals = StringVar()
        sub3Total = StringVar()


        global sub4Sessional
        global sub4MidTerm
        global sub4Finals
        global sub4Total

        sub4Sessional = StringVar()
        sub4MidTerm = StringVar()
        sub4Finals = StringVar()
        sub4Total = StringVar()


        global sub5Sessional
        global sub5MidTerm
        global sub5Finals
        global sub5Total


        sub5Sessional = StringVar()
        sub5MidTerm = StringVar()
        sub5Finals = StringVar()
        sub5Total = StringVar()


        self.LSub1 = Label( text='Subj # 1',font = ('arial', 12, 'bold'), bg='white').place(relx=0.10, rely=0.27)
        self.LSub1Sessional = Label(text='Sessional', font=('arial', 10, 'bold'), bg='white').place(relx=0.15, rely=0.29)
        self.ESub1Sessional = ttk.Entry(textvariable = sub1Sessional, width = 5, font = ('arial' , 14)).place(relx=0.21, rely=0.29)
        self.LSub1MidTerm = Label( text='Midterm', font=('arial', 10, 'bold'), bg='white').place(relx=0.31, rely=0.29)
        self.ESub1MidTerm = ttk.Entry(textvariable = sub1MidTerm, font=('arial', 14), width = 5).place(relx=0.37, rely=0.29)
        self.LSub1Finals = Label(text='Final', font=('arial', 10, 'bold'), bg='white').place(relx=0.49,rely=0.29)
        self.ESub1Finals = ttk.Entry(textvariable = sub1Finals, width=5, font=('arial', 14)).place(relx=0.54, rely=0.29)
        self.LSub1Total = Label(textvariable = sub1Total, text='0', font=('arial black', 15, 'bold'), bg='white').place(relx= 0.7, rely=0.29)
        self.LSub1Total100 = Label(text='/ 100', font=('arial black', 15, 'bold'), bg='white').place(relx=0.74, rely=0.29)

        self.LSub2 = Label(text='Subj # 2', font=('arial', 12, 'bold'), bg='white').place(relx=0.10, rely=0.38)
        self.LSub2Sessional = Label(text='Sessional', font=('arial', 10, 'bold'), bg='white').place(relx=0.15,rely=0.41)
        self.ESub2Sessional = ttk.Entry(textvariable = sub2Sessional, width=5, font=('arial', 14)).place(relx=0.21, rely=0.41)
        self.LSub2MidTerm = Label(text='Midterm', font=('arial', 10, 'bold'), bg='white').place(relx=0.31,rely=0.41)
        self.ESub2MidTerm = ttk.Entry(textvariable = sub2MidTerm, width=5, font=('arial', 14)).place(relx=0.37, rely=0.41)
        self.LSub2Finals = Label(text='Final', font=('arial', 10, 'bold'), bg='white').place(relx=0.49, rely=0.41)
        self.ESub2Finals = ttk.Entry(textvariable = sub2Finals, width=5, font=('arial', 14)).place(relx=0.54, rely=0.41)
        self.LSub2Total = Label(textvariable = sub2Total ,text='0', font=('arial black', 15, 'bold'), bg='white').place(relx=0.7, rely=0.41)
        self.LSub2Total100 = Label(text='/ 100', font=('arial black', 15, 'bold'), bg='white').place(relx=0.74,
                                                                                                           rely=0.41)


        self.LSub5 = Label(text='Subj # 3', font=('arial', 12, 'bold'), bg='white').place(relx=0.10, rely=0.49)
        self.LSub5Sessional = Label(text='Sessional', font=('arial', 10, 'bold'), bg='white').place(relx=0.15,rely=0.52)
        self.ESub5Sessional = ttk.Entry(textvariable = sub5Sessional ,width=5, font=('arial', 14)).place(relx=0.21, rely=0.52)
        self.LSub5MidTerm = Label(text='Midterm', font=('arial', 10, 'bold'), bg='white').place(relx=0.31,rely=0.52)
        self.ESub5MidTerm = ttk.Entry(textvariable = sub5MidTerm , width=5, font=('arial', 14)).place(relx=0.37, rely=0.52)
        self.LSub5Finals = Label(text='Final', font=('arial', 10, 'bold'), bg='white').place(relx=0.49, rely=0.52)
        self.ESub5Finals = ttk.Entry(textvariable = sub5Finals, width=5, font=('arial', 14)).place(relx=0.54, rely=0.52)
        self.LSub5Total = Label(textvariable = sub5Total ,text='0', font=('arial black', 15, 'bold'), bg='white').place(relx=0.7, rely=0.52)
        self.LSub5Total100 = Label(text='/ 100', font=('arial black', 15, 'bold'), bg='white').place(relx=0.74,
                                                                                                           rely=0.52)

        self.LSub3 = Label(text='Subj # 4', font=('arial', 12, 'bold'), bg='white').place(relx=0.10, rely=0.62)
        self.LSub3Sessional = Label(text='Sessional', font=('arial', 10, 'bold'), bg='white').place(relx=0.15,rely=0.65)
        self.ESub3Sessional = ttk.Entry(textvariable = sub3Sessional, width=5, font=('arial', 14)).place(relx=0.21, rely=0.65)
        self.LSub3MidTerm = Label(text='Midterm', font=('arial', 10, 'bold'), bg='white').place(relx=0.31,rely=0.65)
        self.ESub3MidTerm = ttk.Entry(textvariable = sub3MidTerm,width=5, font=('arial', 14)).place(relx=0.37, rely=0.65)
        self.LSub3Finals = Label(text='Final', font=('arial', 10, 'bold'), bg='white').place(relx=0.49, rely=0.65)
        self.ESub3Finals = ttk.Entry(textvariable = sub3Finals,width=5, font=('arial', 14)).place(relx=0.54, rely=0.65)
        self.LSub3Total = Label(textvariable = sub3Total, text='0', font=('arial black', 15, 'bold'), bg='white').place(relx=0.7, rely=0.65)
        self.LSub3Total100 = Label(text='/ 100', font=('arial black', 15, 'bold'), bg='white').place(relx=0.74,
                                                                                                           rely=0.65)

        self.LSub4 = Label(text='Subj # 5', font=('arial', 12, 'bold'), bg='white').place(relx=0.10, rely=0.73)
        self.LSub4Sessional = Label(text='Sessional', font=('arial', 10, 'bold'), bg='white').place(relx=0.15,rely=0.76)
        self.ESub4Sessional = ttk.Entry(textvariable = sub4Sessional,width=5, font=('arial', 14)).place(relx=0.21, rely=0.76)
        self.LSub4MidTerm = Label(text='Midterm', font=('arial', 10, 'bold'), bg='white').place(relx=0.31,rely=0.76)
        self.ESub4MidTerm = ttk.Entry(textvariable = sub4MidTerm,width=5, font=('arial', 14)).place(relx=0.37, rely=0.76)
        self.LSub4Finals = Label( text='Final', font=('arial', 10, 'bold'), bg='white').place(relx=0.49, rely=0.76)
        self.ESub4Finals = ttk.Entry(textvariable = sub4Finals,width=5, font=('arial', 14)).place(relx=0.54, rely=0.76)
        self.LSub4Total = Label(textvariable = sub4Total, text='0', font=('arial black', 15, 'bold'), bg='white').place(relx=0.7, rely=0.76)
        self.LSub4Total100 = Label(text='/ 100', font=('arial black', 15, 'bold'), bg='white').place(relx=0.74,rely=0.76)
        self.Calculate = ttk.Button(text='Reset', command = Reset).place(relx=0.75, rely=0.85)
        self.Calculate = ttk.Button(text='Calculate', command=cal).place(relx=0.67, rely=0.85)

        self.LPercentage = Label(textvariable  = TPercentage, text='0', font= ('arial', 20, 'bold'), bg='white').place(relx=0.87, rely=0.86)
        self.AFframe = Frame(height=35, width=1280, bg='#3C6739').place(relx=0, y=685)






def goto_GradeCalculator():
    objGradeCalculator = GradeCalculator()

def Reset():
    sub1Sessional.set("")
    sub1MidTerm.set("")
    sub1Finals.set("")
    sub1Total.set("")
    sub2Sessional.set("")
    sub2MidTerm.set("")
    sub2Finals.set("")
    sub2Total.set("")
    sub3Sessional.set("")
    sub3MidTerm.set("")
    sub3Finals.set("")
    sub3Total.set("")
    sub4Sessional.set("")
    sub4MidTerm.set("")
    sub4Finals.set("")
    sub4Total.set("")
    sub5Sessional.set("")
    sub5MidTerm.set("")
    sub5Finals.set("")
    sub5Total.set("")

def cal():
    Subj1Sessional = float(sub1Sessional.get())
    Subj1Midterm = float (sub1MidTerm.get())
    Subj1Finls = float (sub1Finals.get())
    subj1Total = float(Subj1Sessional + Subj1Midterm + Subj1Finls)
    sub1Total.set(subj1Total)

    Subj2Sessional = float(sub2Sessional.get())
    Subj2Midterm = float(sub2MidTerm.get())
    Subj2Finls = float(sub2Finals.get())
    subj2Total = float(Subj2Sessional + Subj2Midterm + Subj2Finls)
    sub2Total.set(subj2Total)

    Subj3Sessional = float(sub3Sessional.get())
    Subj3Midterm = float(sub3MidTerm.get())
    Subj3Finls = float(sub3Finals.get())
    subj3Total = float(Subj3Sessional + Subj3Midterm + Subj3Finls)
    sub3Total.set(subj3Total)

    Subj4Sessional = float(sub4Sessional.get())
    Subj4Midterm = float(sub4MidTerm.get())
    Subj4Finls = float(sub4Finals.get())
    subj4Total = float(Subj4Sessional + Subj4Midterm + Subj4Finls)
    sub4Total.set(subj4Total)

    Subj5Sessional = float(sub5Sessional.get())
    Subj5Midterm = float(sub5MidTerm.get())
    Subj5Finls = float(sub5Finals.get())
    subj5Total = float(Subj5Sessional + Subj5Midterm + Subj5Finls)
    sub5Total.set(subj5Total)

    TTotalMarks = subj1Total + subj2Total + subj3Total + subj4Total + subj5Total
    Percentage1 = TTotalMarks / 5
    Percentage2 = Percentage1 * 100

    TPercentage.set(Percentage2)



    #Total / 500 * 100










    # --------------------- GRADE CALCULATOR (MODULE # 3) END----------------------------#


#--------------------- STUDENT'S STUFF (END)----------------------------#
main = HomeWindow()
main.mainloop()

