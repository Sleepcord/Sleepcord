import tkinter
from tkinter import messagebox
appname = "Portal"
username = ""
onlogin = True
network = "0.0.0.0"
root = tkinter.Tk()

def login():
    tkinter.Label(root, text="Welcome to SleepCord (Pre-Alpha v0.1)!", bg="#202020", fg="#FFFFFF").place(x=5,y=5)
    tkinter.Label(root, text="Username:", bg="#202020", fg="#FFFFFF").place(x=5,y=30)
    tkinter.Label(root, text="IP Address:", bg="#202020", fg="#FFFFFF").place(x=5,y=70)
    tkinter.Label(root, text="Made by the SleepCord Crew with love <3", bg="#202020", fg="#313131").place(x=170,y=180)
    tkinter.Button(root, text="I wand to host a server",bg="#202020", fg="#0050FF", border=0, borderwidth=0, command=host).place(x=5,y=180)

def host():
    onlogin = True

root.title("SleepCord - " + str(appname))
login()

root.configure(bg="#202020")
if onlogin:
    root.geometry("400x200")
    root.resizable(False, False)
else:
    root.geometry("600x400")
    root.resizable(True, True)
root.mainloop()
