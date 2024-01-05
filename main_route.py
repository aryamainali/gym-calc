from tkinter import Tk,Frame
from Login import Login_page
from Dashboard import Dashboard_page


mainwindow = Tk()
mainwindow.rowconfigure(0,weight=1)
mainwindow.columnconfigure(0,weight=1)


page1=Frame(mainwindow)
page2=Frame(mainwindow)
# page3=Frame(mainwindow)

page1.configure(bg='aquamarine')
page2.configure(bg='dark gray')
# page3.configure(bg='dark gray')


for frame in(page1,page2):
    frame.grid(row=0,column=0,sticky='nsew')


def login():
    page2.tkraise()
    mainwindow.update()
    
def logout():
    page1.tkraise()
    
# def go_to_result():
#     page3.tkraise()



Login_page(page1,login)
Dashboard_page(page2,logout)



page1.tkraise()
mainwindow.title("FIT-BIT")
mainwindow.configure(bg='green')
mainwindow.geometry('500x550')
mainwindow.resizable(False,False)
mainwindow.mainloop()
