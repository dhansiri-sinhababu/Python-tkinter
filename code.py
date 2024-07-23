from tkinter import *
from tkinter.messagebox import showinfo, askquestion
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from datetime import datetime


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    message = askquestion('Notepad', "Do you want to save changes")
    if message == "yes":
        saveFile()
    else:
        root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


def undo():
    TextArea.edit_undo()


def redo():
    TextArea.edit_redo()


def time():
    d = datetime.now()
    TextArea.insert('end', d)


def about():
    showinfo("Text Editor", "Text Editor by- Dhansiri & Apurva")


def contact():
    showinfo("Contact", "tkinter@gmail.com")


def feedback():
    askquestion("Feedback", "Is this GUI Helps you?")


if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("logo.ico")
    root.geometry('600x300')
    root.minsize(200, 100)

#     text = ScrolledText(root, height=1000, undo=True)
#     text.pack(fill=tk.BOTH)

    # Add TextArea
    TextArea = Text(root, font="lucida 17")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # for create Menubar
    MenuBar = Menu(root)

    FileMenu = Menu(MenuBar, tearoff=0)

    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)

    MenuBar.add_cascade(label="File", menu=FileMenu)

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)

    EditMenu.add_command(label="Undo", command=undo)
    EditMenu.add_command(label="Redo", command=redo)
    EditMenu.add_separator()
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    EditMenu.add_separator()
    EditMenu.add_command(label="Time/Date", command=time)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)

    HelpMenu.add_command(label="Contact Us", command=contact)
    HelpMenu.add_command(label="Feedback", command=feedback)
    HelpMenu.add_command(label="About Notepad", command=about)
    HelpMenu.add_separator()
    HelpMenu.add_command(label="Exit", command=quitApp)

    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    # Adding Scrollbar 
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
