from tkinter import *
import sqlite3
import tkinter.ttk as ttk
from tkinter import ttk, Tk, StringVar
import time;
from  PIL import *


def Database():
    global conn, cursor
    conn = sqlite3.connect('pythonpro.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXIST `result` (stId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, stName TEXT, courseCode TEXT, facultyName TEXT, quizes TEXT, midterm TEXT, finals TEXT, totalMarks TEXT)")


# --------------------------------------------------------------------FUNCTIONS--------------------------------------------------------------------
def Login_Approval():
    if (USERNAME.get() == '') or (PASSWORD.get() == '   '):
        show_TeacherMain_Window = TeacherHome()


# --------------------------------------------------------------------FUNCTIONS END--------------------------------------------------------------------


# --------------------------------------------------------------------FRAMES--------------------------------------------------------------------

# --------------------------------------------------------------------MAIN WINDOW (HOME)--------------------------------------------------------------------
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
                                     bg='#3C6739',
                                     command=goto_Teacher_Home).place(x=350, rely=0.5, anchor='center')
        self._TeacherLabel = Label(self, text='Teacher Login', font=('arial', 20, 'bold')).place(x=251, y=480)

        self._StudentButton = Button(self, image=self._IconStudentButton, text='Teacher', width=200, height=235,
                                     bg='#3C6739',
                                     command=goto_Student_Home).place(x=920, rely=0.5, anchor='center')
        self._StudentButton = Label(self, text='Student Login', font=('arial', 20, 'bold')).place(x=822, y=480)

        self._HeaderLabel = Label(self, image=self._Header, text='Teacher', width=1277, height=80, bg='#3C6739').place(
            x=0, rely=0)
        self._FooterLabel = Label(self, image=self._Footer, height=40, width=1277, bg='#3C6739').place(x=0.5, y=677)
        # self.geometry("1280x720")
        # self.config(bg='white')
        # self.title("SMS LOGIN")
        # self.resizable(0, 0)
        # global USERNAME
        # global PASSWORD
        # USERNAME = StringVar()
        # PASSWORD = StringVar()

        # self._Header = PhotoImage(file='Header.gif')
        # self._HeaderLabel = Label(self, image=self._Header, height=300, width=300)
        # self._HeaderLabel.place(x=200, y=50)
        # self.button = Button (self, text='Press Me',command=show_login)
        # self.button.place(relx=0.5, rely=0.5)


# --------------------------------------------------------------------MAIN WINDOW (HOME) END--------------------------------------------------------------------

# --------------------------------------------------------------------STUDENT LOGIN FORM--------------------------------------------------------------------
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
                              fg='white').place(relx=0.39, y=470)
        self.SLMessage = Label(self, text='', fg='red', bg='white', font=('arial', 15)).place(relx=0.43,
                                                                                              rely=0.72)


def goto_Student_Home():
    StudentHome = StLoginForm()
    main.withdraw()


# --------------------------------------------------------------------STUDENT LOGIN FORM END--------------------------------------------------------------------
def show_login():
    global open_login
    main.withdraw()
    open_login = Login()


# ++++++++++++++++++++++++++++++++++++++++++++++++++LOGIN FROM++++++++++++++++++++++++++++++++

# --------------------------------------------------------------------TEACHER LOGIN FORM--------------------------------------------------------------------

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


def goto_Teacher_Home():
    TeacherHome = TchrLoginForm()
    main.withdraw()


# --------------------------------------------------------------------TEACHER LOGIN FORM END--------------------------------------------------------------------

# --------------------------------------------------------------------TEACHER HOME (MODULES)--------------------------------------------------------------------
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
                                   font=('arial black', 10), bd=6, command = goto_ReportCard).place(x=520, rely=0.4)
        self.B_EvaloutionForm = Button(self, text='Evaloution Form', width=25, height=13, bg='#3C6739', fg='white',
                                       font=('arial black', 10), bd=6).place(x=930, rely=0.4)

        self.AFframe = Frame(self, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)


def TeacherMainWindow():
    global Teacher_Main_Window
    Teacher_Main_Window = TeacherHome()


# --------------------------------------------------------------------REPORT CARD (MODULE # 1)--------------------------------------------------------------------

