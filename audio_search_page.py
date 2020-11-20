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
from time import sleep
from shutil import copy
import subprocess
import os
import sys
import audio_result_viewer_page
sys.path.insert(1, os.path.join(os.getcwd(),'matching'))
import sqed_dir as sqd
from shutil import copy

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
import json
import create_fingerprint_database 
import datetime 
from ethiopian_date import EthiopianDateConverter


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
if not os.path.exists("audio_cropped"):
    os.makedirs("audio_cropped")
#database = r"C:/Users/dereje/Desktop/Media_Monitoring_Project/Frontend/frontend_codes/fingerprint_database.db"
#create_fingerprint_database.create_database_and_tables(database)
conv = EthiopianDateConverter.to_ethiopian

with open("dejavu.cnf.SQLITE_SAMPLE") as f:
    config = json.load(f)
djv = Dejavu(config)

class Ui_MainWindow(object):
    def setupUi(self,MainWindow,database,Commercial,Stream, Client, Ad, Ad_Duration):
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

        self.myLongTask = TaskThread(Stream= Stream , Ad_Duration= Ad_Duration)
        self.myLongTask.start()
        
        self.myLongTask.valueChanged.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.pushButton.setEnabled)

        
        cropped_audio = self.myLongTask.run()[0]
        Stream_duration = str(self.myLongTask.run()[1])
        

        songs  = []
        Date = datetime.date.today()
        Date_of_broadcast = [Date.month,Date.day,Date.year]
        
        Eth_date = str(conv(Date_of_broadcast[2],Date_of_broadcast[0],Date_of_broadcast[1]))[1:-1]        
        Eth_date = Eth_date.replace('/',',')
        Eth_date = [int(i) for i in Eth_date.split(',')]
        Eth_date = str(Eth_date[1]) + str(',') + str(Eth_date[2]) + str(',') + str(Eth_date[0])
        
        for i in range(len(cropped_audio)):
            songs.append(djv.recognize(FileRecognizer,cropped_audio[i]))
           
            if songs[i]['confidence'] > 100:
                broadcast_information = str("Yes")
                match_time = songs[i]['match_time']
                create_fingerprint_database.insert_audio_broadcast_information_to_database(database,str(Date_of_broadcast),str(Eth_date),str(Client[i]),str(Commercial[i]),broadcast_information,str(Ad[i]),str(Ad_Duration[i]),Stream,Stream_duration,match_time)
            else:
                print "No Audio Found Matching" 
        
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
        result_viewer_page_ui = audio_result_viewer_page.Ui_MainWindow()
        result_viewer_page_ui.setupUi(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video)
        MainWindow.show()

class TaskThread(QThread):
    taskFinished = QtCore.pyqtSignal(int,bool)
    valueChanged = QtCore.pyqtSignal(int) 
    cropped_audio_list = QtCore.pyqtSignal(object)
    indexed_audio = []

    def __init__(self,Stream, Ad_Duration):
        super(QThread, self).__init__()
        self.Stream = Stream
        self.Ad_Duration = Ad_Duration
        print self.Stream

    def run(self):
        self.Stream = str(self.Stream)
        Ad_Duration = self.Ad_Duration

        
        sleep(1)
        '''Getting Duration'''


        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Getting Duration..."))
        Ad_Duration = 121
        St_dur = int(get_sec(getLength(self.Stream)))
        for i in xrange(15,2):
            self.valueChanged.emit(i) 
            sleep(0.5)
        
        
        '''Indexing'''    
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Indexing..."))
        segment_index = int(round(St_dur / Ad_Duration))
        for i in range(15,26,2):
            self.valueChanged.emit(i)
            sleep(0.5)
        

        '''Trimming'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Trimming..."))

        indexed_audio = []
        for i in range(segment_index):
            crop(str(i*Ad_Duration),str(Ad_Duration*(i + 1)),str(self.Stream),str("audio_cropped/audio_crop_" + str(i) + ".mp3"))
            indexed_audio.append(os.getcwd() + "/audio_cropped/audio_crop_" + str(i) + ".mp3")
        self.cropped_audio_list.emit(indexed_audio)

        for i in range(26,41,2):
            self.valueChanged.emit(i)
            sleep(0.5) 
        

        '''Centroid of Gradient Orientation'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Fingerprinting..."))

        for i in range(41,98,4):
            self.valueChanged.emit(i)
            sleep(0.5)

        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Done"))

        self.taskFinished.emit(100,True)  
        return indexed_audio, St_dur