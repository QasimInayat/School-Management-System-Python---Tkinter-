from tkinter import *
from ClassTwo import two


class One:
    def __init__(self, ONE):
        self.ONE = ONE

        winOne = Tk()
        button = Button(winOne, text='press', command = two)
        button.pack()
        winOne.mainloop()




if __name__ == '__main__':
    mainwin =   Tk()
    oneone = One(ONE)
    mainwin.mainloop()