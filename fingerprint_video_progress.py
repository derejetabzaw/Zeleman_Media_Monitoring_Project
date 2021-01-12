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
        
        self.details_push = QtGui.QPushButton(self.centralwidget)
        
        self.details_push.setGeometry(QtCore.QRect(600, 255, 80, 20))

        self.details_push.setObjectName(_fromUtf8("details_push"))
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
        self.myLongTask = TaskThread(MainWindow = MainWindow ,database = database, Client = Client ,Commercial = Commercial, Commercial_Length = Commercial_Length,Ad = Ad)
        self.myLongTask.start()
        

        self.myLongTask.valueChanged.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.progressBar.setValue)
        #self.myLongTask.taskFinished.connect(self.details_push.setEnabled)
        self.myLongTask.taskFinished.connect(self.pushButton.setEnabled)


        self.myLongTask.connect(self.myLongTask, QtCore.SIGNAL('labeltext(QString)'), self.label.setText)
        #self.details_push.clicked.connect(lambda x: self.next_button(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream))
        
        self.pushButton.clicked.connect(lambda x: self.done_button(MainWindow))
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))
        self.details_push.setText(_translate("MainWindow", "Details", None))
        self.details_push.setEnabled(True)
        self.pushButton.setEnabled(False)

        self.pushButton.setText(_translate("MainWindow", "Main Menu", None))
        
        self.label.setText(_translate("MainWindow", "This may take few minutes...", None))

    
    def done_button(self,MainWindow):

        main_menu_ui = main_menu.Ui_MainWindow()
        main_menu_ui.setupUi(MainWindow)
        MainWindow.show()


    # def next_button(self,MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream):
    #     broadcast_information, additional_information = sqd.matching(str(os.path.join(os.getcwd(),'output'))) 
    #     print broadcast_information
    #     Ad_dur = get_sec(getLength(str(Ad))[0:8])
    #     Time_in_video = Ad_dur * (int(additional_information[1]) - 1)
    #     result_viewer_page_ui = result_viewer_page.Ui_MainWindow()
    #     result_viewer_page_ui.setupUi(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video)
    #     MainWindow.show()

class TaskThread(QThread):
    taskFinished = QtCore.pyqtSignal(int,bool)
    valueChanged = QtCore.pyqtSignal(int)
    
    def __init__(self,MainWindow,database,Client,Commercial,Commercial_Length,Ad):
        super(QThread, self).__init__()
        self.Client = Client
        self.Commercial = Commercial
        self.Commercial_Length = Commercial_Length
        self.Ad = Ad
        self.database = database
        self.MainWindow = MainWindow


    def run(self):
        Client = self.Client
        Commercial = self.Commercial
        Commercial_Length = self.Commercial_Length 
        Ad = self.Ad
        database = self.database
        MainWindow = self.MainWindow
        sleep(1)


        original_json = []
        renamed_json = []
        json_filename = []
        fingerprint_script = "ruby dupe.rb"
        fingerprint_array = []
        json_files = []
        progressBar_index = 0
        files = glob.glob(os.getcwd() + "/fingerprints/" + str('*'))
        Commercials_to_fingerprint = Commercial_Length
        



        for file_index in range(Commercials_to_fingerprint):
            while path.exists(os.getcwd() + "/jsons/" + str(Commercial[file_index] + ".json")):
                #print (str(Commercial[i] + ".json") + str(" Fingerprint Already Exists, Do you want to overwrite?"))
                reply = QtGui.QMessageBox.question(MainWindow, 'Message',"Fingerprint Already Exists, Do you want to overwrite?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    os.remove(os.getcwd() + "/jsons/" + str(Commercial[file_index] + ".json"))
                    create_fingerprint_database.delete_video_information_from_database_by_commercial(database,Commercial[file_index])
                    continue 
                else:

                #self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Fingerprint Already Exists, Do you want to overwrite?"))
                    break
            
            else:
                self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Processing files..."))
                copy(str(Ad[file_index]),"fingerprints")

                for i in xrange(progressBar_index,int((progressBar_index + 4)/Commercials_to_fingerprint),1):
                    self.valueChanged.emit(i) 
                    sleep(2)
                progressBar_index += 5


                self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Fingerprinting " + Commercial[file_index]))

                os.system(fingerprint_script)
                
                for i in xrange(progressBar_index,int((progressBar_index + 20)/Commercials_to_fingerprint),1):
                    self.valueChanged.emit(i) 
                    sleep(2)
                progressBar_index += 26   
                
                for video_file in os.listdir("fingerprints"):
                    if video_file.lower().endswith((".mp4",".flv",".mpg",".avi",".wmv",".mpv")):
                        os.remove(os.getcwd() + "/fingerprints/" + video_file)        

                
                for file in os.listdir("fingerprints"):
                    if file.endswith(".json"):
                        json_files.append(file)
                self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Sorting fingerprints for " + Commercial[file_index]))
                
                for i in xrange(progressBar_index,int((progressBar_index + 20)/Commercials_to_fingerprint),2):
                    self.valueChanged.emit(i) 
                    sleep(2)
                progressBar_index += 47


                original_json.append((os.getcwd() + "/fingerprints/" + str(json_files[file_index])).replace("\\","/"))
                renamed_json.append(os.getcwd() + "/jsons/" + str(Commercial[file_index] + ".json"))
                os.rename(original_json[file_index],renamed_json[file_index])
                fingerprint_array.append(load_tester(renamed_json[file_index]))
                Ad_Duration = getLength(Ad[file_index])
                self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Recording " + str(Commercial[file_index]) + "'s information to Database"))
                create_fingerprint_database.insert_video_information_to_database(database,str(Client[file_index]),str(Commercial[file_index]),str(Ad[file_index]),str(Ad_Duration),str(fingerprint_array[file_index]),str(renamed_json[file_index]))
                
                for i in xrange(progressBar_index,int((progressBar_index + 40)/Commercials_to_fingerprint),3):
                    self.valueChanged.emit(i) 
                    sleep(2)
                progressBar_index += 88
        for f in files:
            os.remove(f)
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Finalizing..."))
        for i in xrange(progressBar_index, 90 ,2):
            self.valueChanged.emit(i) 
            sleep(2)
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Done"))
        self.taskFinished.emit(100,True)  
#        exit()






        
        

