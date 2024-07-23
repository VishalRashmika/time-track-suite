from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QSplashScreen
from PyQt6 import uic
from PyQt6.QtCore import Qt
import time
import sys

class SplashScreen(QMainWindow):
    def __init__(self):
        super(SplashScreen,self).__init__()
        uic.loadUi("./UI/SplashScreen.ui",self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

    def progress(self):
        for i in range(100):
            time.sleep(0.1)
            self.progressBar.setValue(i)
        # event handlers
        # self.btnBrowse.clicked.connect(self.get_file_location)

class ImportScreen(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        uic.loadUi("./UI/ImportScreen.ui")



# def main():
#     app = QApplication([])
#     window = MyGUI()
#     app.exec()

if __name__ == '__main__':
    # main()
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()
    splash.progress()
    splash.close()

    import_page = ImportScreen()
    import_page.show()

    

    # splash.en

    app.exec()


# https://github.com/Wanderson-Magalhaes/Splash_Screen_Python_PySide2