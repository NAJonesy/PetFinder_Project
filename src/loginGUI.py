from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DBcalls import *
from APIcalls import *
import sys


# -------- Setup --------- #
db = DataBase()
app = QApplication([])
app.setStyle('Fusion')
loginWindow = QWidget()
loginWindow.setWindowTitle('Login to Pet Finder API')
loginLayout = QVBoxLayout()

# ----------- Header ---------- #
header = QLabel("Login")
header.setFont(QFont("Arial",20))
loginLayout.addWidget(header)

# ----------- Username --------- #


# ------------ Password --------- #


# ------------ Buttons ---------- #
createAccBtn = QPushButton('Create new account')
def loadCreateAccount():
    window.setLayout(createAccountLayout)
createAccBtn.clicked.connect(lambda: loadCreateAccount())
loginLayout.addWidget(createAccBtn)

# ----------- Guest Link ------------ #





# ---------------------- Create Account Layout ----------------- #
createAccWindow = QWidget()
createAccWindow.setWindowTitle("Account creation")
createAccountLayout = QGridLayout()

caHeader = QLabel('Create an account')
caHeader.setAlignment(Qt.AlignCenter)
createAccountLayout.addWidget(caHeader,1,1,1,2)

caName = QLabel('Name:')
caName.setAlignment(Qt.AlignRight)
caEmail = QLabel('Email:')
caEmail.setAlignment(Qt.AlignRight)
caUsername = QLabel("Username:")
caUsername.setAlignment(Qt.AlignRight)
caPassword = QLabel("Password:")
caPassword.setAlignment(Qt.AlignRight)
caConfirm = QLabel('Confirm Password:')
caConfirm.setAlignment(Qt.AlignRight)

entryCaName = QLineEdit()
entryCaEmail = QLineEdit()
entryCaUsername = QLineEdit()
entryCaPassword = QLineEdit()
entryCaConfirm = QLineEdit()

createAccountLayout.addWidget(caName,2,1)
createAccountLayout.addWidget(entryCaName,2,2)

createAccountLayout.addWidget(caEmail,3,1)
createAccountLayout.addWidget(entryCaEmail,3,2)

createAccountLayout.addWidget(caUsername,4,1)
createAccountLayout.addWidget(entryCaUsername,4,2)

createAccountLayout.addWidget(caPassword,5,1)
createAccountLayout.addWidget(entryCaPassword,5,2)

createAccountLayout.addWidget(caConfirm,6,1)
createAccountLayout.addWidget(entryCaConfirm,6,2)

caCreateBtn = QPushButton("Create Account")
def createAccount():
    pass
caCreateBtn.clicked.connect(lambda: createAccount())

caClearBtn = QPushButton('Clear Info')
def clearEntries():
    entryCaName.clear()
    entryCaEmail.clear()
    entryCaUsername.clear()
    entryCaPassword.clear()
    entryCaConfirm.clear()

caClearBtn.clicked.connect(lambda: clearEntries())

createAccountLayout.addWidget(caCreateBtn,8,2)
createAccountLayout.addWidget(caClearBtn,8,1)
# ------------ Closing --------------- #
window.setLayout(loginLayout)
#window.setLayout(createAccountLayout)
window.show()
app.exec_()