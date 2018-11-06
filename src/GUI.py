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

class GUI(QMainWindow):
    def __init__(self,parent=None):
        super(GUI, self).__init__(parent)
        self.window = QWidget()
        self.window.setWindowTitle('Pet Finder API')
        self.layout = QGridLayout()

# ------------- Header ----------------- #
        self.header = QLabel('PetFinder API')
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setFont(QFont("Arial",24))
        self.layout.addWidget(self.header, 1,4)

        self.slogan = QLabel('Find your best friend today!')
        self.slogan.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.slogan,2,4)

# -------------- ListBox -------------- #
        self.listbox = QListWidget()
        self.listbox.addItem("Press buttons to populate table.")
        self.layout.addWidget(self.listbox,3,1,5,3)


# --------------- Buttons -------------- #
        self.button1 = QPushButton('Hi')
        def changeListBox():
            self.listbox.addItem("Hey")
            return

        self.button1.clicked.connect(lambda: changeListBox())
        self.layout.addWidget(self.button1)

        self.clearBtn = QPushButton('Clear List')
        def clearListBox():
            self.listbox.clear()
            return
        self.clearBtn.clicked.connect(lambda: clearListBox())
        self.layout.addWidget(self.clearBtn,3,5)


        self.getRandomBtn = QPushButton('Random Pet')
        def getRandomPet():
            pet = api.getRandomPet()
            self.listbox.addItem(pet,pet.name)#.setData(pet)
            favorites.append(pet)
            return
        self.getRandomBtn.clicked.connect(lambda: getRandomPet())
        self.layout.addWidget(self.getRandomBtn,4,4)

        self.showFavesBtn = QPushButton('Show Favorites')
        def ListFavorites():
            clearListBox()
            if favorites != list():       
                for fave in favorites:
                    self.listbox.addItem(fave.name)
            else:
                self.listbox.addItem("No favorites added yet.")   
            return
        self.showFavesBtn.clicked.connect(lambda: ListFavorites())
        self.layout.addWidget(self.showFavesBtn,5,4)

        self.addToFavesBtn = QPushButton('Add pet to favorites.')
        def addPetToFavorites():
            favorites.append(self.listbox.currentItem())
            return
        self.addToFavesBtn.clicked.connect(lambda: addPetToFavorites())
        self.layout.addWidget(self.addToFavesBtn,6,4)

# --------------- Entries -------------- #
        self.entry1 = QLineEdit()
        self.layout.addWidget(self.entry1, 3,4)


# --------------- Check Boxes ------------ #
        self.checkboxDog = QCheckBox('Dog')
        self.layout.addWidget(self.checkboxDog)

# --------------- Image ----------------- #
        self.image = QLabel()
        self.image.setPixmap(QPixmap("http://photos.petfinder.com/photos/pets/43080876/1/?bust=1540483928&width=60&-pnt.jpg"))
        self.image.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.image, 3,6)

# --------------- Status Bar ----------- #
        self.status = QStatusBar()
        self.statusLabel = QLabel('Powered by Petfinder.com')
        self.status.addWidget(self.statusLabel)
        self.layout.addWidget(self.status,8,8,1,8)

# ------------ Closing --------------- #
        self.window.setLayout(self.layout)
        #elf.setCentralWidget(self.window)
        self.window.show()
        #app.exec_()


# ----------------- Functions ------------ #

        def changeListBox():
            listbox.addItem("Hey")

# 
# Special thanks to Michael Herrmann
# https://build-system.fman.io/pyqt5-tutorial