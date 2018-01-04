from tkinter import  *
import sqlite3
import tkinter.ttk as ttk
from tkinter import  ttk, Tk, StringVar
import time;
from  PIL import *

AttendanceReg = Tk()
AttendanceReg.geometry('1300x720')
AttendanceReg.resizable(0, 0)
AttendanceReg.title('Attendance Register')
AttendanceReg.config(bg='white')

AHframe = Frame(AttendanceReg, height=40, width=1280, bg='#3C6739').place(relx=0, y=0)
AHHeading = Label(AttendanceReg, text='ATTENDANCE REGISTER', font=('impact', 18), bg='#3C6739', fg='white').place(
        relx=0.4, rely=0)

LeftMayFrame = Frame(AttendanceReg, width=1002, height=650, bd=2, relief="raise", bg='white')
LeftMayFrame.pack(side=LEFT)
RightMayFrame = Frame(AttendanceReg, width=350, height=650, bd=2, relief="raise", bg='white')
RightMayFrame.pack(side=RIGHT)

LeftMayFrame1 = Frame(LeftMayFrame, width=1000, height=100, bd=2, relief="raise", bg='white')
LeftMayFrame1.place(y=0.70)
LeftMayFrame2 = Frame(LeftMayFrame, width=1000, height=546, bd=2, relief="raise", bg='white')
LeftMayFrame2.place(y=101)

RightMayFrame1 = Frame(RightMayFrame, width=350, height=350,bd=2, relief="raise", bg='white')
RightMayFrame1.place(y=0.100)
RightMayFrame2 = Frame(RightMayFrame, width=350, height=350, bd=2, relief="raise", bg='white')
RightMayFrame2.place(y=300)
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

def ResetButton():
    image0 = PhotoImage(file="")
    image = cont.create_image(100, 150, image=image0)
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")
    value12.set("")
    value13.set("")
    value14.set("")
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ IMAGES @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#cont1 = Canvas(RightMayFrame2, width = 350, height = 425, bg= "black")
#cont1.place(x=0, y=0 )
#image2 = PhotoImage(file = "StudentIconn.png")
#cont1.create_image(200, 200, image = image2)

cont = Canvas(RightMayFrame1, width = 250, height = 350, bg='white')
cont.place(relx=0.1, y=0)
name = ''
stname_L = Label(RightMayFrame2).place(relx=0.5 , rely=0.5)
image0 = PhotoImage(file = "stdeomo.png")
image =  cont.create_image(100, 150, image = image0)

