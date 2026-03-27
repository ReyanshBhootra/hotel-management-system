import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess

class Admin_Login_Page:
    MAX_ATTEMPTS = 2

    def __init__(self, root):
        self.root = root
        self.login_attempts = 0
        self.root.geometry("580x440+620+270")
        self.root.title('Login')
        self.root.resizable(0, 0)  # Make the window non-resizable

        img1 = ImageTk.PhotoImage(Image.open("./images/pattern.png"))
        l1 = tk.Label(master=self.root, image=img1)
        l1.pack()

        img2 = Image.open('./images/rizzler_hotel.png')
        img2 = img2.resize((260, 50))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbling = tk.Label(master=self.root, image=self.photoimg2, bd=0, relief=tk.RIDGE, bg='gray25')
        lbling.place(x=160, y=70, width=260, height=50)

        # creating a custom frame
        frame = tk.Frame(master=l1, width=320, height=340, bd=0, highlightthickness=0, background='gray25')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = tk.Label(master=frame, text="Admin Login", font=('roman times', 18, 'bold', 'underline'), fg='red',
                      bg='gray25')
        l2.place(x=84, y=85)

        self.admin_email = tk.Entry(master=frame, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                                    bd=0, fg='blue')
        self.admin_email.place(x=50, y=135)
        self.admin_email.insert(0, 'Email')
        self.admin_email.bind('<FocusIn>', self.email_enter)
        self.admin_email.bind('<Return>', self.switch_focus)  # Bind Enter key event

        self.admin_password = tk.Entry(master=frame, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                                       bd=0, fg='blue')
        self.admin_password.place(x=50, y=190)
        self.admin_password.insert(0, 'Password')
        self.admin_password.bind('<FocusIn>', self.password_enter)

        # Login Button
        loginButton = tk.Button(master=frame, text='Login', font=('Open Sans', 14, 'bold'),
                                fg='white', bg='firebrick1', activeforeground='white',
                                activebackground='firebrick1', cursor='hand2', bd=0, width=16, command=self.login)
        loginButton.place(x=64, y=260)

        self.root.mainloop()

    # Function to handle Email entry focus event
    def email_enter(self, event):
        if self.admin_email.get() == 'Email':
            self.admin_email.delete(0, tk.END)

    # Function to handle password entry focus event
    def password_enter(self, event):
        if self.admin_password.get() == 'Password':
            self.admin_password.delete(0, tk.END)
            self.admin_password.config(show='*')

    def login(self):
        try:
            # Check if the email is in a lockout period
            if self.login_attempts >= self.MAX_ATTEMPTS:
                if self.root:
                    messagebox.showerror("Login Failed", "Too many login attempts.")
                    self.root.destroy()  # Close the root window
                return  # Stop further processing

            email = self.admin_email.get()
            password = self.admin_password.get()
            if not email:
                raise ValueError("Please enter the email")
            if not password:
                raise ValueError("Please enter the password")
            if email == "ray@rizz.com" and password == "rizzlerhotel":
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                # Open the admin_control.py file using subprocess
                subprocess.Popen(['python', 'admin_control.py'])

                # Check if the root window still exists before destroying it
                if self.root:
                    self.root.destroy()
            else:
                self.login_attempts += 1
                raise ValueError("Invalid email or password")

        except ValueError as e:
            messagebox.showerror("Login Failed", str(e))

            # Check if the root window still exists before calling focus_force()
            if self.root and self.admin_email:
                self.admin_email.focus_force()  # Set focus back to admin_email entry

    #to move between entries using the enter key
    def switch_focus(self, event):
        focus_next = self.root.focus_get().tk_focusNext()
        if focus_next:
            focus_next.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    admin_login_page = Admin_Login_Page(root)
    root.mainloop()
