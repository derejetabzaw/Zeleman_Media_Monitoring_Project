# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os
import shutil
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import create_fingerprint_database 
import os
from converter import load_tester
from shutil import copy
import ntpath
from proprocess import get_sec,getLength,trimmer
import main_menu
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
import json
import glob
from os import path

if not os.path.exists("fingerprints"):
    os.makedirs("fingerprints")
if not os.path.exists("audio_output"):
    os.makedirs("audio_output")
if not os.path.exists("jsons"):
    os.makedirs("jsons")



# with open("dejavu.cnf.SAMPLE") as f:
#     config = json.load(f)

database = str(os.getcwd() + "/" + str("fingerprint_database.db")).replace("\\","/")
create_fingerprint_database.create_database_and_tables(database)
with open("dejavu.cnf.SQLITE_SAMPLE") as f:
    config = json.load(f)
djv = Dejavu(config)

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
default_path = os.path.dirname(os.path.abspath(__file__))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(740, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 715, 580))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        self.Video = QtGui.QWidget(self.centralwidget)
        self.Video.setGeometry(QtCore.QRect(0, 0, 715, 580))
        self.Video.setObjectName(_fromUtf8("Video"))

        self.Audio = QtGui.QWidget(self.centralwidget)
        self.Audio.setGeometry(QtCore.QRect(0, 0, 715, 580))
        self.Audio.setObjectName(_fromUtf8("Audio"))

        
        self.Client_label = QtGui.QLabel(self.Video)
        self.Client_label.setGeometry(QtCore.QRect(10, 50, 100, 20))
        self.Client_label.setText("Client")

        self.Commercial = QtGui.QLabel(self.Video)
        self.Commercial.setGeometry(QtCore.QRect(10, 80, 100, 20))
        self.Commercial.setText("Commercial")

        self.Ad_label = QtGui.QLabel(self.Video)
        self.Ad_label.setGeometry(QtCore.QRect(10, 110, 100, 20))
        self.Ad_label.setText("TV Ad")
        
        
        self.Client_Text_Edit = QtGui.QLineEdit(self.Video)
        self.Client_Text_Edit.setGeometry(QtCore.QRect(80,50,150,20))
        
        self.Commercial_Text_Edit = QtGui.QLineEdit(self.Video)
        self.Commercial_Text_Edit.setGeometry(QtCore.QRect(80,80,150,20))
        
        self.Ad_Text_Edit = QtGui.QLineEdit(self.Video)
        self.Ad_Text_Edit.setGeometry(QtCore.QRect(80,110,500,20))

        self.browse = QtGui.QPushButton(self.Video)
        self.browse.setGeometry(QtCore.QRect(600,105,75,25))
        self.browse.setText("Browse")



        self.add_ad = QtGui.QPushButton(self.Video)
        self.add_ad.setGeometry(QtCore.QRect(600,135,75,25))
        self.add_ad.setText("More Ad")

        
        self.fingerprint = QtGui.QPushButton(self.Video)
        self.fingerprint.setGeometry(QtCore.QRect(600,510,100,25))
        self.fingerprint.setText("Fingerprint")
        
        self.browse.clicked.connect(self.browse_ad_additional_button_click)
        self.add_ad.clicked.connect(self.more_ad_add)
        self.count = 0 

        self.Client_label_2 = QtGui.QLabel(self.Video)
        self.Commercial_2 = QtGui.QLabel(self.Video)
        self.Ad_label_2 = QtGui.QLabel(self.Video)
        self.Client_Text_Edit_2 = QtGui.QLineEdit(self.Video)
        self.Client_Text_Edit_2.hide()
        self.Commercial_Text_Edit_2 = QtGui.QLineEdit(self.Video)
        self.Commercial_Text_Edit_2.hide()
        self.Ad_Text_Edit_2 = QtGui.QLineEdit(self.Video)
        self.Ad_Text_Edit_2.hide()
        self.browse_2 = QtGui.QPushButton(self.Video)
        self.browse_2.clicked.connect(self.browse_ad_additional_button_click_2)
        self.remove = QtGui.QPushButton(self.Video)
        self.remove.hide()

        self.Client_label_3 = QtGui.QLabel(self.Video)
        self.Commercial_3 = QtGui.QLabel(self.Video)
        self.Ad_label_3 = QtGui.QLabel(self.Video)
        self.Client_Text_Edit_3 = QtGui.QLineEdit(self.Video)
        self.Commercial_Text_Edit_3 = QtGui.QLineEdit(self.Video)
        self.Ad_Text_Edit_3 = QtGui.QLineEdit(self.Video)
        self.browse_3 = QtGui.QPushButton(self.Video)
        self.browse_3.clicked.connect(self.browse_ad_additional_button_click_3)
        self.remove_2 = QtGui.QPushButton(self.Video)
        self.remove_2.hide()
        self.Client_Text_Edit_3.hide()

        self.Commercial_Text_Edit_3.hide()

        self.Ad_Text_Edit_3.hide()


        self.Client_label_4 = QtGui.QLabel(self.Video)
        self.Commercial_4 = QtGui.QLabel(self.Video)
        self.Ad_label_4 = QtGui.QLabel(self.Video)
        self.Client_Text_Edit_4 = QtGui.QLineEdit(self.Video)
        self.Commercial_Text_Edit_4 = QtGui.QLineEdit(self.Video)
        self.Ad_Text_Edit_4 = QtGui.QLineEdit(self.Video)
        self.browse_4 = QtGui.QPushButton(self.Video)
        self.browse_4.clicked.connect(self.browse_ad_additional_button_click_4)
        self.remove_3 = QtGui.QPushButton(self.Video)
        self.remove_3.hide()
        self.Client_Text_Edit_4.hide()

        self.Commercial_Text_Edit_4.hide()

        self.Ad_Text_Edit_4.hide()
        self.browse_4.hide()
        self.browse_3.hide()
        self.browse_2.hide()

        Client = ""
        Commercial = ""
        Ad = ""
        self.Client_Text_Edit.setText(str(Client))
        self.Commercial_Text_Edit.setText(str(Commercial))
        self.Ad_Text_Edit.setText(str(Ad))
        
        # self.Client_Text_Edit.text()
        # self.Commercial.text()
        # self.Ad_Text_Edit.text()

        Client_2 = ""
        Commercial_2 = ""
        Ad_2 = ""
        self.Client_Text_Edit_2.setText(str(Client_2))
        self.Commercial_Text_Edit_2.setText(str(Commercial_2))
        self.Ad_Text_Edit_2.setText(str(Ad_2))
        self.Client_Text_Edit_2.text()
        self.Commercial_2.text()
        self.Ad_Text_Edit_2.text()

        Client_3 = ""
        Commercial_3 = ""
        Ad_3 = ""
        self.Client_Text_Edit_3.setText(str(Client_3))
        self.Commercial_Text_Edit_3.setText(str(Commercial_3))
        self.Ad_Text_Edit_3.setText(str(Ad_3))

        self.Client_Text_Edit_3.text()
        self.Commercial_3.text()
        self.Ad_Text_Edit_3.text()


        Client_4 = ""
        Commercial_4 = ""
        Ad_4 = ""
        self.Client_Text_Edit_4.setText(str(Client_4))
        self.Commercial_Text_Edit_4.setText(str(Commercial_4))
        self.Ad_Text_Edit_4.setText(str(Ad_4))

        self.Client_Text_Edit_4.text()
        self.Commercial_4.text()
        self.Ad_Text_Edit_4.text()





        self.fingerprint.clicked.connect(lambda x: self.fingerprint_button(
            [str(self.Client_Text_Edit.text()),str(self.Client_Text_Edit_2.text()),str(self.Client_Text_Edit_3.text()),str(self.Client_Text_Edit_4.text())],
            [str(self.Commercial_Text_Edit.text()),str(self.Commercial_Text_Edit_2.text()),str(self.Commercial_Text_Edit_3.text()),str(self.Commercial_Text_Edit_4.text())],
            [str(self.Ad_Text_Edit.text()),str(self.Ad_Text_Edit_2.text()),str(self.Ad_Text_Edit_3.text()),str(self.Ad_Text_Edit_4.text())]))


        self.tabWidget.addTab(self.Video, _fromUtf8(""))
        self.tabWidget.addTab(self.Audio, _fromUtf8(""))

        MainWindow.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Video), _translate("MainWindow", "Video", None))        











        """-----------------------------AudioTab----------------------------"""









        self.audio_Client_label = QtGui.QLabel(self.Audio)
        self.audio_Client_label.setGeometry(QtCore.QRect(10, 50, 100, 20))
        self.audio_Client_label.setText("Client")

        self.audio_Commercial = QtGui.QLabel(self.Audio)
        self.audio_Commercial.setGeometry(QtCore.QRect(10, 80, 100, 20))
        self.audio_Commercial.setText("Commercial")

        self.audio_Ad_label = QtGui.QLabel(self.Audio)
        self.audio_Ad_label.setGeometry(QtCore.QRect(10, 110, 100, 20))
        self.audio_Ad_label.setText("Radio Ad")
        
        
        self.audio_Client_Text_Edit = QtGui.QLineEdit(self.Audio)
        self.audio_Client_Text_Edit.setGeometry(QtCore.QRect(80,50,150,20))
        
        self.audio_Commercial_Text_Edit = QtGui.QLineEdit(self.Audio)
        self.audio_Commercial_Text_Edit.setGeometry(QtCore.QRect(80,80,150,20))
        
        self.audio_Ad_Text_Edit = QtGui.QLineEdit(self.Audio)
        self.audio_Ad_Text_Edit.setGeometry(QtCore.QRect(80,110,500,20))



        self.audio_browse = QtGui.QPushButton(self.Audio)
        self.audio_browse.setGeometry(QtCore.QRect(600,105,75,25))
        self.audio_browse.setText("Browse")



        self.audio_add_ad = QtGui.QPushButton(self.Audio)
        self.audio_add_ad.setGeometry(QtCore.QRect(600,135,75,25))
        self.audio_add_ad.setText("More Ad")

        
        self.audio_fingerprint = QtGui.QPushButton(self.Audio)
        self.audio_fingerprint.setGeometry(QtCore.QRect(600,510,100,25))
        self.audio_fingerprint.setText("Fingerprint")
        
        self.audio_browse.clicked.connect(self.audio_browse_ad_additional_button_click)
        self.audio_add_ad.clicked.connect(self.audio_more_ad_add)
        self.audio_count = 0 

        self.audio_Client_label_2 = QtGui.QLabel(self.Audio)
        self.audio_Commercial_2 = QtGui.QLabel(self.Audio)
        self.audio_Ad_label_2 = QtGui.QLabel(self.Audio)
        self.audio_Client_Text_Edit_2 = QtGui.QLineEdit(self.Audio)
        self.audio_Client_Text_Edit_2.hide()
        self.audio_Commercial_Text_Edit_2 = QtGui.QLineEdit(self.Audio)
        self.audio_Commercial_Text_Edit_2.hide()
        self.audio_Ad_Text_Edit_2 = QtGui.QLineEdit(self.Audio)
        self.audio_Ad_Text_Edit_2.hide()
        self.audio_browse_2 = QtGui.QPushButton(self.Audio)
        self.audio_browse_2.clicked.connect(self.audio_browse_ad_additional_button_click_2)
        self.audio_remove = QtGui.QPushButton(self.Audio)
        self.audio_remove.hide()

        self.audio_Client_label_3 = QtGui.QLabel(self.Audio)
        self.audio_Commercial_3 = QtGui.QLabel(self.Audio)
        self.audio_Ad_label_3 = QtGui.QLabel(self.Audio)
        self.audio_Client_Text_Edit_3 = QtGui.QLineEdit(self.Audio)
        self.audio_Commercial_Text_Edit_3 = QtGui.QLineEdit(self.Audio)
        self.audio_Ad_Text_Edit_3 = QtGui.QLineEdit(self.Audio)
        self.audio_browse_3 = QtGui.QPushButton(self.Audio)
        self.audio_browse_3.clicked.connect(self.audio_browse_ad_additional_button_click_3)
        self.audio_remove_2 = QtGui.QPushButton(self.Audio)
        self.audio_remove_2.hide()
        self.audio_Client_Text_Edit_3.hide()

        self.audio_Commercial_Text_Edit_3.hide()

        self.audio_Ad_Text_Edit_3.hide()


        self.audio_Client_label_4 = QtGui.QLabel(self.Audio)
        self.audio_Commercial_4 = QtGui.QLabel(self.Audio)
        self.audio_Ad_label_4 = QtGui.QLabel(self.Audio)
        self.audio_Client_Text_Edit_4 = QtGui.QLineEdit(self.Audio)
        self.audio_Commercial_Text_Edit_4 = QtGui.QLineEdit(self.Audio)
        self.audio_Ad_Text_Edit_4 = QtGui.QLineEdit(self.Audio)
        self.audio_browse_4 = QtGui.QPushButton(self.Audio)
        self.audio_browse_4.clicked.connect(self.audio_browse_ad_additional_button_click_4)
        self.audio_remove_3 = QtGui.QPushButton(self.Audio)
        self.audio_remove_3.hide()
        self.audio_Client_Text_Edit_4.hide()

        self.audio_Commercial_Text_Edit_4.hide()

        self.audio_Ad_Text_Edit_4.hide()
        self.audio_browse_4.hide()
        self.audio_browse_3.hide()
        self.audio_browse_2.hide()

        audio_Client = ""
        audio_Commercial = ""
        audio_Ad = ""
        self.audio_Client_Text_Edit.setText(str(Client))
        self.audio_Commercial_Text_Edit.setText(str(Commercial))
        self.audio_Ad_Text_Edit.setText(str(Ad))
        
        # self.Client_Text_Edit.text()
        # self.Commercial.text()
        # self.Ad_Text_Edit.text()

        audio_Client_2 = ""
        audio_Commercial_2 = ""
        audio_Ad_2 = ""
        self.audio_Client_Text_Edit_2.setText(str(Client_2))
        self.audio_Commercial_Text_Edit_2.setText(str(Commercial_2))
        self.audio_Ad_Text_Edit_2.setText(str(Ad_2))
        self.audio_Client_Text_Edit_2.text()
        self.audio_Commercial_2.text()
        self.audio_Ad_Text_Edit_2.text()

        audio_Client_3 = ""
        audio_Commercial_3 = ""
        audio_Ad_3 = ""
        self.audio_Client_Text_Edit_3.setText(str(Client_3))
        self.audio_Commercial_Text_Edit_3.setText(str(Commercial_3))
        self.audio_Ad_Text_Edit_3.setText(str(Ad_3))

        self.audio_Client_Text_Edit_3.text()
        self.audio_Commercial_3.text()
        self.audio_Ad_Text_Edit_3.text()


        audio_Client_4 = ""
        audio_Commercial_4 = ""
        audio_Ad_4 = ""
        self.audio_Client_Text_Edit_4.setText(str(Client_4))
        self.audio_Commercial_Text_Edit_4.setText(str(Commercial_4))
        self.audio_Ad_Text_Edit_4.setText(str(Ad_4))

        self.audio_Client_Text_Edit_4.text()
        self.audio_Commercial_4.text()
        self.audio_Ad_Text_Edit_4.text()

        self.back = QtGui.QPushButton(self.Video)
        self.back.setGeometry(QtCore.QRect(500,510,100,25))
        self.back.setText("Back")

        self.audio_back = QtGui.QPushButton(self.Audio)
        self.audio_back.setGeometry(QtCore.QRect(500,510,100,25))
        self.audio_back.setText("Back")
        
        self.back.clicked.connect(lambda x: self.back_button(MainWindow))
        self.audio_back.clicked.connect(lambda x: self.back_button(MainWindow))




        self.audio_fingerprint.clicked.connect(lambda x: self.audio_fingerprint_button(
            [str(self.audio_Client_Text_Edit.text()),str(self.audio_Client_Text_Edit_2.text()),str(self.audio_Client_Text_Edit_3.text()),str(self.audio_Client_Text_Edit_4.text())],
            [str(self.audio_Commercial_Text_Edit.text()),str(self.audio_Commercial_Text_Edit_2.text()),str(self.audio_Commercial_Text_Edit_3.text()),str(self.audio_Commercial_Text_Edit_4.text())],
            [str(self.audio_Ad_Text_Edit.text()),str(self.audio_Ad_Text_Edit_2.text()),str(self.audio_Ad_Text_Edit_3.text()),str(self.audio_Ad_Text_Edit_4.text())]))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Audio), _translate("MainWindow", "Audio", None))

    def browse_ad_additional_button_click(self):
        self.Ad_Text_Edit.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Video" ,default_path,"Video (*.mpg *.flv *.wmv *.mpv *.mp4 *.avi)"))
    def browse_ad_additional_button_click_2(self):
        self.Ad_Text_Edit_2.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Video" ,default_path,"Video (*.mpg *.flv *.wmv *.mpv *.mp4 *.avi)"))
    def browse_ad_additional_button_click_3(self):
        self.Ad_Text_Edit_3.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Video" ,default_path,"Video (*.mpg *.flv *.wmv *.mpv *.mp4 *.avi)"))
    def browse_ad_additional_button_click_4(self):
        self.Ad_Text_Edit_4.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Video" ,default_path,"Video (*.mpg *.flv *.wmv *.mpv *.mp4 *.avi)"))
    def more_ad_add(self):
        self.count += 1 
        if self.count ==1:
            self.Client_label_2.setGeometry(QtCore. QRect(10, 50+self.count*120, 100, 20))
            self.Client_label_2.setText("Client_" + str(self.count))
            self.Commercial_2.setGeometry(QtCore.QRect(10, 80+self.count*120, 100, 20))
            self.Commercial_2.setText("Commercial_" + str(self.count))
            self.Ad_label_2.setGeometry(QtCore.QRect(10, 110+self.count*120, 100, 20))
            self.Ad_label_2.setText("Ad_" + str(self.count))
            self.Client_Text_Edit_2.setGeometry(QtCore.QRect(80,50+self.count*120,150,20))
            self.Commercial_Text_Edit_2.setGeometry(QtCore.QRect(80,80+self.count*120,150,20))
            self.Ad_Text_Edit_2.setGeometry(QtCore.QRect(80,110+self.count*120,500,20))
            self.browse_2.setGeometry(QtCore.QRect(600,105+self.count*120,75,25))
            self.browse_2.setText("Browse")
            self.remove.setGeometry(QtCore.QRect(600,80+self.count*120,75,25))
            self.remove.setText("Remove")
            self.Client_label_2.show()
            self.Commercial_2.show()
            self.Ad_label_2.show()
            self.Client_Text_Edit_2.show()
            self.Commercial_Text_Edit_2.show()
            self.Ad_Text_Edit_2.show()
            self.browse_2.show()
            self.remove.show()
            self.remove.clicked.connect(lambda x: self.remove_button(self.count))
        if self.count ==2:
            self.Client_label_3.setGeometry(QtCore.QRect(10, 50+self.count*120, 100, 20))
            self.Client_label_3.setText("Client_" + str(self.count))
            self.Commercial_3.setGeometry(QtCore.QRect(10, 80+self.count*120, 100, 20))
            self.Commercial_3.setText("Commercial_" + str(self.count))
            self.Ad_label_3.setGeometry(QtCore.QRect(10, 110+self.count*120, 100, 20))
            self.Ad_label_3.setText("Ad_" + str(self.count))
            self.Client_Text_Edit_3.setGeometry(QtCore.QRect(80,50+self.count*120,150,20))
            self.Commercial_Text_Edit_3.setGeometry(QtCore.QRect(80,80+self.count*120,150,20))
            self.Ad_Text_Edit_3.setGeometry(QtCore.QRect(80,110+self.count*120,500,20))
            self.browse_3.setGeometry(QtCore.QRect(600,105+self.count*120,75,25))
            self.browse_3.setText("Browse")
            self.remove_2.setGeometry(QtCore.QRect(600,80+self.count*120,75,25))
            self.remove_2.setText("Remove")
            self.Client_label_3.show()
            self.Commercial_3.show()
            self.Ad_label_3.show()
            self.Client_Text_Edit_3.show()
            self.Commercial_Text_Edit_3.show()
            self.Ad_Text_Edit_3.show()
            self.browse_3.show()
            self.remove.setDisabled(True)
            self.remove_2.show()
            self.remove_2.clicked.connect(lambda x: self.remove_button_2(self.count))

        if self.count ==3:
            self.Client_label_4.setGeometry(QtCore.QRect(10, 50+self.count*120, 100, 20))
            self.Client_label_4.setText("Client_" + str(self.count))

            self.Commercial_4.setGeometry(QtCore.QRect(10, 80+self.count*120, 100, 20))
            self.Commercial_4.setText("Commercial_" + str(self.count))
            self.Ad_label_4.setGeometry(QtCore.QRect(10, 110+self.count*120, 100, 20))
            self.Ad_label_4.setText("Ad_" + str(self.count))
            self.Client_Text_Edit_4.setGeometry(QtCore.QRect(80,50+self.count*120,150,20))
            self.Commercial_Text_Edit_4.setGeometry(QtCore.QRect(80,80+self.count*120,150,20))
            self.Ad_Text_Edit_4.setGeometry(QtCore.QRect(80,110+self.count*120,500,20))
            self.browse_4.setGeometry(QtCore.QRect(600,105+self.count*120,75,25))
            self.browse_4.setText("Browse")
            self.remove_3.setGeometry(QtCore.QRect(600,80+self.count*120,75,25))
            self.remove_3.setText("Remove")
            self.Client_label_4.show()
            self.Commercial_4.show()
            self.Ad_label_4.show()
            self.Client_Text_Edit_4.show()
            self.Commercial_Text_Edit_4.show()
            self.Ad_Text_Edit_4.show()
            self.browse_4.show()
            self.remove_2.setDisabled(True)
            self.remove_3.show()
            self.remove_3.clicked.connect(lambda x: self.remove_button_3(self.count))


    def remove_button(self,count):
        self.Client_label_2.hide()
        self.Commercial_2.hide()
        self.Ad_label_2.hide()
        self.Client_Text_Edit_2.hide()
        self.Commercial_Text_Edit_2.hide()
        self.Ad_Text_Edit_2.hide()
        self.browse_2.hide()
        self.remove.hide()
        self.count = 0

    def remove_button_2(self,count):
        self.Client_label_3.hide()
        self.Commercial_3.hide()
        self.Ad_label_3.hide()
        self.Client_Text_Edit_3.hide()
        self.Commercial_Text_Edit_3.hide()
        self.Ad_Text_Edit_3.hide()
        self.browse_3.hide()
        self.remove_2.hide()
        self.remove.setDisabled(False)

        self.count = 1
    def remove_button_3(self,count):
        self.Client_label_4.hide()
        self.Commercial_4.hide()
        self.Ad_label_4.hide()
        self.Client_Text_Edit_4.hide()
        self.Commercial_Text_Edit_4.hide()
        self.Ad_Text_Edit_4.hide()
        self.browse_4.hide()
        self.remove_3.hide()
        self.remove_2.setDisabled(False)
        self.count = 2

    def fingerprint_button(self,Client,Commercial,Ad):
        original_json = []
        renamed_json = []
        json_filename = []
        fingerprint_script = "ruby dupe.rb"
        fingerprint_array = []
        json_files = []
        files = glob.glob(os.getcwd() + "/fingerprints/" + str('*'))
        for i in range(self.count + 1):
            
            if path.exists(os.getcwd() + "/jsons/" + str(Commercial[i] + ".json")):
                print (str(Commercial[i] + ".json") + str(" Fingerprint Already Exists, Do you want to overwrite?"))
                break
            
            else:
                #fingerprint_script.append("ruby dupe.rb " + str(Commercial[i]))
                #fingerprint_script
                copy(str(Ad[i]),"fingerprints")        
                print(str("Fingerprinting: ") + str(Ad[i])) + str(" Video_") + str(i)
            
                os.system(fingerprint_script)
                
                for video_file in os.listdir("fingerprints"):
                    if video_file.lower().endswith((".mp4",".flv",".mpg",".avi",".wmv",".mpv")):
                        os.remove(os.getcwd() + "/fingerprints/" + video_file)        

  
                for file in os.listdir("fingerprints"):
                    if file.endswith(".json"):
                        json_files.append(file)
            
                original_json.append((os.getcwd() + "/fingerprints/" + str(json_files[i])).replace("\\","/"))
                renamed_json.append(os.getcwd() + "/jsons/" + str(Commercial[i] + ".json"))
                os.rename(original_json[i],renamed_json[i])
                fingerprint_array.append(load_tester(renamed_json[i]))
                Ad_Duration = getLength(Ad[i])
                create_fingerprint_database.insert_video_information_to_database(database,str(Client[i]),str(Commercial[i]),str(Ad[i]),str(Ad_Duration),str(fingerprint_array[i]),str(renamed_json[i]))
        for f in files:
            os.remove(f)
        exit()







    """-------------------------AudioMethods--------------------------"""







    def audio_browse_ad_additional_button_click(self):
        self.audio_Ad_Text_Edit.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Audio" ,default_path,"Audio (*.mp3 *.wma *.wav)"))
    def audio_browse_ad_additional_button_click_2(self):
        self.audio_Ad_Text_Edit_2.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Audio" ,default_path,"Audio (*.mp3 *.wma *.wav)"))
    def audio_browse_ad_additional_button_click_3(self):
        self.audio_Ad_Text_Edit_3.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Audio" ,default_path,"Audio (*.mp3 *.wma *.wav)"))
    def audio_browse_ad_additional_button_click_4(self):
        self.audio_Ad_Text_Edit_4.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Audio" ,default_path,"Audio (*.mp3 *.wma *.wav)"))
    def audio_more_ad_add(self):
        self.audio_count += 1 
        if self.audio_count ==1:
            self.audio_Client_label_2.setGeometry(QtCore. QRect(10, 50+self.audio_count*120, 100, 20))
            self.audio_Client_label_2.setText("Client_" + str(self.audio_count))
            self.audio_Commercial_2.setGeometry(QtCore.QRect(10, 80+self.audio_count*120, 100, 20))
            self.audio_Commercial_2.setText("Commercial_" + str(self.audio_count))
            self.audio_Ad_label_2.setGeometry(QtCore.QRect(10, 110+self.audio_count*120, 100, 20))
            self.audio_Ad_label_2.setText("Radio Ad_" + str(self.audio_count))
            self.audio_Client_Text_Edit_2.setGeometry(QtCore.QRect(80,50+self.audio_count*120,150,20))
            self.audio_Commercial_Text_Edit_2.setGeometry(QtCore.QRect(80,80+self.audio_count*120,150,20))
            self.audio_Ad_Text_Edit_2.setGeometry(QtCore.QRect(80,110+self.audio_count*120,500,20))
            self.audio_browse_2.setGeometry(QtCore.QRect(600,105+self.audio_count*120,75,25))
            self.audio_browse_2.setText("Browse")
            self.audio_remove.setGeometry(QtCore.QRect(600,80+self.audio_count*120,75,25))
            self.audio_remove.setText("Remove")
            self.audio_Client_label_2.show()
            self.audio_Commercial_2.show()
            self.audio_Ad_label_2.show()
            self.audio_Client_Text_Edit_2.show()
            self.audio_Commercial_Text_Edit_2.show()
            self.audio_Ad_Text_Edit_2.show()
            self.audio_browse_2.show()
            self.audio_remove.show()
            self.audio_remove.clicked.connect(lambda x: self.audio_remove_button(self.audio_count))
        if self.audio_count ==2:
            self.audio_Client_label_3.setGeometry(QtCore.QRect(10, 50+self.audio_count*120, 100, 20))
            self.audio_Client_label_3.setText("Client_" + str(self.audio_count))
            self.audio_Commercial_3.setGeometry(QtCore.QRect(10, 80+self.audio_count*120, 100, 20))
            self.audio_Commercial_3.setText("Commercial_" + str(self.audio_count))
            self.audio_Ad_label_3.setGeometry(QtCore.QRect(10, 110+self.audio_count*120, 100, 20))
            self.audio_Ad_label_3.setText("Radio Ad_" + str(self.audio_count))
            self.audio_Client_Text_Edit_3.setGeometry(QtCore.QRect(80,50+self.audio_count*120,150,20))
            self.audio_Commercial_Text_Edit_3.setGeometry(QtCore.QRect(80,80+self.audio_count*120,150,20))
            self.audio_Ad_Text_Edit_3.setGeometry(QtCore.QRect(80,110+self.audio_count*120,500,20))
            self.audio_browse_3.setGeometry(QtCore.QRect(600,105+self.audio_count*120,75,25))
            self.audio_browse_3.setText("Browse")
            self.audio_remove_2.setGeometry(QtCore.QRect(600,80+self.audio_count*120,75,25))
            self.audio_remove_2.setText("Remove")
            self.audio_Client_label_3.show()
            self.audio_Commercial_3.show()
            self.audio_Ad_label_3.show()
            self.audio_Client_Text_Edit_3.show()
            self.audio_Commercial_Text_Edit_3.show()
            self.audio_Ad_Text_Edit_3.show()
            self.audio_browse_3.show()
            self.audio_remove.setDisabled(True)
            self.audio_remove_2.show()
            self.audio_remove_2.clicked.connect(lambda x: self.audio_remove_button_2(self.audio_count))

        if self.audio_count ==3:
            self.audio_Client_label_4.setGeometry(QtCore.QRect(10, 50+self.audio_count*120, 100, 20))
            self.audio_Client_label_4.setText("Client_" + str(self.audio_count))

            self.audio_Commercial_4.setGeometry(QtCore.QRect(10, 80+self.audio_count*120, 100, 20))
            self.audio_Commercial_4.setText("Commercial_" + str(self.audio_count))
            self.audio_Ad_label_4.setGeometry(QtCore.QRect(10, 110+self.audio_count*120, 100, 20))
            self.audio_Ad_label_4.setText("Radio Ad_" + str(self.count))
            self.audio_Client_Text_Edit_4.setGeometry(QtCore.QRect(80,50+self.audio_count*120,150,20))
            self.audio_Commercial_Text_Edit_4.setGeometry(QtCore.QRect(80,80+self.audio_count*120,150,20))
            self.audio_Ad_Text_Edit_4.setGeometry(QtCore.QRect(80,110+self.audio_count*120,500,20))
            self.audio_browse_4.setGeometry(QtCore.QRect(600,105+self.audio_count*120,75,25))
            self.audio_browse_4.setText("Browse")
            self.audio_remove_3.setGeometry(QtCore.QRect(600,80+self.audio_count*120,75,25))
            self.audio_remove_3.setText("Remove")
            self.audio_Client_label_4.show()
            self.audio_Commercial_4.show()
            self.audio_Ad_label_4.show()
            self.audio_Client_Text_Edit_4.show()
            self.audio_Commercial_Text_Edit_4.show()
            self.audio_Ad_Text_Edit_4.show()
            self.audio_browse_4.show()
            self.audio_remove_2.setDisabled(True)
            self.audio_remove_3.show()
            self.audio_remove_3.clicked.connect(lambda x: self.audio_remove_button_3(self.audio_count))

    
    def audio_remove_button(self,count):
        self.audio_Client_label_2.hide()
        self.audio_Commercial_2.hide()
        self.audio_Ad_label_2.hide()
        self.audio_Client_Text_Edit_2.hide()
        self.audio_Commercial_Text_Edit_2.hide()
        self.audio_Ad_Text_Edit_2.hide()
        self.audio_browse_2.hide()
        self.audio_remove.hide()
        self.audio_count = 0

    def audio_remove_button_2(self,count):
        self.audio_Client_label_3.hide()
        self.audio_Commercial_3.hide()
        self.audio_Ad_label_3.hide()
        self.audio_Client_Text_Edit_3.hide()
        self.audio_Commercial_Text_Edit_3.hide()
        self.audio_Ad_Text_Edit_3.hide()
        self.audio_browse_3.hide()
        self.audio_remove_2.hide()
        self.audio_remove.setDisabled(False)

        self.audio_count = 1
    def audio_remove_button_3(self,count):
        self.audio_Client_label_4.hide()
        self.audio_Commercial_4.hide()
        self.audio_Ad_label_4.hide()
        self.audio_Client_Text_Edit_4.hide()
        self.audio_Commercial_Text_Edit_4.hide()
        self.audio_Ad_Text_Edit_4.hide()
        self.audio_browse_4.hide()
        self.audio_remove_3.hide()
        self.audio_remove_2.setDisabled(False)
        self.audio_count = 2

    def audio_fingerprint_button(self,Client,Commercial,Ad):
        for i in range(self.audio_count + 1):            
            if not os.path.exists("audio_output"):
              os.makedirs("audio_output")
            copy(str(Ad[i]),"audio_output")
            Ad_Duration = getLength(Ad[i])
            create_fingerprint_database.insert_audio_information_to_database(database,str(Client[i]),str(Commercial[i]),str(Ad[i]),str(Ad_Duration))
        djv.fingerprint_directory(os.getcwd() + "/audio_output/", [".mp3"])
        for audio_file in os.listdir("audio_output"):
            if audio_file.lower().endswith((".mp3",".wma",".wav")):
                os.remove(os.getcwd() + "/audio_output/" + audio_file)  
        exit()
    def back_button(self,MainWindow):
        main_menu_ui = main_menu.Ui_MainWindow()
        main_menu_ui.setupUi(MainWindow)
        MainWindow.show()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
