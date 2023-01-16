# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from sys import stderr, stdout
from PyQt5 import QtCore, QtGui, QtWidgets
import configparser,os,shutil

directory_path= os.path.dirname(__file__)
print(directory_path)
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QProcess,Qt,QTimer
from PyQt5.QtWidgets import QWidget,QLabel , QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lhost_abel = QtWidgets.QLabel(self.centralwidget)
        self.lhost_abel.setGeometry(QtCore.QRect(60, 70, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lhost_abel.setFont(font)
        self.lhost_abel.setObjectName("lhost_abel")
        self.user_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_lineEdit.setGeometry(QtCore.QRect(210, 80, 231, 25))
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.submit_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.checked())
        self.submit_pushButton.setGeometry(QtCore.QRect(40, 210, 89, 25))
        font = QtGui.QFont()
        # font.setBold(False)
        font.setWeight(75)
        self.submit_pushButton.setFont(font)
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.run_pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.Loading())
        self.run_pushButton.setGeometry(QtCore.QRect(200, 210, 89, 25))
        self.run_pushButton.setObjectName("run_pushButton")
        self.op_pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.openSaveDialog())
        self.op_pushButton.setGeometry(QtCore.QRect(370, 210, 89, 25))
        self.op_pushButton.setObjectName("op_pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 290, 791, 301))
        self.plainTextEdit.setObjectName("plainTextEdit")
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
        self.lhost_abel.setText(_translate("MainWindow", "Hostname"))
        self.submit_pushButton.setText(_translate("MainWindow", "Submit"))
        self.run_pushButton.setText(_translate("MainWindow", "Run"))
        self.op_pushButton.setText(_translate("MainWindow", "Save Output"))

    def message(self,s):
        self.plainTextEdit.appendPlainText(s)

    def checked(self):
        self.plainTextEdit.clear()  
        a= open(r"{}requirement.ini".format(directory_path),'w') 
        try:
            f1=configparser.ConfigParser()
            f1.add_section("Section1")
            f1.set("Section1","hostname",self.user_lineEdit.text())
            f1.write(a)
            a.close
            self.plainTextEdit.appendPlainText("hostname: {}".format(self.user_lineEdit.text()))
            self.plainTextEdit.appendPlainText("Data append successfully")

        except Exception as e:
            print(e)
            pass     

    def handle_stdout(self):
        data=self.p.readAllStandardOutput()
        stdout=bytes(data).decode("utf8")
        self.message(stdout)
        self.file.write(stdout)

    def handle_stderr(self):
        data=self.p.readAllStandardError()
        stderr=bytes(data).decode("utf8")
        self.message(stderr)
        

    def Process_finished(self):
        self.message("Process finished")
        self.file=open('save.txt','w')
        self.stopani()
        self.p=None

    def start_process(self):
        self.p=None
        if self.p is None:
            self.plainTextEdit.clear()
            self.message("Executing Process")
            self.p= QProcess()
            self.file=open('save.txt','w')
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.finished.connect(self.Process_finished)
            self.p.start("python",['/home/sharma_priya/Documents/Desktopapp/Session6/ping.py'])    

    def Loading(self):
        self.main_win=QWidget()
        self.verticalLayout=QtWidgets.QVBoxLayout(self.main_win)
        self.label_ani=QLabel(self.main_win)
        self.movie=QMovie("loading.gif")
        self.label_ani.setMovie(self.movie)
        self.verticalLayout.addWidget(self.label_ani,0,QtCore.Qt.AlignHCenter)
        self.main_win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.main_win.setAttribute(QtCore.Qt.WA_TranslucentBackground,on=True)
        self.startani()
        self.main_win.showMaximized()
        self.timer=QTimer(self.main_win)
        self.timer.singleShot(100,self.start_process)

    def startani(self):
        self.movie.start()

    def stopani(self):
        self.movie.stop()
        self.main_win.close()       

    def openSaveDialog(self):
        option=QFileDialog.Options()
        file_path='{}/home/sharma_priya/Documents/Desktopapp/Session6/save.txt'.format(directory_path)
        option=QFileDialog.DontUseNativeDialog
        file=QFileDialog.getSaveFileName(self.centralwidget,"save file window title","default.txt","All files(*)",options=option)
        print(file[0])
        shutil.copyfile(file_path,file[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
