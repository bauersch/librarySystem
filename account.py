from tkinter import *

window = Tk()
window.title("Account Management")
window.geometry("500x500")

usernameLabel = Label(window, text="Username").place(x = 40, y = 60)
passwordlabel= Label(window, text="Password").place(x=40,y=100)

submitButton= Button(window, text="Submit").place(x=40, y=140)

usernameTextField= Entry(window, width = 40).place(x=40,y=80)
passwordTextField= Entry(window, width=40).place(x=40,y=120)

window.mainloop()