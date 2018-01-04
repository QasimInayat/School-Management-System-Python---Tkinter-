from tkinter import  *
from tkinter import  ttk, Tk, StringVar
import time;
import datetime

import sqlite3
from PIL import Image,ImageTk
import  tkFontChooser

gg='#134e86'#secondary color
g="#0a2845#"#color
gw="white"

def TLogin ():
    #username = USERNAME.get()
    #password = PASSWORD.get()
    if(USERNAME.get() == "") or (PASSWORD.get() == "   "):
        quitt()
        Attendance()

def quitt ():
    TeacherLoginForm.destroy()

#------------------------------------------------TEACHER BUTTON START-------------------------------------------#

#------------------------------------------------TEACHER MOUDLE 1 (Attendance Register) START-------------------------------------------#

def Attendance ():
    global AttendanceReg
    AttendanceReg = Tk()
    AttendanceReg.geometry('1280x720')
    AttendanceReg.resizable(0,0)
    AttendanceReg.title('Attendance Register')
    AttendanceReg.config(bg='white')

    AHframe = Frame(AttendanceReg, height = 40, width = 1280, bg  ='#3C6739').place(relx=0, y=0)
    AHHeading = Label(AttendanceReg, text='ATTENDANCE REGISTER', font = ('impact', 18), bg= '#3C6739', fg='white').place(relx=0.4, rely=0)


    LeftMayFrame = Frame(AttendanceReg, width = 1002, height = 650, bd= 2, relief = "raise", bg='white')
    LeftMayFrame.pack(side = LEFT)
    RightMayFrame = Frame(AttendanceReg, width = 350, height = 650,  bd =2, relief = "raise", bg='white')
    RightMayFrame.pack(side = RIGHT)

    LeftMayFrame1 = Frame(LeftMayFrame, width = 1000, height = 100, bd= 2, relief = "raise", bg='white')
    LeftMayFrame1.place(y=0.70)
    LeftMayFrame2 = Frame(LeftMayFrame, width = 1000, height = 546, bd = 2, relief = "raise", bg='white')
    LeftMayFrame2.place(y=101)

    RightMayFrame1 = Frame(RightMayFrame, width = 350, height = 215, bd =2 , relief = "raise", bg='white')
    RightMayFrame1.place(y= 0.100)
    RightMayFrame2 = Frame(RightMayFrame, width = 350, height = 431, bd = 2, relief = "raise", bg='white')
    RightMayFrame2.place(y=215)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ VARIABLES @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ VARIABLES END @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ COMPONENTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    DateofOrder.set(time.strftime("%d/%m/%y"))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ COMPONENTS END @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LeftMayFrame 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    lblNo = Label(LeftMayFrame1, font = ('arial', 10, 'bold'), text="No" , bg='white').place(x=50,rely=0.3)
    lblStudentNo = Label(LeftMayFrame1, font = ('arial', 10, 'bold'), text="Student No." , bg='white').place(x=120, rely=0.3)
    lblStudentName = Label(LeftMayFrame1, font = ('arial', 10, 'bold'), text="Student Name" , bg='white').place(x=240, rely=0.3)
    lblCourseCode = Label(LeftMayFrame1, font = ('arial', 10, 'bold'), text="Course Code" , bg='white').place(x=400, rely=0.3)

    box = ttk.Combobox(LeftMayFrame1, textvariable = value0, state = 'readonly')
    box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
    box.current(0)
    box.place(x=550, rely=0.3)

    btnArrow = ttk.Button(LeftMayFrame1, text = 'Fill').place(x=720, rely=0.27)

    btnReset  = ttk.Button(LeftMayFrame1, text = 'Reset').place(x=815, rely = 0.27)

    #btnExit = Button(LeftMayFrame1, text='Exit', padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width = 12, height = 1).grid(row=0, column = 7)

    lblDateofOrder = Label(LeftMayFrame1, font = ('arial', 10, 'bold'), textvariable = DateofOrder, padx=2, pady= 2, bd =2 , fg='black', bg='white', relief =  'sunken').place(x=900, rely=0.3)



    SNo1 = Label(LeftMayFrame2, text='1', font =('arial', 10, 'bold'), bg='white').place(x=53, y=10)
    StID1 = Label(LeftMayFrame2, text='4115', font =('arial', 10, 'bold'), bg='white').place(x=122, y=10)
    StName1 = Label(LeftMayFrame2, text='M. Qasim', font=('arial', 10, 'bold'), bg='white').place(x=240, y=10)
    CourseCode1 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=10)
    box = ttk.Combobox(LeftMayFrame2, textvariable=value1, state='readonly')
    box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
    box.current(0)
    box.place(x=550, y=10)
    StDetails1 = ttk.Button(LeftMayFrame2, text='View Details', width=27).place(x=720, y=10)

    SNo2 = Label(LeftMayFrame2, text='2', font=('arial', 10, 'bold'), bg='white').place(x=53, y=48)
    StID2 = Label(LeftMayFrame2, text='4116', font=('arial', 10, 'bold'), bg='white').place(x=122, y=48)
    StName2 = Label(LeftMayFrame2, text='M. Qasim', font=('arial', 10, 'bold'), bg='white').place(x=240, y=48)
    CourseCode2 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=48)
    box = ttk.Combobox(LeftMayFrame2, textvariable=value2, state='readonly')
    box['values'] = ('', 'Presnet', 'Absent', 'Leave', 'Late', 'Sick')
    box.current(0)
    box.place(x=550, y=48)
    StDetails2 = ttk.Button(LeftMayFrame2, text='View Details', width=27).place(x=720, y=48)


    AFframe = Frame(AttendanceReg, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)
