# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Page_2(object):
    def setupUi(self, MainWindow_Page_2):
        MainWindow_Page_2.setObjectName("MainWindow_Page_2")
        MainWindow_Page_2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow_Page_2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 120, 291, 321))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow_Page_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_Page_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow_Page_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_Page_2)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Page_2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_Page_2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Page_2)

    def retranslateUi(self, MainWindow_Page_2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Page_2.setWindowTitle(_translate("MainWindow_Page_2", "MainWindow"))
        self.label.setText(_translate("MainWindow_Page_2", "Hi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Page_2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Page_2()
    ui.setupUi(MainWindow_Page_2)
    MainWindow_Page_2.show()
    sys.exit(app.exec_())
