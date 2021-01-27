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
import time_converter as tc
import result_viewer_page
sys.path.insert(1, os.path.join(os.getcwd(),'matching'))
import sqed_dir as sqd
import sqed
from shutil import copy
import datetime 
from ethiopian_date import EthiopianDateConverter
import append_csv as acsv
conv = EthiopianDateConverter.to_ethiopian

import time 

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
    #def setupUi(self,MainWindow,Commercial,Stream,Ad_seconds,fingerprint):
    def setupUi(self,MainWindow,database,Stream,Station,Commercial,Ad_seconds,fingerprint,Commercial_Length,scan_type,start_time):
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
        self.myLongTask = TaskThread(MainWindow = MainWindow,database = database,Station = Station,Stream = Stream,Commercial = Commercial,Ad_seconds = Ad_seconds,fingerprint = fingerprint,Commercial_Length = Commercial_Length,scan_type = scan_type ,start_time = start_time)
        self.myLongTask.start()
        

        self.myLongTask.valueChanged.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.pushButton.setEnabled)
        

        self.myLongTask.connect(self.myLongTask, QtCore.SIGNAL('labeltext(QString)'), self.label.setText)
        # self.pushButton.clicked.connect(lambda x: self.next_button(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream))
        self.pushButton.clicked.connect(lambda x: self.next_button(MainWindow,Station))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))
        self.pushButton.setText(_translate("MainWindow", "Next", None))
        self.pushButton.setEnabled(False)
        self.label.setText(_translate("MainWindow", "This may take few minutes...", None))

    # def next_button(self,MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream):
        
    def next_button(self,MainWindow,Station):
        # broadcast_information, additional_information = sqd.matching(str(os.path.join(os.getcwd(),'output'))) 
        # print broadcast_information
        # print match_json,Broadcast_information,scene_index
        # global Date_of_broadcast
        Date = datetime.date.today()
        # Date_of_broadcast = [Date.month,Date.day,Date.year]
        
        # global Eth_date
        # Eth_date = str(conv(Date_of_broadcast[2],Date_of_broadcast[0],Date_of_broadcast[1]))[1:-1]        
        # Eth_date = Eth_date.replace('/',',')
        # Eth_date = [int(i) for i in Eth_date.split(',')]
        # Ethiopian_date = str(Eth_date[1]) + str(',') + str(Eth_date[2]) + str(',') + str(Eth_date[0])
        
        now = datetime.datetime.now()
        Time = now.strftime("%H:%M:%S")
        Stream_Duartion = int(get_sec(getLength(Stream)))

        
        # Ad_dur = get_sec(getLength(str(Ad))[0:8])
        # Time_in_video = Ad_dur * (int(additional_information[1]) - 1)
        # Time_in_video = "4:34" 
        print (all_clients)
        print (all_ad)
        print (Commercial)
        print (all_ad_lengths)
        print (commercial_ad_time_seconds)
        print (Commercial_Length)
        print (Broadcast_information)
        print (match_json)
        print (scene_index)
        print (Time_in_video)
        result_viewer_page_ui = result_viewer_page.Ui_MainWindow()
        result_viewer_page_ui.setupUi(MainWindow,Date,Eth_date,Time,all_clients,Commercial,Commercial_Length,Station,all_ad,Stream,Broadcast_information,all_ad_lengths,Time_in_video)
        MainWindow.show()

