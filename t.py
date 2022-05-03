from tkinter import *

main_screen = Tk()
main_screen.geometry("300x250")
main_screen.title("Account Login")
Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()
Button(text="Admin Login", height="2", width="30").pack()
Label(text="").pack()
Button(text="Register", height="2", width="30").pack()

main_screen.mainloop()