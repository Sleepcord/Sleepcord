from tkinter import *

background = "#202020"
foreground = "#FFFFFF"
entrybg = "#303030"
buttonbg = "#303030"
linkbutton = "#0000FF"
border = 0

sidecolor = "#151515"
headermaincolor = "#303030"
sidebordercolor = "#252525"
sideheadercolor = "#101010"

appwidth = 500
appheight = 400

place = "PlaceHolder"

def update_size(event):
    global appwidth, appheight
    appwidth = root.winfo_width()
    appheight = root.winfo_height()
    sidebar.config(height=appheight, width=int(appwidth/2 - (appwidth/6)))

    borderside.config(height=appheight, width=5)
    borderside.place(x=int(appwidth/2 - (appwidth/6)), y=0)

    sideheader.config(width=int(appwidth/2 - (appwidth/6)), height=35)

    mainheader.config(width=appwidth/1.5, height=35)
    mainheader.place(x=int(appwidth/2 - (appwidth/6)) + 5, y=0)

    PlaceName.config(text=place, bg=sideheadercolor, fg=foreground, font=("arial", 12))
    PlaceName.place(in_=sideheader, relx=0.5, rely=0.5, anchor="center")

    Chatter.config(width=int(appwidth/2 - (appwidth/6)), font=("Arial", 12))
    Chatter.pack_configure(ipady=10)
    Chatter.place(x=50,y=50)


root = Tk()
chatterentry = StringVar(value="")

root.geometry(f"{appwidth}x{appheight}") 
root.minsize(width=500, height=400)
root.title("Sleepcord - " + str(place))
root.config(bg=background)

#back
sidebar = Frame(root, bg=sidecolor)
borderside = Frame(root, bg=sidebordercolor)
sideheader = Frame(root, bg=sideheadercolor)
mainheader = Frame(root, bg=headermaincolor)
PlaceName = Label(root)
sidebar.place(x=0, y=0)
sideheader.place(x=0, y=0)

#front
Chatter = Entry(root, textvariable=chatterentry, background=background, foreground=foreground, border=border)


# always at the end
root.bind("<Configure>", update_size)
root.mainloop()