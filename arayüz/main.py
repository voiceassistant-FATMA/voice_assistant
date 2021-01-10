import sys
from PyQt5 import QtCore 
from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QPushButton,QListWidget,QListWidgetItem 
from PyQt5.QtGui import QFont, QIcon

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Fatma'
        self.left = 50
        self.top = 50
        self.width = 480
        self.height = 640
        
        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.initUI()
        self.setFixedSize(480, 640)
        self.setStyleSheet("background-color: #292929; color:white;")


        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox1 = QtWidgets.QLineEdit(self)
        self.textbox1.move(20,580)
        self.textbox1.resize(370,40)

        self.textbox2 = QtWidgets.QLineEdit(self)
        self.textbox2.move(20,60)
        self.textbox2.resize(440,500)

       

        self.label1 = QtWidgets.QLabel("Fatma",self)
        self.label1.move(200,20)
        self.label1.setFont(QFont("Arial",16))
        self.button = QtWidgets.QPushButton("Push",self)
        self.button.setGeometry(400,580,60,40)

       
        
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())