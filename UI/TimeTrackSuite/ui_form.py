# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_TTS(object):
    def setupUi(self, TTS):
        if not TTS.objectName():
            TTS.setObjectName(u"TTS")
        TTS.setEnabled(True)
        TTS.resize(1215, 699)
        self.MainStack = QStackedWidget(TTS)
        self.MainStack.setObjectName(u"MainStack")
        self.MainStack.setGeometry(QRect(0, 0, 1211, 691))
        self.ImportPage = QWidget()
        self.ImportPage.setObjectName(u"ImportPage")
        self.label = QLabel(self.ImportPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 40, 211, 71))
        font = QFont()
        font.setFamilies([u"Cascadia Mono"])
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label_3 = QLabel(self.ImportPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 177, 311, 51))
        font1 = QFont()
        font1.setFamilies([u"Cascadia Code"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.txtMovieLocation = QLineEdit(self.ImportPage)
        self.txtMovieLocation.setObjectName(u"txtMovieLocation")
        self.txtMovieLocation.setGeometry(QRect(110, 247, 361, 31))
        font2 = QFont()
        font2.setFamilies([u"Cascadia Code"])
        font2.setPointSize(10)
        self.txtMovieLocation.setFont(font2)
        self.line = QFrame(self.ImportPage)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(24, 670, 1162, 20))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line_2 = QFrame(self.ImportPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 20, 31, 661))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_3 = QFrame(self.ImportPage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(1170, 20, 31, 661))
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_4 = QFrame(self.ImportPage)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(24, 10, 1162, 20))
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.btMovieBrowse = QPushButton(self.ImportPage)
        self.btMovieBrowse.setObjectName(u"btMovieBrowse")
        self.btMovieBrowse.setGeometry(QRect(480, 247, 101, 31))
        font3 = QFont()
        font3.setFamilies([u"Cascadia Code"])
        font3.setPointSize(16)
        self.btMovieBrowse.setFont(font3)
        self.chkbxMovies = QCheckBox(self.ImportPage)
        self.chkbxMovies.setObjectName(u"chkbxMovies")
        self.chkbxMovies.setGeometry(QRect(80, 190, 31, 26))
        self.label_4 = QLabel(self.ImportPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 225, 121, 21))
        font4 = QFont()
        font4.setFamilies([u"Cascadia Code"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_4.setFont(font4)
        self.label_5 = QLabel(self.ImportPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 314, 101, 51))
        self.label_5.setFont(font1)
        self.btnAnimeBrowse = QPushButton(self.ImportPage)
        self.btnAnimeBrowse.setObjectName(u"btnAnimeBrowse")
        self.btnAnimeBrowse.setGeometry(QRect(480, 384, 101, 31))
        self.btnAnimeBrowse.setFont(font3)
        self.txtAnimeLocation = QLineEdit(self.ImportPage)
        self.txtAnimeLocation.setObjectName(u"txtAnimeLocation")
        self.txtAnimeLocation.setGeometry(QRect(110, 384, 361, 31))
        self.txtAnimeLocation.setFont(font2)
        self.label_6 = QLabel(self.ImportPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 362, 121, 21))
        self.label_6.setFont(font4)
        self.chkbxAnime = QCheckBox(self.ImportPage)
        self.chkbxAnime.setObjectName(u"chkbxAnime")
        self.chkbxAnime.setGeometry(QRect(80, 327, 31, 26))
        self.txtCodingLocation = QLineEdit(self.ImportPage)
        self.txtCodingLocation.setObjectName(u"txtCodingLocation")
        self.txtCodingLocation.setGeometry(QRect(110, 527, 361, 31))
        self.txtCodingLocation.setFont(font2)
        self.chkbxCoding = QCheckBox(self.ImportPage)
        self.chkbxCoding.setObjectName(u"chkbxCoding")
        self.chkbxCoding.setGeometry(QRect(80, 470, 31, 26))
        self.label_7 = QLabel(self.ImportPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 457, 121, 51))
        self.label_7.setFont(font1)
        self.btnCodingBrowse = QPushButton(self.ImportPage)
        self.btnCodingBrowse.setObjectName(u"btnCodingBrowse")
        self.btnCodingBrowse.setGeometry(QRect(480, 527, 101, 31))
        self.btnCodingBrowse.setFont(font3)
        self.label_8 = QLabel(self.ImportPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 505, 121, 21))
        self.label_8.setFont(font4)
        self.line_5 = QFrame(self.ImportPage)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(640, 150, 31, 461))
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(5)
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.txtLogLocation = QLineEdit(self.ImportPage)
        self.txtLogLocation.setObjectName(u"txtLogLocation")
        self.txtLogLocation.setGeometry(QRect(750, 422, 361, 31))
        self.txtLogLocation.setFont(font2)
        self.chkbxLog = QCheckBox(self.ImportPage)
        self.chkbxLog.setObjectName(u"chkbxLog")
        self.chkbxLog.setGeometry(QRect(720, 365, 31, 26))
        self.label_9 = QLabel(self.ImportPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(750, 352, 231, 51))
        self.label_9.setFont(font1)
        self.btnLogBrowse = QPushButton(self.ImportPage)
        self.btnLogBrowse.setObjectName(u"btnLogBrowse")
        self.btnLogBrowse.setGeometry(QRect(1010, 460, 101, 31))
        self.btnLogBrowse.setFont(font3)
        self.label_10 = QLabel(self.ImportPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(750, 400, 121, 21))
        self.label_10.setFont(font4)
        self.btnImport = QPushButton(self.ImportPage)
        self.btnImport.setObjectName(u"btnImport")
        self.btnImport.setGeometry(QRect(1020, 610, 131, 51))
        font5 = QFont()
        font5.setFamilies([u"Cascadia Code"])
        font5.setPointSize(18)
        font5.setBold(True)
        self.btnImport.setFont(font5)
        self.label_11 = QLabel(self.ImportPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(700, 200, 491, 111))
        font6 = QFont()
        font6.setFamilies([u"Cascadia Code"])
        self.label_11.setFont(font6)
        self.pushButton = QPushButton(self.ImportPage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 193, 31, 21))
        icon = QIcon()
        icon.addFile(u"src/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setFlat(True)
        self.pushButton_2 = QPushButton(self.ImportPage)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 330, 31, 21))
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setFlat(True)
        self.pushButton_3 = QPushButton(self.ImportPage)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(210, 474, 31, 21))
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setFlat(True)
        self.MainStack.addWidget(self.ImportPage)
        self.OperationsPage = QWidget()
        self.OperationsPage.setObjectName(u"OperationsPage")
        self.label_2 = QLabel(self.OperationsPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 260, 261, 111))
        font7 = QFont()
        font7.setPointSize(18)
        font7.setBold(True)
        self.label_2.setFont(font7)
        self.MainStack.addWidget(self.OperationsPage)

        self.retranslateUi(TTS)

        self.MainStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TTS)
    # setupUi

    def retranslateUi(self, TTS):
        TTS.setWindowTitle(QCoreApplication.translate("TTS", u"TTS", None))
        self.label.setText(QCoreApplication.translate("TTS", u"Import", None))
        self.label_3.setText(QCoreApplication.translate("TTS", u"Movies/TV Series", None))
        self.btMovieBrowse.setText(QCoreApplication.translate("TTS", u"Browse", None))
        self.chkbxMovies.setText("")
        self.label_4.setText(QCoreApplication.translate("TTS", u"Location:", None))
        self.label_5.setText(QCoreApplication.translate("TTS", u"Anime", None))
        self.btnAnimeBrowse.setText(QCoreApplication.translate("TTS", u"Browse", None))
        self.label_6.setText(QCoreApplication.translate("TTS", u"Location:", None))
        self.chkbxAnime.setText("")
        self.chkbxCoding.setText("")
        self.label_7.setText(QCoreApplication.translate("TTS", u"Coding", None))
        self.btnCodingBrowse.setText(QCoreApplication.translate("TTS", u"Browse", None))
        self.label_8.setText(QCoreApplication.translate("TTS", u"Location:", None))
        self.chkbxLog.setText("")
        self.label_9.setText(QCoreApplication.translate("TTS", u"Previous Log", None))
        self.btnLogBrowse.setText(QCoreApplication.translate("TTS", u"Browse", None))
        self.label_10.setText(QCoreApplication.translate("TTS", u"Location:", None))
        self.btnImport.setText(QCoreApplication.translate("TTS", u"Import", None))
        self.label_11.setText(QCoreApplication.translate("TTS", u"What is previous log ? \n"
"If you have run this software before, the log file \n"
"exported by the software is the previous log,\n"
"You can use this log \n"
"file to import the previously calculated \n"
"data in order to save time.", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_2.setText(QCoreApplication.translate("TTS", u"Page 2", None))
    # retranslateUi

