# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_all.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.no_label = QtWidgets.QLabel(self.centralwidget)
        self.no_label.setGeometry(QtCore.QRect(20, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.no_label.setFont(font)
        self.no_label.setObjectName("no_label")
        self.a_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.a_checkBox.setGeometry(QtCore.QRect(140, 130, 92, 23))
        self.a_checkBox.setObjectName("a_checkBox")
        self.b_checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.b_checkBox_2.setGeometry(QtCore.QRect(260, 130, 92, 23))
        self.b_checkBox_2.setObjectName("b_checkBox_2")
        self.c_checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.c_checkBox_3.setGeometry(QtCore.QRect(380, 130, 92, 23))
        self.c_checkBox_3.setObjectName("c_checkBox_3")
        self.checkBoxs=[self.a_checkBox,self.b_checkBox_2,self.c_checkBox_3]
        self.all_checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.all_checkBox_4.setGeometry(QtCore.QRect(490, 130, 121, 21))
        self.all_checkBox_4.setObjectName("all_checkBox_4")
        self.all_checkBox_4.stateChanged.connect(self.onstatechange)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda: self.checked())
        self.pushButton.setGeometry(QtCore.QRect(260, 240, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 310, 521, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.op_label = QtWidgets.QLabel(self.frame)
        self.op_label.setGeometry(QtCore.QRect(40, 20, 301, 171))
        self.op_label.setObjectName("op_label")
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
        self.no_label.setText(_translate("MainWindow", "Number\'s"))
        self.a_checkBox.setText(_translate("MainWindow", "1"))
        self.b_checkBox_2.setText(_translate("MainWindow", "2"))
        self.c_checkBox_3.setText(_translate("MainWindow", "3"))
        self.all_checkBox_4.setText(_translate("MainWindow", "Select All"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.op_label.setText(_translate("MainWindow", "Output"))

    def checked(self):
        if self.a_checkBox.isChecked()==True:
            self.a="1"
        else:
            self.a=""
        if self.b_checkBox_2.isChecked()==True:
            self.b="2"
        else:
            self.b="" 
        if self.c_checkBox_3.isChecked()==True:
            self.c="3" 
        else:
            self.c="" 
        self.op_label.setText(f'{self.a}{self.b}{self.c}')  

    def onstatechange(self,state):
        for checkBox in self.checkBoxs:
            checkBox.setCheckState(state)                       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