#------------------------------------------------TEACHER MOUDLE 1 END-------------------------------------------#

#------------ ------------------------------------TEACHER LOGIN START-------------------------------------------#
def TeacherLogin ():
    global TeacherLoginForm
    TeacherLoginForm = Tk()
    TeacherLoginForm .geometry('1280x720')
    TeacherLoginForm.resizable(0,0)
    TeacherLoginForm.title('Teacher Login')
    TeacherLoginForm.config(bg='white')




    frameH = Frame(TeacherLoginForm, height = 50, width = 1277, bg  ='#3C6739').place(relx=0, y=30)
    frameC = Frame(TeacherLoginForm, height = 80, width = 1277,bg='#F0F0F0').place(x=0 ,y=90)
    LTeacherLogin = Label(TeacherLoginForm, font=('impact', 30, 'bold'), text="TEACHER'S LOGIN").place(relx=0.4, y=100)
    frameF = Frame(TeacherLoginForm, height=50, width=1277, bg='#3C6739').place(relx=0, y=180)

    TLusername = Label(TeacherLoginForm, text='username', bg='white',  font = ('arial', 20)).place(x=490, y=356)
    TEusername = ttk.Entry(TeacherLoginForm, textvariable = USERNAME, font= ('arial', 20)).place(relx=0.5,rely=0.5)
    TLPassword = Label(TeacherLoginForm, text='password', bg='white', font=('arial', 20)).place(x=490, y=410)
    TEPassword = ttk.Entry(TeacherLoginForm, textvariable = PASSWORD, font=('arial', 20),show = '*').place(x=639, y=410)
    TBLogin = Button(TeacherLoginForm, text='LOGIN', padx=190, pady=5, font=('arial', 12, 'bold'), bg='#3C6739', fg='white', command = TLogin).place(relx=0.39, y=470)
    TLMessage = Label(TeacherLoginForm, text='', fg='red', bg='white', font=('arial', 15)).place(relx=0.43,rely=0.72)




    # ------------------------------------------------TEACHER LOGIN END-------------------------------------------#
#------------------------------------------------TEACHER BUTTON END-------------------------------------------#




#------------------------------------------------STUDENT BUTTON-------------------------------------------#

