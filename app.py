# imports all Qt widgets
from PyQt6.QtWidgets import *
import sys #command line arguments

app = QApplication(sys.argv) #declare applicatation

#Xreate the widget and then show
window = QWidget()
window.setWindowTitle("Paul's Note App")
window.resize(400, 300) #set the size of the window 

notes =  QTextEdit(window) #create a text edit widget
notes.setGeometry(10, 10, 380, 280) #set the size and position of the text edit widget
#distance from the left, distance from the top, width, height

clear_button = QPushButton("Clear", window) #create a button widget
clear_button.setGeometry(10, 300, 80, 30) #set the
clear_button.clicked.connect(notes.clear) #connect the button to the clear function

copy_button = QPushButton("Copy", window) #create a button widget
copy_button.setGeometry(100, 300, 80, 30) #set the geometry of the button
copy_button.clicked.connect(notes.copy) #connect the button to the copy function

paste_button = QPushButton("Paste", window) #create a button widget
paste_button.setGeometry(190, 300, 80, 30) #set the geometry of the button
paste_button.clicked.connect(notes.paste) #connect the button to the paste function

window.show() 

#Execeute
sys.exit(app.exec())

