import tkinter
from tkinter import messagebox
import random

randomnum = random.randrange(1000,9999)
appname = "Portal"
username = "User_" + str(randomnum)
onlogin = True
network = "0.0.0.0"
root = tkinter.Tk()

def loger():
    tkinter.Label(root, text="Welcome to SleepCord (Pre-Alpha v0.1)!", bg="#202020", fg="#FFFFFF").place(x=5,y=5)
    tkinter.Label(root, text="Username:", bg="#202020", fg="#FFFFFF").place(x=5,y=30)
    tkinter.Label(root, text="IP Address:", bg="#202020", fg="#FFFFFF").place(x=5,y=70)
    tkinter.Label(root, text="Made by the SleepCord Crew with love <3", bg="#202020", fg="#313131").place(x=170,y=180)
    tkinter.Button(root, text="Connect",bg="#A0A0A0", fg="#000000", border=1, borderwidth=0.5, command=login).place(x=5,y=115)
    tkinter.Button(root, text="I wand to host a server",bg="#202020", fg="#0050FF", border=0, borderwidth=0, command=host).place(x=5,y=180)

    usernamep = tkinter.Entry(root, width=50, border=0)
    usernamep.place(x=70, y=30)
    usernamep.insert(0, username)
    iplog = tkinter.Entry(root, width=50, border=0)
    iplog.place(x=70, y=70)
    iplog.insert(0, network)

def host():
    onlogin = False
    network = 'localhost'
    print('Lancement du hosting...')
    import hoster
    print("Lancement de 'hoster.py'")
    # à continué plus tard.

def login():
    onlogin = False

root.title("SleepCord - " + str(appname))
loger()
root.configure(bg="#202020")
root.iconbitmap("icon.ico")
if onlogin:
    root.geometry("400x200")
    root.resizable(False, False)
else:
    root.geometry("600x400")
    root.resizable(True, True)
    
print('Application executé')
root.mainloop()
