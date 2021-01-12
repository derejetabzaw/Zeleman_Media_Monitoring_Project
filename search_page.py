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
conv = EthiopianDateConverter.to_ethiopian



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
    def setupUi(self,MainWindow,database,Stream,Commercial,Ad_seconds,fingerprint,Commercial_Length):
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
        self.myLongTask = TaskThread(MainWindow = MainWindow,database = database,Stream = Stream,Commercial = Commercial,Ad_seconds = Ad_seconds,fingerprint = fingerprint,Commercial_Length = Commercial_Length)
        self.myLongTask.start()
        

        self.myLongTask.valueChanged.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.pushButton.setEnabled)
        

        self.myLongTask.connect(self.myLongTask, QtCore.SIGNAL('labeltext(QString)'), self.label.setText)
        # self.pushButton.clicked.connect(lambda x: self.next_button(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream))
        self.pushButton.clicked.connect(lambda x: self.next_button(MainWindow))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))
        self.pushButton.setText(_translate("MainWindow", "Next", None))
        self.pushButton.setEnabled(False)
        self.label.setText(_translate("MainWindow", "This may take few minutes...", None))

    # def next_button(self,MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream):
        
    def next_button(self,MainWindow):
        # broadcast_information, additional_information = sqd.matching(str(os.path.join(os.getcwd(),'output'))) 
        # print broadcast_information
        # print match_json,Broadcast_information,scene_index
        Date = datetime.date.today()
        Date_of_broadcast = [Date.month,Date.day,Date.year]
        
        Eth_date = str(conv(Date_of_broadcast[2],Date_of_broadcast[0],Date_of_broadcast[1]))[1:-1]        
        Eth_date = Eth_date.replace('/',',')
        Eth_date = [int(i) for i in Eth_date.split(',')]
        Ethiopian_date = str(Eth_date[1]) + str(',') + str(Eth_date[2]) + str(',') + str(Eth_date[0])
        Time = "12:51"
        Station = "EBC"
        Stream_Duartion = int(get_sec(getLength(Stream)))

        
        # Ad_dur = get_sec(getLength(str(Ad))[0:8])
        # Time_in_video = Ad_dur * (int(additional_information[1]) - 1)
        Time_in_video = "4:34" 
        print (all_clients)
        print (all_ad)
        print (Commercial)
        print all_ad_lengths
        print (Commercial_Length)
        result_viewer_page_ui = result_viewer_page.Ui_MainWindow()
        result_viewer_page_ui.setupUi(MainWindow,Date,Eth_date,Time,all_clients,Commercial,Commercial_Length,Station,all_ad,Stream,Broadcast_information,all_ad_lengths,Time_in_video)
        MainWindow.show()

class TaskThread(QThread):
    taskFinished = QtCore.pyqtSignal(int,bool)
    valueChanged = QtCore.pyqtSignal(int)
    
    def __init__(self,MainWindow,database,Stream,Commercial,Ad_seconds,fingerprint,Commercial_Length):
        super(QThread, self).__init__()
        self.MainWindow  = MainWindow
        self.database = database
        self.Stream = Stream
        self.Commercial = Commercial
        self.Ad_seconds = Ad_seconds
        self.fingerprint = fingerprint
        self.Commercial_Length = Commercial_Length


    def run(self):
        #self.Stream = str(self.Stream)
        global Commercial
        global Commercial_Length
        global match_json
        global Broadcast_information
        global scene_index
        global all_ad_lengths
        global all_clients
        global all_ad
        global Stream
        MainWindow = self.MainWindow
        database = self.database
        Stream = self.Stream
        Commercial = self.Commercial
        Ad_seconds = self.Ad_seconds 
        fingerprint = self.fingerprint
        Commercial_Length = self.Commercial_Length

        commercial_ad_time_seconds = self.Ad_seconds  
        commercial_fingerprint = self.fingerprint  

        sleep(3)

        upper_bound = 0.15
        threshold_seconds = 60
        match_json = []
        Broadcast_information = []
        
        
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Preparing"))
        
        
        for image_files in os.listdir("tiles"):
            if image_files.lower().endswith((".png",".jpeg")):
                os.remove(os.getcwd() + "/tiles/" + image_files) 
              
        for image_files in os.listdir("tmp"):
            if image_files.lower().endswith((".png",".jpeg")):
                os.remove(os.getcwd() + "/tmp/" + image_files) 


        # for video_file in os.listdir("cropped_threshold"):
        #     if video_file.lower().endswith((".json",".mp4",".flv",".mpg",".avi",".wmv",".mpv")):
        #         os.remove(os.getcwd() + "/cropped_threshold/" + video_file)        
        
        # for video_file in os.listdir("cropped_content"):
        #     if video_file.lower().endswith((".json",".mp4",".flv",".mpg",".avi",".wmv",".mpv")):
        #         os.remove(os.getcwd() + "/cropped_content/" + video_file) 



        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Detecting Threshold for " + str(Stream) ))
        # split.video_threshold_scene_detector(Stream,threshold_seconds)
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Detecting Content..."))
        directory = (os.getcwd() + str("/")+str("cropped_content")).replace("\\","/")
        contentfingerprint = []
        fingerprint_script = "ruby dupe_3.rb"  
        all_commercials = []
        all_ad_lengths = []
        all_clients = []
        
        all_ad = []
        
        scene_index = []

        
        
        '''Comparing Fingerprints'''
        for file_index in range(Commercial_Length):
            for check_fingerprint_exists in os.listdir("cropped_content"):
                if check_fingerprint_exists.lower().endswith((".json")):
                    break
            else:
                # split.video_content_scene_detector(str(Ad_seconds[file_index]))
                # os.system(fingerprint_script)
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

                if (0.01 < squared_mean_error < upper_bound):
                    match_json.append(contentfingerprint[i])
                    Broadcast_information.append(str("Yes"))
                    scene_index.append(i)            
                    break
                # else:
                #     Broadcast_information = str("No")
            

        for i in range(85,99,2):
            self.valueChanged.emit(i)
            # sleep(3) 
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Done"))
        self.taskFinished.emit(100,True)  
        

