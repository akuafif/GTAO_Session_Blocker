import tkinter as tk
from tkinter import ttk
import webbrowser

def callback(url):
    webbrowser.open_new_tab(url)

def About():
    win = tk.Toplevel()
    win.wm_title("About")

    tk.Label(win, text="About",font=("Arial", 25)).grid(row=0, column=0, padx=5, pady=2, columnspan=2, sticky='ew')

    tk.Label(win, text="Created by Aki [rarakat#3152]",font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=2, columnspan=2, sticky='ew')

    tk.Label(win, text="GitHub:",font=("Arial", 12)).grid(row=3, column=0, sticky='w', padx=5,pady=5)
    githublbl = tk.Label(win, text=r"https://github.com/fscene8/GTAO_Session_Blocker", font=("Arial", 12), fg="blue", cursor="hand2")
    githublbl.grid(row=3, column=1, padx=5, pady=5, sticky='w')
    githublbl.bind("<Button-1>", lambda e: callback("https://github.com/fscene8/GTAO_Session_Blocker"))
    
    tk.Label(win, text="GTA Crew:",font=("Arial", 12)).grid(row=4, column=0, sticky='w', padx=5, pady=5)
    sclbl = tk.Label(win, text="https://socialclub.rockstargames.com/crew/sgpckias/", font=("Arial", 12), fg="blue", cursor="hand2")
    sclbl.grid(row=4, column=1, padx=5, pady=5, sticky='w')
    sclbl.bind("<Button-1>", lambda e: callback("https://socialclub.rockstargames.com/crew/sgpckias/"))

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky='s')

    win.resizable(False, False) 

    # Gets the requested values of the height and width.
    windowWidth = win.winfo_reqwidth()
    windowHeight = win.winfo_reqheight()
    
    # Gets both half the screen width/height and window width/height
    positionRight = int(win.winfo_screenwidth()/2 - windowWidth / 2)
    positionDown = int(win.winfo_screenheight()/2 - windowHeight/ 2)
    
    # Positions the window in the center of the page.
    win.geometry("+{}+{}".format(positionRight, positionDown))  


def HowTo():
    win = tk.Toplevel()
    win.wm_title("About")

    tk.Label(win, text="How to use",font=("Arial", 25)).grid(row=0, column=0, padx=5, pady=2, columnspan=2, sticky='ew')

    tk.Label(win, text="Step 1  > ",font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=2, sticky='w')
    tk.Label(win, text="Run GTA Online", font=("Arial", 11)).grid(row=1, column=1, padx=5, pady=2, sticky='w')
    
    tk.Label(win, text="Step 2  > ",font=("Arial", 11)).grid(row=2, column=0, padx=5, pady=2, sticky='w')
    tk.Label(win, text="Suspend the process and be the session host", font=("Arial", 12)).grid(row=2, column=1, padx=5, pady=2, sticky='w')

    tk.Label(win, text="Step 3  > ",font=("Arial", 11)).grid(row=3, column=0, padx=5, pady=2, sticky='w')
    tk.Label(win, text="Invite your friend to your session and right click their IP to whitelist", font=("Arial", 11)).grid(row=3, column=1, padx=5, pady=2, sticky='w')

    tk.Label(win, text="Step 4  > ",font=("Arial", 11)).grid(row=4, column=0, padx=5, pady=2, sticky='w')
    tk.Label(win, text="Toggle on the firewall to prevent public from entering", font=("Arial", 11)).grid(row=4, column=1, padx=5, sticky='w')

    tk.Label(win, text=" ", font=("Arial", 11)).grid(row=5, column=1, padx=5, sticky='w')

    tk.Label(win, text="Notes 1 > ",font=("Arial", 11)).grid(row=6, column=0, padx=5, pady=2, sticky='sw')
    tk.Label(win, text="How to know if I'm the host?", font=("Arial", 11)).grid(row=6, column=1, padx=5, pady=2, sticky='sw')
    tk.Label(win, text="You will see that the 'Ago' column will be very low (0-8s) and you will be flooded ", font=("Arial", 11)).grid(row=7, column=1, padx=5, sticky='nw')
    tk.Label(win, text="with Take-Two R* IP address from US, New York (192.168.x.x), untill you turned on the firewall.", font=("Arial", 11)).grid(row=8, column=1, padx=5, sticky='nw')
    tk.Label(win, text="'Packet In' counter will be higher too for player IP in session if you're the host.", font=("Arial", 11)).grid(row=9, column=1, padx=5, sticky='nw')

    tk.Label(win, text="Notes 2 > ",font=("Arial", 11)).grid(row=10, column=0, padx=5, pady=10, sticky='w')
    tk.Label(win, text="You need to toggle off your firewall for your friend to rejoin the session again", font=("Arial", 11)).grid(row=10, column=1, padx=5, pady=10, sticky='w')

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=11, column=0, columnspan=2, padx=5, pady=10, sticky='s')

    win.resizable(False, False) 

    # Gets the requested values of the height and width.
    windowWidth = win.winfo_reqwidth()
    windowHeight = win.winfo_reqheight()
    
    # Gets both half the screen width/height and window width/height
    positionRight = int(win.winfo_screenwidth()/2 - windowWidth / 2)
    positionDown = int(win.winfo_screenheight()/2 - windowHeight/ 2)
    
    # Positions the window in the center of the page.
    win.geometry("+{}+{}".format(positionRight, positionDown))  