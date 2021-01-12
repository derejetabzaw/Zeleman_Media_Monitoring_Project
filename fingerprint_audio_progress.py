# -*- coding: utf-8 -*-
# search_page.py 
# Form implementation generated from reading ui file 'frontend_3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from proprocess import get_sec,getLength,trimmer,crop 
import create_fingerprint_database
import scenesplit as split
from time import sleep
from shutil import copy
import subprocess
import os
from os import path
import sys
import result_viewer_page
sys.path.insert(1, os.path.join(os.getcwd(),'matching'))
import sqed_dir as sqd
import sqed
from shutil import copy
import glob
from converter import load_tester
import audio_comparison as ac
import main_menu


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
if not os.path.exists("cropped"):
    os.makedirs("cropped")



class Ui_MainWindow(object):
    def setupUi(self,MainWindow,database,Client,Commercial,Commercial_Length,Ad):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(795, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        
        self.pushButton.setGeometry(QtCore.QRect(690, 530, 100, 30))

        # self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 225, 600, 50))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.progressBar = QtGui.QProgressBar(self.layoutWidget)
        

        self.verticalLayout.addWidget(self.progressBar)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

       
        self.progressBar.setRange(0,100)
        self.myLongTask = TaskThread(database = database, Client = Client ,Commercial = Commercial,Commercial_Length = Commercial_Length, Ad = Ad)
        self.myLongTask.start()
        

        self.myLongTask.valueChanged.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.progressBar.setValue)

        self.myLongTask.taskFinished.connect(self.pushButton.setEnabled)
        

        self.myLongTask.connect(self.myLongTask, QtCore.SIGNAL('labeltext(QString)'), self.label.setText)
        self.pushButton.clicked.connect(lambda x: self.done_button(MainWindow))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))
        self.pushButton.setText(_translate("MainWindow", "Main Menu", None))
        self.pushButton.setEnabled(False)
        self.label.setText(_translate("MainWindow", "This may take few minutes...", None))

    def done_button(self,MainWindow):

        main_menu_ui = main_menu.Ui_MainWindow()
        main_menu_ui.setupUi(MainWindow)
        MainWindow.show()

class TaskThread(QThread):
    taskFinished = QtCore.pyqtSignal(int,bool)
    valueChanged = QtCore.pyqtSignal(int)
    
    def __init__(self,database,Client,Commercial,Commercial_Length,Ad):
        super(QThread, self).__init__()
        self.Client = Client
        self.Commercial = Commercial
        self.Commercial_Length = Commercial_Length
        self.Ad = Ad
        self.database = database


    def run(self):
        Client = self.Client
        Commercial = self.Commercial
        Commercial_Length = self.Commercial_Length 
 
        Ad = self.Ad
        database = self.database
        Commercials_to_fingerprint = Commercial_Length
        sleep(1)
        progressBar_index = 0
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Processing files..."))
        for file_index in range(Commercials_to_fingerprint):   
            if not os.path.exists("audio_output"):
              os.makedirs("audio_output")
            for i in xrange(progressBar_index,int((progressBar_index + 4)/Commercials_to_fingerprint),1):
                self.valueChanged.emit(i) 
                sleep(3)
            progressBar_index += 5

            self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Restructuring Audio Files..."))
            copy(str(Ad[file_index]),"audio_output")
            for i in xrange(progressBar_index,int((progressBar_index + 15)/Commercials_to_fingerprint),2):
                self.valueChanged.emit(i) 
                sleep(3)
            
            self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Getting Audio Duration for: " + str(Commercial[file_index])))

            Ad_Duration = getLength(Ad[file_index])
            
            progressBar_index += 16 
            for i in xrange(progressBar_index,int((progressBar_index + 12 )/Commercials_to_fingerprint),2):
                self.valueChanged.emit(i) 
                sleep(3)

            progressBar_index += 29
            self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Writing Supplementary Fingerprint information into Database"))
            create_fingerprint_database.insert_audio_information_to_database(database,str(Client[file_index]),str(Commercial[file_index]),str(Ad[file_index]),str(Ad_Duration))

            for i in xrange(progressBar_index,int((progressBar_index + 20 )/Commercials_to_fingerprint),1):
                self.valueChanged.emit(i) 
                sleep(3)
            progressBar_index += 50
            self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Fingerprinting " + str(Commercial[file_index])))

            ac.audio_fingerprint(os.getcwd())
            
            for i in xrange(progressBar_index,int((progressBar_index + 30 )/Commercials_to_fingerprint),2):
                self.valueChanged.emit(i) 
                sleep(3)
            
            progressBar_index += 10  
            self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Cleaning Directory..."))


            for audio_file in os.listdir("audio_output"):
                if audio_file.lower().endswith((".mp3",".wma",".wav")):
                    os.remove(os.getcwd() + "/audio_output/" + audio_file)

            for i in xrange(progressBar_index,int((progressBar_index + 5 )/Commercials_to_fingerprint),1):
                self.valueChanged.emit(i) 
                sleep(0.5)  
        
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Done"))
        self.taskFinished.emit(100,True)  

        





        
        

