from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import pymysql.connections
from tkinter import messagebox

class RoomDetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Details")
        self.root.geometry("1200x565+327+218")
        # Disable maximizing the window
        self.root.resizable(False, False)

        lbl_title = Label(self.root, text=('ROOM DETAILS'), font=('Georgia', 18, 'bold'), bg='black',
                          fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1200, height=50)

        # ----------------logo-----------------
        img1 = Image.open(r".\images\hotelLogo.png")
        img1 = img1.resize((100, 41))
        self.photoimg2 = ImageTk.PhotoImage(img1)

        lbling = Label(self.root, image=self.photoimg2, bd=2, background='gold', relief=RIDGE)
        lbling.place(x=5, y=6, width=100, height=41)

        # ------------------labelFrame---------------------
        labelFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text='Add New Room', padx=2,
                                    font=('Georgia', 14, 'bold'), fg='firebrick4')
        labelFrameLeft.place(x=10, y=50, width=560, height=170)

        # floor entry
        lbl_floor = Label(labelFrameLeft, text='Floor:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor= StringVar()
        self.entry_floor = ttk.Entry(labelFrameLeft, textvariable=self.var_floor,width=21, font=('Georgia', 12, 'bold'))
        self.entry_floor.grid(row=0, column=1, sticky=W)
        self.entry_floor.focus()
        self.entry_floor.bind('<Return>', self.switch_focus)  # Bind Enter key event


        # room no entry
        lbl_RoomNo = Label(labelFrameLeft, text='Room Number:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        self.var_room_no= StringVar()
        entry_RoomNo = ttk.Entry(labelFrameLeft,textvariable=self.var_room_no, width=21, font=('Georgia', 12, 'bold'))
        entry_RoomNo.grid(row=1, column=1, sticky=W)
        entry_RoomNo.bind('<Return>', self.switch_focus)  # Bind Enter key event

        # ROOM TYPE
        label_RoomType = Label(labelFrameLeft, text='Room Type:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        label_RoomType.grid(row=2, column=0, sticky=W)

        self.var_roomtype= StringVar()
        self.combo_RoomType = ttk.Combobox(labelFrameLeft,textvariable=self.var_roomtype,font=('Georgia', 12, 'bold'), width=19, state='readonly')
        self.combo_RoomType['values'] = ("Single", "Double", "Suite", "Deluxe Suite")
        self.combo_RoomType.grid(row=2, column=1, sticky=W)
        self.combo_RoomType.bind('<Return>', self.open_combo_dropdown)

        # -----------------------------------buttons--------------------------
        btn_frame = Frame(labelFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=370, y=0, width=173, height=134)

        btnAdd = Button(btn_frame, text='Add', command=self.add_data, font=('Georgia', 12, 'bold'), bg='black',
                        fg='gold', width=14, activeforeground='gold', activebackground='black')
        btnAdd.grid(row=0, column=0, padx=3)

        btnUpdate = Button(btn_frame, text='Update',command=self.update,  font=('Georgia', 12, 'bold'), bg='black',
                           fg='gold', width=14, activeforeground='gold', activebackground='black')
        btnUpdate.grid(row=1, column=0, padx=2)

        btnDelete = Button(btn_frame, text='Delete', command=self.delete, font=('Georgia', 12, 'bold'), bg='black',
                           fg='gold', width=14, activeforeground='gold', activebackground='black')
        btnDelete.grid(row=2, column=0, padx=2)

        btnReset = Button(btn_frame, text='Reset',command=self.reset,  font=('Georgia', 12, 'bold'), bg='black',
                          fg='gold', width=14, activeforeground='gold', activebackground='black')
        btnReset.grid(row=3, column=0, padx=3)

        # ================================table frame search==========================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text='Show Room Details', padx=2,
                                 font=('Georgia', 14, 'bold'), fg='firebrick4')
        Table_Frame.place(x=580, y=50, width=610, height=500)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_Frame, columns=("floor", "room_no", "room_type",),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # Define column names and their corresponding text labels in a dictionary
        column_headings = {
            'floor': 'Floor',
            'room_no': 'Room Number',
            'room_type': 'Room Type'
        }

        # Set column headings using a loop
        for column, heading in column_headings.items():
            self.room_table.heading(column, text=heading)

        self.room_table['show'] = 'headings'

        # Define the columns and their respective widths in a dictionary
        columns = {
            'floor': 100,
            'room_no': 100,
            'room_type': 100
        }

        # Set column headings using a loop
        for column, heading in column_headings.items():
            self.room_table.heading(column, text=heading)

        # Set column widths using a loop
        for column, width in columns.items():
            self.room_table.column(column, width=width, anchor=CENTER)

        # Configure the style for heading
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Comfortaa', 13, 'bold', 'underline'))

        # Configure the style for the data
        style.configure("Treeview", font=('Georgia', 11))  # Change the font size and family here

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()

        # Create the 'roominfo' table if it doesn't exist
        self.create_roomdetails_table()

    # Database connection method
    def connect_to_database(self):
        return pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')

    # Create the roomdetails table if it doesn't exist in the database
    def create_roomdetails_table(self):
        try:
            con = self.connect_to_database()
            my_cursor = con.cursor()

            # Define the 'roomdetails' table schema
            table_schema = '''
                CREATE TABLE IF NOT EXISTS roomdetails (
                    floor VARCHAR(255),
                    room_no INT PRIMARY KEY,
                    room_type VARCHAR(20)
                )
            '''
            my_cursor.execute(table_schema)
            con.commit()

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Database Error: {e}", parent=self.root)

    # Add data method
    def add_data(self):
        try:
            if not all([self.var_roomtype.get(), self.var_room_no.get().isdigit(), self.var_floor.get().isdigit()]):
                messagebox.showerror('Error', 'Invalid input. Please check your entries.', parent=self.root)
            else:
                # If everything looks good, we can proceed to add the room
                con = self.connect_to_database()
                my_cursor = con.cursor()

                # Check if the room number already exists
                check_query = "SELECT * FROM roomdetails WHERE room_no = %s"
                check_value = (self.var_room_no.get(),)
                my_cursor.execute(check_query, check_value)
                existing_record = my_cursor.fetchone()

                if existing_record:
                    messagebox.showerror('Error', 'Room number already exists. Please choose a different room number.', parent=self.root)
                else:
                    # If the room number is unique, we can proceed
                    # Insert new room details
                    my_cursor.execute('''
                        INSERT INTO roomdetails VALUES (%s, %s, %s)
                    ''', (
                        self.var_floor.get(),
                        self.var_room_no.get(),
                        self.var_roomtype.get()
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Room Added", parent=self.root)
                    self.fetch_data()
                    self.reset()
                    self.entry_floor.focus()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)

    # Fetch data method with context manager
    def fetch_data(self):
        try:
            with self.connect_to_database() as con:
                my_cursor = con.cursor()
                my_cursor.execute('select * from roomdetails')
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.room_table.delete(*self.room_table.get_children())
                    for i in rows:
                        self.room_table.insert('', END, values=i)
                my_cursor.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Database Error: {e}", parent=self.root)

    def get_cursor(self, event=''):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content.get('values', ())  # Use get method to handle None

        if row:
            self.var_floor.set(row[0])
            self.var_room_no.set(row[1])
            self.var_roomtype.set(row[2])
        else:
            # Handle the case where 'row' is empty or None
            # You may want to reset the variables or take appropriate action
            self.var_floor.set("")
            self.var_room_no.set("")
            self.var_roomtype.set("")


    # Update data method
    def update(self):
        try:
            if not all([self.var_roomtype.get(), self.var_room_no.get().isdigit(), self.var_floor.get().isdigit()]):
                messagebox.showerror('Error', 'Invalid input. Please check your entries.', parent=self.root)
            else:
                con = self.connect_to_database()
                my_cursor = con.cursor()

                # Check if the room number exists
                check_query = "SELECT * FROM roomdetails WHERE room_no = %s"
                check_value = (self.var_room_no.get(),)
                my_cursor.execute(check_query, check_value)
                existing_record = my_cursor.fetchone()

                if existing_record:
                    # Delete the existing record
                    delete_query = "DELETE FROM roomdetails WHERE room_no = %s"
                    delete_value = (self.var_room_no.get(),)
                    my_cursor.execute(delete_query, delete_value)

                    # Insert a new record with the updated room_no
                    insert_query = "INSERT INTO roomdetails VALUES (%s, %s, %s)"
                    insert_value = (self.var_floor.get(), self.var_room_no.get(), self.var_roomtype.get())
                    my_cursor.execute(insert_query, insert_value)

                    con.commit()
                    self.fetch_data()
                    con.close()
                    messagebox.showinfo('Update', 'Room has been updated successfully', parent=self.root)
                    self.reset()
                    self.entry_floor.focus()
                else:
                    messagebox.showerror('Error', 'Room does not exist in the database. Cannot update.', parent=self.root)
                    self.entry_floor.focus()

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)

    # the reset all the fields
    def reset(self):
        self.var_roomtype.set("")
        self.var_room_no.set("")
        self.var_floor.set("")

        # Deselect all items in the details_table
        self.room_table.selection_remove(self.room_table.selection())

    # delete data
    def delete(self):
        try:
            # Input validation to ensure all required fields are filled correctly
            if not all([self.var_room_no.get().isdigit()]):
                messagebox.showerror('Error', 'Invalid input. Please check your entries.', parent=self.root)
            else:
                # Proceeding with room deletion
                delete = messagebox.askyesno('Confirm Deletion', 'Are you sure you want to delete this room?',
                                             parent=self.root)
                if delete:
                    con = self.connect_to_database()
                    my_cursor = con.cursor()
                    query = "delete from roomdetails where room_no=%s"
                    value = (self.var_room_no.get(),)
                    my_cursor.execute(query, value)
                    con.commit()

                    # Check if there is only one record left in the customerinfo table
                    my_cursor.execute("SELECT COUNT(*) FROM roomdetails")
                    count = my_cursor.fetchone()[0]
                    con.close()

                    # If there is no record left, clear the details_table
                    if count == 0:
                        self.room_table.delete(*self.room_table.get_children())
                    else:
                        self.fetch_data()  # Fetch updated data after deletion

                    messagebox.showinfo('Success', 'Room Deleted', parent=self.root)
                    self.reset()  # Reset the entry fields after successful deletion
                    self.entry_floor.focus()
                else:
                    messagebox.showinfo('Info', 'Deletion Cancelled', parent=self.root)
        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}', parent=self.root)

    #to move between entries using the enter key
    def switch_focus(self, event):
        focus_next = self.root.focus_get().tk_focusNext()
        if focus_next:
            focus_next.focus_set()

    #to opne the entry box using the enter key
    def open_combo_dropdown(self, event):
        self.combo_RoomType.focus()
        self.combo_RoomType.event_generate('<Down>')


if __name__ == '__main__':
    root = tk.Tk()
    obj = RoomDetails(root)
    root.mainloop()