def Database():
    global conn, cursor
    conn = sqlite3.connect('pythontut.db')
    cursor = conn.cursor();
    print('Connected!')

    cursor.execute("CREATE TABLE IF NOT EXIST `result` (stId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, stName TEXT, courseCode TEXT, facultyName TEXT, quizes TEXT, midterm TEXT, finals TEXT, totalMarks TEXT)")


class ReportCard(Tk):

    def __init__(self, *RC, **master):
        Tk.__init__(self, *RC, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Teacher Login')
        self.config(bg='white')

        self.btn1 = Button(self, text='Show', command = goto_show_records).place(relx=0.5, rely=0.5)
        self.btn2 = Button(self, text = 'Show2').place(relx=0.3, rely=0.3)

class show_records(Tk):

    def __init__(self, *viewing, **master):
        Tk.__init__(self, *viewing, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Teacher Login')
        self.config(bg='white')

        btn3 = Button(self, text='Show Records', command = Read).pack()

        self.Right = Frame(self, width=600, height=500, bd=8, relief="raise")
        self.Right.pack(side=TOP)

        global tree

        scrollbary = Scrollbar(self.Right, orient = VERTICAL)
        scrollbarx = Scrollbar(self.Right, orient = HORIZONTAL)
        tree = ttk.Treeview(self.Right, columns=("stId", "stName", "courseCode", "facultyName", "quizes", "midterm", "finals", "totalMarks"),
                            selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)

        tree.heading('stId', text="Student ID", anchor=W)
        tree.heading('stName', text="Student Name", anchor=W)
        tree.heading('courseCode', text="Course Code", anchor=W)
        tree.heading('facultyName', text="Faculty Name", anchor=W)
        tree.heading('quizes', text="Quizes", anchor=W)
        tree.heading('midterm', text="Midterm", anchor=W)
        tree.heading('finals', text="Finals", anchor=W)
        tree.heading('totalMarks', text="Total Marks", anchor=W)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=80)
        tree.column('#2', stretch=NO, minwidth=0, width=120)
        tree.column('#3', stretch=NO, minwidth=0, width=80)
        tree.column('#4', stretch=NO, minwidth=0, width=150)
        tree.column('#5', stretch=NO, minwidth=0, width=120)
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        tree.column('#7', stretch=NO, minwidth=0, width=120)
        tree.pack()




def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `result` ORDER BY `stName` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    cursor.close()
    conn.close()

def goto_show_records():
    objshow_records = show_records()

def goto_ReportCard():
    objReportCard = ReportCard()
# --------------------------------------------------------------------REPORT CARD (MODULE # 1) END--------------------------------------------------------------------



# --------------------------------------------------------------------REPORT CARD (MODULE # 2)--------------------------------------------------------------------
class AttendanceRegister(Tk):
    db_name = 'Databse.db'

    def __init__(self, *AttendanceReg, **master):
        Tk.__init__(self, *AttendanceReg, **master)
        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Attendance Register')
        self.config(bg='white')

        self.AHframe = Frame(self, height=40, width=1280, bg='#3C6739').place(relx=0, y=0)
        self.AHHeading = Label(self, text='ATTENDANCE REGISTER', font=('impact', 18), bg='#3C6739', fg='white').place(
            relx=0.4, rely=0)

        self.LeftMayFrame = Frame(self, width=1002, height=650, bd=2, relief="raise", bg='white')
        self.LeftMayFrame.pack(side=LEFT)
        self.RightMayFrame = Frame(self, width=350, height=650, bd=2, relief="raise", bg='white')
        self.RightMayFrame.pack(side=RIGHT)

        self.LeftMayFrame1 = Frame(self.LeftMayFrame, width=1000, height=100, bd=2, relief="raise", bg='white')
        self.LeftMayFrame1.place(y=0.70)
        self.LeftMayFrame2 = Frame(self.LeftMayFrame, width=1000, height=546, bd=2, relief="raise", bg='white')
        self.LeftMayFrame2.place(y=101)

        self.RightMayFrame1 = Frame(self.RightMayFrame, width=350, height=215, bd=2, relief="raise", bg='white')
        self.RightMayFrame1.place(y=0.100)
        self.RightMayFrame2 = Frame(self.RightMayFrame, width=350, height=431, bd=2, relief="raise", bg='white')
        self.RightMayFrame2.place(y=215)
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ VARIABLES @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        DateofOrder = StringVar()

        value0 = StringVar()
        value1 = StringVar()
        value2 = StringVar()
        value3 = StringVar()
        value4 = StringVar()
        value5 = StringVar()
        value6 = StringVar()
        value7 = StringVar()
        value8 = StringVar()
        value9 = StringVar()
        value10 = StringVar()
        value11 = StringVar()
        value12 = StringVar()
        value13 = StringVar()
        value14 = StringVar()

        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ VARIABLES END @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ COMPONENTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        #  self.DateofOrder.set(self.time.strftime("%d/%m/%y"))

        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ COMPONENTS END @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LeftMayFrame 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        self.lblNo = Label(self.LeftMayFrame1, font=('arial', 10, 'bold'), text="No", bg='white').place(x=50, rely=0.3)
        self.lblStudentNo = Label(self.LeftMayFrame1, font=('arial', 10, 'bold'), text="Student No.", bg='white').place(
            x=120, rely=0.3)
        self.lblStudentName = Label(self.LeftMayFrame1, font=('arial', 10, 'bold'), text="Student Name",
                                    bg='white').place(x=240, rely=0.3)
        self.lblCourseCode = Label(self.LeftMayFrame1, font=('arial', 10, 'bold'), text="Course Code",
                                   bg='white').place(x=400, rely=0.3)

        self.box = ttk.Combobox(self.LeftMayFrame1, textvariable=value0, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, rely=0.3)

        self.btnArrow = ttk.Button(self.LeftMayFrame1, text='Fill').place(x=720, rely=0.27)

        self.btnReset = ttk.Button(self.LeftMayFrame1, text='Reset').place(x=815, rely=0.27)

        self.btnExit = ttk.Button(self.LeftMayFrame1, text='Exit', command=ButtonExit).place(x=910, rely=0.25)
        # self.lblDateofOrder = Label(self.LeftMayFrame1, font = ('arial', 10, 'bold'), textvariable = DateofOrder, padx=2, pady= 2, bd =2 , fg='black', bg='white', relief =  'sunken').place(x=900, rely=0.3)

        self.SNo1 = Label(self.LeftMayFrame2, text='1', font=('arial', 10, 'bold'), bg='white').place(x=53, y=10)
        self.StID1 = Label(self.LeftMayFrame2, text='4115', font=('arial', 10, 'bold'), bg='white').place(x=122, y=10)
        self.StName1 = Label(self.LeftMayFrame2, text='M. Qasim', font=('arial', 10, 'bold'), bg='white').place(x=240,
                                                                                                                y=10)
        self.CourseCode1 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                y=10)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value1, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=10)
        self.StDetails1 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=10)

        self.SNo2 = Label(self.LeftMayFrame2, text='2', font=('arial', 10, 'bold'), bg='white').place(x=53, y=48)
        self.StID2 = Label(self.LeftMayFrame2, text='4116', font=('arial', 10, 'bold'), bg='white').place(x=122, y=48)
        self.StName2 = Label(self.LeftMayFrame2, text='M. Yasir Raza', font=('arial', 10, 'bold'), bg='white').place(
            x=240, y=48)
        self.CourseCode2 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                y=48)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value2, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=48)
        self.StDetails2 = Button(self.LeftMayFrame2, text='View Details', width=27, command=ChangeColor).place(x=720,
                                                                                                               y=48)

        self.SNo3 = Label(self.LeftMayFrame2, text='3', font=('arial', 10, 'bold'), bg='white').place(x=53, y=86)
        self.StID3 = Label(self.LeftMayFrame2, text='4117', font=('arial', 10, 'bold'), bg='white').place(x=122, y=86)
        self.StName3 = Label(self.LeftMayFrame2, text='Ali Ahmed', font=('arial', 10, 'bold'), bg='white').place(x=240,
                                                                                                                 y=86)
        self.CourseCode3 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                y=86)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value3, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=86)
        self.StDetails3 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=86)

        self.SNo4 = Label(self.LeftMayFrame2, text='4', font=('arial', 10, 'bold'), bg='white').place(x=53, y=124)
        self.StID4 = Label(self.LeftMayFrame2, text='4118', font=('arial', 10, 'bold'), bg='white').place(x=122, y=124)
        self.StName4 = Label(self.LeftMayFrame2, text='Ali Ather', font=('arial', 10, 'bold'), bg='white').place(x=240,
                                                                                                                 y=124)
        self.CourseCode4 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                y=124)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value4, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=124)
        self.StDetails4 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=124)

        self.SNo5 = Label(self.LeftMayFrame2, text='5', font=('arial', 10, 'bold'), bg='white').place(x=53, y=162)
        self.StID5 = Label(self.LeftMayFrame2, text='4119', font=('arial', 10, 'bold'), bg='white').place(x=122, y=162)
        self.StName5 = Label(self.LeftMayFrame2, text='M. Shariq', font=('arial', 10, 'bold'), bg='white').place(x=240,
                                                                                                                 y=162)
        self.CourseCode5 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                y=162)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value5, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=162)
        self.StDetails5 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=162)

        self.SNo6 = Label(self.LeftMayFrame2, text='6', font=('arial', 10, 'bold'), bg='white').place(x=53, y=200)
        self.StID6 = Label(self.LeftMayFrame2, text='4120', font=('arial', 10, 'bold'), bg='white').place(x=122, y=200)
        self.StName6 = Label(self.LeftMayFrame2, text='M. Haris', font=('arial', 10, 'bold'), bg='white').place(x=240,
                                                                                                                y=200)
        self.CourseCode6 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                y=200)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value6, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=200)
        self.StDetails6 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=200)

        self.SNo7 = Label(self.LeftMayFrame2, text='7', font=('arial', 10, 'bold'), bg='white').place(x=53, y=238)
        self.StID7 = Label(self.LeftMayFrame2, text='4121', font=('arial', 10, 'bold'), bg='white').place(x=122, y=238)
        self.StName7 = Label(self.LeftMayFrame2, text='M. Aqib', font=('arial', 10, 'bold'), bg='white').place(x=240,
                                                                                                               y=238)
        self.CourseCode7 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                y=238)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value7, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=238)
        self.StDetails7 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=238)

        self.SNo8 = Label(self.LeftMayFrame2, text='8', font=('arial', 10, 'bold'), bg='white').place(x=53, y=276)
        self.StID8 = Label(self.LeftMayFrame2, text='4122', font=('arial', 10, 'bold'), bg='white').place(x=122, y=276)
        self.StName8 = Label(self.LeftMayFrame2, text='M. Saqib', font=('arial', 10, 'bold'), bg='white').place(x=240,
                                                                                                                y=276)
        self.CourseCode8 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                y=276)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value8, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=276)
        self.StDetails8 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=276)

        self.SNo9 = Label(self.LeftMayFrame2, text='9', font=('arial', 10, 'bold'), bg='white').place(x=53, y=314)
        self.StID9 = Label(self.LeftMayFrame2, text='4123', font=('arial', 10, 'bold'), bg='white').place(x=122, y=314)
        self.StName9 = Label(self.LeftMayFrame2, text='Jahanzaib Afzal', font=('arial', 10, 'bold'), bg='white').place(
            x=240, y=314)
        self.CourseCode9 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                y=314)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value9, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=314)
        self.StDetails9 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=314)

        self.SNo10 = Label(self.LeftMayFrame2, text='10', font=('arial', 10, 'bold'), bg='white').place(x=53, y=352)
        self.StID10 = Label(self.LeftMayFrame2, text='4124', font=('arial', 10, 'bold'), bg='white').place(x=122, y=352)
        self.StName10 = Label(self.LeftMayFrame2, text='Shoaib Khan', font=('arial', 10, 'bold'), bg='white').place(
            x=240, y=352)
        self.CourseCode10 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                 y=352)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value10, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=352)
        self.StDetails10 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=352)

        self.SNo11 = Label(self.LeftMayFrame2, text='11', font=('arial', 10, 'bold'), bg='white').place(x=53, y=390)
        self.StID11 = Label(self.LeftMayFrame2, text='4125', font=('arial', 10, 'bold'), bg='white').place(x=122, y=390)
        self.StName11 = Label(self.LeftMayFrame2, text='Adnan Abdullah', font=('arial', 10, 'bold'), bg='white').place(
            x=240, y=390)
        self.CourseCode11 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                 y=390)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value11, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=390)
        self.StDetails11 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=390)

        self.SNo12 = Label(self.LeftMayFrame2, text='12', font=('arial', 10, 'bold'), bg='white').place(x=53, y=428)
        self.StID12 = Label(self.LeftMayFrame2, text='4126', font=('arial', 10, 'bold'), bg='white').place(x=122, y=428)
        self.StName12 = Label(self.LeftMayFrame2, text='M. Asim', font=('arial', 10, 'bold'), bg='white').place(x=240,
                                                                                                                y=428)
        self.CourseCode12 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                 y=428)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value12, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=428)
        self.StDetails12 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=428)

        self.SNo13 = Label(self.LeftMayFrame2, text='13', font=('arial', 10, 'bold'), bg='white').place(x=53, y=466)
        self.StID13 = Label(self.LeftMayFrame2, text='4127', font=('arial', 10, 'bold'), bg='white').place(x=122, y=466)
        self.StName13 = Label(self.LeftMayFrame2, text='Aqeel Memon', font=('arial', 10, 'bold'), bg='white').place(
            x=240, y=466)
        self.CourseCode13 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                 y=466)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value13, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=466)
        self.StDetails13 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=466)

        self.SNo14 = Label(self.LeftMayFrame2, text='14', font=('arial', 10, 'bold'), bg='white').place(x=53, y=504)
        self.StID14 = Label(self.LeftMayFrame2, text='4128', font=('arial', 10, 'bold'), bg='white').place(x=122, y=504)
        self.StName14 = Label(self.LeftMayFrame2, text='Hammad Qureshi', font=('arial', 10, 'bold'), bg='white').place(
            x=240, y=504)
        self.CourseCode14 = Label(self.LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,
                                                                                                                 y=504)
        self.box = ttk.Combobox(self.LeftMayFrame2, textvariable=value14, state='readonly')
        self.box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
        self.box.current(0)
        self.box.place(x=550, y=504)
        self.StDetails14 = ttk.Button(self.LeftMayFrame2, text='View Details', width=27).place(x=720, y=504)
        self.AFframe = Frame(self, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)


