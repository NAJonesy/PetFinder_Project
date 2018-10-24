try:
    from Tkinter import *    
except ImportError:
    from tkinter import *  

root = Tk()
root.geometry('800x800+500+300')
root.title('PetFinder')


headerLabel = Label(root,text="Find your new best friend today!")
headerLabel.config(font=("Courier",30))
headerLabel.pack(ipady = 1)

topFrame = Frame(root,height=2).pack(fill=X)
bottomFrame = Frame(root,bg='#D1D0F8').pack(side=BOTTOM)

mainListBox = Listbox(topFrame, height= 2)
scrollbar = Scrollbar(topFrame, orient=VERTICAL)
mainListBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=mainListBox.yview)
scrollbar.pack(side=RIGHT)
mainListBox.insert(1,"Test")
mainListBox.insert(2,"looks")
mainListBox.insert(3,"good")
mainListBox.pack(fill=X)
myButton = Button(bottomFrame,text="submit").pack() #command = addListItem(mainListBox)).pack()

testlabel = Label(bottomFrame,text="Hey there",bg="red",fg="black").pack(fill = BOTH)

nameEntry = Entry(root, state="readonly").pack()


footer = Label(bottomFrame,text="This application is powered by Petfinder.com",bd=1,relief=SUNKEN,anchor=W).pack(side=BOTTOM,fill=X)


root.mainloop()

def do_something():
    pass

