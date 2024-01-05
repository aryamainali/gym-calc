import tkinter as tk 
from tkinter import Label,Button,Entry,messagebox
import pymysql,hashlib

connection = pymysql.connect(
                                host='localhost',
                                user='root',
                                password='********',
                                database='proUI'
)

def Login_page(page,login):
    l0=Label(page,text='login')
    l0.pack()
    
    l2 =Label(page,text="User Name")
    l2.place(x=60,y=60)    
    e1 =Entry(page)
    e1.place(x=140,y=60)
    
    l3 =Label(page,text="Password")
    l3.place(x=60,y=90)    
    e2 =Entry(page,show="*")
    e2.place(x=140,y=90)
    
    
    def Login_to_page():
        username = e1.get()
        password = e2.get()

        cur = connection.cursor()
        cur.execute("SELECT * FROM USERS WHERE LOWER(USERNAME) = %s", (username.lower(),))
        result = cur.fetchone()

        if result is not None:
            db_username = result[0]
            db_password = result[1]
            print(db_username, db_password)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            if db_password == hashed_password:
                print(hashed_password)
                messagebox.showinfo("Success", "Successfully logged in")
                login()
                     
            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            messagebox.showerror("Error", "Invalid username")

        # Clear the entry fields
        e1.delete(0, 'end')
        e2.delete(0, 'end')


    login_button = Button(page, text="Login", command=Login_to_page)
    login_button.place(x=330, y=140)


    # b1=Button(page,text='proceed',padx=5,pady=0,command=login)
    # b1.place(x=280,y=55)

    # e1=Entry(page)
    # e1.place(x=120,y=38)

    # e2=Entry(page)
    # e2.place(x=120,y=73)
