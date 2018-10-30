from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import sys

# -------------- Setup -------------------- #
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()

# ------------- Header ----------------- #
header = QLabel('PetFinder API\n')
header.setAlignment(Qt.AlignCenter)
#header.setFont()
#header.setStyle(QLabel.labeltext, Qt.bold)
#header.textFormat("font:12pt;")

layout.addWidget(header)

layout.addWidget(QLabel('Find your best friend today!'))

# -------------- ListBox -------------- #
listbox = QListWidget()
listbox.addItem("Test")
listbox.addItem("Test...1...2")
layout.addWidget(listbox)




# --------------- Status Bar ----------- #


# ------------ closing --------------- #
window.setLayout(layout)
window.show()
app.exec_()


# 
# Special thanks to Michael Herrmann
# https://build-system.fman.io/pyqt5-tutorial