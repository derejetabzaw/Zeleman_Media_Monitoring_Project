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
import result_viewer_page
from time import sleep
from shutil import copy
import subprocess
import os
import sys
import audio_result_viewer_page
sys.path.insert(1, os.path.join(os.getcwd(),'matching'))
import sqed_dir as sqd
from shutil import copy
import audio_comparison as ac
import json
import create_fingerprint_database 
import datetime 
from ethiopian_date import EthiopianDateConverter
import time_converter as tc


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
conv = EthiopianDateConverter.to_ethiopian




confidence_tune = 150

class Ui_MainWindow(object):
    def setupUi(self,MainWindow,Date_of_broadcast,Eth_date,database,Commercial,Commercial_Length,Station,Stream, Client, Ad, Ad_Duration):
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
        self.audio_scan_progress_bar = Audio_TaskThread(Stream= Stream ,Ad = Ad, Ad_Duration= Ad_Duration, database = database, Date_of_broadcast = Date_of_broadcast,Eth_date = Eth_date ,Client = Client,Commercial = Commercial,Commercial_Length = Commercial_Length)
        self.audio_scan_progress_bar.start()
        self.audio_scan_progress_bar.audio_valueChanged.connect(self.progressBar.setValue)
        self.audio_scan_progress_bar.audio_taskFinished.connect(self.progressBar.setValue)
        self.audio_scan_progress_bar.audio_taskFinished.connect(self.pushButton.setEnabled)

        

        
        self.audio_scan_progress_bar.connect(self.audio_scan_progress_bar, QtCore.SIGNAL('labeltext(QString)'), self.label.setText)
        self.pushButton.clicked.connect(lambda x: self.next_button(MainWindow,Date_of_broadcast,Eth_date,Station))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))
        self.pushButton.setText(_translate("MainWindow", "Next", None))
        self.pushButton.setEnabled(False)
        self.label.setText(_translate("MainWindow", "This may take few minutes...", None))


    def next_button(self,MainWindow,Date,Eth_date,Station):
        
        now = datetime.datetime.now()
        Time = now.strftime("%H:%M:%S")
        Stream_Duartion = int(get_sec(getLength(Stream)))

        print Date
        print Eth_date
        print Time 
        print Client
        print Commercial 
        print Commercial_Length
        print Station 
        print Ad 
        print Stream 
        print Broadcast_information
        print Ad_Durations
        print match_time
        result_viewer_page_ui = result_viewer_page.Ui_MainWindow()
        result_viewer_page_ui.setupUi(MainWindow,Date,Eth_date,Time,Client,Commercial,Commercial_Length,Station,Ad,Stream,Broadcast_information,Ad_Durations,match_time)
        MainWindow.show()


class Audio_TaskThread(QThread):
    audio_taskFinished = QtCore.pyqtSignal(int,bool)
    audio_valueChanged = QtCore.pyqtSignal(int) 

    def __init__(self,Stream,Ad,Ad_Duration,database,Date_of_broadcast,Eth_date,Client,Commercial,Commercial_Length):
        super(QThread, self).__init__()
        self.Stream = Stream
        self.Ad = Ad
        self.Ad_Duration = Ad_Duration
        self.database = database
        self.Date_of_broadcast = Date_of_broadcast
        self.Eth_date = Eth_date
        self.Client = Client
        self.Commercial = Commercial
        self.Commercial_Length = Commercial_Length
                
    def run(self):
        global Stream
        global Ad_Durations
        global Ad 
        global Client 
        global Commercial 
        global Commercial_Length
        global Broadcast_information
        global match_time
        global Ad_Durations
        Stream = self.Stream
        Ad_Durations = self.Ad_Duration
        Ad = self.Ad
        database = str(self.database)
        Date_of_broadcast = str(self.Date_of_broadcast)
        Eth_date = str(self.Eth_date)
        Client = self.Client
        Commercial = self.Commercial
        Commercial_Length = self.Commercial_Length

        sleep(1)

        '''Getting Duration'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Getting Duration..."))
        

        St_dur = int(get_sec(getLength(Stream)))
        for i in xrange(15,2):
            self.audio_valueChanged.emit(i) 
            sleep(0.5)

        
        '''Indexing'''    
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Indexing..." ))
        
        progress_bar_index = 15 

        Least_duration = sorted(Ad_Durations)

        Ad_Duration = tc.time_converter(Least_duration[0])
        segment_index = int(round(St_dur / int(Ad_Duration))) + 1

        '''Trimming'''
        
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Trimming... "))
        indexed_audio = []
        indexed_audio_durations = []
        audio_marks = [0] * segment_index
        adder = 0
        for i in range(segment_index):
            crop(str(i*int(Ad_Duration)),str(int(Ad_Duration)*(i + 1)),str(self.Stream),str("audio_cropped/audio_crop_" + str(i) + ".mp3"))
            indexed_audio.append(os.getcwd() + "/audio_cropped/audio_crop_" + str(i) + ".mp3")
            indexed_audio_durations.append(get_sec(getLength(indexed_audio[i])))
            audio_marks[i] = adder + indexed_audio_durations[i] 
            adder += indexed_audio_durations[i]

        
        songs = ac.audio_compare(indexed_audio)





        for i in range(progress_bar_index,progress_bar_index + 10 ,2):
            self.audio_valueChanged.emit(i)
            sleep(0.5) 
        progress_bar_index += 25



        
        Broadcast_information = ["No"] * Commercial_Length
        match_time = [0] * Commercial_Length        
        for index in range(Commercial_Length):
            for i in range(progress_bar_index,progress_bar_index + 5,2):
                self.audio_valueChanged.emit(i)
                sleep(0.5)
            progress_bar_index += 5 

            
            self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Finding Match: " + str(Commercial[index])))

            Stream_duration = St_dur

            for i in range(len(indexed_audio)):
                if songs[i]['confidence'] > confidence_tune and songs[i]['song_name'] == str(os.path.splitext(os.path.basename(Ad[index]))[0]):
                    Broadcast_information[index] = "Yes"
                    match_time[index] = audio_marks[i]
                    break


            '''Writing to Database'''
            # self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Recording to Database"))
            # create_fingerprint_database.insert_audio_broadcast_information_to_database(database,str(Date_of_broadcast),str(Eth_date),str(Client[index]),str(Commercial[index]),broadcast_information,str(Ad[index]),str(Ad_Duration),Stream,Stream_duration,str(match_time))
            # for i in range(progress_bar_index,progress_bar_index + 10 ,2):
            #     self.audio_valueChanged.emit(i)
            #     sleep(0.5)
            progress_bar_index += 10 
            

            progress_bar_index += 2 
        
        for audio_file in os.listdir("audio_cropped"):
                if audio_file.lower().endswith((".mp3",".wma",".wav")):
                    os.remove(os.getcwd() + "/audio_cropped/" + audio_file)  

        for i in range(progress_bar_index, 99 ,2):
            self.audio_valueChanged.emit(i)
            sleep(0.5)
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Done"))        
        self.audio_taskFinished.emit(100,True)  



