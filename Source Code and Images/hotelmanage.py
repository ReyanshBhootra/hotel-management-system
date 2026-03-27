from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_win
from room_booking import RoomBooking
from room_details import RoomDetails
from tkinter import messagebox
from admin_login import Admin_Login_Page

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        # Open the window in maximized state
        self.root.state('zoomed')
        # Bind the window close event to a function
        root.protocol("WM_DELETE_WINDOW", self.disable_close_button)

        # ----------------ist img-----------------
        img1 = Image.open(r".\images\hotel1.png")
        img1 = img1.resize((1550, 140))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbling = Label(self.root, image=self.photoimg1, bd=3,background='black', relief=RIDGE)
        lbling.place(x=0, y=0, width=1550, height=140)

        # ----------------logo-----------------
        img2 = Image.open(r".\images\hotelLogo.png")
        img2 = img2.resize((230, 140))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root, image=self.photoimg2, bd=4,background='gold', relief=RIDGE)
        lbling.place(x=0, y=0, width=230, height=140)

        # ---------------title------------------
        lbl_title = Label(self.root, text=('HOTEL MANAGEMENT SYSTEM'), font=('Georgia', 40, 'bold'), bg='NavyBlue',
                          fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # --------------main frame------------------
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # --------------Front Desk Actions--------------
        lbl_FrontDeskA = Label(main_frame, text='FRONT DESK ACTIONS', font=('times new roman', 20, 'bold'), bg='black',
                               fg='gold', bd=4, relief=RIDGE)
        lbl_FrontDeskA.place(x=0, y=0, width=325)

        # --------------button----------------------------
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=325, height=180)

        cust_btn = Button(btn_frame, text='CUSTOMER', width=29, font=('times new roman', 14, 'bold'),
                          bg='DarkSlateBlue', fg='white', bd=0, cursor='hand2', activebackground='DarkSlateBlue',
                          activeforeground='white', highlightbackground='DarkSlateBlue', command=self.cust_details)
        cust_btn.grid(row=0, column=0)

        room_btn = Button(btn_frame, text='BOOK ROOM', width=29,command=self.roombooking_details,
                          font=('times new roman', 14, 'bold'), bg='DarkSlateBlue',
                          fg='white', bd=0, cursor='hand2', activebackground='DarkSlateBlue', activeforeground='white',
                          highlightbackground='DarkSlateBlue')
        room_btn.grid(row=1, column=0)

        details_btn = Button(btn_frame, text='ROOM DETAILS', command=self.roomdetails,width=29, font=('times new roman', 14, 'bold'),
                             bg='DarkSlateBlue', fg='white', bd=0, cursor='hand2', activebackground='DarkSlateBlue',
                             activeforeground='white', highlightbackground='DarkSlateBlue')
        details_btn.grid(row=2, column=0)

        admin_btn = Button(btn_frame, text='ADMIN',command=self.admin_login, width=29, font=('times new roman', 14, 'bold'),
                            bg='DarkSlateBlue', fg='white', bd=0, cursor='hand2', activebackground='DarkSlateBlue',
                            activeforeground='white', highlightbackground='DarkSlateBlue')
        admin_btn.grid(row=3, column=0)

        logout_btn = Button(btn_frame, text='LOGOUT', width=29, command=self.logout,font=('times new roman', 14, 'bold'), bg='Sienna',
                            fg='white', bd=0, cursor='hand2', activebackground='Sienna', activeforeground='white',
                            highlightbackground='Sienna')
        logout_btn.grid(row=4, column=0)

        # ---------------------------------right side image---------------------------------
        img3 = Image.open(r"./images/hotel2.png")
        img3 = img3.resize((1225, 597))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbling1 = Label(main_frame, image=self.photoimg3, bd=0, relief=RIDGE)
        lbling1.place(x=327, y=0, width=1225, height=597)

        # -----------------------------down image----------------------------
        img4 = Image.open(r"./images/hotel3.png")
        img4 = img4.resize((324, 210))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbling2 = Label(main_frame, image=self.photoimg4, bd=0, relief=RIDGE)
        lbling2.place(x=1, y=216, width=324, height=190)

        img5 = Image.open(r"./images/hotel4.png")
        img5 = img5.resize((324, 190))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lbling3 = Label(main_frame, image=self.photoimg5, bd=0, relief=RIDGE)
        lbling3.place(x=1, y=407, width=324, height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def roombooking_details(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)

    def roomdetails(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomDetails(self.new_window)

    def logout(self):
        self.root.destroy()
        import signin

    def admin_login(self):
        self.new_window = Toplevel(self.root)
        admin_login_page = Admin_Login_Page(self.new_window)

    def disable_close_button(self):
        """
        Displays a message when the close button is clicked, informing the user to logout instead.
        """
        # Display a messagebox with the desired message
        messagebox.showinfo("Information", "Close button is disabled. Please logout instead.")


if __name__ == '__main__':
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