image1 = PhotoImage(file = "st1.png")
def pic1():
    image = cont.create_image(100, 150, image = image1)


    lstName = Label(RightMayFrame2, text=VStNam1, font=('arial black', 20, 'bold'), bg ='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

        #VStNam1 = 'M. Qasim'
        #VStAddress = 'ABC , Karachi'
        #VstContact = '03123432'

image2 = PhotoImage(file = "st2.png")
def pic2 ():
    image = cont.create_image(100, 150, image = image2)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam2, font=('arial black', 20, 'bold'), bg ='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image3 = PhotoImage(file = "st3.png")
def pic3():
    image = cont.create_image(100, 150, image=image3)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam3, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image4 = PhotoImage(file = "st4.png")
def pic4():
    image = cont.create_image(100, 150, image=image4)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam4, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image5 = PhotoImage(file="st5.png")
def pic5():
    image = cont.create_image(100, 150, image=image5)
    lstName = Label(RightMayFrame2, text="", font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="", font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="", font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam5, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image6 = PhotoImage(file="st6.png")
def pic6():
    image = cont.create_image(100, 150, image=image6)
    lstName = Label(RightMayFrame2, text="", font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="", font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="", font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam6, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image7 = PhotoImage(file="st7.png")
def pic7():
    image = cont.create_image(100, 150, image=image7)
    lstName = Label(RightMayFrame2, text=VStNam7, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image8 = PhotoImage(file="st8.png")
def pic8():
    image = cont.create_image(100, 150, image=image8)
    lstName = Label(RightMayFrame2, text="", font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="", font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="", font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam8, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image9 = PhotoImage(file="st9.png")
def pic9():
    image = cont.create_image(100, 150, image=image9)
    lstName = Label(RightMayFrame2, text="", font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="", font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="", font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam9, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image10 = PhotoImage(file="st10.png")
def pic10():
    image = cont.create_image(100, 150, image=image10)
    lstName = Label(RightMayFrame2, text="", font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="", font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="", font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam10, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image11 = PhotoImage(file="st11.png")
def pic11():
    image = cont.create_image(100, 150, image=image11)
    lstName = Label(RightMayFrame2, text="", font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="", font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="", font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam11, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image12 = PhotoImage(file="st12.png")
def pic12():
    image = cont.create_image(100, 150, image=image12)
    lstName = Label(RightMayFrame2, text="", font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="", font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="", font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam12, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image13 = PhotoImage(file="st13.png")
def pic13():
    image = cont.create_image(100, 150, image=image13)
    lstName = Label(RightMayFrame2, text="", font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="", font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="", font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam13, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)


image14 = PhotoImage(file="st14.png")
def pic14():
        image = cont.create_image(100, 150, image=image14)
        lstName = Label(RightMayFrame2, text="", font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
        lstName = Label(RightMayFrame2, text="", font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
        lstName = Label(RightMayFrame2, text="", font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

        lstName = Label(RightMayFrame2, text=VStNam14, font=('arial black', 20, 'bold'), bg ='white').place(x=80, y=0.5)
        lstName = Label(RightMayFrame2, text=VStAddress, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
        lstName = Label(RightMayFrame2, text=VstContact, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)









            # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ FUNCTIONS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ExitButton():
    AttendanceReg.destroy()

def FillButton():
    if value0.get() == "Present":
        value1.set("Present")
        value2.set("Present")
        value3.set("Present")
        value4.set("Present")
        value5.set("Present")
        value6.set("Present")
        value7.set("Present")
        value8.set("Present")
        value9.set("Present")
        value10.set("Present")
        value11.set("Present")
        value12.set("Present")
        value13.set("Present")
        value14.set("Present")

    elif value0.get() == "Absent":
        value1.set("Absent")
        value2.set("Absent")
        value3.set("Absent")
        value4.set("Absent")
        value5.set("Absent")
        value6.set("Absent")
        value7.set("Absent")
        value8.set("Absent")
        value9.set("Absent")
        value10.set("Absent")
        value11.set("Absent")
        value12.set("Absent")
        value13.set("Absent")
        value14.set("Absent")

    elif value0.get() == "Leave":
        value1.set("Leave")
        value2.set("Leave")
        value3.set("Leave")
        value4.set("Leave")
        value5.set("Leave")
        value6.set("Leave")
        value7.set("Leave")
        value8.set("Leave")
        value9.set("Leave")
        value10.set("Leave")
        value11.set("Leave")
        value12.set("Leave")
        value13.set("Leave")
        value14.set("Leave")

    elif value0.get() == "Late":
        value1.set("Late")
        value2.set("Late")
        value3.set("Late")
        value4.set("Late")
        value5.set("Late")
        value6.set("Late")
        value7.set("Late")
        value8.set("Late")
        value9.set("Late")
        value10.set("Late")
        value11.set("Late")
        value12.set("Late")
        value13.set("Late")
        value14.set("Late")


    elif value0.get() == "Sick":
        value1.set("Sick")
        value2.set("Sick")
        value3.set("Sick")
        value4.set("Sick")
        value5.set("Sick")
        value6.set("Sick")
        value7.set("Sick")
        value8.set("Sick")
        value9.set("Sick")
        value10.set("Sick")
        value11.set("Sick")
        value12.set("Sick")
        value13.set("Sick")
        value14.set("Sick")




        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ VARIABLES END @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ COMPONENTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

DateofOrder.set(time.strftime("%d/%m/%y"))

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ COMPONENTS END @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LeftMayFrame 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

lblNo = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="No", bg='white').place(x=50, rely=0.3)
lblStudentNo = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="Student No.", bg='white').place(x=120, rely=0.3)
lblStudentName = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="Student Name", bg='white').place(x=240,
                                                                                                             rely=0.3)
lblCourseCode = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="Course Code", bg='white').place(x=400, rely=0.3)

box = ttk.Combobox(LeftMayFrame1, textvariable=value0, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, rely=0.3)

btnFill = ttk.Button(LeftMayFrame1, text='Fill', command = FillButton).place(x=720, rely=0.27)

btnReset = ttk.Button(LeftMayFrame1, text='Reset', command = ResetButton).place(x=815, rely=0.27)

    # btnExit = Button(LeftMayFrame1, text='Exit', padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width = 12, height = 1).grid(row=0, column = 7)

lblDateofOrder = Label(LeftMayFrame1, font=('arial', 10, 'bold'), textvariable=DateofOrder, padx=2, pady=2, bd=2,fg='black', bg='white', relief='sunken').place(x=900, rely=0.3)
VStNam1 = 'M. Qasim'
VStAddress = 'ABC , Karachi'
VstContact = '03123432'
SNo1 = Label(LeftMayFrame2, text='1', font =('arial', 10, 'bold'), bg='white').place(x=53, y=10)
StID1 = Label(LeftMayFrame2, text='4115', font =('arial', 10, 'bold'), bg='white').place(x=122, y=10)
StName1 = Label(LeftMayFrame2, text='M. Qasim', font=('arial', 10, 'bold'), bg='white').place(x=240, y=10)
CourseCode1 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=10)
box = ttk.Combobox(LeftMayFrame2, textvariable=value1, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=10)
StDetails1 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic1).place(x=720, y=10)

VStNam2 = 'M. Yasir Raza'
SNo2 = Label(LeftMayFrame2, text='2', font=('arial', 10, 'bold'), bg='white').place(x=53, y=48)
StID2 = Label(LeftMayFrame2, text='4116', font=('arial', 10, 'bold'), bg='white').place(x=122, y=48)
StName2 = Label(LeftMayFrame2, text='M. Yasir Raza', font=('arial', 10, 'bold'), bg='white').place(x=240, y=48)
CourseCode2 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=48)
box = ttk.Combobox(LeftMayFrame2, textvariable=value2, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=48)
StDetails2 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic2).place(x=720, y=48)

VStNam3 = 'Ali Ahmed'
SNo3 = Label(LeftMayFrame2, text='3', font=('arial', 10, 'bold'), bg='white').place(x=53, y=86)
StID3 = Label(LeftMayFrame2, text='4117', font=('arial', 10, 'bold'), bg='white').place(x=122, y=86)
StName3 = Label(LeftMayFrame2, text='Ali Ahmed', font=('arial', 10, 'bold'), bg='white').place(x=240,y=86)
CourseCode3 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=86)
box = ttk.Combobox(LeftMayFrame2, textvariable=value3, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=86)
StDetails3 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic3).place(x=720, y=86)


VStNam4 = 'Ali Ather'
SNo4 = Label(LeftMayFrame2, text='4', font=('arial', 10, 'bold'), bg='white').place(x=53, y=124)
StID4 = Label(LeftMayFrame2, text='4118', font=('arial', 10, 'bold'), bg='white').place(x=122, y=124)
StName4 = Label(LeftMayFrame2, text='Ali Ather', font=('arial', 10, 'bold'), bg='white').place(x=240,y=124)
CourseCode4 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=124)
box = ttk.Combobox(LeftMayFrame2, textvariable=value4, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=124)
StDetails4 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic4).place(x=720, y=124)

VStNam5 = 'M. Shariq'
SNo5 = Label(LeftMayFrame2, text='5', font=('arial', 10, 'bold'), bg='white').place(x=53, y=162)
StID5 = Label(LeftMayFrame2, text='4119', font=('arial', 10, 'bold'), bg='white').place(x=122, y=162)
StName5 = Label(LeftMayFrame2, text='M. Shariq', font=('arial', 10, 'bold'), bg='white').place(x=240,y=162)
CourseCode5 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=162)
box = ttk.Combobox(LeftMayFrame2, textvariable=value5, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=162)
StDetails5 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic5).place(x=720, y=162)

