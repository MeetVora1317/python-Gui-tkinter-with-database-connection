import mysql.connector
from tkinter import *
import tkinter.messagebox as tkmessagebox

# screen details 
root = Tk()
root.title("Registeration Form ")
width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# variable used in program
email = StringVar()
passw = StringVar()
full_name = StringVar()
phone_number = StringVar()
# all variable declration end here

#all  Function start here

# for database connection
 
def Database():
    global conn, cursor
    conn= mysql.connector.connect(host ="localhost",user = 'root',password = 'root',db ="demo")
    cursor = conn.cursor()
    print(conn,cursor)

# for exit from a UI 
def Exit():
    result = tkmessagebox.askquestion('System','Are you sure you want to exit ?', icon='warning')
    if result == 'yes':
        root.destroy()
        exit()

# for Register User
def Register():
    Database()
    print(cursor)
    if email.get() == "" or passw.get() == ""or full_name.get()== "" or phone_number.get() == "":
        lbl_result.config(text ='Please complete the required field!',fg='orange')
    else:   
        email_data =email.get() 
        query = "SELECT * FROM `base_user` WHERE email = '{0}'".format(email_data)
        cursor.execute(query)
        if cursor.fetchone() is not None:
            lbl_result.config(text = 'another user  with same name is already present',fg='orange')
        else:
            cursor.execute("INSERT INTO `base_user`(full_name,password,email, phone_number,is_active,is_staff,is_superuser) VALUES(%s, %s, %s, %s,True,False,False)", (str(full_name.get()), str(passw.get()), str(email.get()), str(phone_number.get())))
            conn.commit()
            email_set.set("")
            passw_set.set("")
            fullname_set.set("")
            phone_set.set("")
            lbl_result.config(text="Successfully Created!", fg="green")
        cursor.close()
        conn.close()

# all function end here

# frame to be displayed
TitleFrame = Frame(root,height=100,width=640,bd=1,relief =SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=TOP,pady=20)


# All label

lbl_title = Label(TitleFrame,text="Register Form",font=('arial',20),bd=1,width=640)
lbl_title.pack()
lbl_email = Label(RegisterFrame,text='Email',font=('arial',20))
lbl_email.grid(row=1,column=0)
lbl_password = Label(RegisterFrame,text='password',font=('arial',20))
lbl_password.grid(row=2,column=0)
lbl_fullname = Label(RegisterFrame,text='full name',font=('arial',20))
lbl_fullname.grid(row=3,column=0)
lbl_phonenumber = Label(RegisterFrame,text='phone number',font=('arial',20))
lbl_phonenumber.grid(row=4,column=0)
lbl_result = Label(RegisterFrame,text='',font=('arial',20))
lbl_result.grid(row=5,columnspan=2)

# all Entry value
email_set = StringVar()
passw_set = StringVar()
fullname_set = StringVar()
phone_set = StringVar()
email = Entry(RegisterFrame,font=('arial',20),textvariable=email_set,width=15)
email.grid(row=1,column=1)
passw = Entry(RegisterFrame,font=('arial',20),textvariable=passw_set,width=15)
passw.grid(row=2,column=1)
full_name = Entry(RegisterFrame,font=('arial',20),textvariable=fullname_set,width=15)
full_name.grid(row=3,column=1)
phone_number = Entry(RegisterFrame,font=('arial',20),textvariable=phone_set,width=15)
phone_number.grid(row=4,column=1)

# button for register and delete
btn_register = Button(RegisterFrame,font=('arial',20),text='Register',command=Register)
btn_register.grid(row=7,columnspan=2)
btn_exit = Button(RegisterFrame,font=('arial',20),text='Exit',command =Exit)
btn_exit.grid(row=20 ,columnspan=2)

# menubar at the top for exit
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Exit",command= Exit)
menubar.add_cascade(label='File',menu=filemenu)
root.config(menu=menubar)

if __name__ == '__main__':
    root.mainloop()
