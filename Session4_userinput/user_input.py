# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import configparser,os

directory_path=os.path.dirname(__file__)
print(directory_path)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(20, 120, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.namelabel.setFont(font)
        self.namelabel.setObjectName("namelabel")
        self.ip_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_lineEdit.setGeometry(QtCore.QRect(200, 130, 181, 25))
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 290, 521, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.op_plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.op_plainTextEdit.setGeometry(QtCore.QRect(20, 50, 491, 191))
        self.op_plainTextEdit.setObjectName("op_plainTextEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 10, 101, 17))
        self.label.setObjectName("label")
        self.run_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.checked())
        self.run_pushButton.setGeometry(QtCore.QRect(250, 210, 89, 25))
        self.run_pushButton.setObjectName("run_pushButton")
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
        self.namelabel.setText(_translate("MainWindow", "Hostname"))
        self.label.setText(_translate("MainWindow", "Output"))
        self.run_pushButton.setText(_translate("MainWindow", "Run"))

    def message(self,s):
        self.op_plainTextEdit.appendPlainText(s)

    def checked(self):
        self.op_plainTextEdit.clear()
        a=open(r"{}requirement.ini".format(directory_path),'w')
        try:
            f1=configparser.ConfigParser()
            f1.add_section("Section1")
            f1.set("Section1","Hostname",self.ip_lineEdit.text())
            f1.write(a)
            a.close()
            self.op_plainTextEdit.appendPlainText('HostnameL: {}'.format(self.ip_lineEdit.text()))
            self.op_plainTextEdit.appendPlainText("Data append successfully")

        except Exception as e:
            print(e)
            pass        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())