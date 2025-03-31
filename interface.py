# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TELA NOVO CADASTRO,LOGIN ULTIMA VERSAO QT.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(843, 643)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 470, 211, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 70, 271, 61))
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(48)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-400, -830, 1291, 2001))
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setPixmap(QPixmap(u"fundo azul.jpg"))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(380, 70, 431, 431))
        self.stackedWidget.setStyleSheet(u"QWidge {\n"
"    background-color: rgba(245, 245, 245, 70);\n"
"    border-radius: 12px;\n"
"    border: 2px solid rgba(255, 255, 255, 150);\n"
"    backdrop-filter: blur(15px);\n"
"    padding: 5px;\n"
"}\n"
"QWidget {\n"
"    background-color: rgba(255, 255, 255, 20); /* 50 = 20% de opacidade */\n"
"    border-radius: 15px;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    \n"
"    /* Efeito de desfoque (requer c\u00f3digo adicional - ver explica\u00e7\u00e3o abaixo) */\n"
"    backdrop-filter: blur(10px);\n"
"}")
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.stackedWidget_loginPage1_3 = QWidget()
        self.stackedWidget_loginPage1_3.setObjectName(u"stackedWidget_loginPage1_3")
        self.label_5 = QLabel(self.stackedWidget_loginPage1_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-80, 0, 571, 51))
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(14)
        font1.setItalic(False)
        self.label_5.setFont(font1)
        self.label_user_3 = QLabel(self.stackedWidget_loginPage1_3)
        self.label_user_3.setObjectName(u"label_user_3")
        self.label_user_3.setGeometry(QRect(20, 90, 391, 71))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_user_3.setFont(font2)
        self.label_user_3.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"border:3\n"
"}")
        self.lineEdit_passwrd_3 = QLineEdit(self.stackedWidget_loginPage1_3)
        self.lineEdit_passwrd_3.setObjectName(u"lineEdit_passwrd_3")
        self.lineEdit_passwrd_3.setGeometry(QRect(80, 200, 301, 31))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setItalic(False)
        self.lineEdit_passwrd_3.setFont(font3)
        self.lineEdit_passwrd_3.setStyleSheet(u"QLineEdit {\n"
"    /* Borda e fundo */\n"
"    border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
"}")
        self.label_passwrd_3 = QLabel(self.stackedWidget_loginPage1_3)
        self.label_passwrd_3.setObjectName(u"label_passwrd_3")
        self.label_passwrd_3.setGeometry(QRect(20, 180, 391, 71))
        self.label_passwrd_3.setFont(font2)
        self.label_passwrd_3.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"border:3\n"
"}")
        self.bttn_login = QPushButton(self.stackedWidget_loginPage1_3)
        self.bttn_login.setObjectName(u"bttn_login")
        self.bttn_login.setGeometry(QRect(70, 310, 131, 31))
        self.bttn_login.setFont(font2)
        self.bttn_login.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.5);\n"
"    border: 2px solid rgba(255, 255, 255, 0.3); /* Borda branca transl\u00facida */\n"
"    color: #333333; /* Texto totalmente opaco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #CFD8DC;\n"
"    border-color: rgba(255, 255, 255,255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A0B2C8; /* Azul acinzentado */\n"
"border-color: #003366; /* Azul escuro */\n"
"}\n"
" QPushButton{border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QPushButton {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
""
                        "}")
        self.bttn_alterindex_2 = QPushButton(self.stackedWidget_loginPage1_3)
        self.bttn_alterindex_2.setObjectName(u"bttn_alterindex_2")
        self.bttn_alterindex_2.setGeometry(QRect(230, 310, 131, 31))
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(False)
        self.bttn_alterindex_2.setFont(font4)
        self.bttn_alterindex_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.5);\n"
