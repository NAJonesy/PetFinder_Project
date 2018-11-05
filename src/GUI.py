from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DBcalls import *
from APIcalls import *
import sys

# -------------- Setup -------------------- #
api = API()
db = DataBase()
favorites = list()
pets = list()
shelters = list()


app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
window.setWindowTitle('Pet Finder API')
layout = QVBoxLayout()
layout2 = QGridLayout()

# ------------- Header ----------------- #
header = QLabel('PetFinder API')
header.setAlignment(Qt.AlignCenter)
header.setFont(QFont("Arial",24))
layout.addWidget(header)
layout2.addWidget(header, 1,4)

slogan = QLabel('Find your best friend today!')
slogan.setAlignment(Qt.AlignCenter)
layout.addWidget(slogan)
layout2.addWidget(slogan,2,4)

# -------------- ListBox -------------- #
listbox = QListWidget()
listbox.addItem("Press buttons to populate table.")
layout.addWidget(listbox)
layout2.addWidget(listbox,3,1,5,3)


# --------------- Buttons -------------- #
button1 = QPushButton('Hi')
def changeListBox():
    listbox.addItem("Hey")
    return

button1.clicked.connect(lambda: changeListBox())
layout.addWidget(button1)

clearBtn = QPushButton('Clear List')
def clearListBox():
    listbox.clear()
    return
clearBtn.clicked.connect(lambda: clearListBox())
layout.addWidget(clearBtn)
layout2.addWidget(clearBtn,3,5)


getRandomBtn = QPushButton('Random Pet')
def getRandomPet():
    pet = api.getRandomPet()
    listbox.addItem(pet,pet.name)#.setData(pet)
    favorites.append(pet)
    return
getRandomBtn.clicked.connect(lambda: getRandomPet())
layout.addWidget(getRandomBtn)
layout2.addWidget(getRandomBtn,4,4)

showFavesBtn = QPushButton('Show Favorites')
def ListFavorites():
    clearListBox()
    if favorites != list():       
        for fave in favorites:
            listbox.addItem(fave.name)
    else:
        listbox.addItem("No favorites added yet.")   
    return
showFavesBtn.clicked.connect(lambda: ListFavorites())
layout.addWidget(showFavesBtn)
layout2.addWidget(showFavesBtn,5,4)

addToFavesBtn = QPushButton('Add pet to favorites.')
def addPetToFavorites():
    favorites.append(listbox.currentItem())
    return
addToFavesBtn.clicked.connect(lambda: addPetToFavorites())
layout.addWidget(addToFavesBtn)
layout2.addWidget(addToFavesBtn,6,4)

# --------------- Entries -------------- #
entry1 = QLineEdit()
layout.addWidget(entry1)
layout2.addWidget(entry1, 3,4)


# --------------- Check Boxes ------------ #
checkboxDog = QCheckBox('Dog')
layout.addWidget(checkboxDog)

# --------------- Image ----------------- #
image = QLabel()
image.setPixmap(QPixmap("http://photos.petfinder.com/photos/pets/43080876/1/?bust=1540483928&width=60&-pnt.jpg"))
image.setAlignment(Qt.AlignRight)
layout.addWidget(image)
layout2.addWidget(image, 3,6)

# --------------- Status Bar ----------- #
status = QStatusBar()
statusLabel = QLabel('Powered by Petfinder.com')
status.addWidget(statusLabel)
layout.addWidget(status)
layout2.addWidget(status,8,8,1,8)

# ------------ Closing --------------- #
window.setLayout(layout)
window.show()
app.exec_()


# ----------------- Functions ------------ #

def changeListBox():
    listbox.addItem("Hey")

# 
# Special thanks to Michael Herrmann
# https://build-system.fman.io/pyqt5-tutorial