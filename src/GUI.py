from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DBcalls import *
from APIcalls import *
#from loginGUI import Login
#from MainGUI import main
import sys

# -------------- Setup -------------------- #
api = API()
db = DataBase()
favorites = list()
pets = list()
shelters = list()

class GUI(QMainWindow):
    def __init__(self,parent=None,user = ''):
        super(GUI, self).__init__(parent)
        
        api = API()
        db = DataBase()
        favorites = list()
        pets = list()
        shelters = list()
        
        self.window = QWidget()
        self.window.setWindowTitle('Pet Finder API')
        #self.window.setIcon(QIcon('/images/paw_print.png'))
        self.layout = QGridLayout()
        
        if(user != 'guest' and user != ''):
            favorites = db.getFavorites(user)

# ------------- Header ----------------- #
        self.header = QLabel('PetFinder API')
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setFont(QFont("Arial",24))
        self.layout.addWidget(self.header, 1,2)

        self.slogan = QLabel('Find your best friend today!')
        self.slogan.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.slogan,2,2)

# -------------- ListBox -------------- #
        self.listbox = QListWidget()
        self.listbox.addItem("Press buttons to populate table.")
        def listboxPet():
            name = self.listbox.currentItem().text()
            for pet in pets:
                if pet.name == name:
                    selectedPet = pet
            changePetEntries(selectedPet)
        self.listbox.itemClicked.connect(lambda: listboxPet())
        self.layout.addWidget(self.listbox,3,1,8,2)

# -------------- Pet Labels ---------- #
        self.petNameLabel = QLabel("Name:")
        self.petNameLabel.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.petNameLabel,3,3)
        self.petAgeLabel = QLabel("Age:")
        self.petAgeLabel.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.petAgeLabel,4,3)
        self.petAnimalLabel = QLabel("Animal:")
        self.petAnimalLabel.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.petAnimalLabel,5,3)
        self.petDescriptionLabel = QLabel("Description:")
        self.petDescriptionLabel.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.petDescriptionLabel,11,1)
        self.petMixLabel = QLabel("Mix:")
        self.petMixLabel.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.petMixLabel,6,3)
        self.petSexLabel = QLabel("Sex:")
        self.petSexLabel.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.petSexLabel,7,3)
        self.petSizeLabel = QLabel("Size:")
        self.petSizeLabel.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.petSizeLabel,8,3)
        self.petBreedsLabel = QLabel("Breeds:")      
        self.petBreedsLabel.setAlignment(Qt.AlignRight)  
        self.layout.addWidget(self.petBreedsLabel,9,3)

        #self.petMediaLabel = QLabel(QPIXMAP)


# ------------------ Pet Entries ------------ #

        self.petNameEntry = QLineEdit()
        self.petNameEntry.setReadOnly(True)
        self.layout.addWidget(self.petNameEntry,3,4)
        self.petAgeEntry = QLineEdit()
        self.petAgeEntry.setReadOnly(True)
        self.layout.addWidget(self.petAgeEntry,4,4)
        self.petAnimalEntry = QLineEdit()
        self.petAnimalEntry.setReadOnly(True)
        self.layout.addWidget(self.petAnimalEntry,5,4)
        
        
#         self.petDescriptionEntry = QLineEdit()
#         self.petDescriptionEntry.setReadOnly(True)
#         self.petDescriptionEntry.sizeHint()
#         self.layout.addWidget(self.petDescriptionEntry,11,2,3,3)
        
        
        self.petDescription2 = QTextEdit()
        self.petDescription2.setReadOnly(True)
        self.layout.addWidget(self.petDescription2,11,2,4,4)
        
        self.petMixEntry = QLineEdit()
        self.petMixEntry.setReadOnly(True)
        self.layout.addWidget(self.petMixEntry,6,4)
        self.petSexEntry = QLineEdit()
        self.petSexEntry.setReadOnly(True)
        self.layout.addWidget(self.petSexEntry,7,4)
        self.petSizeEntry = QLineEdit()
        self.petSizeEntry.setReadOnly(True)
        self.layout.addWidget(self.petSizeEntry,8,4)
        self.petBreedsEntry = QLineEdit()
        self.petBreedsEntry.setReadOnly(True)
        self.layout.addWidget(self.petBreedsEntry,9,4,1,2)


# -------------- Shelter Labels ------------- #
        self.shelterNameLabel = QLabel("Name:")
        self.shelterPhoneLabel = QLabel("Name:")
        self.shelterEmailLabel = QLabel("Name:")
        self.shelterAddressLabel = QLabel("Name:")
        self.shelterCityLabel = QLabel("Name:")
        self.shelterStateLabel = QLabel("Name:")
        self.shelterZipLabel = QLabel("Name:")
        self.shelterCountryLabel = QLabel("Name:")
        #self.shelterLatitudeLabel = QLabel("Name:")
        #self.shelterLongitudeLabel = QLabel("Name:")



