import sys
#from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Testing")
        self.setWindowIcon(QIcon('images/paw_print.png'))
        
        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = self.menuBar()
        #fileMenu.addAction()
        
def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
run()