def goto_AttendanceRegister():
    global go_to_Attendance_Register
    go_to_Attendance_Register = AttendanceRegister()


def ButtonExit():
    go_to_Attendance_Register.destroy()


def open():
    from SMS_PythonProject import testing


# -----------------------

# --------------------------------------------------------------------TEACHER HOME (MODULES) END--------------------------------------------------------------------

# --------------------------------------------------------------------FRAMES END--------------------------------------------------------------------
class Login(Tk):
    def __init__(self, *login, **master):
        Tk.__init__(self, *login, **master)

        self.geometry("1000x600")
        self.config(bg='white')
        self.title("SMS LOGIN")
        self.resizable(0, 0)
        self.button = Button(self, text='BACK', command=back_to_main)
        self.button.place(relx=0.5, rely=0.5)
        self.button = Button(self, text='GO', command=Window2)
        self.button.place(relx=0.5, rely=0.5)


def back_to_main():
    open_login.withdraw()
    main.deiconify()


class another(Tk):
    def __init__(self, *win2, **master):
        Tk.__init__(self, *win2, **master)

        self.geometry("1000x600")
        self.config(bg='white')
        self.title("SMS LOGIN")
        self.resizable(0, 0)

        self.bb = Button(self, text='CHANGE COLOR', command=ChangeColor)
        self.bb.place(relx=0.5, rely=0.5)
        self.b2 = Label(self, text='HHAHAHAAHAH', fg="blue")
        self.b2.place(x=200, y=200)


def ChangeColor():
    # w.b2.config(fg='red')
    try:
        go_to_Attendance_Register.AHHeading.config(fg='red')
    except:
        AttributeError
    else:
        print("hoja yar")


def Window2():
    global w
    global main

    open_login.withdraw()
    w = another()


main = HomeWindow()
main.mainloop()