#------------------------------------------------STUDENET LOGIN START-------------------------------------------#

def StudentLogin ():
    global  StudentLoginForm
    StudentLoginForm = Tk()
    StudentLoginForm.geometry('1280x720')
    StudentLoginForm.resizable(0,0)
    StudentLoginForm.title('Student Login')
    StudentLoginForm.config(bg='white')

    frameH2 = Frame(StudentLoginForm, height = 50, width = 1277, bg  ='#3C6739').place(relx=0, y=30)
    frameC2 = Frame(StudentLoginForm, height = 80, width = 1277,bg='#F0F0F0').place(x=0 ,y=90)
    LStudentLogin = Label(StudentLoginForm, font=('impact', 30, 'bold'), text="STUDENT'S LOGIN").place(relx=0.4, y=100)
    frameF = Frame(StudentLoginForm, height=50, width=1277, bg='#3C6739').place(relx=0, y=180)

    SLusername = Label(StudentLoginForm, text='username', bg='white',  font = ('arial', 20)).place(x=490, y=356)
    SEusername = ttk.Entry(StudentLoginForm, font= ('arial', 20), textvariable = USERNAME).place(relx=0.5,rely=0.5)
    SLPassword = Label(StudentLoginForm, text='password', bg='white', font=('arial', 20)).place(x=490, y=410)
    SEPassword = ttk.Entry(StudentLoginForm, font=('arial', 20),  textvariable = PASSWORD, show = '*').place(x=639, y=410)
    SBLogin = Button(StudentLoginForm, text='LOGIN', padx=190, pady=5, font=('arial', 12, 'bold'), bg='#3C6739', fg='white', command = TLogin).place(relx=0.39, y=470)
    SLMessage = Label(StudentLoginForm, text='', fg='red', bg='white', font=('arial', 15)).place(relx=0.43,rely=0.72)



#------------------------------------------------STUDENT LOGIN END-------------------------------------------#

#------------------------------------------------STUDENT BUTTON END-------------------------------------------#







win = Tk()
win.geometry("1280x720+0+0")
win.config(bg='white')
win.title("SMS LOGIN")
win.resizable(0,0)

USERNAME = StringVar()
PASSWORD = StringVar()

_Header = PhotoImage(file='Header.gif')
_HeaderLabel = Label(win, image = _Header, height=300, width=300).place(x=500, y=2000)

_Footer = PhotoImage(file ="FOOTER.gif")


_HeadLabel = Label(win, text='abc', width=100, height=100, bg='#3C6739').place(x=-5500, y=1000)
_background = PhotoImage(file='Background.gif')
_image = PhotoImage(file='HomeBackground.gif')

_IconTeacherButton = PhotoImage(file="TeacherIcon.gif")
_IconStudentButton = PhotoImage(file='StudentIcon.gif')



_Label1 = Label(win, image=_background).place(x=0, y=0)
_Label2 = Label(win, image=_image). place(relx=0.5, rely=0.5, anchor = 'center', height = 450, width = 920)

_TeacherButton = Button(win, image=_IconTeacherButton, text='Teacher', width=200, height=235, bg='#3C6739', command = TeacherLogin).place(x=350, rely=0.5, anchor = 'center')
_TeacherLabel = Label(win, text='Teacher Login', font=('arial', 20, 'bold')).place(x=251, y=480)


_StudentButton = Button(win, image=_IconStudentButton, text='Teacher', width=200, height=235, bg='#3C6739', command=  StudentLogin).place(x=920, rely=0.5, anchor = 'center')
_StudentButton = Label(win, text='Student Login', font=('arial', 20, 'bold')).place(x=822, y=480)

_HeaderLabel = Label(win, image=_Header, text='Teacher', width=1277, height=80, bg='#3C6739').place(x=0, rely=0)
_FooterLabel = Label(win, image = _Footer,height=40, width=1277, bg='#3C6739').place(x = 0.5, y = 677)


win.mainloop()


