from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox
import re
from tkinter import ttk
import tkinter as tk

def clear(): #Function which clears the entry fields after registeration is successful
    emailEntry.delete(0,END)
    first_nameEntry.delete(0,END)
    last_nameEntry.delete(0,END)
    contact_noEntry.delete(0,END)
    security_ansEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirm_passEntry.delete(0,END)
    check.set(0)
    combo_security_Q.delete(0,END)

def ValidateEmail(email_id):
    # Regular expression to validate email format
    regex = re.compile(r'[A-Za-z0-9._]+@(gmail|yahoo|outlook|aol|'
                       r'icloud|protonmail|zoho|yandex|mail|gmx|rediffmail|lycos|rizz)\.(com)$')
    return re.match(regex, email_id)

def validate_email_format(email_entry):
    email = email_entry.get().strip()  # Remove leading and trailing whitespaces
    admin_email = "ray@rizz.com"

    if not email:
        error_label.config(text='', fg='white')  # Clear error label if email is blank
    elif email.lower() == admin_email.lower():
        error_label.config(text="This email is reserved.", fg='blue', font=('Microsoft Yahei UI Light', 8, 'bold'))
        email_entry.focus()
        error_label.place(x=730, y=298)
    elif not ValidateEmail(email) or len(email) > 50:
        error_label.config(text='Invalid Email Format. Example: @domain.com', fg='blue', font=('Microsoft Yahei UI Light', 8, 'bold'))
        email_entry.focus()
        error_label.place(x=678, y=298)
    else:
        error_label.config(text='', fg='white')  # Clear error label if email is valid

def connect_database():
    if (
        emailEntry.get() == ''
        or first_nameEntry.get() == ''
        or last_nameEntry.get() == ''
        or contact_noEntry.get() == ''
        or passwordEntry.get() == ''
        or security_ansEntry.get() == ''
        or combo_security_Q.get() == ''
    ):
        messagebox.showerror('Error', 'All Fields Are Required')
    elif len(passwordEntry.get()) <= 8:
        messagebox.showerror('Error', 'Password must be greater than 8 characters')
    elif passwordEntry.get() != confirm_passEntry.get():
        messagebox.showerror('Error', 'Please make sure your passwords match')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept Terms & Conditions')
    elif not ValidateEmail(emailEntry.get()):
        messagebox.showerror('Error', 'The email address is not valid')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='0808')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return

        try:
            query = 'create database hoteldata'
            mycursor.execute(query)
            query = 'use hoteldata'
            mycursor.execute(query)
            query = 'create table employeeinfo(id int auto_increment primary key not null, email varchar(50), firstname varchar(25),' \
                    ' lastname varchar(25), contactnumber varchar(13),securityquestion varchar(50),securityanswer varchar(50), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use hoteldata')

        # trying to get the data from the database where the email is the same as the entry field
        query = 'select * from employeeinfo where email=%s'
        mycursor.execute(query, (emailEntry.get()))

        row = mycursor.fetchone()
        if row is not None:
            messagebox.showerror('Error', 'This email is already taken')
        else:
            security_question = combo_security_Q.get()
            security_answer = security_ansEntry.get()
            query = 'insert into employeeinfo(email,firstname,lastname,contactnumber,securityquestion,securityanswer,password) values(%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query, (
                emailEntry.get(), first_nameEntry.get(), last_nameEntry.get(), contact_noEntry.get(),
                combo_security_Q.get(), security_ansEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup_window.destroy()
            import signin

def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.title('Hotel Staff Signup Page')
signup_window.resizable(False, False)
background = ImageTk.PhotoImage(file="./images/bg2.png")
bgLable=Label(signup_window, image=background)
bgLable.grid()

#HEADING
heading = Label(signup_window, text="CREATE AN ACCOUNT", font=('Microsoft Yahei UI Light', 27, 'bold'),
                bg='white', fg='firebrick4', padx=10, pady=10)
heading.place(x=475, y=70)

#FIRST NAME
first_nameLabel=Label(signup_window, text='First Name:', font=('Microsoft Yahei UI Light', 13, 'bold'), bg='white', fg='firebrick1')
first_nameLabel.place(x=430,y=160)

first_nameEntry=Entry(signup_window,width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), fg='white', bg='firebrick1')
first_nameEntry.place(x=430,y=190)

#LAST NAME
last_nameEntry=Entry(signup_window,width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), fg='white', bg='firebrick1')
last_nameEntry.place(x=690,y=190)

last_nameLabel=Label(signup_window, text='Last Name:', font=('Microsoft Yahei UI Light', 13, 'bold'), bg='white', fg='firebrick1')
last_nameLabel.place(x=690,y=160)


# CONTACT NO.
contact_noLabel = Label(signup_window, text='Contact Number:', font=('Microsoft Yahei UI Light', 13, 'bold'), bg='white', fg='firebrick1')
contact_noLabel.place(x=430, y=240)

# Create the contact number entry field
contact_noEntry = Entry(signup_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), fg='white', bg='firebrick1')
contact_noEntry.place(x=430, y=270)
# Function to validate input in contact number entry
def validate_contact_number_input(P):
    allowed_characters = "0123456789+"  # Define allowed characters
    return all(char in allowed_characters for char in P) and len(P) <= 13  # Allow specified characters and limit length to 13