"    border: 2px solid rgba(255, 255, 255, 0.3); /* Borda branca transl\u00facida */\n"
"    color: #333333; /* Texto totalmente opaco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #CFD8DC;\n"
"    border-color: rgba(255, 255, 255,255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A0B2C8; /* Azul acinzentado */\n"
"border-color: #003366; /* Azul escuro */\n"
"}\n"
" QPushButton{border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QPushButton {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
""
                        "}")
        self.lineEdit_user_2 = QLineEdit(self.stackedWidget_loginPage1_3)
        self.lineEdit_user_2.setObjectName(u"lineEdit_user_2")
        self.lineEdit_user_2.setGeometry(QRect(80, 110, 301, 31))
        self.lineEdit_user_2.setFont(font3)
        self.lineEdit_user_2.setStyleSheet(u"QLineEdit {\n"
"    /* Borda e fundo */\n"
"    border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
"}")
        self.stackedWidget.addWidget(self.stackedWidget_loginPage1_3)
        self.label_user_3.raise_()
        self.label_passwrd_3.raise_()
        self.label_5.raise_()
        self.lineEdit_passwrd_3.raise_()
        self.bttn_login.raise_()
        self.bttn_alterindex_2.raise_()
        self.lineEdit_user_2.raise_()
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.lineEdit_email = QLineEdit(self.page_3)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(70, 210, 321, 30))
        self.lineEdit_email.setFont(font3)
        self.lineEdit_email.setStyleSheet(u"QLineEdit {\n"
"    /* Borda e fundo */\n"
"    border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
"}")
        self.label_name_4 = QLabel(self.page_3)
        self.label_name_4.setObjectName(u"label_name_4")
        self.label_name_4.setGeometry(QRect(10, 80, 411, 51))
        self.label_name_4.setFont(font2)
        self.label_name_4.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"border:3\n"
"}")
        self.lineEdit_name = QLineEdit(self.page_3)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(60, 90, 351, 30))
        self.lineEdit_name.setFont(font3)
        self.lineEdit_name.setStyleSheet(u"QLineEdit {\n"
"    /* Borda e fundo */\n"
"    border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 36);\n"
"}")
        self.label_user_6 = QLabel(self.page_3)
        self.label_user_6.setObjectName(u"label_user_6")
        self.label_user_6.setGeometry(QRect(10, 140, 241, 51))
        font5 = QFont()
        font5.setFamilies([u"MS Shell Dlg 2"])
        font5.setPointSize(10)
        self.label_user_6.setFont(font5)
        self.label_user_6.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"border:2\n"
"}")
        self.lineEdit_user = QLineEdit(self.page_3)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.lineEdit_user.setGeometry(QRect(60, 150, 181, 30))
        self.lineEdit_user.setFont(font3)
        self.lineEdit_user.setStyleSheet(u"QLineEdit {\n"
"    /* Borda e fundo */\n"
"    border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
"}")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 140, 171, 51))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"border:2\n"
"}")
        self.comboBox = QComboBox(self.page_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(330, 150, 91, 31))
        font6 = QFont()
        font6.setFamilies([u"MS Shell Dlg 2"])
        font6.setPointSize(8)
        font6.setItalic(False)
        self.comboBox.setFont(font6)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: F7F7F9  /* Cor de fundo */\n"
"    color: F7F7F9         /* Cor do texto */\n"
"    border: 1px solid #ccc;     /* Borda */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: #e0e0e0;  /* Cor do bot\u00e3o de dropdown */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: White;  /* Cor do menu dropdown */\n"
"    color: Black;             /* Cor do texto no menu */\n"
"}")
        self.label_passwrd_6 = QLabel(self.page_3)
        self.label_passwrd_6.setObjectName(u"label_passwrd_6")
        self.label_passwrd_6.setGeometry(QRect(10, 260, 411, 91))
        self.label_passwrd_6.setFont(font2)
        self.label_passwrd_6.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"border:2\n"
"}")
        self.lineEdit_passwrd = QLineEdit(self.page_3)
        self.lineEdit_passwrd.setObjectName(u"lineEdit_passwrd")
        self.lineEdit_passwrd.setGeometry(QRect(70, 270, 281, 30))
        self.lineEdit_passwrd.setFont(font3)
        self.lineEdit_passwrd.setStyleSheet(u"QLineEdit {\n"
"    /* Borda e fundo */\n"
"    border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
"}")
        self.label_email_4 = QLabel(self.page_3)
        self.label_email_4.setObjectName(u"label_email_4")
        self.label_email_4.setGeometry(QRect(10, 200, 411, 51))
        self.label_email_4.setFont(font2)
        self.label_email_4.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"border:2\n"
"}")
        self.lineEdit_passwrd_2 = QLineEdit(self.page_3)
        self.lineEdit_passwrd_2.setObjectName(u"lineEdit_passwrd_2")
        self.lineEdit_passwrd_2.setGeometry(QRect(70, 310, 281, 30))
        self.lineEdit_passwrd_2.setFont(font3)
        self.lineEdit_passwrd_2.setStyleSheet(u"QLineEdit {\n"
"    /* Borda e fundo */\n"
"    border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
"}")
        self.bttn_register = QPushButton(self.page_3)
        self.bttn_register.setObjectName(u"bttn_register")
        self.bttn_register.setGeometry(QRect(60, 370, 131, 31))
        self.bttn_register.setFont(font2)
        self.bttn_register.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.5);\n"