VStNam6 = 'M. Haris'
SNo6 = Label(LeftMayFrame2, text='6', font=('arial', 10, 'bold'), bg='white').place(x=53, y=200)
StID6 = Label(LeftMayFrame2, text='4120', font=('arial', 10, 'bold'), bg='white').place(x=122, y=200)
StName6 = Label(LeftMayFrame2, text='M. Haris', font=('arial', 10, 'bold'), bg='white').place(x=240,y=200)
CourseCode6 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=200)
box = ttk.Combobox(LeftMayFrame2, textvariable=value6, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=200)
StDetails6 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic6).place(x=720, y=200)

VStNam7 = 'M. Aqib'
SNo7 = Label(LeftMayFrame2, text='7', font=('arial', 10, 'bold'), bg='white').place(x=53, y=238)
StID7 = Label(LeftMayFrame2, text='4121', font=('arial', 10, 'bold'), bg='white').place(x=122, y=238)
StName7 = Label(LeftMayFrame2, text='M. Aqib', font=('arial', 10, 'bold'), bg='white').place(x=240,y=238)
CourseCode7 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=238)
box = ttk.Combobox(LeftMayFrame2, textvariable=value7, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=238)
StDetails7 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic7).place(x=720, y=238)


VStNam8 = 'M. Saqib'
SNo8 = Label(LeftMayFrame2, text='8', font=('arial', 10, 'bold'), bg='white').place(x=53, y=276)
StID8 = Label(LeftMayFrame2, text='4122', font=('arial', 10, 'bold'), bg='white').place(x=122, y=276)
StName8 = Label(LeftMayFrame2, text='M. Saqib', font=('arial', 10, 'bold'), bg='white').place(x=240,y=276)
CourseCode8 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=276)
box = ttk.Combobox(LeftMayFrame2, textvariable=value8, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=276)
StDetails8 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic8).place(x=720, y=276)


