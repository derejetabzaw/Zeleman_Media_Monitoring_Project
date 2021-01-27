# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import create_fingerprint_database 
import search_page
import audio_search_page
import main_menu
import scenesplit as split
import sqed_dir as sqd
from shutil import copy
import sqed
from os import path
import time_converter
import datetime 
from ethiopian_date import EthiopianDateConverter
import fingerprint

'''Timer --- Will Be removed later '''
import time 
start_time = time.time()

if not os.path.exists("cropped_threshold"):
    os.makedirs("cropped_threshold")
if not os.path.exists("cropped_content"):
    os.makedirs("cropped_content")

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

database = str(os.getcwd() + "/" + str("fingerprint_database.db")).replace("\\","/")

conv = EthiopianDateConverter.to_ethiopian
      
class Ui_MainWindow(object):
    def setupUi(self, MainWindow,scan_type):
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

        self.back = QtGui.QPushButton(self.Video)
        self.back.setGeometry(QtCore.QRect(500,510,100,25))
        self.back.setText("Back")

        self.audio_back = QtGui.QPushButton(self.Audio)
        self.audio_back.setGeometry(QtCore.QRect(500,510,100,25))
        self.audio_back.setText("Back")




        self.TV_Stations = QtGui.QLabel(self.Video)
        self.TV_Stations.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.TV_Stations.setText("TV Station")
        
        self.Tv_Station_Choice = QtGui.QComboBox(self.Video)
        self.Tv_Station_Choice.setGeometry(QtCore.QRect(80,20,150,20))
        
        self.Tv_Station_Add_Choice = QtGui.QPushButton(self.Video)
        self.Tv_Station_Add_Choice.setGeometry(QtCore.QRect(240,17,75,25))
        self.Tv_Station_Add_Choice.setText("Add")
        self.Tv_Station_Add_Choice.clicked.connect(lambda x: self.add_tv_station(MainWindow))
        
    
        self.Tv_Station_Choice.addItems(["EBC","EBS","FANA","ARTS","WALTA"])




        
        self.upload_stream_label = QtGui.QLabel(self.Video)
        self.upload_stream_label.setGeometry(QtCore.QRect(10, 50, 100, 20))
        self.upload_stream_label.setText("TV Stream")

        self.upload_stream_Text_Edit = QtGui.QLineEdit(self.Video)
        self.upload_stream_Text_Edit.setGeometry(QtCore.QRect(80,50,530,20))
 
       	self.browse = QtGui.QPushButton(self.Video)
        self.browse.setGeometry(QtCore.QRect(630,50,75,20))
        self.browse.setText("Browse")


        self.Commercial = QtGui.QLabel(self.Video)
        self.Commercial.setGeometry(QtCore.QRect(10, 120, 100, 20))
        self.Commercial.setText("Commercial")




        self.Commercial_Text_Edit = QtGui.QLineEdit(self.Video)
        self.Commercial_Text_Edit.setGeometry(QtCore.QRect(80,120,150,20))

        self.add_commercial = QtGui.QPushButton(self.Video)
        self.add_commercial.setGeometry(QtCore.QRect(260,120,50,20))
        self.add_commercial.setText("Add")

        self.clear_button = QtGui.QPushButton(self.Video)
        self.clear_button.hide()

        self.clear_button_2 = QtGui.QPushButton(self.Video)
        self.clear_button_2.hide()

        self.clear_button_3 = QtGui.QPushButton(self.Video)
        self.clear_button_3.hide()

        
        self.Commercial_1 = QtGui.QLabel(self.Video)
        # self.Commercial_1.setGeometry(QtCore.QRect(10, 160, 100, 20))
        # self.Commercial_1.setText("Commercial_1")

        self.Commercial_Text_Edit_1 = QtGui.QLineEdit(self.Video)
        self.Commercial_Text_Edit_1.setGeometry(QtCore.QRect(80,160,150,20))
        self.Commercial_Text_Edit_1.hide()

        self.Commercial_2 = QtGui.QLabel(self.Video)
        # self.Commercial_2.setGeometry(QtCore.QRect(10, 200, 100, 20))
        # self.Commercial_2.setText("Commercial_2")

       	self.Commercial_Text_Edit_2 = QtGui.QLineEdit(self.Video)
        self.Commercial_Text_Edit_2.setGeometry(QtCore.QRect(80,200,150,20))
        self.Commercial_Text_Edit_2.hide()

        self.Commercial_3 = QtGui.QLabel(self.Video)


       	self.Commercial_Text_Edit_3 = QtGui.QLineEdit(self.Video)
        self.Commercial_Text_Edit_3.setGeometry(QtCore.QRect(80,240,150,20)) 
        self.Commercial_Text_Edit_3.hide()

        self.browse.clicked.connect(self.browse_ad_additional_button_click)
        self.add_commercial.clicked.connect(self.more_ad_add)
        self.count = 0 




        self.search = QtGui.QPushButton(self.Video)
        self.search.setGeometry(QtCore.QRect(600,510,100,25))
        self.search.setText("Search")
        self.search.clicked.connect(lambda x: self.search_button(MainWindow,database,
        	[str(self.Commercial_Text_Edit.text()),
            str(self.Commercial_Text_Edit_1.text()),
            str(self.Commercial_Text_Edit_2.text()),
            str(self.Commercial_Text_Edit_3.text())],
            str(self.upload_stream_Text_Edit.text()),
            str(self.Tv_Station_Choice.currentText()),scan_type))
        
        self.back.clicked.connect(lambda x: self.back_button(MainWindow))
        self.audio_back.clicked.connect(lambda x: self.back_button(MainWindow))

        self.tabWidget.addTab(self.Video, _fromUtf8(""))
        self.tabWidget.addTab(self.Audio, _fromUtf8(""))


        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Video), _translate("MainWindow", "Video", None))        

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Audio), _translate("MainWindow", "Audio", None))



        MainWindow.setCentralWidget(self.centralwidget)
    

        










        """------------------------------AudioTab-----------------------------------"""
        




        self.Radio_Stations = QtGui.QLabel(self.Audio)
        self.Radio_Stations.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.Radio_Stations.setText("Radio Station")
        self.Radio_Station_Choice = QtGui.QComboBox(self.Audio)
        self.Radio_Station_Choice.setGeometry(QtCore.QRect(80,20,150,20))

        self.Radio_Station_Add_Choice = QtGui.QPushButton(self.Audio)
        self.Radio_Station_Add_Choice.setGeometry(QtCore.QRect(240,17,75,25))
        self.Radio_Station_Add_Choice.setText("Add")
        self.Radio_Station_Add_Choice.clicked.connect(lambda x: self.add_radio_station(MainWindow))

    







        self.audio_upload_stream_label = QtGui.QLabel(self.Audio)
        self.audio_upload_stream_label.setGeometry(QtCore.QRect(10, 50, 100, 20))
        self.audio_upload_stream_label.setText("Radio Stream")

        self.audio_upload_stream_Text_Edit = QtGui.QLineEdit(self.Audio)
        self.audio_upload_stream_Text_Edit.setGeometry(QtCore.QRect(80,50,530,20))
 
        self.audio_browse = QtGui.QPushButton(self.Audio)
        self.audio_browse.setGeometry(QtCore.QRect(630,50,75,20))
        self.audio_browse.setText("Browse")


        self.audio_Commercial = QtGui.QLabel(self.Audio)
        self.audio_Commercial.setGeometry(QtCore.QRect(10, 120, 100, 20))
        self.audio_Commercial.setText("Commercial")




        self.audio_Commercial_Text_Edit = QtGui.QLineEdit(self.Audio)
        self.audio_Commercial_Text_Edit.setGeometry(QtCore.QRect(80,120,150,20))

        self.audio_add_commercial = QtGui.QPushButton(self.Audio)
        self.audio_add_commercial.setGeometry(QtCore.QRect(260,120,50,20))
        self.audio_add_commercial.setText("Add")

        self.audio_clear_button = QtGui.QPushButton(self.Audio)
        self.audio_clear_button.hide()

        self.audio_clear_button_2 = QtGui.QPushButton(self.Audio)
        self.audio_clear_button_2.hide()

        self.audio_clear_button_3 = QtGui.QPushButton(self.Audio)
        self.audio_clear_button_3.hide()

        
        self.audio_Commercial_1 = QtGui.QLabel(self.Audio)
        # self.Commercial_1.setGeometry(QtCore.QRect(10, 160, 100, 20))
        # self.Commercial_1.setText("Commercial_1")

        self.audio_Commercial_Text_Edit_1 = QtGui.QLineEdit(self.Audio)
        self.audio_Commercial_Text_Edit_1.setGeometry(QtCore.QRect(80,160,150,20))
        self.audio_Commercial_Text_Edit_1.hide()

        self.audio_Commercial_2 = QtGui.QLabel(self.Audio)
        # self.Commercial_2.setGeometry(QtCore.QRect(10, 200, 100, 20))
        # self.Commercial_2.setText("Commercial_2")

        self.audio_Commercial_Text_Edit_2 = QtGui.QLineEdit(self.Audio)
        self.audio_Commercial_Text_Edit_2.setGeometry(QtCore.QRect(80,200,150,20))
        self.audio_Commercial_Text_Edit_2.hide()

        self.audio_Commercial_3 = QtGui.QLabel(self.Audio)


        self.audio_Commercial_Text_Edit_3 = QtGui.QLineEdit(self.Audio)
        self.audio_Commercial_Text_Edit_3.setGeometry(QtCore.QRect(80,240,150,20)) 
        self.audio_Commercial_Text_Edit_3.hide()

        self.audio_browse.clicked.connect(self.audio_browse_ad_additional_button_click)
        self.audio_add_commercial.clicked.connect(self.audio_more_ad_add)
        self.audio_count = 0 

        self.Radio_Station_Choice.addItems(["FMADDIS", "SHEGERFM", "AHADU","AFROFM"])

        self.audio_search = QtGui.QPushButton(self.Audio)
        self.audio_search.setGeometry(QtCore.QRect(600,510,100,25))
        self.audio_search.setText("Search")
        self.audio_search.clicked.connect(lambda x: self.audio_search_button(MainWindow,database,
            [str(self.audio_Commercial_Text_Edit.text()),
            str(self.audio_Commercial_Text_Edit_1.text()),
            str(self.audio_Commercial_Text_Edit_2.text()),
            str(self.audio_Commercial_Text_Edit_3.text())],
            str(self.audio_upload_stream_Text_Edit.text()),
            str(self.Radio_Station_Choice.currentText())))
        
    def add_radio_station(self,MainWindow):
        self.dialog_for_radio_station_choice = QtGui.QDialog(self.Audio)
        self.add_radio_option = QtGui.QPushButton("Add",self.dialog_for_radio_station_choice)
        self.RADIO_Option_Text_Edit = QtGui.QLineEdit(self.dialog_for_radio_station_choice)
        self.RADIO_Option_Text_Edit.setGeometry(QtCore.QRect(50,50,150,20))
        self.add_radio_option.move(85,80)
        self.dialog_for_radio_station_choice.setWindowTitle("Add RADIO-Station")
        self.add_radio_option.clicked.connect(lambda x: self.add_options_to_radio_index(MainWindow,str(self.RADIO_Option_Text_Edit.text())))
        self.dialog_for_radio_station_choice.exec_()
    def add_options_to_radio_index(self,MainWindow,new_radio_station):
        self.Radio_Station_Choice.addItem(new_radio_station)
        self.Radio_Station_Choice.setItemText(0,new_radio_station)
        self.dialog_for_radio_station_choice.close()
    








    def add_tv_station(self,MainWindow):
        self.dialog_for_tv_station_choice = QtGui.QDialog(self.Video)
        self.add_option = QtGui.QPushButton("Add",self.dialog_for_tv_station_choice)
        self.TV_Option_Text_Edit = QtGui.QLineEdit(self.dialog_for_tv_station_choice)
        self.TV_Option_Text_Edit.setGeometry(QtCore.QRect(50,50,150,20))
        self.add_option.move(85,80)
        self.dialog_for_tv_station_choice.setWindowTitle("Add TV-Station")
        self.add_option.clicked.connect(lambda x: self.add_options_to_index(MainWindow,str(self.TV_Option_Text_Edit.text())))
        self.dialog_for_tv_station_choice.exec_()
    def add_options_to_index(self,MainWindow,new_tv_station):
        self.Tv_Station_Choice.addItem(new_tv_station)
        count = self.Tv_Station_Choice.count()
        self.Tv_Station_Choice.setCurrentIndex(count - 1)
        self.dialog_for_tv_station_choice.close()









    def browse_ad_additional_button_click(self):
        self.upload_stream_Text_Edit.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Video" ,default_path,"Video (*.mpg *.flv *.wmv *.mpv *.mp4 *.avi)"))

    def search_button(self,MainWindow,database,Commercial,Stream,Station,scan_type):
    	fingerprint_information = []
        Commercials = []
        Commercial_Length = (self.count + 1)
        commercial_ad_time = []
        commercial_fingerprints = []
        commercial_ad_time_seconds = []
        
        
        if (self.count == 0) and (self.Commercial_Text_Edit.text() ==""):
            all_commercials_from_database = create_fingerprint_database.select_all_commercial_video_information_from_database(database)
            for x in range(len(all_commercials_from_database)):
                Commercials.append(all_commercials_from_database[x][0])
                commercial_ad_time.append(all_commercials_from_database[x][1])
                commercial_fingerprints.append(all_commercials_from_database[x][2])
                commercial_ad_time_seconds.append(time_converter.time_converter(commercial_ad_time[x])) 
            '''Take the smallest ad second'''
            commercial_ad_time_seconds.sort()
            Commercial_Length = len(Commercials)
            Ad_seconds = commercial_ad_time
            # search_page_ui = search_page.Ui_MainWindow()
            # search_page_ui.setupUi(MainWindow,database,Stream,Commercials,commercial_ad_time_seconds,commercial_fingerprints,Commercial_Length)

        else:
            for i in range(self.count + 1):
                if path.exists(os.getcwd() + "/jsons/" + str(Commercial[i] + ".json")) is False:
                    reply = QtGui.QMessageBox.question(MainWindow, 'Message',"Fingerprint Doesn't Exists, Do you want to fingerprint it?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                    if reply == QtGui.QMessageBox.Yes:
                        fingerprint_page_ui = fingerprint.Ui_MainWindow()
                        fingerprint_page_ui.setupUi(MainWindow)
                        continue  
                    else:
                        break 
                else:
                    fingerprint_information.append(create_fingerprint_database.select_video_information_from_database_by_commercial(
                        database,
                        Commercial[i]))
                    
                    #commercial_client = fingerprint_information[i][0][0]
                    #commercial_ad_directory = fingerprint_information[i][0][1]
                    Commercials.append(Commercial[i])
                    commercial_ad_time.append(fingerprint_information[i][0][2])
                    commercial_fingerprints.append(fingerprint_information[i][0][3])
                
                    commercial_ad_time_seconds.append(time_converter.time_converter(commercial_ad_time[i]))
                """Scanning Should have two options 
                EASY/QUICK 
                
                NORMAL(Recommended) 
                """
                
                """Advanced"""
        search_page_ui = search_page.Ui_MainWindow()
        search_page_ui.setupUi(MainWindow,database,Stream,Station,Commercials,commercial_ad_time_seconds,commercial_fingerprints,Commercial_Length,scan_type,start_time)

        MainWindow.show()
    def back_button(self,MainWindow):
        main_menu_ui = main_menu.Ui_MainWindow()
        main_menu_ui.setupUi(MainWindow)
        MainWindow.show()
       
    def clear_commercials_2(self,count):
	    self.Commercial_3.hide()
	    self.Commercial_Text_Edit_3.hide()
	    self.clear_button_3.hide()
	    self.clear_button_2.setDisabled(False)
	    self.count = 2

    def clear_commercials_1(self,count):
		self.Commercial_2.hide()
		self.Commercial_Text_Edit_2.hide()
		self.clear_button_2.hide()
		self.clear_button.setDisabled(False)
		self.count = 1

    def clear_commercials(self,count):
	    self.Commercial_1.hide()
	    self.Commercial_Text_Edit_1.hide()
	    self.clear_button.hide()
	    self.count = 0


	

    def more_ad_add(self):
    	self.count += 1 
        if self.count ==1:
        	self.Commercial_1.setGeometry(QtCore.QRect(10, self.count*40 + 120 , 100, 20))
        	self.Commercial_1.setText("Commercial_"+ str(self.count))
        	self.Commercial_1.show()
        	self.Commercial_Text_Edit_1.show()
        	self.clear_button.setGeometry(QtCore.QRect(260,self.count*40 + 120,70,20))
           	self.clear_button.setText("Clear")
        	self.clear_button.show()
        	self.clear_button.clicked.connect(lambda x: self.clear_commercials(self.count))


        if self.count ==2:
	        self.Commercial_2.setGeometry(QtCore.QRect(10, self.count*40 + 120 , 100, 20))
	    	self.Commercial_2.setText("Commercial_"+ str(self.count))
	    	self.Commercial_2.show()
	        self.Commercial_Text_Edit_2.show()
	        self.clear_button.setDisabled(True)
	        self.clear_button_2.setGeometry(QtCore.QRect(260,self.count*40 + 120,70,20))
           	self.clear_button_2.setText("Clear")
        	self.clear_button_2.show()
        	self.clear_button_2.clicked.connect(lambda x: self.clear_commercials_1(self.count)) 

        if self.count ==3:
	        self.Commercial_3.setGeometry(QtCore.QRect(10, self.count*40 + 120 , 100, 20))
	    	self.Commercial_3.setText("Commercial_"+ str(self.count))
	    	self.Commercial_3.show()
	        self.Commercial_Text_Edit_3.show()

	        self.clear_button_2.setDisabled(True)
	        self.clear_button_3.setGeometry(QtCore.QRect(260,self.count*40 + 120,70,20))
           	self.clear_button_3.setText("Clear")
        	self.clear_button_3.show()
        	self.clear_button_3.clicked.connect(lambda x: self.clear_commercials_2(self.count))

















        """-------------------------------AudioMethod------------------------"""





















    def audio_browse_ad_additional_button_click(self):
        self.audio_upload_stream_Text_Edit.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Audio" ,default_path,"Audio (*.mp3 *.wma *.wav)"))

    def audio_search_button(self,MainWindow,database,Commercial,Stream,Station):
        Client = []
        Ad = []
        Ad_Duration = []
        Audio_Commercial_Length = (self.audio_count + 1)
        Date = datetime.date.today()
        Date_of_broadcast = [Date.month,Date.day,Date.year]
        
        Eth_date = str(conv(Date_of_broadcast[2],Date_of_broadcast[0],Date_of_broadcast[1]))[1:-1]        
        Eth_date = Eth_date.replace('/',',')
        Eth_date = [int(i) for i in Eth_date.split(',')]
        Eth_date = str(Eth_date[1]) + str(',') + str(Eth_date[2]) + str(',') + str(Eth_date[0])
        for i in range(self.audio_count + 1):
            Client.append(create_fingerprint_database.select_audio_information_from_database_by_commercial(database,str(Commercial[i]))[0][0])
            Ad.append(create_fingerprint_database.select_audio_information_from_database_by_commercial(database,str(Commercial[i]))[0][1])
            Ad_Duration.append(create_fingerprint_database.select_audio_information_from_database_by_commercial(database,str(Commercial[i]))[0][2])
        
        audio_search_page_ui = audio_search_page.Ui_MainWindow()
        audio_search_page_ui.setupUi(MainWindow,Date_of_broadcast,Eth_date,str(database),Commercial,Audio_Commercial_Length,str(Station),str(Stream), Client, Ad , Ad_Duration)
        MainWindow.show()
        import sys
        sys.exit(app.exec_())

        exit()
    def audio_clear_commercials_2(self,count):
        self.audio_Commercial_3.hide()
        self.audio_Commercial_Text_Edit_3.hide()
        self.audio_clear_button_3.hide()
        self.audio_clear_button_2.setDisabled(False)
        self.audio_count = 2

    def audio_clear_commercials_1(self,count):
        self.audio_Commercial_2.hide()
        self.audio_Commercial_Text_Edit_2.hide()
        self.audio_clear_button_2.hide()
        self.audio_clear_button.setDisabled(False)
        self.audio_count = 1

    def audio_clear_commercials(self,count):
        self.audio_Commercial_1.hide()
        self.audio_Commercial_Text_Edit_1.hide()
        self.audio_clear_button.hide()
        self.audio_count = 0


    

    def audio_more_ad_add(self):
        self.audio_count += 1 
        if self.audio_count ==1:
            self.audio_Commercial_1.setGeometry(QtCore.QRect(10, self.audio_count*40 + 120 , 100, 20))
            self.audio_Commercial_1.setText("Commercial_"+ str(self.audio_count))
            self.audio_Commercial_1.show()
            self.audio_Commercial_Text_Edit_1.show()
            self.audio_clear_button.setGeometry(QtCore.QRect(260,self.audio_count*40 + 120,70,20))
            self.audio_clear_button.setText("Clear")
            self.audio_clear_button.show()
            self.audio_clear_button.clicked.connect(lambda x: self.audio_clear_commercials(self.audio_count))


        if self.audio_count ==2:
            self.audio_Commercial_2.setGeometry(QtCore.QRect(10, self.audio_count*40 + 120 , 100, 20))
            self.audio_Commercial_2.setText("Commercial_"+ str(self.audio_count))
            self.audio_Commercial_2.show()
            self.audio_Commercial_Text_Edit_2.show()
            self.audio_clear_button.setDisabled(True)
            self.audio_clear_button_2.setGeometry(QtCore.QRect(260,self.audio_count*40 + 120,70,20))
            self.audio_clear_button_2.setText("Clear")
            self.audio_clear_button_2.show()
            self.audio_clear_button_2.clicked.connect(lambda x: self.audio_clear_commercials_1(self.audio_count)) 

        if self.audio_count ==3:
            self.audio_Commercial_3.setGeometry(QtCore.QRect(10, self.audio_count*40 + 120 , 100, 20))
            self.audio_Commercial_3.setText("Commercial_"+ str(self.audio_count))
            self.audio_Commercial_3.show()
            self.audio_Commercial_Text_Edit_3.show()

            self.audio_clear_button_2.setDisabled(True)
            self.audio_clear_button_3.setGeometry(QtCore.QRect(260,self.audio_count*40 + 120,70,20))
            self.audio_clear_button_3.setText("Clear")
            self.audio_clear_button_3.show()
            self.audio_clear_button_3.clicked.connect(lambda x: self.audio_clear_commercials_2(self.audio_count))




	


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        


        



        





 
 