"    border: 5px solid rgba(255, 255, 255, 0.3); /* Borda branca transl\u00facida */\n"
"    color: #333333; /* Texto totalmente opaco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #CFD8DC;\n"
"    border-color: rgba(255, 255, 255,255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A0B2C8; /* Azul acinzentado */\n"
"border-color: #003366; /* Azul escuro */\n"
"}\n"
" QPushButton{border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QPushButton {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
""
                        "}")
        self.bttn_alterindex = QPushButton(self.page_3)
        self.bttn_alterindex.setObjectName(u"bttn_alterindex")
        self.bttn_alterindex.setGeometry(QRect(240, 370, 131, 31))
        self.bttn_alterindex.setFont(font2)
        self.bttn_alterindex.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.5);\n"
"    border: 2px solid rgba(255, 255, 255, 0.3); /* Borda branca transl\u00facida */\n"
"    color:#003366; /* Texto totalmente opaco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #CFD8DC;\n"
"    border-color: rgba(255, 255, 255,255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A0B2C8; /* Azul acinzentado */\n"
"border-color: #003366; /* Azul escuro */\n"
"}\n"
" QPushButton{border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QPushButton {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
"}")
        self.bttn_passwrdview = QPushButton(self.page_3)
        self.bttn_passwrdview.setObjectName(u"bttn_passwrdview")
        self.bttn_passwrdview.setGeometry(QRect(350, 290, 41, 31))
        self.bttn_passwrdview.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.5);\n"
"    border: 2px solid rgba(255, 255, 255, 0.3); /* Borda branca transl\u00facida */\n"
"    color: #333333; /* Texto totalmente opaco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #CFD8DC;\n"
"    border-color: rgba(255, 255, 255,255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A0B2C8; /* Azul acinzentado */\n"
"border-color: #003366; /* Azul escuro */\n"
"}\n"
" QPushButton{border: 2px solid rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    background-color: rgba(0, 0, 0, 0); /* Totalmente transparente */\n"
"    \n"
"    /* Espa\u00e7amento interno */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Cor do texto */\n"
"    color: white;\n"
"    \n"
"    /* Melhora a renderiza\u00e7\u00e3o */\n"
"    background-clip: padding-box;\n"
"}\n"
"\n"
"/* Efeito ao focar */\n"
"QPushButton {\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
""
                        "}")
        icon = QIcon()
        icon.addFile(u"../Downloads/visibility_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_passwrdview.setIcon(icon)
        self.bttn_passwrdview.setIconSize(QSize(24, 24))
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-30, 0, 471, 51))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.page_3)
        self.label_email_4.raise_()
        self.label_name_4.raise_()
        self.lineEdit_name.raise_()
        self.label_user_6.raise_()
        self.lineEdit_user.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.label_passwrd_6.raise_()
        self.lineEdit_passwrd.raise_()
        self.lineEdit_email.raise_()
        self.lineEdit_passwrd_2.raise_()
        self.bttn_register.raise_()
        self.bttn_alterindex.raise_()
        self.bttn_passwrdview.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_3.raise_()
        self.label.raise_()
        self.label_7.raise_()
        self.stackedWidget.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">POWERED BY (NOME DO GRUPO)</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#ffffff;\">BEM VINDO</span></p></body></html>", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">LOGIN</span></p></body></html>", None))
        self.label_user_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">User  </span></p></body></html>", None))
        self.lineEdit_passwrd_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua Senha...", None))
        self.label_passwrd_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Senha</span></p></body></html>", None))
        self.bttn_login.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.bttn_alterindex_2.setText(QCoreApplication.translate("MainWindow", u"Novo Usu\u00e1rio", None))
        self.lineEdit_user_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu Usu\u00e1rio...", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe seu E-mail...", None))
        self.label_name_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Nome</span></p></body></html>", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe seu Nome completo...", None))
        self.label_user_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">User  </span></p></body></html>", None))
        self.lineEdit_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe seu Usu\u00e1rio...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Permiss\u00e3o", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Recepcionista", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Gerente", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_passwrd_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Senha</span></p></body></html>", None))
        self.lineEdit_passwrd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe sua Senha...", None))
        self.label_email_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">E-mail</span></p></body></html>", None))
        self.lineEdit_passwrd_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirme sua Senha...", None))
        self.bttn_register.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.bttn_alterindex.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.bttn_passwrdview.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">NOVO CADASTRO</span></p></body></html>", None))
    # retranslateUi

