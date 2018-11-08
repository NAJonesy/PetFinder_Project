from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CreateAccountGUI import *
from loginGUI import *
import sys

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    main = Login()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()