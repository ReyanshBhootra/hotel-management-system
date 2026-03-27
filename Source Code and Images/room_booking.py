from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import pymysql.connections
from tkinter import messagebox
from tkcalendar import *
from datetime import datetime
from time import strftime

class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Window")
        self.root.geometry("1200x565+327+218")
        # Disable maximizing the window
        self.root.resizable(False, False)


        # ----------------variables------------------------
        self.var_email = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_availableroom = StringVar()
        self.var_meal = StringVar()
        self.var_noOfDays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal = StringVar()
        self.var_total = StringVar()

        lbl_title = Label(self.root, text=('ROOM BOOKING DETAILS'), font=('Georgia', 18, 'bold'), bg='black',
                          fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1200, height=50)

        # ----------------logo-----------------
        img2 = Image.open(r".\images\hotelLogo.png")
        img2 = img2.resize((100, 41))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root, image=self.photoimg2, bd=2, background='gold', relief=RIDGE)
        lbling.place(x=5, y=6, width=100, height=41)

        # ------------------labelFrame---------------------
        labelFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text='Room Booking Details', padx=2,
                                    font=('Georgia', 14, 'bold'), fg='firebrick4')
        labelFrameLeft.place(x=5, y=50, width=450, height=512)

        # ------------------------------------Labels and entrys-----------------------------
        # email entry
        lbl_email = Label(labelFrameLeft, text='Customer Email:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_email.grid(row=0, column=0, sticky=W)

        self.entry_email = ttk.Entry(labelFrameLeft, width=21, textvariable=self.var_email, font=('Georgia', 12, 'bold'))
        self.entry_email.grid(row=0, column=1, sticky=W)

        # checkIn
        lbl_checkInDate = Label(labelFrameLeft, text='CheckIn Date:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_checkInDate.grid(row=1, column=0, sticky=W)

        self.txtCheckInDate = ttk.Entry(labelFrameLeft, width=28, textvariable=self.var_checkin, font=('Georgia', 12, 'bold'))
        self.txtCheckInDate.insert(0, "mm/dd/yyyy")
        self.txtCheckInDate.grid(row=1, column=1, sticky=W)
        # Bind the calendar to the entry widget for check in
        self.txtCheckInDate.bind("<1>", self.pick_date_checkin)


        # checkOut
        lbl_checkOut = Label(labelFrameLeft, text='CheckOut Date:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_checkOut.grid(row=2, column=0, sticky=W)

        self.txtCheckOutDate = ttk.Entry(labelFrameLeft, width=28, textvariable=self.var_checkout, font=('Georgia', 12, 'bold'))
        self.txtCheckOutDate.insert(0, 'mm/dd/yyyy')
        self.txtCheckOutDate.grid(row=2, column=1, sticky=W)
        # Bind the calendar to the entry widget for check out
        self.txtCheckOutDate.bind("<1>", self.pick_date_checkout)

        # Room Type
        label_RoomType = Label(labelFrameLeft, text='Room Type:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)
        self.var_roomtype = StringVar()
        self.combo_RoomType = ttk.Combobox(labelFrameLeft, font=('Georgia', 12, 'bold'), textvariable=self.var_roomtype,
                                          width=26, state='readonly')
        self.combo_RoomType['values'] = ("Single", "Double", "Suite", "Deluxe Suite")
        self.combo_RoomType.grid(row=3, column=1, sticky=W)
        # Bind the function to update available rooms when room type changes
        self.combo_RoomType.bind("<<ComboboxSelected>>", self.update_available_rooms)

        # Available Room
        lbl_AvailableRoom = Label(labelFrameLeft, text='Available Room:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_AvailableRoom.grid(row=4, column=0, sticky=W)

        self.var_availableroom = StringVar()
        self.combo_AvailableRoom = ttk.Combobox(labelFrameLeft, font=('Georgia', 12, 'bold'), textvariable=self.var_availableroom,
                                                width=26, state='readonly')
        self.combo_AvailableRoom.grid(row=4, column=1, sticky=W)


        # Meal
        lbl_meal = Label(labelFrameLeft, text='Meal:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)
        # Use a Listbox for multiple meal selection
        self.listbox_meal = Listbox(labelFrameLeft, width=28, selectmode=MULTIPLE, font=('Georgia', 12, 'bold'), height=3,
                                    selectbackground='firebrick4', selectforeground='black')  # Set selectbackground and selectforeground
        self.listbox_meal.grid(row=5, column=1, sticky=W)
        # Populate the Listbox with meal options
        meal_options = ["Breakfast", "Lunch", "Dinner"]
        for meal in meal_options:
            self.listbox_meal.insert(END, meal)

        #No. of days
        lbl_NumberOfDays = Label(labelFrameLeft, text='Number of Days:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_NumberOfDays.grid(row=6, column=0, sticky=W)

        self.txtNumberOfDays = ttk.Entry(labelFrameLeft, width=28, textvariable=self.var_noOfDays,
                                    font=('Georgia', 12, 'bold'), state='readonly')  # Set to read-only
        self.txtNumberOfDays.grid(row=6, column=1, sticky=W)

        # Paid Tax
        lbl_PaidTax = Label(labelFrameLeft, text='Paid Tax:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_PaidTax.grid(row=7, column=0, sticky=W)
        # pound symbol
        lbl_poundsymbol= Label(labelFrameLeft, text='£', font=('Georgia', 12, 'bold'))
        lbl_poundsymbol.place(x=133, y=270)

        self.txtPaidTax = ttk.Entry(labelFrameLeft, width=28, textvariable=self.var_paidtax, font=('Georgia', 12, 'bold'),
                               state='readonly')  # Set to read-only
        self.txtPaidTax.grid(row=7, column=1, sticky=W)

        # Sub Total
        lbl_SubTotal = Label(labelFrameLeft, text='Sub Total:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_SubTotal.grid(row=8, column=0, sticky=W)
        # pound symbol
        lbl_poundsymbol= Label(labelFrameLeft, text='£', font=('Georgia', 12, 'bold'))
        lbl_poundsymbol.place(x=133, y=303)

        self.txtSubTotal = ttk.Entry(labelFrameLeft, width=28, textvariable=self.var_subtotal, font=('Georgia', 12, 'bold'),
                                state='readonly')  # Set to read-only
        self.txtSubTotal.grid(row=8, column=1, sticky=W)

        # Total Cost
        lbl_TotalCost = Label(labelFrameLeft, text='Total Cost:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_TotalCost.grid(row=10, column=0, sticky=W)
        # pound symbol
        lbl_poundsymbol= Label(labelFrameLeft, text='£', font=('Georgia', 12, 'bold'))
        lbl_poundsymbol.place(x=133, y=337)

        self.txtTotalCost = ttk.Entry(labelFrameLeft, width=28, textvariable=self.var_total, font=('Georgia', 12, 'bold'),
                                 state='readonly')  # Set to read-only
        self.txtTotalCost.grid(row=10, column=1, sticky=W)

        #----------------------------fetch button------------------------
        # FETCH DATA BUTTON
        btnfetchData = Button(labelFrameLeft, command=self.Fetch_email, text='Fetch Data', font=('Georgia', 9, 'bold'),
                              bg='black', fg='firebrick1', width=8, activeforeground='firebrick1',
                              activebackground='black')
        btnfetchData.place(x=358, y=4)

        # ---------------------------bill button-------------------------
        btnBill = Button(labelFrameLeft, text='Bill', command=self.total,font=('Georgia', 12, 'bold'), bg='black', fg='firebrick1',
                         width=8, activeforeground='firebrick1', activebackground='black')
        btnBill.grid(row=11, column=0, padx=1, sticky=W)

        # -----------------------------------buttons--------------------------
        btn_frame = Frame(labelFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=15, y=420, width=416, height=40)

        btnAdd = Button(btn_frame, text='Add', command=self.add_data, font=('Georgia', 12, 'bold'), bg='black',
                        fg='gold', width=8, activeforeground='gold', activebackground='black')
        btnAdd.grid(row=0, column=0, padx=3)

        btnUpdate = Button(btn_frame, text='Update', command=self.update, font=('Georgia', 12, 'bold'), bg='black',
                           fg='gold', width=8, activeforeground='gold', activebackground='black')
        btnUpdate.grid(row=0, column=1, padx=2)

        btnDelete = Button(btn_frame, text='Delete', command=self.delete, font=('Georgia', 12, 'bold'), bg='black',
                           fg='gold', width=8, activeforeground='gold', activebackground='black')
        btnDelete.grid(row=0, column=2, padx=2)

        btnReset = Button(btn_frame, text='Reset', command=self.reset, font=('Georgia', 12, 'bold'), bg='black',
                          fg='gold', width=8, activeforeground='gold', activebackground='black')
        btnReset.grid(row=0, column=3, padx=3)

        # -------------------------------right side image--------------------------------------

        img3 = Image.open(r".\images\roomimg.png")
        img3 = img3.resize((520, 230))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbling = Label(self.root, image=self.photoimg3, bd=2, relief=RIDGE)
        lbling.place(x=786, y=51, width=410, height=233)

        # ================================table frame search==========================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text='View Details And Search System', padx=2,
                                 font=('Georgia', 14, 'bold'), fg='firebrick4')
        Table_Frame.place(x=455, y=280, width=738, height=282)

        lblSearchBy = Label(Table_Frame, text='Search By:', font=('Georgia', 12, 'bold'), bg='red', fg='white')
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)


        # email or mobile number to search from
        self.search_var = StringVar()
        combo_SearchBy = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=('Georgia', 12, 'bold'), width=20,
                                      state='readonly')
        combo_SearchBy['values'] = ("Email", "Mobile Number")
        combo_SearchBy.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearchBy = ttk.Entry(Table_Frame, width=21, textvariable=self.txt_search, font=('Georgia', 12, 'bold'))
        txtSearchBy.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text='Search',command=self.search, font=('Georgia', 12, 'bold'), bg='black', fg='gold', width=7,
                           activeforeground='gold', activebackground='black')
        btnSearch.grid(row=0, column=3, padx=4)

        btnShowAll = Button(Table_Frame, text='Show All',command=self.fetch_data,font=('Georgia', 12, 'bold'), bg='black', fg='gold', width=7,
                            activeforeground='gold', activebackground='black')
        btnShowAll.grid(row=0, column=4, padx=2)

        # =================================show data=========================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=763, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, columns=(
        "email", "checkInDate", "checkOutDate", "roomtype", "availableroom", "meal", "numberOfDays", "paid_tax", "subtotal", "total_cost",),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # Define column names and their corresponding text labels in a dictionary
        column_headings = {
            'email': 'Email',
            'checkInDate': 'CheckIn-Date',
            'checkOutDate': 'CheckOut-Date',
            'roomtype': 'Room-Type',
            'availableroom': 'Available-Room',
            'meal': 'Meal',
            'numberOfDays': 'NumberOfDays',
            'paid_tax' : 'Paid-Tax',
            'subtotal' : 'Subtotal',
            'total_cost' : 'Total'
        }

        # Set column headings using a loop
        for column, heading in column_headings.items():
            self.room_table.heading(column, text=heading)

        self.room_table['show'] = 'headings'

        # Define the columns and their respective widths in a dictionary
        columns = {
            'email': 100,
            'checkInDate': 100,
            'checkOutDate': 100,
            'roomtype': 100,
            'availableroom': 100,
            'meal': 100,
            'numberOfDays': 100,
            'paid_tax' : 100,
            'subtotal' : 100,
            'total_cost' : 100
        }

        # Set column widths using a loop
        for column, width in columns.items():
            self.room_table.column(column, width=width)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()

        # Create the 'roominfo' table if it doesn't exist
        self.create_roominfo_table()

    def update_available_rooms(self, event):
        selected_room_type = self.var_roomtype.get()

        # Save the current meal selections
        selected_meals = [self.listbox_meal.get(idx) for idx in self.listbox_meal.curselection()]

        if selected_room_type:
            con = self.connect_to_database()
            my_cursor = con.cursor()
            my_cursor.execute('SELECT room_no FROM roomdetails WHERE room_type=%s', (selected_room_type,))
            rows = my_cursor.fetchall()

            # Clear previous values and update with new ones
            current_selection = self.combo_AvailableRoom.get()  # Save current room selection
            self.var_availableroom.set("")  # Clear previous selection
            self.combo_AvailableRoom['values'] = rows

            # Restore the previous room selection
            if current_selection in rows:
                self.combo_AvailableRoom.set(current_selection)

            # Restore the previous meal selections only if there are available meals
            if self.listbox_meal.size() > 0 and selected_meals:
                self.listbox_meal.selection_clear(0, END)
                for meal in selected_meals:
                    try:
                        index = self.listbox_meal.get(0, END).index(meal)
                        self.listbox_meal.selection_set(index)
                    except ValueError:
                        pass

        con.close()

    # to pick the date for check in
    def pick_date_checkin(self, event):
        global cal, date_window
        date_window = Toplevel()
        date_window.grab_set()
        date_window.title('Choose Check-in Date')
        date_window.geometry('250x220+590+370')

        # Set the minimum date to the current date
        today = datetime.today().date()
        cal = Calendar(date_window, selectmode='day', date_pattern='mm/dd/y', mindate=today)
        cal.place(x=0, y=0)

        submit_btm = Button(date_window, text='Submit', command=self.grab_date_checkin,
                            font=('Georgia', 10, 'bold'), bg='black', fg='gold', width=7,
                           activeforeground='gold', activebackground='black')
        submit_btm.place(x=91, y=188)
    
    # to pick the date for check out
    def pick_date_checkout(self, event):
        global cal, date_window
        date_window = Toplevel()
        date_window.grab_set()
        date_window.title('Choose Check-out Date')
        date_window.geometry('250x220+590+370')

        # Set the minimum date to the current date
        today = datetime.today().date()
        cal = Calendar(date_window, selectmode='day', date_pattern='mm/dd/y', mindate=today)
        cal.place(x=0, y=0)

        submit_btm = Button(date_window, text='Submit', command=self.grab_date_checkout,
                            font=('Georgia', 10, 'bold'), bg='black', fg='gold', width=7,
                           activeforeground='gold', activebackground='black')
        submit_btm.place(x=91, y=188)

    # to grab the check in date from the calender and add it to entry
    def grab_date_checkin(self):
        self.txtCheckInDate.delete(0, END)
        self.txtCheckInDate.insert(0, cal.get_date())
        date_window.destroy()

    # to grab the check out date from the calender and add it to entry
    def grab_date_checkout(self):
        self.txtCheckOutDate.delete(0, END)
        self.txtCheckOutDate.insert(0, cal.get_date())
        date_window.destroy()

    # Database connection method
    def connect_to_database(self):
        return pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')

    # Create the 'roominfo' table if it doesn't exist
    def create_roominfo_table(self):
        try:
            con = self.connect_to_database()
            my_cursor = con.cursor()

            # Define the 'roominfo' table schema
            table_schema = '''
                CREATE TABLE IF NOT EXISTS roominfo (
                    email VARCHAR(255) PRIMARY KEY,
                    checkin_date VARCHAR(10),
                    checkout_date VARCHAR(10),
                    room_type VARCHAR(20),
                    available_room INT,
                    meal VARCHAR(255),
                    number_of_days INT,
                    paid_tax DECIMAL(10, 2),
                    subtotal DECIMAL(10, 2),
                    total_cost DECIMAL(10, 2)
                )
            '''
            my_cursor.execute(table_schema)
            con.commit()

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Database Error: {e}", parent=self.root)

    # Fetch data method with context manager
    def fetch_data(self):
        try:
            with self.connect_to_database() as con:
                my_cursor = con.cursor()
                my_cursor.execute('select * from roominfo')
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.room_table.delete(*self.room_table.get_children())
                    for i in rows:
                        self.room_table.insert('', END, values=i)
                my_cursor.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Database Error: {e}", parent=self.root)

    # Add data method
    def add_data(self):
        try:
            if (
                self.var_email.get() == '' or
                self.var_checkin.get() == '' or
                self.var_checkout.get() == '' or
                self.var_roomtype.get() == '' or
                self.var_availableroom.get() == '' or
                self.var_noOfDays.get() == ''
            ):
                messagebox.showerror('Error', 'All fields are required', parent=self.root)
            else:
                # Check if the room is available for the specified date range
                if not self.is_room_available_to_add():
                    messagebox.showerror('Error', 'Selected room is not available for the specified date range', parent=self.root)
                    return

                # Check if the email exists in the customerinfo table
                con = self.connect_to_database()
                my_cursor = con.cursor()
                query = 'SELECT COUNT(*) FROM customerinfo WHERE email=%s'
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                count = my_cursor.fetchone()[0]
                con.close()

                if count == 0:
                    messagebox.showerror('Error', 'This email is not registered', parent=self.root)
                    return

                # Convert the selected meals into a comma-separated string
                selected_meals_str = ', '.join(self.listbox_meal.get(index) for index in self.listbox_meal.curselection())

                # Proceed with adding room booking details
                con = self.connect_to_database()
                my_cursor = con.cursor()
                my_cursor.execute('''
                    INSERT INTO roominfo VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (
                    self.var_email.get(), self.var_checkin.get(), self.var_checkout.get(),
                    self.var_roomtype.get(), self.var_availableroom.get(), selected_meals_str,
                    self.var_noOfDays.get(), self.var_paidtax.get(),
                    self.var_subtotal.get(),
                    self.var_total.get()
                ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
                self.fetch_data()
                self.reset()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)

    # Check if the selected room is available for the specified date range
    def is_room_available_to_add(self):
        # Establish a database connection
        con = self.connect_to_database()
        my_cursor = con.cursor()

        # Construct the SQL query
        query = '''
            SELECT COUNT(*)
            FROM roominfo
            WHERE available_room=%s
              AND (
                (checkin_date >= %s AND checkin_date <= %s)
                OR (checkout_date >= %s AND checkout_date <= %s)
                OR (%s >= checkin_date AND %s <= checkout_date)
              )
        '''
        # Define query parameters
        values = (
            self.var_availableroom.get(),
            self.var_checkin.get(), self.var_checkout.get(),
            self.var_checkin.get(), self.var_checkout.get(),
            self.var_checkin.get(), self.var_checkout.get()
        )

        # Execute the SQL query
        my_cursor.execute(query, values)

        # Fetch the count of matching records
        count = my_cursor.fetchone()[0]

        # Close the database connection
        con.close()

        # Return True if the room is available; otherwise, return False
        return count == 0


    # Update data method
    def update(self):
        # Convert the selected meals into a comma-separated string
        selected_meals_str = ', '.join(self.listbox_meal.get(index) for index in self.listbox_meal.curselection())
        try:
            # Check if required fields are filled
            if (
                self.var_email.get() == '' or
                self.var_checkin.get() == '' or
                self.var_checkout.get() == '' or
                self.var_roomtype.get() == '' or
                self.var_availableroom.get() == '' or
                self.var_noOfDays.get() == ''
            ):
                messagebox.showerror('Error', 'All fields are required', parent=self.root)
            else:
                # Check if the email exists in the database
                if not self.email_exists_for_update():
                    messagebox.showerror('Error', 'Email does not exist in the database. Cannot update.', parent=self.root)
                    return

                # Check if the room is available for the specified date range
                if not self.is_room_available_for_update():
                    messagebox.showerror('Error', 'Selected room is not available for the specified date range', parent=self.root)
                    return

                con = self.connect_to_database()
                my_cursor = con.cursor()
                my_cursor.execute('''
                    UPDATE roominfo SET
                    checkin_date=%s, checkout_date=%s, room_type=%s,
                    available_room=%s, meal=%s, number_of_days=%s,
                    paid_tax=%s, subtotal=%s, total_cost=%s
                    WHERE email=%s
                ''', (
                    self.var_checkin.get(), self.var_checkout.get(),
                    self.var_roomtype.get(), self.var_availableroom.get(),
                    selected_meals_str,
                    self.var_noOfDays.get(), self.var_paidtax.get(),
                    self.var_subtotal.get(), self.var_total.get(),
                    self.var_email.get()
                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('Update', 'Room details have been updated successfully', parent=self.root)
                self.reset()
                self.entry_email.focus()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)


    # Check if the selected room is available for the specified date range (for update)
    def is_room_available_for_update(self):
        con = self.connect_to_database()
        my_cursor = con.cursor()
        query = '''
            SELECT COUNT(*)
            FROM roominfo
            WHERE available_room=%s
              AND (
                (checkin_date >= %s AND checkin_date <= %s AND email != %s)
                OR (checkout_date >= %s AND checkout_date <= %s AND email != %s)
                OR (%s >= checkin_date AND %s <= checkout_date AND email != %s)
              )
        '''
        values = (
            self.var_availableroom.get(),
            self.var_checkin.get(), self.var_checkout.get(), self.var_email.get(),
            self.var_checkin.get(), self.var_checkout.get(), self.var_email.get(),
            self.var_checkin.get(), self.var_checkout.get(), self.var_email.get()
        )
        my_cursor.execute(query, values)
        count = my_cursor.fetchone()[0]
        con.close()
        return count == 0

    # Function to check if email exists in the database for update
    def email_exists_for_update(self):
        try:
            con = self.connect_to_database()
            my_cursor = con.cursor()
            my_cursor.execute('SELECT * FROM roominfo WHERE email=%s', (self.var_email.get(),))
            existing_record = my_cursor.fetchone()
            con.close()
            return existing_record is not None
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)
            return False

    # delete data
    def delete(self):
        try:
            # Check if the email exists in the database
            if not self.email_exists_for_delete():
                messagebox.showerror('Error', 'Email does not exist in the database. Cannot delete.', parent=self.root)
                return
    
            delete = messagebox.askyesno('Confirm Deletion', 'Are you sure you want to delete the room booking for the customer with email?',
                                         parent=self.root)
            if delete:
                con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
                my_cursor = con.cursor()
                query = "DELETE FROM roominfo WHERE Email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                con.commit()
    
                # Check if there is only one record left in the customerinfo table
                my_cursor.execute("SELECT COUNT(*) FROM roominfo")
                count = my_cursor.fetchone()[0]
                con.close()
    
                # If there is no record left, clear the details_table
                if count == 0:
                    self.room_table.delete(*self.room_table.get_children())
                else:
                    self.fetch_data()  # Fetch updated data after deletion
    
                messagebox.showinfo('Success', 'Room booking details have been deleted successfully', parent=self.root)
                self.reset()  # Reset the entry fields after successful deletion
                self.entry_email.focus()
            else:
                messagebox.showinfo('Info', 'Deletion Cancelled', parent=self.root)
        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}', parent=self.root)

    # Function to check if email exists in the database for deletion
    def email_exists_for_delete(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
            my_cursor = con.cursor()
            my_cursor.execute('SELECT * FROM roominfo WHERE Email=%s', (self.var_email.get(),))
            existing_record = my_cursor.fetchone()
            con.close()
            return existing_record is not None
        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}', parent=self.root)
            return False

    # the reset all the fields
    def reset(self):
        self.var_email.set("")
        self.var_checkin.set("mm/dd/yyyy")
        self.var_checkout.set("mm/dd/yyyy")
        self.var_roomtype.set("")
        self.var_availableroom.set("")
        self.listbox_meal.selection_clear(0, END)
        self.var_noOfDays.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_total.set("")

        # Deselect all items in the details_table
        self.room_table.selection_remove(self.room_table.selection())

    # get cursor
    def get_cursor(self, event=''):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row_values = content.get('values', [])

        # Check if row_values is not empty before updating the reference number
        if row_values:
            self.var_email.set(row_values[0])
            self.var_checkin.set(row_values[1])
            self.var_checkout.set(row_values[2])
            self.var_roomtype.set(row_values[3])
            self.var_availableroom.set(row_values[4])
            self.var_noOfDays.set(row_values[6])
            self.var_paidtax.set(str(row_values[7]))
            self.var_subtotal.set(str(row_values[8]))
            self.var_total.set(str(row_values[9]))

            # Clear previous selection in the meal list box
            self.listbox_meal.selection_clear(0, END)
            # Check if the 'meal' field is not empty in the database
            if row_values[5]:
                # Split the stored meals into a list
                stored_meals = row_values[5].split(', ')
                # Iterate through stored meals and select them in the list box
                for meal in stored_meals:
                    try:
                        index = self.listbox_meal.get(0, END).index(meal)
                        self.listbox_meal.selection_set(index)
                    except ValueError:
                        pass
        else:
            # If row_values is empty, reset all fields
            self.reset()

    # -----------------------all data-------------------------------
    def Fetch_email(self):
        if self.var_email.get() == '':
            messagebox.showerror('Error', 'Please enter an email', parent=self.root)
        else:
            con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
            my_cursor = con.cursor()
            query = ('select FirstName from customerinfo where email=%s')
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'This email is not registered', parent=self.root)
            else:
                con.commit()
                con.close()

                showDataFrame = LabelFrame(self.root, bd=4, relief=RIDGE, text='Customer Details',padx=2,
                                           font=('Georgia', 14, 'bold'), fg='RoyalBlue3')
                showDataFrame.place(x=455, y=50, width=330, height=180)

                lblFirstName = Label(showDataFrame, text='First Name:', font=('Georgia', 12, 'bold'), fg= 'firebrick4')
                lblFirstName.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row, font=('Georgia', 11, 'bold'))
                lbl.place(x=110, y=0)

                # EMAIL
                con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
                my_cursor = con.cursor()
                query = ('select LastName from customerinfo where email=%s')
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblLastName = Label(showDataFrame, text='Last Name:', font=('Georgia', 12, 'bold'), fg= 'firebrick4')
                lblLastName.place(x=0, y=30)

                lbl = Label(showDataFrame, text=row, font=('Georgia', 11, 'bold'))
                lbl.place(x=110, y=30)

                # GENDER
                con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
                my_cursor = con.cursor()
                query = ('select Gender from customerinfo where email=%s')
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataFrame, text='Gender:', font=('Georgia', 12, 'bold'), fg= 'firebrick4')
                lblGender.place(x=0, y=60)

                lbl = Label(showDataFrame, text=row, font=('Georgia', 11, 'bold'))
                lbl.place(x=110, y=60)

                # MOBILE
                con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
                my_cursor = con.cursor()
                query = ('select `Mobile Number` from customerinfo where email=%s')
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblMobileNumber = Label(showDataFrame, text='Mobile No:', font=('Georgia', 12, 'bold'), fg= 'firebrick4')
                lblMobileNumber.place(x=0, y=90)

                lbl = Label(showDataFrame, text=row, font=('Georgia', 11, 'bold'))
                lbl.place(x=110, y=90)

                # CITIZENSHIP
                con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
                my_cursor = con.cursor()
                query = ('select citizenship from customerinfo where email=%s')
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblCitizenship = Label(showDataFrame, text='Citizenship:', font=('Georgia', 12, 'bold'), fg= 'firebrick4')
                lblCitizenship.place(x=0, y=120)

                # Check if the row is not empty before accessing its value
                if row:
                    citizenship_value = row[0]  # Extract the value from the tuple
                    lbl = Label(showDataFrame, text=citizenship_value, font=('Georgia', 11, 'bold'))
                    lbl.place(x=108, y=120)
                else:
                    lbl = Label(showDataFrame, text="N/A", font=('Georgia', 11, 'bold'))  # Handle the case where the value is not found
                    lbl.place(x=108, y=120)
    # -----------------------all data-------------------------------

    # search system
    def search(self):
        try:
            if not self.txt_search.get() or not self.search_var.get():
                messagebox.showerror("Error", "Please select a valid search criteria and enter search term.", parent=self.root)
            else:
                con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
                my_cursor = con.cursor()

                # Use parameterized queries to prevent SQL injection
                search_attribute = str(self.search_var.get())

                if search_attribute in ['Mobile Number', 'Email']:
                    # Check if the entered value is an exact match
                    query = "SELECT * FROM roominfo WHERE email IN (SELECT email FROM customerinfo WHERE `{}` = %s)".format(search_attribute)
                    search_term = self.txt_search.get()  # Assuming the value is entered without wildcards
                else:
                    query = "SELECT * FROM roominfo WHERE `{}` LIKE %s".format(search_attribute)
                    my_cursor.execute(query, (search_term,))


                my_cursor.execute(query, (search_term,))

                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.room_table.delete(*self.room_table.get_children())
                    for i in rows:
                        self.room_table.insert('', END, values=i)
                    con.commit()
                else:
                    messagebox.showinfo("Info", "No matching records found.", parent=self.root)

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)

        finally:
            try:
                my_cursor.close()
                con.close()
            except Exception as e:
                pass

        # Clear the data inside the search entry only if records were found
        if len(rows) != 0:
            self.txt_search.set("")  # Add this line to reset the entry to an empty string

    # to calculate the paidtax, subtotal, and total with meal cost and no of days stayed
    def total(self):
        try:
            # Check if required fields are filled
            if (
                self.var_email.get() == '' or
                self.var_checkin.get() == '' or
                self.var_checkout.get() == '' or
                self.var_roomtype.get() == '' or
                self.var_availableroom.get() == ''
            ):
                messagebox.showerror('Error', 'All fields are required', parent=self.root)
                return

            # Convert check-in and check-out dates to datetime objects
            checkInDate = datetime.strptime(self.var_checkin.get(), '%m/%d/%Y')
            checkOutDate = datetime.strptime(self.var_checkout.get(), '%m/%d/%Y')
            # Check if check-in date is earlier than check-out date
            if checkInDate >= checkOutDate:
                messagebox.showerror('Error', 'Check-in date must be earlier than check-out date', parent=self.root)
                self.entry_email.focus()
                return
            # Calculate the number of days
            no_of_days = abs((checkOutDate - checkInDate).days)
            self.var_noOfDays.set(str(no_of_days))  # Update the number of days field

            # Meal prices per day
            meal_prices_per_day = {'Breakfast': 19, 'Lunch': 35, 'Dinner': 50}

            # If no meals are selected, set meal_price to 0
            selected_meals = self.listbox_meal.curselection()
            meal_price = 0 if not selected_meals else sum(
                meal_prices_per_day.get(self.listbox_meal.get(index), 0) * no_of_days for index in selected_meals
            )

            # Set room type prices
            room_type_prices = {'Single': 500, 'Double': 700, 'Suite': 999, 'Deluxe Suite': 1499}

            # Calculate room type price for the entire stay
            room_type_price = room_type_prices.get(self.var_roomtype.get(), 0) * no_of_days

            # Calculate other costs for the entire stay
            subtotal = meal_price + room_type_price
            paid_tax = 0.09 * subtotal
            total = subtotal + paid_tax

            # Set the calculated values to the corresponding variables
            self.var_paidtax.set(str('%.2f' % paid_tax))
            self.var_subtotal.set(str('%.2f' % subtotal))
            self.var_total.set(str('%.2f' % total))

            # Update the corresponding entry fields
            self.txtNumberOfDays.config(state='normal')
            self.txtNumberOfDays.delete(0, END)
            self.txtNumberOfDays.insert(0, str(no_of_days))
            self.txtNumberOfDays.config(state='readonly')

            self.txtPaidTax.config(state='normal')
            self.txtPaidTax.delete(0, END)
            self.txtPaidTax.insert(0, str('%.2f' % paid_tax))
            self.txtPaidTax.config(state='readonly')

            self.txtSubTotal.config(state='normal')
            self.txtSubTotal.delete(0, END)
            self.txtSubTotal.insert(0, str('%.2f' % subtotal))
            self.txtSubTotal.config(state='readonly')

            self.txtTotalCost.config(state='normal')
            self.txtTotalCost.delete(0, END)
            self.txtTotalCost.insert(0, str('%.2f' % total))
            self.txtTotalCost.config(state='readonly')

        except Exception as e:
            messagebox.showerror('Error', f'Error calculating total: {e}', parent=self.root)


if __name__ == '__main__':
    root = tk.Tk()
    obj = RoomBooking(root)
    root.mainloop()

