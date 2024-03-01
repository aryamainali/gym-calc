import tkinter as Tk
from tkinter import Label, Button, Radiobutton, Entry, Text, ttk, Listbox, messagebox, END
import pymysql.cursors

# Database connection
# mysql connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='********',
    database='proUI'
)

cur = connection.cursor()
cur.execute("SELECT * FROM Usertable")
data = cur.fetchall()

# Dashboard page
def Dashboard_page(page, logout):
    # Styling and colors
    style = ttk.Style()
    style.configure("CustomTab.TFrame", background="navy", fieldbackground="navy")
    style.configure("CustomTab.Treeview", background="light blue", fieldbackground="light blue")

    # Create tabs within the dashboard table
    tab = ttk.Notebook(page)
    tab1 = ttk.Frame(tab, style="CustomTab.TFrame")
    tab3 = ttk.Frame(tab, style="CustomTab.TFrame")
    tab2 = ttk.Frame(tab, style="CustomTab.TFrame")
    tab4 = ttk.Frame(tab, style="CustomTab.TFrame")

    # Assign names to the tab tables
    tab.add(tab1, text='Description')
    tab.add(tab2, text="Select Training Plans")
    tab.add(tab3, text='Register')
    tab.add(tab4, text='Calculate')
    tab.pack(expand=1, fill='both')
    
     # Label for the gym's best fitness in the Description tab
    l1 = Label(tab1, text='Best Fitness')
    l1.configure(bg='red')
    l1.place(x=30, y=40)

    # Empty text box in the Description tab
    l2 =Text(tab1, bg="pale goldenrod", padx=30, pady=30, height=10, width=38)
    l2.insert(END, "Welcome to our gyms monthly calculator\n"
                  "Helping our customer is our \nmajor responsibility.\n"
                  "We are really proud of our customer\n\n\n"
                  "Thank You for choosing us!!!!!!!!")

    l2.place(x=120, y=30)
    # Tree table with two columns to display gym plans
    tree = ttk.Treeview(tab1, columns=("c1", "c2", "c3"), show='headings', style="CustomTab.Treeview")
    tree.column('#1', width=50)
    tree.column('#2', width=300)
    tree.column('#3', width=50)

    # Assign heading names
    tree.heading("#1", text='Index No')
    tree.heading("#2", text='Training Plan')
    tree.heading("#3", text='Prices')

    # Insert data into the tree table
    tree.insert('', 'end', values=(1, 'Beginner (2 sessions per week) - weekly fee', '1000'))
    tree.insert('', 'end', values=(2, 'Intermediate (3 sessions per week) - weekly fee', '2000'))
    tree.insert('', 'end', values=(3, 'Elite (more than 5 sessions per week) - weekly fee', '3000'))
    tree.insert('', 'end', values=(4, 'Private Trainer - per hour', '500'))
    tree.insert('', 'end', values=(5, 'Sauna - per session', '1500'))
    tree.insert('', 'end', values=(6, 'Swimming - per session', '500'))

    # Place the tree table
    tree.place(x=30, y=280, width=450, height=150)

        # Configuring registration tab for new users
    lb = Listbox(tab3)
    lb.place(x=330, y=30)

    # Customer name
    l0 = Label(tab3, text="For new users")
    l0.config(bg="pink")
    l0.pack()

    l1 = Label(tab3, text='Customer Name')
    l1.config(bg='red', padx=15, pady=3)
    l1.place(x=10, y=35)

    e1 = Entry(tab3)
    e1.place(x=160, y=38)

    # Customer address
    l2 = Label(tab3, text='Customer Address')
    l2.config(bg='red', padx=15, pady=3)
    l2.place(x=10, y=70)

    e2 = Entry(tab3)
    e2.place(x=160, y=76)

    # Customer email
    l3 = Label(tab3, text='Customer Email')
    l3.config(bg='red', padx=15, pady=3)
    l3.place(x=10, y=100)

    e3 = Entry(tab3)
    e3.place(x=160, y=108)

    # Weight category
    l4 = Label(tab3, text='Weight In (KG)')
    l4.config(bg='red', padx=15, pady=3)
    l4.place(x=10, y=134)

    e4 = Entry(tab3)
    e4.place(x=160, y=138)

    # Target weight
    l5 = Label(tab3, text='Target Weight')
    l5.config(bg='red', padx=15, pady=3)
    l5.place(x=10, y=166)

    e5 = Entry(tab3)
    e5.place(x=160, y=170)

    # Configuring registration tab for existing users
    l6 = Label(tab3, text="For existing users")
    l6.config(bg='pink', padx=15, pady=3)
    l6.place(x=100, y=265)

    l7 = Label(tab3, text="Customer Name")
    l7.config(bg='pink', padx=15, pady=3)
    l7.place(x=10, y=310)
    e8 = Entry(tab3)
    e8.place(x=160, y=310)

    l8 = Label(tab3, text="Customer Email")
    l8.config(bg='pink', padx=15, pady=3)
    l8.place(x=10, y=360)
    e9 = Entry(tab3)
    e9.place(x=160, y=360)
    
    
    
    def new_register():
        global selected_plan, selected_sauna, private_coaching_hours, swimming_session
        cur = connection.cursor()
        cur.execute("SELECT * FROM Usertable WHERE customer_email = %s", (e3.get()))
        existing_user = cur.fetchone()

        if existing_user:
            messagebox.showinfo("Duplicate email Entry", "User can still view or update information.")
            return
        else:
            # Insert the new user into the database
            cur.execute("INSERT INTO Usertable (customer_name, customer_address, customer_email, tranning_plans, sauna, swimming, personnel_train_hour, weight_kg, target_weight_kg) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (e1.get(), e2.get(), e3.get(), selected_plan, selected_sauna, swimming_session, private_coaching_hours, e4.get(), e5.get()))
            connection.commit()
            messagebox.showinfo("Entry Added", "New entry has been successfully added.")
            lb.insert(END, e1.get(), e2.get(), e3.get(), e4.get(), e4.get())
        e2.delete(0, END)
        e3.delete(0, END)
        

        
    
    
    new_entry_button=Button(tab3,text="register",command=new_register)
    new_entry_button.place(y=220,x=220)
    
    def on_check():
        global selected_plan, selected_sauna, private_coaching_hours, swimming_session
        cur=connection.cursor()
        cur.execute("SELECT * FROM Usertable WHERE customer_name = %s AND customer_email = %s", (e8.get(),e9.get()))
        existing_user = cur.fetchone()
        if not existing_user:
            messagebox.showerror("Invalid request","User with this email doesnot exists in the database.")
        
        else: 
            cur.execute("UPDATE Usertable SET tranning_plans = %s , sauna=%s,swimming=%s, personnel_train_hour=%s"
                        "WHERE customer_email = %s",
                        (selected_plan,selected_sauna,swimming_session,private_coaching_hours,e9.get()))
            connection.commit()
            messagebox.showinfo("Update Successful", "Training plan has been updated for the existing user.")   
            lb.insert(END, existing_user)           
            messagebox.showinfo("Entry Found", "user with this email exixt in database.")
            
            
    check_button =Button(tab3,text="check/update\nold and new entry",command=on_check)
    check_button.place(x=260,y=400)       
    

# --------------------------------------------------------------/\\
    
    # Create a variable to store the selected value
    training_plan = Tk.IntVar()
    training_plan.set(1) 

    # Create the radio buttons for selecting the training plan
    r1 = Radiobutton(tab2, text="Beginner", variable=training_plan, value=1)
    r2 = Radiobutton(tab2, text="Intermediate", variable=training_plan, value=2)
    r3 = Radiobutton(tab2, text="Elite", variable=training_plan, value=3)

    # Place the radio buttons at specific coordinates
    r1.place(x=200, y=40)
    r2.place(x=200, y=75)
    r3.place(x=200, y=108)
    
    l2 = Label(tab2, text="tranning plans")
    l2.config(bg='red', padx=15, pady=3)
    l2.place(x=10, y=40)


    # Sauna entry
    l2 = Label(tab2, text="Do you want to add\n sauna sessions?")
    l2.config(bg='red', padx=15, pady=3)
    l2.place(x=10, y=150)

    sauna = Tk.IntVar()

    # Create the radio buttons for selecting whether to use the sauna
    r4 = Radiobutton(tab2, text="Yes", variable=sauna, value=1)
    r5 = Radiobutton(tab2, text="No", variable=sauna, value=0)

    # Place the radio buttons at specific coordinates
    r4.place(x=200, y=150)
    r5.place(x=250, y=150)

    # Private trainer entry
    l3 = Label(tab2, text="Enter the number of hours\n of private coaching: ")
    l3.config(bg='red', padx=15, pady=3)
    l3.place(x=10, y=250)

    e6 = Entry(tab2)
    e6.place(x=200, y=260)

    l4 = Label(tab2, text="Swimming sessions")
    l4.config(bg='red', padx=15, pady=3)
    l4.place(x=10, y=320)
    e7 = Entry(tab2)
    e7.place(x=200, y=320)

    def store_values():
        global selected_plan, selected_sauna, private_coaching_hours, swimming_session

        # Get the selected training plan
        plan_value = training_plan.get()
        if plan_value == 1:
            selected_plan = "Beginner"
        elif plan_value == 2:
            selected_plan = "Intermediate"
        elif plan_value == 3:
            selected_plan = "Elite"
        else:
            selected_plan = ""

        # Get the selected sauna value
        sauna_bool = sauna.get()
        if sauna_bool == 1:
            selected_sauna = "Yes"
        else:
            selected_sauna = "No"

        # Get the private coaching hours
        private_coaching_hours = e6.get()

        # Get the swimming sessions
        swimming_session = e7.get()

        print(selected_plan, selected_sauna, private_coaching_hours, swimming_session)

    
    store_button = Button(tab2, text="Submit", command=store_values)
    store_button.place(x=250, y=380)


# --------------------------------------------------------------------------------



# calculate USers


    
    def compare_weight():
        global weight_comparison
        current_weight=float(e4.get())
        target_weight=float(e5.get())
        if current_weight < target_weight:
            weight_comparison = "Underweight"
            
        elif current_weight > target_weight:
            weight_comparison = "Overweight"
            
        else:
            weight_comparison = "Normal weight"
        print(weight_comparison)
    
    weight_button = Button(tab3, text="store weight", command=compare_weight)
    weight_button.place(x=400, y=350)
    
    # Function to calculate and display the cost of training

    
    result_listbox = Tk.Listbox(tab4, background="grey", width=70, height=16)
    result_listbox.grid(row=0, column=0, padx=10, pady=10)
    def calculate_cost():
        global customer_name
        customer_name = (e1.get() or e8.get() )
        plan_value = training_plan.get()

        if plan_value == "":
            messagebox.showerror("Error", "Please select a training plan.")
            return

        try:
            plan_value = int(plan_value)
        except ValueError:
            messagebox.showerror("Error", "Invalid training plan selected.")
            return

        if plan_value == 1:
            selected_plan = "Beginner"
            plan_cost = 1000 * 4
        elif plan_value == 2:
            selected_plan = "Intermediate"
            plan_cost = 2000 * 4
        elif plan_value == 3:
            selected_plan = "Elite"
            plan_cost = 3000 * 4
        else:
            messagebox.showerror("Error", "Invalid training plan selected.")
            return

        sauna_bool = sauna.get()

        if sauna_bool == "":
            messagebox.showerror("Error", "Please select whether to use the sauna.")
            return

        try:
            sauna_bool = int(sauna_bool)
        except ValueError:
            messagebox.showerror("Error", "Invalid sauna option selected.")
            return

        if sauna_bool == 1:
            selected_sauna = "Yes"
            sauna_cost = 1500
        elif sauna_bool == 0:
            selected_sauna = "No"
            sauna_cost = 0
        else:
            messagebox.showerror("Error", "Invalid sauna option selected.")
            return

        private_coaching_hours = e6.get()

        if private_coaching_hours == "":
            messagebox.showerror("Error", "Please enter the number of hours of private coaching.")
            return

        try:
            private_coaching_hours = int(private_coaching_hours)
        except ValueError:
            messagebox.showerror("Error", "Invalid value for private coaching hours.")
            return

        private_coaching_cost = private_coaching_hours * 500

        swimming_sessions = e7.get()

        if swimming_sessions == "":
            messagebox.showerror("Error", "Please enter the number of swimming sessions.")
            return

        try:
            swimming_sessions = int(swimming_sessions)
        except ValueError:
            messagebox.showerror("Error", "Invalid value for swimming sessions.")
            return

        swimming_cost = swimming_sessions * 500

        total_cost = plan_cost + sauna_cost + private_coaching_cost + swimming_cost

        result_listbox.insert(END, "Customer name: {}".format(customer_name))
        result_listbox.insert(END, "Training plan: {}".format(selected_plan))
        result_listbox.insert(END, "Training plan cost: {:.2f}".format(plan_cost))
        result_listbox.insert(END, "Sauna option: {}".format(selected_sauna))
        result_listbox.insert(END, "Sauna cost: {:.2f}".format(sauna_cost))
        result_listbox.insert(END, "Private coaching hours: {}".format(private_coaching_hours))
        result_listbox.insert(END, "Private coaching cost: {:.2f}".format(private_coaching_cost))
        result_listbox.insert(END, "Swimming sessions: {}".format(swimming_sessions))
        result_listbox.insert(END, "Swimming cost: {:.2f}".format(swimming_cost))
        result_listbox.insert(END, "Total cost for the month: {:.2f}".format(total_cost))
        result_listbox.insert(END, "Weight Comparison: {}".format(weight_comparison))


    calculate_button = Tk.Button(tab4, text="Calculate Cost", command=calculate_cost)
    calculate_button.grid(row=1, column=0, padx=10, pady=10)