# Register the validation function for the entry to allow specified characters and limit length to 13
validate_contact_number_input = signup_window.register(validate_contact_number_input)
contact_noEntry.config(validate="key", validatecommand=(validate_contact_number_input, "%P"))



#EMAIL
emailLabel=Label(signup_window, text='Email:', font=('Microsoft Yahei UI Light', 13, 'bold'), bg='white', fg='firebrick1')
emailLabel.place(x=690,y=240)

emailEntry=Entry(signup_window,width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), fg='white', bg='firebrick1')
emailEntry.place(x=690,y=270)
emailEntry.bind('<FocusOut>', lambda event: validate_email_format(emailEntry))

#ERROR LABEL FOR EMAIL
error_label = Label(signup_window, text='', font=('Microsoft Yahei UI Light', 8, 'bold'), bg='white')

# SELECT SECURITY QUESTIONS
security_qLabel = tk.Label(signup_window, text='Select Security Question:', font=('Microsoft Yahei UI Light', 13, 'bold'), bg='white', fg='firebrick1')
security_qLabel.place(x=430, y=330)

combo_security_Q = ttk.Combobox(signup_window, font=('Microsoft Yahei UI Light', 11, 'bold'), state='readonly')
combo_security_Q.place(x=430, y=360, width=229)
combo_security_Q['values'] = ("", 'Your Birth Place', 'Your Favorite Book', 'Your Nick Name')
combo_security_Q.current(0)


#SECURITY ANSWER
security_ansLabel=Label(signup_window, text='Security Answer:', font=('Microsoft Yahei UI Light', 13, 'bold'), bg='white', fg='firebrick1')
security_ansLabel.place(x=690,y=330)

security_ansEntry=Entry(signup_window,width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), fg='white', bg='firebrick1')
security_ansEntry.place(x=690,y=360)

#PASSWORD
passwordLabel=Label(signup_window, text='Password:', font=('Microsoft Yahei UI Light', 13, 'bold'), bg='white', fg='firebrick1')
passwordLabel.place(x=430,y=420)

passwordEntry=Entry(signup_window,width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), fg='white', bg='firebrick1')
passwordEntry.place(x=430,y=450)

#CONFIRM PASSWORD
confirm_passLabel=Label(signup_window, text='Confirm Password:', font=('Microsoft Yahei UI Light', 13, 'bold'), bg='white', fg='firebrick1')
confirm_passLabel.place(x=690,y=420)

confirm_passEntry=Entry(signup_window,width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), fg='white', bg='firebrick1')
confirm_passEntry.place(x=690,y=450)

#CHECK BUTTON
check=IntVar()
terms_conditions=Checkbutton(signup_window, text='I agree to the Terms & Conditions', font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white'
                             , fg='firebrick1', activebackground='white', activeforeground='firebrick1', cursor='hand2', variable=check)
terms_conditions.place(x=545,y=490)


#SIGN UP BUTTON
signupButton=Button(signup_window, text='Signup', font=('Open Sans', 16, 'bold'), bd=0, bg='firebrick1', fg='white'
                    , activebackground='firebrick1', activeforeground='white', cursor='hand2', width=17, command=connect_database)
signupButton.place(x=565,y=525)

#ALREADY HAVE AN ACCOUNT TEXT
alreadyaccount=Label(signup_window, text='Already have an account?', font=('Open Sans', 9, 'bold'), bg='white', fg='firebrick4')
alreadyaccount.place(x=700,y=604)


#BACK TO LOGIN IN PAGE- LOGIN BUTTON
loginButton=Button(signup_window, text='Log in', font=('Open Sans', 9, 'bold underline')
                   ,bg='white', fg='blue', bd=0, cursor='hand2', activebackground='white'
                   ,activeforeground='blue',command=login_page)
loginButton.place(x=852, y=603)


# Function to switch focus between entries using Enter key
def switch_focus(event):
    if signup_window.focus_get() == first_nameEntry:
        last_nameEntry.focus_set()
    elif signup_window.focus_get() == last_nameEntry:
        contact_noEntry.focus_set()
    elif signup_window.focus_get() == contact_noEntry:
        emailEntry.focus_set()
    elif signup_window.focus_get() == emailEntry:
        combo_security_Q.focus_set()
    elif signup_window.focus_get() == combo_security_Q:
        security_ansEntry.focus_set()
    elif signup_window.focus_get() == security_ansEntry:
        passwordEntry.focus_set()
    elif signup_window.focus_get() == passwordEntry:
        confirm_passEntry.focus_set()
    elif signup_window.focus_get() == confirm_passEntry:
        connect_database()  # Trigger the registration function when Enter is pressed in the confirm password entry

# Bind the Enter key to switch focus between entries
first_nameEntry.bind('<Return>', switch_focus)
last_nameEntry.bind('<Return>', switch_focus)
contact_noEntry.bind('<Return>', switch_focus)
emailEntry.bind('<Return>', switch_focus)
combo_security_Q.bind('<Return>', switch_focus)
security_ansEntry.bind('<Return>', switch_focus)
passwordEntry.bind('<Return>', switch_focus)
confirm_passEntry.bind('<Return>', switch_focus)


signup_window.mainloop()