class TaskThread(QThread):
    taskFinished = QtCore.pyqtSignal(int,bool)
    valueChanged = QtCore.pyqtSignal(int)
    
    def __init__(self,MainWindow,database,Station,Stream,Commercial,Ad_seconds,fingerprint,Commercial_Length,scan_type,start_time):
        super(QThread, self).__init__()
        self.MainWindow  = MainWindow
        self.database = database
        self.Stream = Stream
        self.Commercial = Commercial
        self.Ad_seconds = Ad_seconds
        self.fingerprint = fingerprint
        self.Commercial_Length = Commercial_Length
        self.start_time = start_time
        self.Station = Station
        self.scan_type = scan_type

    def run(self):
        global Commercial
        global Commercial_Length
        global match_json
        global Broadcast_information
        global scene_index
        global all_ad_lengths
        global all_clients
        global all_ad
        global Stream
        global match_json
        global directory
        global Time_in_video
        global commercial_ad_time_seconds
        global Station
        global Date_of_broadcast
        global Eth_date
        global scan_type


        MainWindow = self.MainWindow
        database = self.database
        Stream = self.Stream
        Commercial = self.Commercial
        Ad_seconds = self.Ad_seconds 
        fingerprint = self.fingerprint
        Commercial_Length = self.Commercial_Length
        Station = self.Station
        
        start_time = self.start_time

        commercial_ad_time_seconds = self.Ad_seconds  
        commercial_fingerprint = self.fingerprint  
        scan_type = self.scan_type
        sleep(3)

        upper_bound = 0.12
        threshold_seconds = 60

        Date = datetime.date.today()
        Date_of_broadcast = [Date.month,Date.day,Date.year]
        Eth_date = str(conv(Date_of_broadcast[2],Date_of_broadcast[0],Date_of_broadcast[1]))[1:-1]        
        Eth_date = Eth_date.replace('/',',')
        Eth_date = [int(i) for i in Eth_date.split(',')]
        Ethiopian_date = str(Eth_date[1]) + str(',') + str(Eth_date[2]) + str(',') + str(Eth_date[0])
        
        now = datetime.datetime.now()
        Time = now.strftime("%H:%M:%S")

        Stream_duration = int(get_sec(getLength(Stream)))
        match_json = []

       

        
        
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Preparing"))
        
        
        for image_files in os.listdir("tiles"):
            if image_files.lower().endswith((".png",".jpeg",".jpg")):
                os.remove(os.getcwd() + "/tiles/" + image_files) 
              
        for image_files in os.listdir("tmp"):
            if image_files.lower().endswith((".png",".jpeg",".jpg")):
                os.remove(os.getcwd() + "/tmp/" + image_files) 


        for video_file in os.listdir("cropped_threshold"):
            if video_file.lower().endswith((".json",".mp4",".flv",".mpg",".avi",".wmv",".mpv")):
                os.remove(os.getcwd() + "/cropped_threshold/" + video_file)        
        
        for video_file in os.listdir("cropped_content"):
            if video_file.lower().endswith((".csv",".json",".mp4",".flv",".mpg",".avi",".wmv",".mpv")):
                os.remove(os.getcwd() + "/cropped_content/" + video_file) 


        print scan_type


        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Detecting Threshold for " + str(Stream) ))
        split.video_threshold_scene_detector(Stream,threshold_seconds)
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Detecting Content..."))
        contentfingerprint = []
        if (scan_type == "Easy"):
            directory = (os.getcwd() + str("/")+str("cropped_threshold/")).replace("\\","/")
            fingerprint_script = "ruby dupe_2.rb"  
        if (scan_type == "Normal"):
            directory = (os.getcwd() + str("/")+str("cropped_content/")).replace("\\","/")
            fingerprint_script = "ruby dupe_3.rb"  
        


        directory = (os.getcwd() + str("/")+str("cropped_content/")).replace("\\","/")
        fingerprint_script = "ruby dupe_3.rb"  
        all_commercials = []
        all_ad_lengths = []
        all_clients = []
        
        all_ad = []
        
        scene_index = []

        Broadcast_information = ["No"] * Commercial_Length
        Time_in_video = [0] * Commercial_Length
        

        
        '''Comparing Fingerprints'''
        for file_index in range(Commercial_Length):
            for check_fingerprint_exists in os.listdir("cropped_content"):
                if check_fingerprint_exists.lower().endswith((".json")):
                    break
            else:
                if (scan_type == "Normal"):
                    split.video_content_scene_detector(str(Ad_seconds[file_index]))
                os.system(fingerprint_script)
                self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Fingerprinting..."))
        
                
            
            for i in xrange(60,4):
                self.valueChanged.emit(i) 
                sleep(3)
    
            '''Collecting Fingerprints'''    
            self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Collecting Fingerprints..."))
            for filename in os.listdir(directory):
                if filename.endswith(".json"):
                    contentfingerprint.append(str(directory) + str("/") +str(filename))
            for i in range(61,84,6):
                self.valueChanged.emit(i)
                sleep(3)
            


        
            '''Detecting Threshold'''
            self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Comparing Fingerprints with " + str(Commercial[file_index])))

            
            all_clients.append(create_fingerprint_database.select_video_information_from_database_by_commercial(database,Commercial[file_index])[0][0])
            all_ad.append(create_fingerprint_database.select_video_information_from_database_by_commercial(database,Commercial[file_index])[0][1])
            all_ad_lengths.append(tc.time_converter(create_fingerprint_database.select_video_information_from_database_by_commercial(database,Commercial[file_index])[0][2]))
            
            for i in range(len(contentfingerprint)):
                squared_mean_error = sqed.mean_error_calculator(4,2,100,str(commercial_fingerprint[file_index].replace("\\","/")),str(contentfingerprint[i]))
                print squared_mean_error
                print contentfingerprint[i]
                if (0.01 < squared_mean_error < upper_bound):
                    match_json.append(contentfingerprint[i])
                    scene_index.append(i) 
                    Broadcast_information[file_index] = "Yes"           
                    Time_in_video[file_index] = (str(acsv.normlaized_timestamps(directory)[0][i]))
                    break
            
            '''Writing to Database'''
            self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Recording Data to Database"))
            create_fingerprint_database.insert_video_broadcast_information_to_database(database,Station,str(Date_of_broadcast),str(Eth_date),str(all_clients[file_index]),str(Commercial[file_index]),Broadcast_information[file_index],str(all_ad[file_index]),str(commercial_ad_time_seconds[file_index]),Stream,Stream_duration,str(Time_in_video[file_index]))
            for i in range(85,89,2):
                self.valueChanged.emit(i)
                sleep(0.5)
            


        for i in range(90,99,2):
            self.valueChanged.emit(i)
            sleep(3) 
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Done"))
        print("--- %s seconds ---" % (time.time() - start_time))
        self.taskFinished.emit(100,True)  
        

