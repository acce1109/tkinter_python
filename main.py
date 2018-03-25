from tkinter import *
import tkinter.messagebox as mbox
import tkinter.filedialog as fd
from  PIL import ImageTk, Image


class Project:

    def __init__(self, master):
        frame = Frame(master, bg="blue", width=300, height=500)
        frame.pack(side=TOP, fill=X)

#*********************** MessageBox **************************
       # mbox.showinfo("Pomoc", "Monkey can live up to 300 yeats.")
        #answer = mbox.askquestion("Question 1", "Do you like silly faces?")

        #if answer == "yes":
         #   print("8===D")


#***********************Main Menu*******************************
        menu = Menu(master)
        master.config(menu=menu)
        #|File|
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Exit", command=frame.quit)
        #|Edit|
        editMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Open Image", command=self.image_open)
        editMenu.add_command(label="Save", command=self.file_save)

#************************ Toolbar ********************************


        self.AXH1 = Checkbutton(frame, text="AXH", command=self.doNothing)
        self.AXH1.pack(side=LEFT, padx=5, pady=5)
        self.AXH2 = Checkbutton(frame, text="AXH", command=self.doNothing)
        self.AXH2.pack(side=LEFT, padx=5, pady=5)
        self.printButt = Button(frame, text="Print", command=self.doNothing)
        self.printButt.pack(side=RIGHT, padx=2, pady=2)
        self.AXH3 = Checkbutton(frame, text="AXH", command=self.doNothing)
        self.AXH3.pack(side=LEFT, padx=5, pady=5)
        self.AXH4 = Checkbutton(frame, text="AXH", command=self.doNothing)
        self.AXH4.pack(side=LEFT, padx=5, pady=5)
        self.printButt2 = Button(frame, text="Print", command=self.doNothing)
        self.printButt2.pack(side=RIGHT, padx=2, pady=2)
        #self.printButton = Button(frame, text="Print message", command=self.printMessage)
        #self.printButton.pack(side=LEFT, padx=5, pady=5)



#************************ Status Bar *******************************

        self.status = Label(master, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)


    def printMessage(self):
        print("Wow, this atcually worked!")



    def doNothing(self):
        print("Ok ok...")


    def file_save(self):
        name=fd.asksaveasfile(mode='w',defaultextension=".txt")
        if name is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text2save=str(fd.text.get(1.0,END))
        name.write(text2save)
        name.close()

    def openfn(self):
        filename = fd.askopenfilename(title='open')
        return filename
    def image_open(self):
        x = self.openfn()
        img = Image.open(x)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(root, image=img)
        panel.image = img
        panel.pack()




root = Tk()
root.title("Something to try on...")

start = Project(root)
root.mainloop()