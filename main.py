from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import Qt

class MyGUI(QMainWindow):
    fileName = ""
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("./UI/splash-screen/form.ui",self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.show()

        # event handlers
        # self.btnBrowse.clicked.connect(self.get_file_location)

        



def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

if __name__ == '__main__':
    main()