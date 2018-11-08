from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DBcalls import *
from APIcalls import *
from GUI import GUI
import sys

class CreateAccount(QMainWindow):
    
    def __init__(self, parent=None):
        super(CreateAccount, self).__init__(parent)
# -------- Setup --------- #
        db = DataBase()
        #app = QApplication([sys.argv])
        #app.setStyle('Fusion')

# ------------ Layout --------------#
        self.createAccWindow = QWidget()
        self.createAccWindow.setWindowTitle("Account creation")
        self.createAccountLayout = QGridLayout()

# ------------ Meat and Potatoes ---------- #
        self.caHeader = QLabel('Create an account')
        self.caHeader.setAlignment(Qt.AlignCenter)
        self.createAccountLayout.addWidget(self.caHeader,1,1,1,2)

        self.caName = QLabel('Name:')
        self.caName.setAlignment(Qt.AlignRight)
        self.caEmail = QLabel('Email:')
        self.caEmail.setAlignment(Qt.AlignRight)
        self.caUsername = QLabel("Username:")
        self.caUsername.setAlignment(Qt.AlignRight)
        self.caPassword = QLabel("Password:")
        self.caPassword.setAlignment(Qt.AlignRight)
        self.caConfirm = QLabel('Confirm Password:')
        self.caConfirm.setAlignment(Qt.AlignRight)

        self.entryCaName = QLineEdit()
        self.entryCaEmail = QLineEdit()
        self.entryCaUsername = QLineEdit()
        self.entryCaPassword = QLineEdit()
        self.entryCaConfirm = QLineEdit()

        self.createAccountLayout.addWidget(self.caName,2,1)
        self.createAccountLayout.addWidget(self.entryCaName,2,2)

        self.createAccountLayout.addWidget(self.caEmail,3,1)
        self.createAccountLayout.addWidget(self.entryCaEmail,3,2)

        self.createAccountLayout.addWidget(self.caUsername,4,1)
        self.createAccountLayout.addWidget(self.entryCaUsername,4,2)

        self.createAccountLayout.addWidget(self.caPassword,5,1)
        self.createAccountLayout.addWidget(self.entryCaPassword,5,2)

        self.createAccountLayout.addWidget(self.caConfirm,6,1)
        self.createAccountLayout.addWidget(self.entryCaConfirm,6,2)

# --------------- Account creation -------------- #
        self.caCreateBtn = QPushButton("Create Account")
        def createAccount(self):
            if self.entryCaPassword.text() == self.entryCaConfirm.text():
                name = self.entryCaName.text()
                username = self.entryCaUsername.text()
                password = self.entryCaPassword.text() 
                email = self.entryCaEmail.text()
                created = db.addUser(username,password,email,name)
                if created:
                    msg = QMessageBox()
                    msg.setText("Your account has been created.")
                    msg.setInformativeText("You can now store your favorite pets to your account!")
                    msg.setWindowTitle("Welcome!")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    self.createAccWindow.close()
                    GUI(user = username)
                else:
                    print("Created = false")
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Account creation error.")
                    
                    dupUsername = False
                    dupEmail = False
                    ##check if username or email is dup.
                    if dupUsername and dupEmail:
                        msg.setInformativeText("This account already exists!")
                    elif dupUsername:
                        msg.setInformativeText("Account with this username already exists!")
                    elif dupEmail:
                        msg.setInformativeText("This email is already associated with an account.")
                    msg.setWindowTitle("Account creation error.")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    #error message and retry
                    #an account with that username or email...
                    pass
            else:
                #error message 
                #passwords dont match please try again
                # clear both password fields
                pass
            pass
        self.caCreateBtn.clicked.connect(lambda: createAccount(self))

# ---------------- Clear Data ------------------- #
        self.caClearBtn = QPushButton('Clear Info')
        def clearEntries(self):
            self.entryCaName.clear()
            self.entryCaEmail.clear()
            self.entryCaUsername.clear()
            self.entryCaPassword.clear()
            self.entryCaConfirm.clear()

        self.caClearBtn.clicked.connect(lambda: clearEntries(self))

        self.createAccountLayout.addWidget(self.caCreateBtn,8,2)
        self.createAccountLayout.addWidget(self.caClearBtn,8,1)

# ----------- Closing ------------- #
        self.createAccWindow.setLayout(self.createAccountLayout)
        self.createAccWindow.show()
        #app.exec_()