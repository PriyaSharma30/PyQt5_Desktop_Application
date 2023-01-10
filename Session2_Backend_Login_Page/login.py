# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from Page2 import Ui_MainWindow_Page_2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, 9, 631, 541))
        self.widget.setObjectName("widget")
        self.LogIn = QtWidgets.QWidget(self.widget)
        self.LogIn.setGeometry(QtCore.QRect(260, 49, 311, 431))
        self.LogIn.setStyleSheet("*{ \n"
"    border : none;\n"
"}\n"
"#LogIn{\n"
"    background-color:rgb(54,54,54);\n"
"    border-radius:15px;\n"
"}\n"
"#password, #username{background-color:rgba(0,0,0,0);\n"
"   border-bottom:2px solid rgba(46,82,101,200);\n"
"   color:rgb(214,214,214);\n"
"}")
        self.LogIn.setObjectName("LogIn")
        self.log_in = QtWidgets.QLabel(self.LogIn)
        self.log_in.setGeometry(QtCore.QRect(90, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.log_in.setFont(font)
        self.log_in.setStyleSheet("color:rgb(255, 255, 255);")
        self.log_in.setObjectName("log_in")
        self.username = QtWidgets.QLineEdit(self.LogIn)
        self.username.setGeometry(QtCore.QRect(60, 140, 170, 25))
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.LogIn)
        self.password.setGeometry(QtCore.QRect(60, 200, 170, 25))
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.login_2 = QtWidgets.QPushButton(self.LogIn, clicked = lambda: self.login())
        self.login_2.setGeometry(QtCore.QRect(110, 310, 89, 25))
        self.login_2.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.login_2.setObjectName("login_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.log_in.setText(_translate("MainWindow", "Login"))
        self.username.setPlaceholderText(_translate("MainWindow", "username"))
        self.password.setPlaceholderText(_translate("MainWindow", "password"))
        self.login_2.setText(_translate("MainWindow", "Login"))

    def login(self):
        self.msg=QtWidgets.QMessageBox()
        if self.username.text()=="Priya" and self.password.text()=="123":
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow_Page_2()
            self.ui.setupUi(self.window)
            self.window.showMaximized()
            MainWindow.hide()
        else:
            self.msg.setText("Incorrect username and password")
            self.msg.exec_()    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
