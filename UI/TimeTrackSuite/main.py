from PyQt6.QtWidgets import *
from PyQt6 import uic

class MyGUI(QMainWindow):
    fileName = ""
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("form.ui",self)
        self.show()

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

if __name__ == '__main__':
    main()