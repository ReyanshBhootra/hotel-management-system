from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import re
from hotelmanage import HotelManagementSystem

#for staff to login in
def login_user():
    if staffemailEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='0808')
            mycursor=con.cursor()
            query='use hoteldata'
            mycursor.execute(query)
            query='select * from employeeinfo where email=%s and password=%s'
            mycursor.execute(query,(staffemailEntry.get(),passwordEntry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid email or password')
            else:
                #destroy signin and open hotelmanage
                login_window.destroy()
                root = Tk()
                obj = HotelManagementSystem(root)
                root.mainloop()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return


#destory sign in and open signup
def signup_page():
    login_window.destroy()
    import signup

# Function to display a message box when the image is clicked
def show_message():
    messagebox.showinfo("Work in Progress", "This feature is under development.")

# Function to hide the password and change the eye button to show
def hide():
    # Change the eye icon to open eye and configure the password entry to show characters
    eyeButton.config(image=openEyeImage)
    passwordEntry.config(show='')
    # Change the eye button command to show when clicked
    eyeButton.config(command=show)

# Function to show the password and change the eye button to hide
def show():
    # Change the eye icon to closed eye and configure the password entry to hide characters
    eyeButton.config(image=closeEyeImage)
    passwordEntry.config(show='*')
    # Change the eye button command to hide when clicked
    eyeButton.config(command=hide)

# Function to handle Email entry focus event
def user_enter(event):
    if staffemailEntry.get() == 'Email':
        staffemailEntry.delete(0, END)

# Function to handle password entry focus event
def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)
        passwordEntry.config(show='*')

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def ValidateEmail(email_id):
    regex = re.compile(r'[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.match(regex, email_id)

def forget_pass():
    def validate_email():
        email = email_entry.get()
        con = pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
        mycursor = con.cursor()
        query = 'SELECT securityquestion FROM employeeinfo WHERE email=%s'
        mycursor.execute(query, (email,))
        security_question = mycursor.fetchone()

        if security_question:
            validationQuestion_label.config(text=security_question[0], font=('arial', 11, 'bold'), fg='purple4')
            validationQuestion_label.place(x=478, y=188)  # Set the position of the security question label
            validationEmail_label.config(text='', fg='white')  # Clear the validation message
        else:
            validationEmail_label.config(text='Email is not valid', fg='red')
            validationEmail_label.place(x=480, y=140)  # Set the position of the validation message label
            validationQuestion_label.config(text='', fg='white')  # Clear the security question
        con.close()

    def switch_focus(event):
        if window.focus_get() == email_entry:
            security_ansEntry.focus_set()
        elif window.focus_get() == security_ansEntry:
            newpass_entry.focus_set()
        elif window.focus_get() == newpass_entry:
            confirmpass_entry.focus_set()
        elif window.focus_get() == confirmpass_entry:
            change_password()  # Trigger the change password function when Enter is pressed in the confirm password entry

    def change_password():
        if email_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error','Password Mismatch',parent=window)
        else:
            con=pymysql.connect(host='localhost', user='root', password='0808', database='hoteldata')
            mycursor=con.cursor()
            query = 'select * from employeeinfo where email=%s and securityanswer=%s'
            mycursor.execute(query,(email_entry.get(), security_ansEntry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error',"Email and Security Answer doesn't match", parent=window)
            else:
                query='update employeeinfo set password=%s where email=%s'
                mycursor.execute(query,(newpass_entry.get(), email_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, please login with new password', parent=window)
                window.destroy()


    window = Toplevel()
    window.resizable(0,0)
    window.title('Change Password')
    bg3Image = ImageTk.PhotoImage(file='./images/bg3.png')
    bglabel=Label(window, image=bg3Image)
    bglabel.image = bg3Image  # This line is necessary to prevent the image from being garbage collected
    bglabel.grid()

    #HEADING FOR THE FORGET PASSWORD WINDOW
    heading_label = Label(window, text="RESET PASSWORD", font=('arial', 18, 'bold'),
                bg='white', fg='purple3')
    heading_label.place(x=490, y=48)

#/////////////////////////////////////////////////////////////////////////

    # VALIDATION LABEL FOR EMAIL
    validationEmail_label = Label(window, text='', font=('arial', 10, 'bold'), bg='white')
    validationEmail_label.place(x=480, y=140)

    #VALIDATION LABEL FOR SECURITY Q
    validationQuestion_label=Label(window, text='', font=('arial', 11, 'bold'), bg='white')
    validationQuestion_label.place(x=480, y=190)

#/////////////////////////////////////////////////////////////////////////

    #EMAIL FOR FORGET_PASS WINDOW
    emailLabel = Label(window, text="Email:", font=('arial', 13, 'bold'), bg='white', fg='orchid3')
    emailLabel.place(x=480, y=90)

    # EMAIL ENTRY FIELD
    email_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='purple3')
    email_entry.place(x=480, y=120)
    email_entry.bind('<FocusOut>', lambda event: validate_email())  # Check email validity on focus out
    Frame(window, width=250, height=2, bg='orchid3').place(x=480, y=140)

    # SECURITY QUESTIN FOR FORGET_PASS WINDOW
    securityQuestion=Label(window, text="Security Question:", font=('arial', 13, 'bold'), bg='white', fg='orchid3')
    securityQuestion.place(x=478, y=160)
    Frame(window, width=250, height=2, bg='orchid3').place(x=480, y=210)

    #SECURITY ANS FOR FORGET_PASS WINDOW
    security_ansLabel= Label(window, text="Security Answer:", font=('arial', 13, 'bold'), bg='white', fg='orchid3')
    security_ansLabel.place(x=478,y=222)

    #SECURITY ANS FIELD
    security_ansEntry= Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='purple3')
    security_ansEntry.place(x=480, y=250)
    Frame(window, width=250, height=2, bg='orchid3').place(x=480,y=270)

    #PASSWORD FOR FORGET_PASS WINDOW
    passwordLabel = Label(window, text="New Password:", font=('arial', 13, 'bold'), bg='white', fg='orchid3')
    passwordLabel.place(x=480, y=285)

    #NEW PASSWORD ENTRY FIELD
    newpass_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='purple3')
    newpass_entry.place(x=480, y=314)
    Frame(window, width=250, height=2, bg='orchid3').place(x=480,y=334)

    #CONFIRM PASS FOR FORGET_PASS WINDOW
    confirmpassLabel = Label(window, text="Confirm Password:", font=('arial', 13, 'bold'), bg='white', fg='orchid3')
    confirmpassLabel.place(x=480, y=352)

    #CONFIRM PASS ENTRY FIELD
    confirmpass_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='purple3')
    confirmpass_entry.place(x=480, y=379)
    Frame(window, width=250, height=2, bg='orchid3').place(x=480,y=399)

    submitButton =Button(window, text='Submit', bd=0,bg='purple3', fg='white',font=('Open Sans','16','bold'),
                         width=19,cursor='hand2',activebackground='purple3', activeforeground='white', command=change_password)
    submitButton.place(x=480,y=418)

    # Bind the Enter key to switch focus between entries
    email_entry.bind('<Return>', switch_focus)
    security_ansEntry.bind('<Return>', switch_focus)
    newpass_entry.bind('<Return>', switch_focus)
    confirmpass_entry.bind('<Return>', switch_focus)

    window.mainloop()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# GUI Part
login_window = Tk()
login_window.geometry("992x664+50+50")
login_window.resizable(0, 0)
login_window.title('Hotel Login Page')

# Load images from the "images" folder and store them as global variables
bgImage = ImageTk.PhotoImage(file='./images/bg.jpg')
openEyeImage = ImageTk.PhotoImage(file='./images/openeye.png')
closeEyeImage = ImageTk.PhotoImage(file='./images/closeye.png')
facebook_Logo = ImageTk.PhotoImage(file='./images/facebook.png')
google_Logo = ImageTk.PhotoImage(file='./images/google.png')
twitter_Logo = ImageTk.PhotoImage(file='./images/twitter.png')

# Display background image
bgLabel = Label(login_window, image=bgImage)
bgLabel.grid(row=0, column=0)

# STAFF LOGIN HEADER
heading = Label(login_window, text="STAFF LOGIN", font=('Microsoft Yahei UI Light', 23, 'bold'),
                bg='white', fg='firebrick4')
heading.place(x=590, y=135)

# Email Entry
staffemailEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                       bd=0, fg='firebrick1')
staffemailEntry.place(x=569, y=210)
staffemailEntry.insert(0, 'Email')
staffemailEntry.bind('<FocusIn>', user_enter)

# Horizontal line under Email
frame1 = Frame(login_window, width=250, height=2, bg="firebrick4")
frame1.place(x=569, y=232)

# PASSWORD Entry
passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                      bd=0, fg='firebrick1')
passwordEntry.place(x=569, y=270)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

