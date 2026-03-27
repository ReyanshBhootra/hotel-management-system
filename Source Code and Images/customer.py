from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import pymysql.connections
import random
from tkinter import messagebox


class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Window")
        self.root.geometry("1200x565+327+218")
        # Disable maximizing the window
        self.root.resizable(False, False)


        #---------------------varibles-----------------------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_citizenship=StringVar()
        self.var_address=StringVar()
        self.var_idProof=StringVar()
        self.var_idNumber=StringVar()


        # ---------------title------------------
        lbl_title = Label(self.root, text=('ADD CUSTOMER DETAILS'), font=('Georgia', 18, 'bold'), bg='black',
                          fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1200, height=50)

        # ----------------logo-----------------
        img2 = Image.open(r".\images\hotelLogo.png")
        img2 = img2.resize((100, 41))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root, image=self.photoimg2, bd=2, background='gold', relief=RIDGE)
        lbling.place(x=5, y=6, width=100, height=41)

        #------------------labelFrame---------------------
        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',padx=2, font=('Georgia', 14, 'bold'), fg='firebrick4')
        labelFrameLeft.place(x=5,y=50,width=430,height=512)

        #------------------------------------Labels and entrys--------------
        #custREF
        lbl_cust_ref=Label(labelFrameLeft, text='Customer Ref', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0,sticky=W)

        entry_ref=ttk.Entry(labelFrameLeft,textvariable=self.var_ref,state='readonly',width=27,font=('Georgia', 12, 'bold'))
        entry_ref.grid(row=0, column=1)

        #FIRST NAME
        fname=Label(labelFrameLeft, text='First Name:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        fname.grid(row=1, column=0,sticky=W)

        self.txtfname=ttk.Entry(labelFrameLeft,textvariable=self.var_fname,width=27,font=('Georgia', 12, 'bold'))
        self.txtfname.grid(row=1, column=1)
        self.txtfname.focus()
        self.txtfname.bind('<Return>', self.switch_focus)  # Bind Enter key event

        #LAST NAME
        lbllname=Label(labelFrameLeft, text='Last Name:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lbllname.grid(row=2, column=0,sticky=W)

        txtlname=ttk.Entry(labelFrameLeft,textvariable=self.var_lname,width=27,font=('Georgia', 12, 'bold'))
        txtlname.grid(row=2, column=1)
        txtlname.bind('<Return>', self.switch_focus)  # Bind Enter key event


        #GENDER COMBOBOX
        label_gender=Label(labelFrameLeft, text='Gender:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        label_gender.grid(row=3, column=0,sticky=W)

        combo_gender=ttk.Combobox(labelFrameLeft,textvariable=self.var_gender, font=('Georgia', 12, 'bold'),width=25, state='readonly')
        combo_gender['values']=("Male", "Female", "Other")
        combo_gender.grid(row=3, column=1)
        combo_gender.bind('<Return>', self.switch_focus)  # Bind Enter key event


        #POST CODE
        lblPostCode=Label(labelFrameLeft, text='PostCode:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0,sticky=W)

        txtPostCode=ttk.Entry(labelFrameLeft,width=27,textvariable=self.var_post,font=('Georgia', 12, 'bold'))
        txtPostCode.grid(row=4, column=1)
        txtPostCode.bind('<Return>', self.switch_focus)  # Bind Enter key event

        #MOBILE NUMBER
        lblMobile=Label(labelFrameLeft, text='Mobile:',font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lblMobile.grid(row=5, column=0,sticky=W)

        def validate_Mobileinput(char):
            # Check if the input is a digit or the plus sign
            return char.isdigit() or char == '+' or char==''

        def validate_IdProofinput(char1):
            # Check if the input is a digit or the plus sign
            return char1.isdigit() or char1==''

        txtMobile = ttk.Entry(labelFrameLeft, width=27, textvariable=self.var_mobile, font=('Georgia', 12, 'bold'))
        txtMobile.grid(row=5, column=1)
        txtMobile['validate'] = 'key'
        txtMobile['validatecommand'] = (txtMobile.register(validate_Mobileinput), '%S')
        txtMobile.bind('<Return>', self.switch_focus)  # Bind Enter key event

        #email
        lblEmail=Label(labelFrameLeft, text='Email:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lblEmail.grid(row=6, column=0,sticky=W)

        txtEmail=ttk.Entry(labelFrameLeft,width=27,textvariable=self.var_email,font=('Georgia', 12, 'bold'))
        txtEmail.grid(row=6, column=1)
        txtEmail.bind('<Return>', self.switch_focus)  # Bind Enter key event

        ###############################################################################################################################################################

        # List of citizenships
        self.citizenships = [
            "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
            "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus",
            "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil",
            "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
            "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the",
            "Congo, Republic of the", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic",
            "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
            "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia",
            "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
            "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan",
            "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan",
            "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
            "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
            "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
            "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria",
            "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay",
            "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
            "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
            "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
            "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
            "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
            "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
            "United States Of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia",
            "Zimbabwe"
        ]

        lblCitizenship = tk.Label(labelFrameLeft, text='Citizenship:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lblCitizenship.grid(row=7, column=0, sticky='w')

        self.var_citizenship = tk.StringVar()
        self.combo_Citizenship = ttk.Combobox(labelFrameLeft,width=25,font=('Georgia', 12, 'bold'), textvariable=self.var_citizenship)
        self.combo_Citizenship['values'] = self.citizenships
        self.combo_Citizenship.grid(row=7, column=1)
        self.combo_Citizenship.bind('<Return>', self.switch_focus)  # Bind Enter key event

        def on_key_release(event):
            query = self.var_citizenship.get().lower()
            filtered_citizenships = [nat for nat in self.citizenships if nat.lower().startswith(query)]
            self.combo_Citizenship['values'] = filtered_citizenships
        self.combo_Citizenship.bind('<KeyRelease>', on_key_release)



        ###############################################################################################################################################################

        #id Proof
        lblIdProof=Label(labelFrameLeft, text='Id Proof Type:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0,sticky=W)

        combo_id=ttk.Combobox(labelFrameLeft, textvariable=self.var_idProof,font=('Georgia', 12, 'bold'),width=25, state='readonly')
        combo_id['values']=("Driving Licence", "Passport")
        combo_id.grid(row=8, column=1)
        combo_id.bind('<Return>', self.switch_focus)  # Bind Enter key event

        #id number
        lblIdNumber=Label(labelFrameLeft, text='Id Number:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0,sticky=W)

        txtIdNumber = ttk.Entry(labelFrameLeft, width=27, textvariable=self.var_idNumber, font=('Georgia', 12, 'bold'))
        txtIdNumber.grid(row=9, column=1)
        txtIdNumber['validate'] = 'key'
        txtIdNumber['validatecommand'] = (txtIdNumber.register(validate_IdProofinput), '%S')
        txtIdNumber.bind('<Return>', self.switch_focus)  # Bind Enter key event

        #address
        lblAddress=Label(labelFrameLeft, text='Address:', font=('Georgia', 12, 'bold'), padx=2, pady=6)
        lblAddress.grid(row=10, column=0,sticky=W)

        txtAddress=ttk.Entry(labelFrameLeft,width=27,textvariable=self.var_address,font=('Georgia', 12, 'bold'))
        txtAddress.grid(row=10, column=1)

        #-----------------------------------buttons--------------------------
        btn_frame = Frame(labelFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text='Add', command=self.add_data, font=('Georgia', 12, 'bold'),
                        bg='black', fg='gold', width=8, activeforeground='gold', activebackground='black')
        btnAdd.grid(row=0, column=0, padx=2)

        btnUpdate=Button(btn_frame, text='Update', command=self.update,font=('Georgia', 12, 'bold'),
                         bg='black', fg='gold', width=8,activeforeground='gold', activebackground='black')
        btnUpdate.grid(row=0, column=1,padx=2)

        btnDelete=Button(btn_frame, text='Delete',command=self.delete, font=('Georgia', 12, 'bold'),
                         bg='black', fg='gold', width=8,activeforeground='gold', activebackground='black')
        btnDelete.grid(row=0, column=2,padx=2)

        btnReset=Button(btn_frame, text='Reset', command=self.reset,font=('Georgia', 12, 'bold'),
                        bg='black', fg='gold', width=8,activeforeground='gold', activebackground='black')
        btnReset.grid(row=0, column=3,padx=2)

        #================================table frame search==========================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details And Search System',padx=2, font=('Georgia', 14, 'bold'), fg='firebrick4')
        Table_Frame.place(x=435,y=50,width=865,height=512)

        lblSearchBy=Label(Table_Frame, text='Search By:', font=('Georgia', 12, 'bold'),bg='red', fg='white')
        lblSearchBy.grid(row=0, column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_SearchBy=ttk.Combobox(Table_Frame, textvariable=self.search_var,font=('Georgia', 12, 'bold'),width=20, state='readonly')
        combo_SearchBy['values']=("Ref", "Email")
        combo_SearchBy.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()
        txtSearchBy=ttk.Entry(Table_Frame,width=21,textvariable=self.txt_search,font=('Georgia', 12, 'bold'))
        txtSearchBy.grid(row=0, column=2,padx=2)

        btnSearch=Button(Table_Frame, text='Search',command=self.search, font=('Georgia', 12, 'bold'), bg='black',
                         fg='gold', width=7,activeforeground='gold', activebackground='black')
        btnSearch.grid(row=0, column=3,padx=4)

        btnShowAll=Button(Table_Frame, text='Show All',command=self.fetch_data,font=('Georgia', 12, 'bold'),
                          bg='black', fg='gold', width=7,activeforeground='gold', activebackground='black')
        btnShowAll.grid(row=0, column=4,padx=2)

        #=================================show data=========================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=763, height=380)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, columns=("ref", "fname", "lname", "gender", "post",
                                                                       "mobile", "email", "citizenship", "idproof",
                                                                       "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        # Define column names and their corresponding text labels in a dictionary
        column_headings = {
            'ref': 'Refer Number',
            'fname': 'First Name',
            'lname': 'Last Name',
            'gender': 'Gender',
            'post': 'PostCode',
            'mobile': 'Mobile',
            'email': 'Email',
            'citizenship': 'Citizenship',
            'idproof': 'Id Proof',
            'idnumber': 'Id Number',
            'address': 'Address'
        }

        # Set column headings using a loop
        for column, heading in column_headings.items():
            self.Cust_Details_Table.heading(column, text=heading)

        self.Cust_Details_Table['show']='headings'

        # Define the columns and their respective widths in a dictionary
        columns = {
            'ref': 100,
            'fname': 100,
            'lname': 100,
            'gender': 100,
            'post': 100,
            'mobile': 100,
            'email': 100,
            'citizenship': 100,
            'idproof': 100,
            'idnumber': 100,
            'address': 100
        }
        # Set column widths using a loop
        for column, width in columns.items():
            self.Cust_Details_Table.column(column, width=width)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()

    def add_data(self):
        try:
            if self.var_ref.get() == '' or self.var_fname.get() == '' or self.var_lname.get() == '' or self.var_gender.get() == '' \
                    or self.var_post.get() == '' or self.var_mobile.get() == '' or self.var_email.get() == '' or self.var_citizenship.get() == '' \
                    or self.var_idProof.get() == '' or self.var_idNumber.get() == '' or self.var_address.get() == '':
                messagebox.showerror('Error', 'All fields are required', parent=self.root)
            else:
                con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
                my_cursor = con.cursor()

                # Check for duplicate email
                my_cursor.execute('SELECT * FROM customerinfo WHERE Email=%s', (self.var_email.get(),))
                duplicate_email = my_cursor.fetchone()
                if duplicate_email:
                    messagebox.showerror('Error', 'This email already exists in the database', parent=self.root)
                    con.close()
                    return

                # Check for duplicate ID number
                my_cursor.execute('SELECT * FROM customerinfo WHERE IdNumber=%s', (self.var_idNumber.get(),))
                duplicate_id = my_cursor.fetchone()
                if duplicate_id:
                    messagebox.showerror('Error', 'This ID number already exists in the database', parent=self.root)
                    con.close()
                    return

                # If no duplicate found, proceed with adding data
                my_cursor.execute('INSERT INTO customerinfo VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                  (self.var_ref.get(), self.var_fname.get(), self.var_lname.get(), self.var_gender.get(),
                                   self.var_post.get(), self.var_mobile.get(), self.var_email.get(),
                                   self.var_citizenship.get(), self.var_idProof.get(), self.var_idNumber.get(),
                                   self.var_address.get()))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success", "Customer details added successfully!", parent=self.root)
                self.reset()  # Reset the entry fields after adding the customer
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)

    def fetch_data(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
            my_cursor = con.cursor()
            my_cursor.execute('select * from customerinfo')
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert('',END, values=i)
                con.commit()
            con.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)

    def get_cursor(self, event=''):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row_values = content.get('values', [])  # Get values from the dictionary, default to an empty list if not present

        # Check if row_values is not empty before updating the reference number
        if row_values:
            self.var_ref.set(row_values[0])
            self.var_fname.set(row_values[1])
            self.var_lname.set(row_values[2])
            self.var_gender.set(row_values[3])
            self.var_post.set(row_values[4])
            self.var_mobile.set(row_values[5])
            self.var_email.set(row_values[6])
            self.var_citizenship.set(row_values[7])
            self.var_idProof.set(row_values[8])
            self.var_idNumber.set(row_values[9])
            self.var_address.set(row_values[10])

    def update(self):
        try:
            if self.var_ref.get() == '' or self.var_fname.get() == '' or self.var_lname.get() == '' or self.var_gender.get() == '' \
                    or self.var_post.get() == '' or self.var_mobile.get() == '' or self.var_email.get() == '' or self.var_citizenship.get() == '' \
                    or self.var_idProof.get() == '' or self.var_idNumber.get() == '' or self.var_address.get() == '':
                messagebox.showerror('Error', 'All fields are required', parent=self.root)
            else:
                con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
                my_cursor = con.cursor()

                # Check for duplicate email
                my_cursor.execute('SELECT * FROM customerinfo WHERE Email=%s AND Ref!=%s', (self.var_email.get(), self.var_ref.get()))
                duplicate_email = my_cursor.fetchone()
                if duplicate_email:
                    messagebox.showerror('Error', 'This email already exists in the database', parent=self.root)
                    con.close()
                    return

                # Check for duplicate ID number
                my_cursor.execute('SELECT * FROM customerinfo WHERE IdNumber=%s AND Ref!=%s', (self.var_idNumber.get(), self.var_ref.get()))
                duplicate_id = my_cursor.fetchone()
                if duplicate_id:
                    messagebox.showerror('Error', 'This ID number already exists in the database', parent=self.root)
                    con.close()
                    return

                # If no duplicate found, proceed with updating data
                my_cursor.execute('UPDATE customerinfo SET FirstName=%s, LastName=%s, Gender=%s, PostCode=%s,'
                                  ' `Mobile Number`=%s, Email=%s, Citizenship=%s, IdProof=%s, IdNumber=%s, Address=%s WHERE Ref=%s', (
                    self.var_fname.get(), self.var_lname.get(), self.var_gender.get(),
                    self.var_post.get(), self.var_mobile.get(), self.var_email.get(),
                    self.var_citizenship.get(), self.var_idProof.get(), self.var_idNumber.get(),
                    self.var_address.get(), self.var_ref.get()))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('Update', 'Customer details have been updated successfully', parent=self.root)
                self.reset()
                self.txtfname.focus()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)

    def delete(self):
        try:
            if self.var_ref.get() == '':
                messagebox.showerror('Error', 'Please enter Ref to delete', parent=self.root)
            else:
                con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
                my_cursor = con.cursor()
                # Check if the data with the given Ref exists in the database
                my_cursor.execute('SELECT * FROM customerinfo WHERE Ref=%s', (self.var_ref.get(),))
                existing_data = my_cursor.fetchone()
                if existing_data:
                    # Data exists, proceed with the deletion
                    delete = messagebox.askyesno('Hotel Management System', 'Do you want to delete this customer?', parent=self.root)
                    if delete:
                        query = "DELETE FROM customerinfo WHERE Ref=%s"
                        value = (self.var_ref.get(),)
                        my_cursor.execute(query, value)
                        con.commit()
                        # Check if there is only one record left in the customerinfo table
                        my_cursor.execute("SELECT COUNT(*) FROM customerinfo")
                        count = my_cursor.fetchone()[0]
                        con.close()
                        # If there is no record left, clear the details_table
                        if count == 0:
                            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                        else:
                            self.fetch_data()  # Fetch updated data after deletion
                        messagebox.showinfo('Success', 'Customer details have been deleted successfully', parent=self.root)
                        self.reset()  # Reset the entry fields after successful deletion
                    else:
                        messagebox.showinfo('Info', 'Deletion Cancelled', parent=self.root)
                else:
                    # Data does not exist, show an error message
                    messagebox.showerror('Error', 'Data with the given Ref does not exist in the database', parent=self.root)
        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}', parent=self.root)

    def reset(self):
        # Reset all entry fields
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_citizenship.set("")
        self.var_idProof.set("")
        self.var_idNumber.set("")
        self.var_address.set("")

        # Generate a new random reference number
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        # Deselect all items in the details_table
        self.Cust_Details_Table.selection_remove(self.Cust_Details_Table.selection())


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

                if search_attribute in ['Email', 'Ref']:
                    # Check if the entered value is an exact match
                    query = "SELECT * FROM customerinfo WHERE email IN (SELECT email FROM customerinfo WHERE `{}` = %s)".format(search_attribute)
                    search_term = self.txt_search.get()  # Assuming the value is entered without wildcards
                else:
                    query = "SELECT * FROM customerinfo WHERE `{}` LIKE %s".format(search_attribute)
                    my_cursor.execute(query, (search_term,))

                my_cursor.execute(query, (search_term,))

                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                    for i in rows:
                        self.Cust_Details_Table.insert('', END, values=i)
                    con.commit()
                    # Clear the data inside the search entry only if records were found
                    self.txt_search.set("")  # Move this line inside the if block
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

    #to move between entries using the enter key
    def switch_focus(self, event):
        focus_next = self.root.focus_get().tk_focusNext()
        if focus_next:
            focus_next.focus_set()





if __name__ == '__main__':
    root = tk.Tk()
    obj = Cust_win(root)
    root.mainloop()
