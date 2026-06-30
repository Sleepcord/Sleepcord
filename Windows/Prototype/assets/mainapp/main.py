from tkinter import *
import webbrowser
from configparser import ConfigParser

# SETUP

title = "Login"
page = 0

globalfile = ConfigParser()
themefile = ConfigParser()

globalfile.read("global.ini")
themefile.read("theme.ini")

themeused = globalfile['THEME']['theme']
themes_list = themefile.sections()
themelist = len(themes_list)

#   bglogin = themefile[themeused]['bgloginimage']
#   if bglogin == 'NaN':
#       bglogin = 0
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

def jbbgithub(): # Mon youtube (J.B.B)
    webbrowser.open_new_tab("https://github.com/johnnyboulayboy")

def madyoutube(): # Youtube à Madeline
    webbrowser.open_new_tab("https://www.youtube.com/@fleetwaysonic.exe1463")

def rickroll(): #I NEVER GOING TO GIVE YOU UP AND NEVER GOING TO LET YOU DOWN
    webbrowser.open_new_tab("https://youtu.be/dQw4w9WgXcQ?si=uv1w7NUUVJJ2_p_K")

def infoonbt(): #Fuck you bluetoons AGAIN :D
    infoonbt = Toplevel()
    infoonbt.title('Fuck you Bluetoons...')
    infoonbt.iconbitmap('assets\\fbt.ico')
    infoonbt.geometry('300x100')
    infoonbt.resizable(False, False)
    infoonbt.configure(bg=background)

    
    Label(infoonbt, text="note: Bro is the reason why sleepcord exist.\nSince He dont wand to a make a fucking account\nOn any other social network bruh.", bg=background ,fg=foreground).pack(padx=0) 
    Button(infoonbt, text="Totally his youtube accound (trust)", bg=buttonbg, fg=foreground, border=border, width=40, command=rickroll).place(x=5, y=50)

def showcredits(): #BLA BLA BLA LOL
    creditspage = Toplevel()
    creditspage.title("SleepCord - Credits")
    creditspage.iconbitmap('assets\\icon.ico')
    creditspage.geometry("280x150")
    creditspage.resizable(False,False)
    creditspage.configure(bg=background)

    Label(creditspage, text="The Sleepcord Crew", bg=background ,fg=foreground).pack(padx=0)
    Label(creditspage, text="Coder - JohnnyBoulayBoy", bg=background ,fg=foreground).place(x=5, y=25)
    Label(creditspage, text="Artist - Madeline_Negagen", bg=background ,fg=foreground).place(x=5, y=55)
    Label(creditspage, text='AssHole :D  -  Bluetoons', bg=background ,fg=foreground).place(x=5, y=85) #Fuck you bluetoons.

    Button(creditspage, text='Github', bg=buttonbg, fg=foreground, border=border, width=16, command=jbbgithub).place(x=150,y=27)
    Button(creditspage, text='Youtube', bg=buttonbg, fg=foreground, border=border, width=15, command=madyoutube).place(x=157,y=57)
    Button(creditspage, text='More', bg=buttonbg, fg=foreground, border=border, width=17, command=infoonbt).place(x=143,y=87)

def thememenu():
    themesmenu = Toplevel()
    themesmenu.title("Select a theme")
    themesmenu.geometry("400x350")
    themesmenu.iconbitmap("assets\\Themes.ico")
    themesmenu.resizable(False, False)
    themesmenu.configure(bg=background)

    Label(themesmenu, text=f"{themelist} themes have been found!",
          bg=background, fg=foreground).pack(pady=10)

    for theme in themes_list:
        Button(
            themesmenu,text=theme,bg=buttonbg,fg=foreground,border=border,width=20,command=lambda t=theme: apply_theme(t)).pack(pady=2)

def apply_theme(theme_name):
    globalfile['THEME']['theme'] = theme_name
    with open("global.ini", "w") as f:
        globalfile.write(f)
    global background, foreground, entrybg, buttonbg, extratextcol, border, hostbg
    themeused = theme_name
    background = themefile[themeused]['background']
    foreground = themefile[themeused]['foreground']
    entrybg = themefile[themeused]['entrybg']
    buttonbg = themefile[themeused]['buttonbg']
    extratextcol = themefile[themeused]['extratextcol']
    border = themefile[themeused]['border']
    hostbg = themefile[themeused]['hosterspecialbg']
    actu()
    

def hoster(): # I wand to host a server
    hostbg = themefile[themeused]['hosterspecialbg']
    hosterpage = Toplevel()
    hosterpage.title('Sleepcord - Hoster')
    hosterpage.iconbitmap('assets\\BSOD.ico')
    hosterpage.configure(bg=background)
    hosterpage.geometry("500x500")
    hosterpage.resizable(False, False)
    Canvas(hosterpage, width=477, height=400, bg=hostbg, border=0, borderwidth=0).place(x=9,y=10)
    Canvas(hosterpage, width=475, height=402, bg=hostbg, border=0, borderwidth=0).place(x=10,y=9)
    Entry(hosterpage, text="'/?' for help", border=border, bg=entrybg, fg=foreground).place(x=5,y=420)

root = Tk()

ipaddress = StringVar(value=globalfile['Main']['ip'])
Username = StringVar(value=globalfile['Main']['username'])

root.title("Sleepcord - " + str(title))
root.iconbitmap("assets\\icon.ico")

def clear_page(window):
    for widget in window.winfo_children():
        widget.destroy()

def actu():
    clear_page(root)
    if page == 0:
        root.geometry("400x170")
        root.resizable(False, False)
        root.configure(bg=background)
        #   if not bglogin == 'NaN':
        #       Canvas(root, Image="assets//Themes//" + str(bglogin)).place(x=0,y=0)
        Label(root, text="Welcome to Sleepcord", bg=background, fg=foreground).pack(padx=0, pady=0)
        Label(root, text="Username:", bg=background, fg=foreground).place(x=5, y=30)
        Label(root, text="Ip address:", bg=background, fg=foreground).place(x=5, y=60)
        Entry(root, textvariable=Username, bg=entrybg, fg=foreground, border=border, width=53).place(x=70, y=33)
        Entry(root, textvariable=ipaddress, bg=entrybg, fg=foreground, border=border, width=53).place(x=70, y=63)

        Button(root, text=" Login ", bg=buttonbg, fg=foreground, border=border, width=54, command=loginthensave).place(x=5, y=90)
        Button(root, text="I wand to host a server", bg=background, foreground=extratextcol, border=border,command=hoster).place(x=5, y=145)
        Button(root, text='Credits', bg=background, fg=foreground, border=border, command=showcredits).place(x=350, y=145)
        Button(root, text='Themes', fg=foreground, bg=background, border=border, command=thememenu).place(x=0,y=0)

actu()

root.mainloop()