# Horizontal line under Password
frame2 = Frame(login_window, width=250, height=2, bg="firebrick4")
frame2.place(x=569, y=292)


# Eye button to show/hide password
eyeButton = Button(login_window, image=closeEyeImage, bd=0, bg='white', activebackground='white',
                   cursor='hand2', command=hide)
eyeButton.place(x=795, y=266)

# Forgot Password Button
forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white',
                   cursor='hand2', font=('Microsoft Yahei UI Light', 9, 'bold'),
                   fg='firebrick3', activeforeground= "firebrick3",command=forget_pass)
forgetButton.place(x=565, y=305)

# Login Button
loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'),
                   fg='white', bg='firebrick1', activeforeground='white',
                   activebackground='firebrick1', cursor='hand2', bd=0, width=19,command=login_user)
loginButton.place(x=569, y=360)

# OR Label
orLabel = Label(login_window, text='-------------- OR --------------', font=('Open Sans', 16),
                fg='firebrick4', bg='white')
orLabel.place(x=574, y=410)

# Social Media Logos as buttons
fbButton = Button(login_window, image=facebook_Logo, bg='white', bd=0, cursor='hand2', command=show_message)
fbButton.place(x=630, y=440)

googleButton = Button(login_window, image=google_Logo, bg='white', bd=0, cursor='hand2', command=show_message)
googleButton.place(x=680, y=440)

twitterButton = Button(login_window, image=twitter_Logo, bg='white', bd=0, cursor='hand2', command=show_message)
twitterButton.place(x=730, y=440)

# Signup Line
signupLabel = Label(login_window, text="Don't have an account?", font=('Open Sans', 9, 'bold'),
                    fg='firebrick4', bg='white')
signupLabel.place(x=585, y=500)

# Create New Account Button
newAccountButton = Button(login_window, text='Create new one', font=('Open Sans', 9, 'bold underline'),
                          fg='blue', bg='white', activeforeground='blue',
                          activebackground='white', cursor='hand2', bd=0, command=signup_page)
newAccountButton.place(x=725, y=500)

# Function to handle pressing Enter key to switch focus between entries
def switch_focus(event):
    if login_window.focus_get() == staffemailEntry:
        passwordEntry.focus_set()
    elif login_window.focus_get() == passwordEntry:
        loginButton.invoke()  # Trigger the login button when Enter is pressed in the password entry


# Bind the Enter key to switch focus between entries
staffemailEntry.bind('<Return>', switch_focus)
passwordEntry.bind('<Return>', switch_focus)


login_window.mainloop()

