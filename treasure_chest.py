#TREASURE CHEST FILE MANAGER#
#             BY ERIK (c) 2023            #


saved = []


FUNCTIONS = [
    "d",
    "cd ..",
    "cd"
]
print("Starting Treasure Chest...")
print("Importing Extensions...")
try:
    import os
    from tkinter import *
    import math
    import random
    
    print("Successfully Loaded Extensions")
except ImportError as error:
    #Get values [17] to [-2] in Import Error
    error = str(error)
    error = list(error)
    error_str = ""
    error_pos = 0

    #Iteration
    for i in error:
        if error_pos >= 17 and error_pos <= len(list(error)) - 2:
            error_str += i
        error_pos += 1

    #Error Message
    print("\nFailure while Loading Extensions. Did you forget to install ", error_str, "?", sep="")
    #Tips
    print("\nTry to install it using PIP. (Syntax:)\n", f"pip install {error_str}\n\nIf that does not work, You may be using the wrong syntax.")
    print("\nThis is another way you can install it. (Syntax:)\n", f"python -m pip install {error_str}\n\nIf neither of them work, the extension may no longer support Python.\n")
    print(f"Here are some tips you can use if an extension isn't installing:\n1. Restart your computer\n   You may be using too many resources, so this could refresh your computer.\n2. Look online to see if support has deprecated for {error_str}. You can also check to see if it exists.\n3. See if people have experienced the same error. If no solution has been met, please email me. I will attempt to use a patch or make a work-around to this error.")
    print("THE PROGRAM WILL NOW SELF-DESTRUCT.")
    exit()

def assist():
    for i in FUNCTIONS:
        print("\n\n")
        if i == "d":
            print(i, "Returns with the current directory you are in.", sep=":")
        elif i == "cd ..":
            print(i, "Escapes out of the current directory:\n[C:\Dave\Desktop\School --> C:\Dave\Desktop]", sep=":")
        elif i == "cd":
            print(i, "Changes the directory [Opens a new window]", sep=":")

def overwrite_directory():
    global Label2
    
    try:
        global SubTreasureChest
        os.chdir(Entr2.get())
        SubTreasureChest.destroy()
    except:
        Label2["text"] = "Insert CD to Change Into\nINVALID DIRECTORY"

def refresh():
    global TreasureChest
    TreasureChest = Tk()
    TreasureChest.title("Treasure Chest")
    global Entr
    Entr = Entry(TreasureChest)
    Entr.grid()
    global Btn
    Btn = Button(TreasureChest, text="Execute", command=lambda: find(Entr.get()))
    Btn.grid(column=1, row=0)
    global Btn2
    Btn2 = Button(TreasureChest, text="Info", command=info)
    Btn2.grid(column=2, row=0)
    global Btn3
    Btn3 = Button(TreasureChest, text="Save", command=save)
    Btn3.grid(column=3, row=0)
    global Btn4
    Btn4 = Button(TreasureChest, text="Help", command=assist)
    Btn4.grid(column=4, row=0)
    global Label1
    Label1 = Label(TreasureChest, text="")
    Label1.grid()

    global btnX
    for i in saved:
        btnX = Button(TreasureChest, text=i, command=lambda: find(i, "BUTTON"))
        btnX.grid(column=1, row=1)

    TreasureChest.mainloop()

def info():
    if Entr.get() in FUNCTIONS:
        if Entr.get() == "d":
            path = "Returns with the current directory you are in."
        elif Entr.get() == "cd ..":
            path = "Escapes out of the current directory:\n[C:\Dave\Desktop\School --> C:\Dave\Desktop]"
        elif Entr.get() == "cd":
            path = "Changes the directory [Opens a new window]"
        Label1["text"] = path


def find(i, a=None):
    global Label1
    if a == "BUTTON":
        global btnX
        i = btnX["text"]
    if i in FUNCTIONS:
        if i == "d":
            path = os.getcwd()
            Label1["text"] = path
        elif i == "cd ..":
            os.chdir('../')
            print("Completed")
            path = os.getcwd()
            Label1["text"] = path
        elif i == "cd":
             global SubTreasureChest
             SubTreasureChest = Tk()
             SubTreasureChest.title('"cd" | TreasureChests')
             global Entr2
             Entr2 = Entry(SubTreasureChest, width=45,)
             Entr2.insert(0, os.getcwd()) 
             Entr2.grid()
             global Label2
             Label2 = Label(SubTreasureChest, text="Insert CD to Change Into")
             Label2.grid()
             Btn5 = Button(SubTreasureChest, text="Change", command=overwrite_directory)
             Btn5.grid(column=3, row=0)
             SubTreasureChest.mainloop()
def save():
    if Entr.get() in FUNCTIONS:
        saved.append(Entr.get())
        if len(saved) > 1:
            del saved[0]
        TreasureChest.destroy()
        refresh()

refresh()

