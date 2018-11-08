from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DBcalls import *
from APIcalls import *
from CreateAccountGUI import *
from GUI import GUI
import sys

class Login(QMainWindow):
    def __init__(self,parent=None):
        super(Login, self).__init__(parent)

# -------- Setup --------- #
        db = DataBase()

        self.loginWindow = QWidget()
        self.loginWindow.setWindowTitle('Login to Pet Finder API')
        self.loginWindow.setFixedSize(325,170)
        self.layout = QGridLayout(self.loginWindow) 

# ----------- Header ---------- #
        self.header = QLabel("Login")
        self.header.setFont(QFont("Arial",20))
        self.header.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.header,1,1,1,5)

# ----------- Username --------- #
        self.userLabel = QLabel("Username:")
        self.userLabel.setAlignment(Qt.AlignRight)
        self.userEntry = QLineEdit()
        self.layout.addWidget(self.userLabel,2,1)
        self.layout.addWidget(self.userEntry,2,2,1,2)


# ------------ Password --------- #
        self.passLabel = QLabel("Password:")
        self.passLabel.setAlignment(Qt.AlignRight)
        self.passEntry = QLineEdit()
        self.passEntry.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.passLabel,3,1)
        self.layout.addWidget(self.passEntry,3,2,1,2)
        self.passEntry.returnPressed.connect(lambda: login())


# ------------ Buttons ---------- #

        self.loginBtn = QPushButton('Login')
        def login():
            username = self.userEntry.text()
            password = self.passEntry.text()
            success = db.login(username,password)
            if success:
                self.loginWindow.close()
                GUI(user=username)
            else: 
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Login error")
                msg.setInformativeText("Username or password is incorrect.")
                msg.setWindowTitle("Login error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                self.passEntry.setText('')
        self.loginBtn.clicked.connect(lambda: login())
        self.layout.addWidget(self.loginBtn,4,2)
        
        self.createAccBtn = QPushButton('Create new account')
        def loadCreateAccount():
            self.loginWindow.close()
            creation = CreateAccount()
            
        self.createAccBtn.clicked.connect(lambda: loadCreateAccount())
        self.layout.addWidget(self.createAccBtn)

# ----------- Guest Link ------------ #
        self.guestLabel = QPushButton()
        self.guestLabel.setText('Continue as guest.')
        self.guestLabel.setFlat(True)
        self.guestLabel.setStyleSheet('QPushButton {color:blue}')
        def guestMain():
            self.loginWindow.close()
            GUI(user = 'guest')
        self.guestLabel.clicked.connect(lambda: guestMain())
        self.layout.addWidget(self.guestLabel,5,3)



# ------------ Closing --------------- #
        self.loginWindow.setLayout(self.layout)
        self.loginWindow.show()
