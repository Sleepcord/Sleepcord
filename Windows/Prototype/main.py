from tkinter import *
import webbrowser
from configparser import ConfigParser

title = "Login"
page = 0

globalfile = ConfigParser()
themefile = ConfigParser()

globalfile.read("global.ini")
themefile.read("theme.ini")

themeused = globalfile['Main']['theme']
background = themefile[themeused]['background']
foreground = themefile[themeused]['foreground']
entrybg = themefile[themeused]['entrybg']
buttonbg = themefile[themeused]['buttonbg']
extratextcol = themefile[themeused]['extratextcol']
border = themefile[themeused]['border']

def loginthensave():
    globalfile['Main']['username'] = Username.get()
    globalfile['Main']['ip'] = ipaddress.get()

    with open("global.ini", "w") as f:
        globalfile.write(f)

def jbbgithub():
    webbrowser.open_new_tab("https://github.com/johnnyboulayboy")

def madyoutube():
    webbrowser.open_new_tab("https://www.youtube.com/@fleetwaysonic.exe1463")

def rickroll():
    webbrowser.open_new_tab("https://youtu.be/dQw4w9WgXcQ?si=uv1w7NUUVJJ2_p_K")

def showcredits():
    creditspage = Toplevel()
    creditspage.title("SleepCord - Credits")
    creditspage.iconbitmap('icon.ico')
    creditspage.geometry("280x150")
    creditspage.resizable(False,False)
    creditspage.configure(bg=background)

    Label(creditspage, text="The Sleepcord Crew", bg=background ,fg=foreground).pack(padx=0)
    Label(creditspage, text="Coder - JohnnyBoulayBoy", bg=background ,fg=foreground).place(x=5, y=25)
    Label(creditspage, text="Artist - Madeline_Negagen", bg=background ,fg=foreground).place(x=5, y=55)
    Label(creditspage, text='Didnt work - Bluetoons', bg=background ,fg=foreground).place(x=5, y=85)

    Button(creditspage, text='Github', bg=buttonbg, fg=foreground, border=border, width=16, command=jbbgithub).place(x=150,y=27)
    Button(creditspage, text='Youtube', bg=buttonbg, fg=foreground, border=border, width=15, command=madyoutube).place(x=157,y=57)
    Button(creditspage, text='Youtube', bg=buttonbg, fg=foreground, border=border, width=17, command=rickroll).place(x=143,y=87)

root = Tk()

ipaddress = StringVar(value=globalfile['Main']['ip'])
Username = StringVar(value=globalfile['Main']['username'])

root.title("Sleepcord - " + str(title))
root.iconbitmap("icon.ico")

if page == 0:
    root.geometry("400x170")
    root.resizable(False, False)
    root.configure(bg=background)

    Label(root, text="Welcome to Sleepcord", bg=background, fg=foreground).pack(padx=0)
    Label(root, text="Username:", bg=background, fg=foreground).place(x=5, y=30)
    Label(root, text="Ip address:", bg=background, fg=foreground).place(x=5, y=60)
    Entry(root, textvariable=Username, bg=entrybg, fg=foreground, border=border, width=53).place(x=70, y=33)
    Entry(root, textvariable=ipaddress, bg=entrybg, fg=foreground, border=border, width=53).place(x=70, y=63)

    Button(root, text=" Login ", bg=buttonbg, fg=foreground, border=border, width=54, command=loginthensave).place(x=5, y=90)
    Button(root, text="I wand to host a server", bg=background, foreground=extratextcol, border=border).place(x=5, y=145)
    Button(root, text='Credits', bg=background, fg=foreground, border=border, command=showcredits).place(x=350, y=145)

root.mainloop()