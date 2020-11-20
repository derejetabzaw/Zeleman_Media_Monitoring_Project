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
import create_fingerprint_database as cfd
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
    def setupUi(self,MainWindow,Commercial,Stream,Ad_seconds,fingerprint):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(795, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        
        self.pushButton.setGeometry(QtCore.QRect(690, 530, 100, 30))

        self.pushButton.setObjectName(_fromUtf8("pushButton"))
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
        #self.myLongTask = TaskThread(Ad = Ad,Stream = Stream)
        self.myLongTask = TaskThread(Stream= Stream , Ad_seconds = Ad_seconds , fingerprint = fingerprint)
        self.myLongTask.start()
        

        self.myLongTask.valueChanged.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.pushButton.setEnabled)
        

        self.myLongTask.connect(self.myLongTask, QtCore.SIGNAL('labeltext(QString)'), self.label.setText)
        self.pushButton.clicked.connect(lambda x: self.next_button(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))
        self.pushButton.setText(_translate("MainWindow", "Next", None))
        self.pushButton.setEnabled(False)
        self.label.setText(_translate("MainWindow", "This may take few minutes...", None))

    def next_button(self,MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream):
        broadcast_information, additional_information = sqd.matching(str(os.path.join(os.getcwd(),'output'))) 
        print broadcast_information
        Ad_dur = get_sec(getLength(str(Ad))[0:8])
        Time_in_video = Ad_dur * (int(additional_information[1]) - 1)
        result_viewer_page_ui = result_viewer_page.Ui_MainWindow()
        result_viewer_page_ui.setupUi(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video)
        MainWindow.show()

class TaskThread(QThread):
    taskFinished = QtCore.pyqtSignal(int,bool)
    valueChanged = QtCore.pyqtSignal(int)
    
    def __init__(self,Stream,Ad_seconds,fingerprint):
        super(QThread, self).__init__()
        self.Stream = Stream
        self.Ad_seconds = Ad_seconds
        self.fingerprint = fingerprint


    def run(self):
        self.Stream = str(self.Stream)
        Stream = self.Stream
        Ad_seconds = self.Ad_seconds 
        fingerprint = self.fingerprint  


        commercial_ad_time_seconds = self.Ad_seconds  
        commercial_fingerprint = self.fingerprint  
        print "Stream: " + str(Stream)
        print "Ad_seconds: " + str(Ad_seconds)
        print "Fingerprint: " + str(fingerprint)
        sleep(1)

        '''Detecting Threshold'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Detecting Threshold..."))
        #split.video_threshold_scene_detector(Stream,commercial_ad_time_seconds)
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Detecting Content..."))
        #split.video_content_scene_detector()
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Fingerprinting..."))
        fingerprint_script = "ruby dupe_2.rb"
        #os.system(fingerprint_script)

        for i in xrange(60,4):
            self.valueChanged.emit(i) 
            sleep(0.5)
        
        '''Collecting Fingerprints'''    
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Collecting Fingerprints..."))
        directory = (os.getcwd() + str("/")+str("cropped_content")).replace("\\","/")
        contentfingerprint = []
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                contentfingerprint.append(str(directory) + str("/") +str(filename))

        for i in range(61,84,6):
            self.valueChanged.emit(i)
            sleep(0.5)
        
                

        '''Comparing Fingerprints'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Comparing Fingerprints..."))
        upper_bound = 0.1
        match_json = []
        for i in range(len(contentfingerprint)):
            squared_mean_error = sqed.mean_error_calculator(4,2,100,str(commercial_fingerprint.replace("\\","/")),str(contentfingerprint[i]))
            if (0 < squared_mean_error < upper_bound):
                match_json.append(contentfingerprint[i])
                print str(commercial_fingerprint) + str(" Was Broadcasted")
                print (commercial_fingerprint,match_json,squared_mean_error)
                
            else:
                #print str(commercial_fingerprint) + " Couldn't Find the video you are looking for"
                pass

        for i in range(85,99,2):
            self.valueChanged.emit(i)
            sleep(0.5) 
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Done"))
        self.taskFinished.emit(100,True)  
        

