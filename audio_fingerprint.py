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


if not os.path.exists("fingerprints"):
    os.makedirs("fingerprints")
if not os.path.exists("jsons"):
    os.makedirs("jsons")
database = str(os.getcwd() + "/" + str("fingerprint_database.db")).replace("\\","/")
create_fingerprint_database.create_database_and_tables(database)

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
        
        self.Client_label = QtGui.QLabel(self.Video)
        self.Client_label.setGeometry(QtCore.QRect(10, 50, 100, 20))
        self.Client_label.setText("Client")

        self.Commercial = QtGui.QLabel(self.Video)
        self.Commercial.setGeometry(QtCore.QRect(10, 80, 100, 20))
        self.Commercial.setText("Commercial")

        self.Ad_label = QtGui.QLabel(self.Video)
        self.Ad_label.setGeometry(QtCore.QRect(10, 110, 100, 20))
        self.Ad_label.setText("Ad")
        
        
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Video), _translate("MainWindow", "Video", None))

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
        # fingerprint_script = "ruby dupe.rb"
        # for i in range(self.count + 1):            
        #     if not os.path.exists("fingerprints"):
        #         os.makedirs("fingerprints")
        #     copy(str(Ad[i]),"fingerprints")        
        #     print(str("Fingerprinting: ") + str(Ad[i])) + str(" Video_") + str(i)
        #     os.system(fingerprint_script)
        #     json_filename = ntpath.basename(str(Ad[i])) + str(".json")
        #     #if-else statment needed to check fingerprint overwriting 
        #     json_path = (os.getcwd() + str("/") + str("fingerprints") + str("/") + json_filename).replace("\\","/")
        #     copy(json_path,"jsons")
        #     fingerprint_array = load_tester(json_path)
        #     Ad_Duration = getLength(Ad[i])
        #     create_fingerprint_database.insert_information_to_database(database,str(Client[i]),str(Commercial[i]),str(Ad[i]),str(Ad_Duration),str(fingerprint_array))
        #     shutil.rmtree((os.getcwd() + str("/") + "fingerprints").replace("\\","/")) 
        # exit()
        pass 
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