VStNam9 = 'Jahanzaib Afzal'
SNo9 = Label(LeftMayFrame2, text='9', font=('arial', 10, 'bold'), bg='white').place(x=53, y=314)
StID9 = Label(LeftMayFrame2, text='4123', font=('arial', 10, 'bold'), bg='white').place(x=122, y=314)
StName9 = Label(LeftMayFrame2, text='Jahanzaib Afzal', font=('arial', 10, 'bold'), bg='white').place(x=240,y=314)
CourseCode9 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=314)
box = ttk.Combobox(LeftMayFrame2, textvariable=value9, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=314)
StDetails9 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic9).place(x=720, y=314)


VStNam10 = 'Adnan Abdullah'
SNo10 = Label(LeftMayFrame2, text='10', font=('arial', 10, 'bold'), bg='white').place(x=53, y=352)
StID10 = Label(LeftMayFrame2, text='4124', font=('arial', 10, 'bold'), bg='white').place(x=122, y=352)
StName10 = Label(LeftMayFrame2, text='Adnan Abdullah', font=('arial', 10, 'bold'), bg='white').place(x=240,y=352)
CourseCode10 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=352)
box = ttk.Combobox(LeftMayFrame2, textvariable=value10, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=352)
StDetails10 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic10).place(x=720, y=352)


VStNam11 = 'Adnan Abdullah'
SNo11 = Label(LeftMayFrame2, text='11', font=('arial', 10, 'bold'), bg='white').place(x=53, y=390)
StID11 = Label(LeftMayFrame2, text='4125', font=('arial', 10, 'bold'), bg='white').place(x=122, y=390)
StName11 = Label(LeftMayFrame2, text='Adnan Abdullah', font=('arial', 10, 'bold'), bg='white').place(x=240,y=390)
CourseCode11 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=390)
box = ttk.Combobox(LeftMayFrame2, textvariable=value11, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=390)
StDetails11 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic11).place(x=720, y=390)


VStNam12 = 'M. Asim'
SNo12 = Label(LeftMayFrame2, text='12', font=('arial', 10, 'bold'), bg='white').place(x=53, y=428)
StID12 = Label(LeftMayFrame2, text='4126', font=('arial', 10, 'bold'), bg='white').place(x=122, y=428)
StName12 = Label(LeftMayFrame2, text='M. Asim', font=('arial', 10, 'bold'), bg='white').place(x=240,y=428)
CourseCode12 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=428)
box = ttk.Combobox(LeftMayFrame2, textvariable=value12, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=428)
StDetails12 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic12).place(x=720, y=428)

VStNam13 = 'Aqeel Memon'
SNo13 = Label(LeftMayFrame2, text='13', font=('arial', 10, 'bold'), bg='white').place(x=53, y=466)
StID13 = Label(LeftMayFrame2, text='4127', font=('arial', 10, 'bold'), bg='white').place(x=122, y=466)
StName13 = Label(LeftMayFrame2, text='Aqeel Memon', font=('arial', 10, 'bold'), bg='white').place(x=240,y=466)
CourseCode13 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=466)
box = ttk.Combobox(LeftMayFrame2, textvariable=value13, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=466)
StDetails13 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic13).place(x=720, y=466)

VStNam14 = 'Hammad Qureshi'
SNo14 = Label(LeftMayFrame2, text='14', font=('arial', 10, 'bold'), bg='white').place(x=53, y=504)
StID14 = Label(LeftMayFrame2, text='4128', font=('arial', 10, 'bold'), bg='white').place(x=122, y=504)
StName14 = Label(LeftMayFrame2, text='Hammad Qureshi', font=('arial', 10, 'bold'), bg='white').place(x=240,y=504)
CourseCode14 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=504)
box = ttk.Combobox(LeftMayFrame2, textvariable=value14, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
box.current(0)
box.place(x=550, y=504)
StDetails14 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic14).place(x=720, y=504)

AFframe = Frame(AttendanceReg, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)




AttendanceReg.mainloop()