# --------------- Buttons -------------- #
        self.loggingBtn = QPushButton()
        if user == 'guest':
            self.loggingBtn.setText('Login')
        else:
            self.loggingBtn.setText('Logout')
        def log():
            if self.loggingBtn.text() == 'Logout':
                self.window.close()
                sys.exit()
                #main()
            pass
        self.loggingBtn.clicked.connect(lambda: log())
        self.layout.addWidget(self.loggingBtn,1,5)
        
        self.addToFavesBtn = QPushButton('Add pet to favorites.')
        def addPetToFavorites():
            if user != 'guest':
                petName = self.listbox.currentItem()
                for pet in pets:
                    if pet.name == petName:
                        favorites.append(pet)
                        db.addFavorite(user,pet)
            else:
                pass
                #Error message box
            return
        self.addToFavesBtn.clicked.connect(lambda: addPetToFavorites())
        self.layout.addWidget(self.addToFavesBtn,14,2)

        self.clearBtn = QPushButton('Clear List')
        def clearListBox():
            self.listbox.clear()
            return
        self.clearBtn.clicked.connect(lambda: clearListBox())
        #self.layout.addWidget(self.clearBtn,3,5)


        self.getRandomBtn = QPushButton('Random Pet')
        def getRandomPet():
            clearPetEntries()
            pet = api.getRandomPet()
            db.addPet(pet)
            clearListBox()
            self.listbox.addItem(pet.name)
            self.listbox.setCurrentItem(self.listbox.itemAt(0,0))
            changePetEntries(pet)
            pets.append(pet)
            return
        self.getRandomBtn.clicked.connect(lambda: getRandomPet())
        self.layout.addWidget(self.getRandomBtn,26,3)

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
        self.layout.addWidget(self.showFavesBtn,14,3)

        
        self.findPetsBtn = QPushButton("Find Pets")
        def findPets():
            clearPetEntries()
            getOptions()
            #send options to API
            #get response
            pass
        self.findPetsBtn.clicked.connect(lambda: findPets())
        self.layout.addWidget(self.findPetsBtn, 26,2)
        



# --------------- Check Boxes ------------ #

        # ---------- animal checkboxes --------- #
        self.animalLabel = QLabel('Animal:')
        self.layout.addWidget(self.animalLabel,16,1)
        self.checkboxDog = QCheckBox('Dog')
        self.layout.addWidget(self.checkboxDog,16,2)
        self.checkboxCat = QCheckBox('Cat')
        self.layout.addWidget(self.checkboxCat,17,2)
        self.checkboxHorse = QCheckBox('Horse')
        self.layout.addWidget(self.checkboxHorse,16,3)
        self.checkboxReptile = QCheckBox('Reptile')
        self.layout.addWidget(self.checkboxReptile,17,3)
        self.checkboxBarnyard = QCheckBox('Barnyard')
        self.layout.addWidget(self.checkboxBarnyard,16,4)
        self.checkboxFurry = QCheckBox('Small Furry')
        self.layout.addWidget(self.checkboxFurry,17,4)
        
        self.animalCheckGroup = QButtonGroup()
        self.animalCheckGroup.addButton(self.checkboxDog)
        self.animalCheckGroup.addButton(self.checkboxCat)
        self.animalCheckGroup.addButton(self.checkboxHorse)
        self.animalCheckGroup.addButton(self.checkboxReptile)
        self.animalCheckGroup.addButton(self.checkboxBarnyard)
        self.animalCheckGroup.addButton(self.checkboxFurry)
        
        # --------- size checkboxes ------------ #
        self.sizeLabel = QLabel('Size:')
        self.layout.addWidget(self.sizeLabel,21,1)
        self.checkBoxSmall = QCheckBox('Small')
        self.layout.addWidget(self.checkBoxSmall,21,2)
        self.checkBoxMedium = QCheckBox('Medium')
        self.layout.addWidget(self.checkBoxMedium,21,3)
        self.checkBoxLarge = QCheckBox('Large')
        self.layout.addWidget(self.checkBoxLarge,21,4)
        self.checkBoxXL = QCheckBox('XL')
        self.layout.addWidget(self.checkBoxXL,21,5)
        
        self.sizeCheckGroup = QButtonGroup()
        self.sizeCheckGroup.addButton(self.checkBoxSmall)
        self.sizeCheckGroup.addButton(self.checkBoxMedium)
        self.sizeCheckGroup.addButton(self.checkBoxLarge)
        self.sizeCheckGroup.addButton(self.checkBoxXL)
        
        # ---------- sex checkboxes ------------- #
        self.sexLabel = QLabel('Sex:')
        self.layout.addWidget(self.sexLabel,23,1)
        self.checkBoxMale = QCheckBox('Male')
        self.layout.addWidget(self.checkBoxMale,23,2)
        self.checkBoxFemale = QCheckBox('Female')
        self.layout.addWidget(self.checkBoxFemale,23,3)
        
        self.sexCheckGroup = QButtonGroup()
        self.sexCheckGroup.addButton(self.checkBoxMale)
        self.sexCheckGroup.addButton(self.checkBoxFemale)
        
        
        # ----------- age checkboxes ------------ #
        self.ageLabel = QLabel('Age:')
        self.layout.addWidget(self.ageLabel,19,1)
        self.checkBoxBaby = QCheckBox('Baby')
        self.layout.addWidget(self.checkBoxBaby,19,2)
        self.checkBoxYoung = QCheckBox('Young')
        self.layout.addWidget(self.checkBoxYoung,19,3)
        self.checkBoxAdult = QCheckBox('Adult')
        self.layout.addWidget(self.checkBoxAdult,19,4)
        self.checkBoxSenior = QCheckBox('Senior')
        self.layout.addWidget(self.checkBoxSenior,19,5)
        
        self.ageCheckGroup = QButtonGroup()
        self.ageCheckGroup.addButton(self.checkBoxAdult)
        self.ageCheckGroup.addButton(self.checkBoxBaby)
        self.ageCheckGroup.addButton(self.checkBoxYoung)
        self.ageCheckGroup.addButton(self.checkBoxSenior)
