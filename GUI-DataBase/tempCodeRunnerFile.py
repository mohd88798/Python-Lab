from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Users"
)

mycursor = mydb.cursor()
# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global email
    global username
    global password
    global email_entry
    global username_entry
    global password_entry
    email = StringVar()
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()

    email_lable = Label(register_screen, text="Email")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

    username_lable = Label(register_screen, text="Username")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Password")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()



def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Admin login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button

def register_user():

    email_info = email.get()
    username_info = username.get()
    password_info = password.get()

    query = "INSERT INTO Register (email, username, password) VALUES (%s, %s, %s)"
    val = (email_info, username_info, password_info)
    mycursor.execute(query, val)

    mydb.commit()

    email_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    try:
        query = "SELECT * FROM Admin"
        mycursor.execute(query)

        result = mycursor.fetchall()
        for x in result:
            if username1 and password1 in x:
                home_page()
            elif username1 not in x:
                user_not_found()
            elif password1 not in x:
                password_not_recognised()
    except Exception as e:
        print("Something went wrong")
        print(e)

# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# home page shows user details can only be accessed using admin login

def home_page():
    global home_screen
    main_screen.destroy()
    home_screen = Tk()

    home_screen.geometry("600x300")

    sql = "SELECT * FROM Register"
    mycursor.execute(sql)
    result =  mycursor.fetchall()
    i = 0 
    items = ['Email', 'Username', 'Password']
    for x in range(1):
        for j in range(len(items)):
            e = Entry(home_screen, width=25, fg='red') 
            e.grid(row=i, column=j) 
            e.insert(END, items[j])
        i=i+1
    for user in result:
        for j in range(len(user)):
            e = Entry(home_screen, width=25, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, user[j])
        i=i+1

    home_screen.mainloop()

# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Admin Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
