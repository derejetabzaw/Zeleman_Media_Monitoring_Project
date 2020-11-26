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
import audio_comparison as ac
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
conv = EthiopianDateConverter.to_ethiopian




confidence_tune = 150

class Ui_MainWindow(object):
    def setupUi(self,MainWindow,Date_of_broadcast,Eth_date,database,Commercial,Stream, Client, Ad, Ad_Duration):
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
        self.audio_scan_progress_bar = Audio_TaskThread(Stream= Stream ,Ad = Ad, Ad_Duration= Ad_Duration, database = database, Date_of_broadcast = Date_of_broadcast,Eth_date = Eth_date ,Client = Client,Commercial = Commercial)
        self.audio_scan_progress_bar.start()
        self.audio_scan_progress_bar.audio_valueChanged.connect(self.progressBar.setValue)
        self.audio_scan_progress_bar.audio_taskFinished.connect(self.progressBar.setValue)
        self.audio_scan_progress_bar.audio_taskFinished.connect(self.pushButton.setEnabled)

        
        #cropped_audio = self.audio_scan_progress_bar.run()[0]
        #Stream_duration = str(self.audio_scan_progress_bar.run()[1])

        
        self.audio_scan_progress_bar.connect(self.audio_scan_progress_bar, QtCore.SIGNAL('labeltext(QString)'), self.label.setText)
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

class Audio_TaskThread(QThread):
    audio_taskFinished = QtCore.pyqtSignal(int,bool)
    audio_valueChanged = QtCore.pyqtSignal(int) 

    def __init__(self,Stream,Ad,Ad_Duration,database,Date_of_broadcast,Eth_date,Client,Commercial):
        super(QThread, self).__init__()
        self.Stream = Stream
        self.Ad = Ad
        self.Ad_Duration = Ad_Duration
        self.database = database
        self.Date_of_broadcast = Date_of_broadcast
        self.Eth_date = Eth_date
        self.Client = Client
        self.Commercial = Commercial
                
    def run(self):
        Stream = self.Stream
        Ad_Duration = self.Ad_Duration
        Ad = str(self.Ad)
        database = str(self.database)
        Date_of_broadcast = str(self.Date_of_broadcast)
        Eth_date = str(self.Eth_date)
        Client = str(self.Client)
        Commercial = str(self.Commercial)
        
        #sleep(1)

        '''Getting Duration'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Getting Duration..."))
        
        Ad_Duration = 30
        St_dur = int(get_sec(getLength(Stream)))
        for i in xrange(15,2):
            self.audio_valueChanged.emit(i) 
            sleep(0.5)

        
        
        '''Indexing'''    
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Indexing..."))
        segment_index = int(round(St_dur / Ad_Duration)) + 1
        print segment_index
        for i in range(15,26,2):
            self.audio_valueChanged.emit(i)
            sleep(0.5)
        

        '''Trimming'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Trimming..."))
        indexed_audio = []
        for i in range(segment_index):
            crop(str(i*Ad_Duration),str(Ad_Duration*(i + 1)),str(self.Stream),str("audio_cropped/audio_crop_" + str(i) + ".mp3"))
            indexed_audio.append(os.getcwd() + "/audio_cropped/audio_crop_" + str(i) + ".mp3")

        for i in range(26,41,2):
            self.audio_valueChanged.emit(i)
            sleep(0.5) 

        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Finding Match..."))

        Stream_duration = St_dur
        songs = ac.audio_compare(indexed_audio)
        match_time = []
        for i in range(len(indexed_audio)):
            if songs[i]['confidence'] > confidence_tune and songs[i]['song_name'] == str(os.path.splitext(os.path.basename(Ad))[0]):
                print (songs[i]['confidence'])
                broadcast_information = str("Yes")
                match_time.append(float(songs[i]['match_time']) + float(songs[i]['offset_seconds']))
                print match_time
                print str(indexed_audio[i]) + " has an Audio Match: " + str(songs[i]['song_name']) + " ,with a confidence of: " + str(songs[i]['confidence']) + " at matchtime: " + str(match_time)
                #create_fingerprint_database.insert_audio_broadcast_information_to_database(database,str(Date_of_broadcast),str(Eth_date),str(Client),str(Commercial),broadcast_information,str(Ad),str(Ad_Duration),Stream,Stream_duration,match_time)
                #break
            else:
                print " Didn't Match "
                broadcast_information = str("No")

        '''Writing to Database'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Recording to Database"))
        for i in range(2):
            create_fingerprint_database.insert_audio_broadcast_information_to_database(database,str(Date_of_broadcast),str(Eth_date),str(Client[i]),str(Commercial[i]),broadcast_information,str(Ad[i]),str(Ad_Duration),Stream,Stream_duration,str(match_time[i]))
            exit()

        for i in range(41,98,4):
            self.audio_valueChanged.emit(i)
            sleep(0.5)

        for audio_file in os.listdir("audio_cropped"):
            if audio_file.lower().endswith((".mp3",".wma",".wav")):
                os.remove(os.getcwd() + "/audio_cropped/" + audio_file)  


        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Done"))

        self.audio_taskFinished.emit(100,True)  
        

# if __name__ == '__main__':
#     import sys
#     Date_of_broadcast = ['11,12,2005','12,5,2006']
#     Eth_date = ['12,1,1996','15,5,1998']
#     database = 'finger.db'
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow()
#     ui = Ui_MainWindow()
#     #ui.setupUi(MainWindow)
    
#     Commercial = "Coca Cola"
#     Stream = "C:/Users/dereje/Desktop/Media_Monitoring_Project/dejavu/stream_audio/stream.mp3"
#     Client = "Zeleman"
#     Ad = "C:/Users/dereje/Desktop/Media_Monitoring_Project/Zele_Ads/Zeleman_Coca-Cola.mp3"
#     Ad_Duration = "30" 
#     ui.setupUi(MainWindow,Date_of_broadcast,Eth_date,database,Commercial,Stream,Client, Ad, Ad_Duration)
#     MainWindow.show()
#     sys.exit(app.exec_())
#     