# --------------- Image ----------------- #
        self.image = QLabel()
        self.pic = QPixmap('/images/print.jpg')#"http://photos.petfinder.com/photos/pets/43080876/1/?bust=1540483928&width=60&-pnt.jpg")
        self.image.setPixmap(self.pic)
        #self.image.setAlignment(Qt.AlignRight)
        self.image.setGeometry(QRect(200,200,200,200))
        self.layout.addWidget(self.image, 3,6,6,2)
        
# -------------- Searching -----------------#
        self.searchingLabel = QLabel("Search ------------------------------------------------------------------------------")
        self.layout.addWidget(self.searchingLabel,15,1,1,8)
        
                
        self.locationLabel = QLabel("Zip Code:")
        self.layout.addWidget(self.locationLabel,24,1)
        self.locationEntry = QLineEdit()
        self.locationEntry.setInputMask("99999")
        self.locationEntry.setPlaceholderText("80005")
        self.locationEntry.setCursorPosition(0)
        self.layout.addWidget(self.locationEntry,24,2)
        
        self.breedLabel = QLabel('Breed:')
        self.layout.addWidget(self.breedLabel,25,1)
        self.breedEntry = QLineEdit()
        self.layout.addWidget(self.breedEntry,25,2)
        
        
#         self.breedCombo = QComboBox()
#         def loadBreeds():
#             print('working')
#         self.breedCombo.activated(0).connect(lambda: loadBreeds())
#         self.layout.addWidget(self.breedCombo,25,2)
        
# --------------- Menu Bar -------------- #
#         self.menu = self.window.menuBar()
#         self.layout.addWidget(self.menu,1,1)

# --------------- Status Bar ----------- #
        self.status = QStatusBar()
        self.status.setMinimumSize(self.status.sizeHint())
        self.status.setStyleSheet('QStatusBar {width:100%;border:5px;}')
        self.statusLabel = QLabel()
        self.statusLabel.setText('''<a href='https://www.petfinder.com/'>Powered by Petfinder.com</a>''')
        self.statusLabel.setOpenExternalLinks(True)
        self.status.addWidget(self.statusLabel)
        #self.layout.addWidget(self.status)

# ------------ Closing --------------- #
        self.window.setLayout(self.layout)
        self.window.show()


# ----------------- Functions ------------ #

        def changePetEntries(pet):
            self.petAgeEntry.setText(pet.age)# = pet.age
            self.petAnimalEntry.setText(pet.animal)
            #self.petDescriptionEntry.setText(pet.description)
            self.petDescription2.setText(pet.description)
            self.petMixEntry.setText(pet.mix)
            self.petNameEntry.setText(pet.name)
            self.petSexEntry.setText(pet.sex)
            self.petSizeEntry.setText(pet.size)
            ##
            self.petBreedsEntry.setText(str(pet.breeds))
            ##
        
        def clearPetEntries():
            self.petAgeEntry.setText('')
            self.petAnimalEntry.setText('')
            #self.petDescriptionEntry.setText('')
            self.petDescription2.setText('')
            self.petMixEntry.setText('')
            self.petNameEntry.setText('')
            self.petSexEntry.setText('')
            self.petSizeEntry.setText('')
            self.petBreedsEntry.setText('')

        def getOptions():
            variables = {}
            
            # ----------- check location entry ------- #
            if self.locationEntry.text() != '':
                # verify info
                pass
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Search criteria error")
                msg.setInformativeText("A zip code is required to search for pets.")
                msg.setWindowTitle("Search error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
                
            # -------- check breed entry ----- #
            if self.breedEntry.text != '':
                #verify info
                pass
            
            # -------- check sex ---------#
            if self.checkBoxMale.isChecked() or self.checkBoxFemale.isChecked():
                if self.checkBoxMale.isChecked():
                    variables['sex'] = 'M'
                elif self.checkBoxFemale.isChecked():
                    variables['sex'] = 'F'
                else:
                    print("How did you end up here??")
                    
            # -------- check age -------- #
            
            # -------- check size -------- #
            
            print(variables)
            return variables
            
# 
# Special thanks to Michael Herrmann
# https://build-system.fman.io/pyqt5-tutorial