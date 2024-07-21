from tkinter import *  # star means everything
from tkinter import ttk, messagebox
import pymysql

from PIL import Image, ImageTk

class Car:
    # ----------------  Create a program window   -----------------------------
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x770+1+1")  # dimensions of the program
        self.root.title("Car management program")

        self.root.configure(background="silver")
        self.root.resizable(False, True)  # prevent size control
        # master: place that label show, option: features for label
        title = Label(self.root,
                      text="[ Car management program ]",
                      bg="#1AAECB",
                      font=("Times", 14, "bold italic"),
                      fg="white",  # color for font
                      )
        title.pack(fill=X)
        # ----------------------------variable----------------------------------------
        self.ID_var = StringVar()
        self.name_var = StringVar()
        self.phone_var = StringVar()
        self.addres_var = StringVar()
        self.gender_var = StringVar()
        self.email_var = StringVar()
        self.type_var = StringVar()
        self.place_var = StringVar()
        self.date_var = StringVar()
        self.del_var = StringVar()
        self.search_var = StringVar()

        # ----------------control tools in program ------------------------
        Mange_Frame = Frame(self.root, background="white" ,)
        Mange_Frame.place(x=1310, y=30, width=210, height=500)

        lbl_main = Label(Mange_Frame, text="Information Board", bg="#1AAECB", fg="white")
        lbl_main.pack(fill=X)
        
        lbl_ID = Label(Mange_Frame, text="ID For Customer", bg="white")
        lbl_ID.pack()

        ID_Entry = Entry(Mange_Frame, textvariable=self.ID_var, bd="5", justify="center")
        ID_Entry.pack()
        
        lbl_name = Label(Mange_Frame, text="Name For Customer", bg="white")
        lbl_name.pack()

        name_Entry = Entry(Mange_Frame, textvariable=self.name_var, bd="5", justify="center")
        name_Entry.pack()

        lbl_phone = Label(Mange_Frame, bg="white", text="Phone Number")
        lbl_phone.pack()

        phone_Entry = Entry(Mange_Frame, textvariable=self.phone_var, bd="5", justify="center")
        phone_Entry.pack()

        addres = Label(Mange_Frame, bg="white", text="Home Address")
        addres.pack()

        address = Entry(Mange_Frame, textvariable=self.addres_var, bd="5", justify="center")
        address.pack()

        gender = Label(Mange_Frame, bg="white", text="Gender")
        gender.pack()
        Combo_Gender = ttk.Combobox(Mange_Frame, textvariable=self.gender_var)  # use for customer to choose between two options or more
        Combo_Gender['value'] = ('male', 'female')
        Combo_Gender.pack()

        Email_phone = Label(Mange_Frame, bg="white", text="Email")
        Email_phone.pack()

        email_Entry = Entry(Mange_Frame, textvariable=self.email_var, bd="5", justify="center")
        email_Entry.pack()

        type = Label(Mange_Frame, bg="white", text="Type of Car")
        type.pack()

        type = Entry(Mange_Frame, textvariable=self.type_var, bd="5", justify="center")
        type.pack()

        place = Label(Mange_Frame, bg="white", text="Place of Construction")
        place.pack()

        place = Entry(Mange_Frame, textvariable=self.place_var, bd="5", justify="center")
        place.pack()

        date = Label(Mange_Frame, bg="white", text="Date of Purchase")
        date.pack()

        date = Entry(Mange_Frame, textvariable=self.date_var, bd="5", justify="center")
        date.pack()

        lbl_Delete = Label(Mange_Frame, fg="red", bg="white", text="Delete information by customer name")
        lbl_Delete.pack()
        Delete = Entry(Mange_Frame, textvariable=self.del_var, bd='2', justify='center')
        Delete.pack()
        # ----------------------------------  buttons ----------------------------------------------------------
        Btn_Frame = Frame(self.root, bg="white")
        Btn_Frame.place(x=1310, y=490, width=210, height=310)
        title1 = Label(Btn_Frame, text="Control Board", font=("Times", 14), fg='white', bg="#1AAECB")
        title1.pack(fill=X)

        add = Button(Btn_Frame, text='Add Customer', bg='#85929E', fg="white", command=self.add_car)
        add.place(x=33, y=39, width=150, height=30)

        delete_car = Button(Btn_Frame, text="Delete Customer", bg="#85929E", fg="white", command=self.delete_car)
        delete_car.place(x=33, y=80, width=150, height=30)

        update_car = Button(Btn_Frame, text="Update Customer", bg="#85929E", fg="white", command=self.update_car)
        update_car.place(x=33, y=115, width=150, height=30)

        about_btn = Button(Btn_Frame, text="Search Customer", bg="#85929E", fg="white", command=self.search_customer)
        about_btn.place(x=33, y=150, width=150, height=30)

        clear_btn = Button(Btn_Frame, text="Clear All", bg="#85929E", fg="white", command=self.clear_all)
        clear_btn.place(x=33, y=185, width=150, height=30)

        exit_btn = Button(Btn_Frame, text="Exit", bg="#85929E", fg="white", command=self.root.quit)
        exit_btn.place(x=33, y=225, width=150, height=30)
        # ------------------------------------ search manage ----------------------------------------------
        search_frame = Frame(self.root, background="white")
        search_frame.place(x=1, y=31, width=1305, height=50)

        lbl_Search = Label(search_frame, text="Search a Car or Tools", bg="white")
        lbl_Search.place(x=10, y=12)

        combo_search = ttk.Combobox(search_frame, justify="left")
        combo_search['value'] = ('  Type of car', 'ID For Coustmer')
        combo_search.place(x=130, y=12)

        search_entry = Entry(search_frame, textvariable=self.search_var, justify='left', bd='2')
        search_entry.place(x=280, y=12)

        search_bt = Button(search_frame, text="Search", bg="#3498BD", fg='WHITE')
        search_bt.place(x=410, y=12, width=100, height=25)
        # ------------------------------------- details and information - ---------------------------------------

        details_Frame = Frame(self.root, bg="#f2f4f4")
        details_Frame.place(x=4, y=82, width=1307, height=678)

        # ----------------------------------- Scroll ----------------------------------------------
        SCROLL_x = Scrollbar(details_Frame, orient=HORIZONTAL)
        SCROLL_y = Scrollbar(details_Frame, orient=VERTICAL)
        
        # ----------------------------------- treeview --------------------------------------------
        self.car_table = ttk.Treeview(details_Frame,
                                      columns=('ID For customer','name for customer', 'phone number', 'address', 'gender', 'email', 'type', 'place made', 'since',),
                                        xscrollcommand=SCROLL_x.set,
                                        yscrollcommand=SCROLL_y.set)
        self.car_table.place(x=17, y=1, width=1285, height=650)

        SCROLL_x.pack(side=BOTTOM, fill=X)
        SCROLL_y.pack(side=LEFT, fill=Y)
        SCROLL_x.config(command=self.car_table.xview)
        SCROLL_y.config(command=self.car_table.yview)

        self.car_table['show'] = 'headings'
        self.car_table.heading('ID For Customer', text="ID For Customer")
        
        self.car_table.heading('name for customer', text="Name for Customer")
        self.car_table.heading('phone number', text="Phone Number")
        self.car_table.heading('address', text="Address")
        self.car_table.heading('gender', text="Gender")
        self.car_table.heading('email', text="Email")
        self.car_table.heading('type', text="Type of car")
        self.car_table.heading('place made', text="Place of construction")
        self.car_table.heading('since', text="Date of purchase")

        self.car_table.column('ID For Customer', width=10)
        self.car_table.column('name for customer', width=100)
        self.car_table.column('phone number', width=65)
        self.car_table.column('address', width=130)
        self.car_table.column('gender', width=30)
        self.car_table.column('email', width=70)
        self.car_table.column('type', width=30)
        self.car_table.column('place made', width=70)
        self.car_table.column('since', width=30)

        # Fetch and display the initial data
        self.fetch_and_display_data()

    # --------------------------- call and connection with database-------------------------------------------
    def add_car(self):
        connect = pymysql.connect(
            host='localhost', user='root', password='', database='cardat'
        )
        cur = connect.cursor()

        cur.execute(f"""
            INSERT INTO `car information` (
                ID_For_Customer,name_of_customer, phone_number, address, gender, email, type_of_car, place_of_construction, date_of_purchasing
            ) VALUES (
                '{self.ID_var.get()}',
                '{self.name_var.get()}',
                '{self.phone_var.get()}',
                '{self.addres_var.get()}',
                '{self.gender_var.get()}',
                '{self.email_var.get()}',
                '{self.type_var.get()}',
                '{self.place_var.get()}',
                '{self.date_var.get()}'
            )
        """)

        connect.commit()
        connect.close()

        self.fetch_and_display_data()
        self.clear_fields()

    def delete_car(self):
        selected_item = self.car_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a record to delete")
            return

        connect = pymysql.connect(
            host='localhost', user='root', password='', database='cardat'
        )
        cur = connect.cursor()

        item = self.car_table.item(selected_item)
        customer_name = item['values'][0]

        cur.execute(f"DELETE FROM `car information` WHERE name_of_customer = '{customer_name}'")
        connect.commit()
        connect.close()

        self.fetch_and_display_data()

    def update_car(self):
        selected_item = self.car_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a record to update")
            return

        connect = pymysql.connect(
            host='localhost', user='root', password='', database='cardat'
        )
        cur = connect.cursor()

        item = self.car_table.item(selected_item)
        customer_name = item['values'][0]

        cur.execute(f"""
            UPDATE `car information` SET 
                phone_number='{self.phone_var.get()}', 
                address='{self.addres_var.get()}', 
                gender='{self.gender_var.get()}', 
                email='{self.email_var.get()}',
                ID='{self.ID_var.get()}',   
                type_of_car='{self.type_var.get()}', 
                place_of_construction='{self.place_var.get()}', 
                date_of_purchasing='{self.date_var.get()}' 
            WHERE name_of_customer='{customer_name}'
        """)

        connect.commit()
        connect.close()

        self.fetch_and_display_data()
        self.clear_fields()

    def fetch_and_display_data(self):
        connect = pymysql.connect(
            host='localhost', user='root', password='', database='cardat'
        )
        cur = connect.cursor()

        cur.execute("SELECT ID_For_Customer,name_of_customer, phone_number, address, gender, email, type_of_car, place_of_construction, date_of_purchasing FROM `car information`")
        rows = cur.fetchall()
# write of two number program 


        for item in self.car_table.get_children():
            self.car_table.delete(item)

        for row in rows:
            self.car_table.insert('', 'end', values=row)

        connect.close()

    def search_customer(self):
        # Implement search functionality if needed
        pass

    def clear_all(self):
        for item in self.car_table.get_children():
            self.car_table.delete(item)

    def clear_fields(self):
        self.ID_var.set("")
        self.name_var.set("")
        self.phone_var.set("")
        self.addres_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.type_var.set("")
        self.place_var.set("")
        self.date_var.set("")


root = Tk()
ob = Car(root)
root.mainloop()  # command to run the program


 

