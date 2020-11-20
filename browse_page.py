# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os
import entry_summary_page
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
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

count = 1
conv = EthiopianDateConverter.to_ethiopian
default_path = os.path.dirname(os.path.abspath(__file__))
class Ui_MainWindow(object):
    def setupUi(self, MainWindow,Date,Time,Client,Commercial,Station,Ad,Stream):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(740, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.tabWidget = QtGui.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 715, 580))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        self.Video = QtGui.QWidget()
        self.Video.setObjectName(_fromUtf8("Video"))
        self.pushButton_3 = QtGui.QPushButton(self.Video)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 500, 100, 30))
        self.pushButton_3.setObjectName(_fromUtf8("Next"))

        '''Ad/Stream Video Browse Layout'''
        self.layoutWidget = QtGui.QWidget(self.Video)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 200, 700, 70))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        
        self.pushButton_plus = QtGui.QPushButton(self.Video)
        self.pushButton_plus.setGeometry(QtCore.QRect(626,265,75,22))
        self.pushButton_plus.setObjectName(_fromUtf8("Add"))

        # self.layoutWidget_ad_plus = QtGui.QWidget(self.Video)
        # self.layoutWidget_ad_plus.setGeometry(QtCore.QRect(20, 265, 300, 100))
        # self.layoutWidget_ad_plus.setObjectName(_fromUtf8("layoutWidget"))
        # self.gridLayout_ad_plus = QtGui.QGridLayout(self.layoutWidget_ad_plus)
        # self.gridLayout_ad_plus.setObjectName(_fromUtf8("gridLayout_3"))
        
    
        
        self.label_ad_plus = QtGui.QLabel(self.Video)
        self.lineEdit_ad_plus = QtGui.QLineEdit(self.Video)
        self.browse_ad_additional_1 = QtGui.QPushButton(self.Video)
        self.label_client_plus = QtGui.QLabel(self.Video)
        self.lineEdit_client_plus = QtGui.QLineEdit(self.Video)
        self.label_commercial_plus = QtGui.QLabel(self.Video)
        self.lineEdit_commercial_plus = QtGui.QLineEdit(self.Video)

        self.label_ad_plus_1 = QtGui.QLabel(self.Video)
        self.lineEdit_ad_plus_1 = QtGui.QLineEdit(self.Video)
        self.browse_ad_additional_2 = QtGui.QPushButton(self.Video)
        self.label_client_plus_1 = QtGui.QLabel(self.Video)
        self.lineEdit_client_plus_1 = QtGui.QLineEdit(self.Video)
        self.label_commercial_plus_1 = QtGui.QLabel(self.Video)
        self.lineEdit_commercial_plus_1 = QtGui.QLineEdit(self.Video)

        self.label_ad_plus_2 = QtGui.QLabel(self.Video)
        self.lineEdit_ad_plus_2 = QtGui.QLineEdit(self.Video)
        self.browse_ad_additional_3 = QtGui.QPushButton(self.Video)
        self.label_client_plus_2 = QtGui.QLabel(self.Video)
        self.lineEdit_client_plus_2 = QtGui.QLineEdit(self.Video)
        self.label_commercial_plus_2 = QtGui.QLabel(self.Video)
        self.lineEdit_commercial_plus_2 = QtGui.QLineEdit(self.Video)
        
        
        # self.label_commercial_plus.setGeometry(QtCore.QRect(480,425,75,22))
        # self.label_commercial_plus.setObjectName(_fromUtf8("label_commercial_plus"))
        # self.label_commercial_plus.setText(_translate("MainWindow", "Commercial(1)", None))
        
        self.pushButton_plus.clicked.connect(lambda x: self.more_ad_video_add_option(
            self.label_ad_plus,
            self.lineEdit_ad_plus,
            self.browse_ad_additional_1,
            self.label_client_plus,
            self.lineEdit_client_plus,
            self.label_commercial_plus,
            self.lineEdit_commercial_plus,
            self.label_ad_plus_1,
            self.lineEdit_ad_plus_1,
            self.browse_ad_additional_2,
            self.label_client_plus_1,
            self.lineEdit_client_plus_1,
            self.label_commercial_plus_1, 
            self.lineEdit_commercial_plus_1,
            self.label_ad_plus_2,
            self.lineEdit_ad_plus_2,
            self.browse_ad_additional_3,
            self.label_client_plus_2,
            self.lineEdit_client_plus_2,
            self.label_commercial_plus_2,
            self.lineEdit_commercial_plus_2))

        
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton.clicked.connect(self.browse_ad)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.browse_ad_2)
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 2, 1, 1)

        


        '''Client/Commercial Infromation'''
       
        
        self.layoutWidget_2 = QtGui.QWidget(self.Video)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 100, 700, 50))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.lineEdit_5 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.label_9 = QtGui.QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_5.addWidget(self.lineEdit_6)
        
        '''Tv Channel'''
        self.layoutWidget_3 = QtGui.QWidget(self.Video)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 150, 150, 50))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_10 = QtGui.QLabel(self.layoutWidget_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_6.addWidget(self.label_10)

        add_option_button = QtGui.QPushButton(self.Video)
        add_option_button.setGeometry(QtCore.QRect(200, 165, 100, 20))
        add_option_button.setObjectName(_fromUtf8("pushButton_10"))
        add_option_button.setText(_translate("MainWindow", "Add", None))

        add_option_button.clicked.connect(self.add_option_button_cliked)

        self.comboBox = QtGui.QComboBox(self.Video)
        self.comboBox.addItem("EBC")
        self.comboBox.addItem("EBS")
        self.comboBox.addItem("JTV")
        self.comboBox.addItem("Asham_TV")
        self.comboBox.addItem("LTV")
        self.comboBox.addItem("Walta_TV")
        self.comboBox.setGeometry(QtCore.QRect(90, 165, 100, 20))

        
        #self.list_widget.setObjectName(_fromUtf8("list_widget"))
        #self.horizontalLayout_6.addWidget(self.list_widget)
        

        '''Date/Time'''
        self.label_3 = QtGui.QLabel(self.Video)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 670, 50))
        self.label_3.setText(_translate("MainWindow", "Date", None))

        self.label_date_format = QtGui.QLabel(self.Video)
        self.label_date_format.setGeometry(QtCore.QRect(50,40,100,30))
        self.label_date_format.setText(_translate("MainWindow", "MM/DD/YYYY", None))

        
        self.dateEdit = QtGui.QDateEdit(self.Video)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setGeometry(QtCore.QRect(50, 25, 100, 20))
        self.dateEdit.setCalendarPopup(True)
        
        self.label_11 = QtGui.QLabel(self.Video)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        
        self.label_4 = QtGui.QLabel(self.Video)
        self.label_4.setGeometry(QtCore.QRect(350, 25, 100, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        
        self.timeEdit = QtGui.QTimeEdit(self.Video)
        self.timeEdit.setGeometry(QtCore.QRect(410, 25, 100, 20))
        self.timeEdit.setTime(QtCore.QTime.currentTime())
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))

        self.layoutWidget.raise_()
        self.pushButton_3.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.tabWidget.addTab(self.Video, _fromUtf8(""))
        
        self.lineEdit_5.setText(str(Client))
        self.lineEdit_6.setText(str(Commercial))
        self.comboBox.setItemText (-1,str(Station))
        self.lineEdit_2.setText(str(Stream))
        self.lineEdit.setText(str(Ad))

        self.pushButton_3.clicked.connect(lambda x: self.next_button(MainWindow,
        self.dateEdit.text(),self.timeEdit.text(),
        self.lineEdit_5.text(),self.lineEdit_6.text(),
        self.comboBox.currentText(),
        self.lineEdit.text(),self.lineEdit_2.text()))


        '''Audio Next'''
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(600, 500, 100, 30))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        
        '''Audio Ad/Stream Audio Browse Layout'''
        self.layoutWidget_5 = QtGui.QWidget(self.tab_2)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 300, 700, 70))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget_5)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_14 = QtGui.QLabel(self.layoutWidget_5)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.layoutWidget_5)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_6.addWidget(self.lineEdit_7, 0, 1, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_6.addWidget(self.lineEdit_8, 1, 1, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.layoutWidget_5) 
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout_6.addWidget(self.pushButton_10, 0, 2, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.layoutWidget_5)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout_6.addWidget(self.pushButton_11, 1, 2, 1, 1)
        
        '''Audio Client/Commercial Infromation'''
        self.layoutWidget1 = QtGui.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 100, 700, 50))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout.addWidget(self.lineEdit_4)
        
        '''Radio Station'''
        self.layoutWidget2 = QtGui.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 200, 150, 50))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.layoutWidget2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.spinBox = QtGui.QSpinBox(self.layoutWidget2)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_4.addWidget(self.spinBox)
        
        '''Audio Date and Time'''
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 670, 50))
        self.label_12.setText(_translate("MainWindow", "Date", None))

        self.label_date_format = QtGui.QLabel(self.tab_2)
        self.label_date_format.setGeometry(QtCore.QRect(50,40,100,30))
        self.label_date_format.setText(_translate("MainWindow", "MM/DD/YYYY", None))

        
        self.dateEdit_3 = QtGui.QDateEdit(self.tab_2)
        self.dateEdit_3.setGeometry(QtCore.QRect(50, 25, 100, 20))
        
        self.label_16 = QtGui.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(350, 10, 670, 50))
        self.label_16.setObjectName(_fromUtf8("label_11"))
        
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(350, 25, 100, 20))
        self.label_13.setObjectName(_fromUtf8("label_4"))
        
        self.timeEdit_2 = QtGui.QTimeEdit(self.tab_2)
        self.timeEdit_2.setGeometry(QtCore.QRect(410, 25, 100, 20))
        self.timeEdit_2.setObjectName(_fromUtf8("timeEdit"))

        add_option_button_2 = QtGui.QPushButton(self.tab_2)
        add_option_button_2.setGeometry(QtCore.QRect(200, 215, 100, 20))
        add_option_button_2.setObjectName(_fromUtf8("pushButton_10"))
        add_option_button_2.setText(_translate("MainWindow", "Add", None))



        self.comboBox_2 = QtGui.QComboBox(self.tab_2)
        self.comboBox_2.addItem("FM 97.1")
        self.comboBox_2.addItem("Ahadu 94.3")
        self.comboBox_2.addItem("FM 96.3")
        self.comboBox_2.addItem("AFROFM 105.3")
        self.comboBox_2.addItem("ShegerFM 102.1")
        self.comboBox_2.addItem("BisratFM 101.1")
        self.comboBox_2.setGeometry(QtCore.QRect(90, 215, 100, 20))
        



        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))
        self.pushButton_3.setText(_translate("MainWindow", "Next ", None))
        self.label_2.setText(_translate("MainWindow", "Stream Video", None))
        self.label.setText(_translate("MainWindow", "Ad Video", None))
        self.pushButton.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_2.setText(_translate("MainWindow", "Browse", None))
        self.label_8.setText(_translate("MainWindow", "Client", None))
        self.label_9.setText(_translate("MainWindow", "Commercial", None))
        self.label_10.setText(_translate("MainWindow", "TV Channel", None))
        #self.label_11.setText(_translate("MainWindow", "Eth Date", None))
        self.label_4.setText(_translate("MainWindow", "Time", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Video), _translate("MainWindow", "Video", None))
        self.pushButton_7.setText(_translate("MainWindow", "Next ", None))
        self.pushButton_plus.setText(_translate("MainWindow", "More-Ad ", None))
        self.label_14.setText(_translate("MainWindow", "Stream Audio", None))
        self.label_15.setText(_translate("MainWindow", "Ad Audio", None))
        self.pushButton_10.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_11.setText(_translate("MainWindow", "Browse", None))
        self.label_5.setText(_translate("MainWindow", "Client", None))
        self.label_6.setText(_translate("MainWindow", "Commercial", None))
        self.label_7.setText(_translate("MainWindow", "Radio Station", None))
        self.label_12.setText(_translate("MainWindow", "Date", None))
        #self.label_13.setText(_translate("MainWindow", "Eth Date", None))
        self.label_16.setText(_translate("MainWindow", "Time", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Audio", None))
    
    def add_option_button_cliked(self):   
        self.add_options = QtGui.QDialog()
        self.enter = QtGui.QPushButton("Enter",self.add_options)
        
        

        self.enter.move(250,50)
        self.add_options.setWindowTitle("Add TV Channel")
        self.tv_channel_option = QtGui.QLineEdit(self.add_options)
        self.tv_channel_option.setGeometry(QtCore.QRect(50,51,180,20))
        self.tv_channel_option.text()
        self.enter.clicked.connect(self.editing_finished)
        self.label_example = QtGui.QLabel(self.add_options)
        self.label_example.setGeometry(QtCore.QRect(50,75,100,30))
        self.label_example.setText(_translate("MainWindow", "(eg. EBC)", None))
        self.add_options.exec_()

    #def combo_box_add_options(self):
    def more_ad_video_add_option(self,
        label_ad_plus,
        lineEdit_ad_plus,
        browse_ad,
        label_client_plus,
        lineEdit_client_plus,
        label_commercial_plus,
        lineEdit_commercial_plus,
        label_ad_plus_1,
        lineEdit_ad_plus_1,
        browse_ad_1,
        label_client_plus_1,
        lineEdit_client_plus_1,
        label_commercial_plus_1, 
        lineEdit_commercial_plus_1,
        label_ad_plus_2,
        lineEdit_ad_plus_2,
        browse_ad_2,
        label_client_plus_2,
        lineEdit_client_plus_2,
        label_commercial_plus_2,
        lineEdit_commercial_plus_2):
        #label(Ad(1)) TextEdit label(Client(1)) TextEdit label(Commerical(1)) TextEdit

        global count         
        if count ==1:

            label_ad_plus.setGeometry(QtCore.QRect(20,265,75,22))
            label_ad_plus.setObjectName(_fromUtf8("label_ad_plus"))
            label_ad_plus.setText("Ad_1")
            lineEdit_ad_plus.setGeometry(QtCore.QRect(87,265,150,22))
            lineEdit_ad_plus.setObjectName(_fromUtf8("lineEdit_ad_plus"))
            #lineEdit_ad_plus.setText("Ad(1)")

            browse_ad.setGeometry(QtCore.QRect(247, 265, 75, 20))
            browse_ad.setText("Browse")


            
            label_client_plus.setGeometry(QtCore.QRect(20,290,75,22))
            label_client_plus.setObjectName(_fromUtf8("label_client_plus"))
            label_client_plus.setText("Client_1")
            lineEdit_client_plus.setGeometry(QtCore.QRect(87,290,150,22))
            lineEdit_client_plus.setObjectName(_fromUtf8("client_plus"))
            #lineEdit_client_plus.setText("Client(1)")

            label_commercial_plus.setGeometry(QtCore.QRect(247,290,75,22))
            label_commercial_plus.setObjectName(_fromUtf8("label_commercial_plus"))
            label_commercial_plus.setText( "Commercial_1")
            lineEdit_commercial_plus.setGeometry(QtCore.QRect(320,290,150,22))
            lineEdit_commercial_plus.setObjectName(_fromUtf8("lineEdit_commercial_plus"))

            browse_ad.clicked.connect(self.browse_ad_additional_button_click_1)
      
        if count ==2:
      
            label_ad_plus_1.setGeometry(QtCore.QRect(20,320,75,22))
            label_ad_plus_1.setObjectName(_fromUtf8("label_ad_plus"))
            label_ad_plus_1.setText("Ad_2")
            lineEdit_ad_plus_1.setGeometry(QtCore.QRect(87,320,150,22))
            lineEdit_ad_plus_1.setObjectName(_fromUtf8("lineEdit_ad_plus"))
            #lineEdit_ad_plus.setText("Ad(1)")

            browse_ad_1.setGeometry(QtCore.QRect(247, 320, 75, 20))
            browse_ad_1.setText("Browse")

            label_client_plus_1.setGeometry(QtCore.QRect(20,345,75,22))
            label_client_plus_1.setObjectName(_fromUtf8("label_client_plus"))
            label_client_plus_1.setText("Client_2")
            lineEdit_client_plus_1.setGeometry(QtCore.QRect(87,345,150,22))
            lineEdit_client_plus_1.setObjectName(_fromUtf8("client_plus"))
            #lineEdit_client_plus.setText("Client(1)")

            label_commercial_plus_1.setGeometry(QtCore.QRect(247,345,75,22))
            label_commercial_plus_1.setObjectName(_fromUtf8("label_commercial_plus"))
            label_commercial_plus_1.setText( "Commercial_2")
            lineEdit_commercial_plus_1.setGeometry(QtCore.QRect(320,345,150,22))
            lineEdit_commercial_plus_1.setObjectName(_fromUtf8("lineEdit_commercial_plus"))

            browse_ad_1.clicked.connect(self.browse_ad_additional_button_click_2)
        if count ==3:

            label_ad_plus_2.setGeometry(QtCore.QRect(20,375,75,22))
            label_ad_plus_2.setObjectName(_fromUtf8("label_ad_plus"))
            label_ad_plus_2.setText("Ad_3")
            lineEdit_ad_plus_2.setGeometry(QtCore.QRect(87,375,150,22))
            lineEdit_ad_plus_2.setObjectName(_fromUtf8("lineEdit_ad_plus"))
            #lineEdit_ad_plus.setText("Ad(1)")

            browse_ad_2.setGeometry(QtCore.QRect(247, 375, 75, 20))
            browse_ad_2.setText("Browse")

            
            label_client_plus_2.setGeometry(QtCore.QRect(20,400,75,22))
            label_client_plus_2.setObjectName(_fromUtf8("label_client_plus"))
            label_client_plus_2.setText("Client_3")
            lineEdit_client_plus_2.setGeometry(QtCore.QRect(87,400,150,22))
            lineEdit_client_plus_2.setObjectName(_fromUtf8("client_plus"))
            #lineEdit_client_plus.setText("Client(1)")

            label_commercial_plus_2.setGeometry(QtCore.QRect(247,400,75,22))
            label_commercial_plus_2.setObjectName(_fromUtf8("label_commercial_plus"))
            label_commercial_plus_2.setText( "Commercial_3")
            lineEdit_commercial_plus_2.setGeometry(QtCore.QRect(320,400,150,22))
            lineEdit_commercial_plus_2.setObjectName(_fromUtf8("lineEdit_commercial_plus"))    
      
            
            
            browse_ad_2.clicked.connect(self.browse_ad_additional_button_click_3)
        count += 1
    def editing_finished(self):
        self.comboBox.addItem(self.tv_channel_option.text())
        self.add_options.close()
    def browse_ad(self):
        '''default_path for video uplaod'''
        self.lineEdit.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Video" ,default_path,"Video (*.mpg *.flv *.wmv *.mpv *.mp4 *.avi)"))

    def browse_ad_2(self):
        self.lineEdit_2.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Stream Video" ,default_path,"Video (*.mpg *.flv *.wmv *.mpv *.mp4 *.avi)"))
    
    def browse_ad_additional_button_click_1(self):
        self.lineEdit_ad_plus.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Video" ,default_path,"Video (*.mpg *.flv *.wmv *.mpv *.mp4 *.avi)"))
    def browse_ad_additional_button_click_2(self):
        self.lineEdit_ad_plus_1.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Video" ,default_path,"Video (*.mpg *.flv *.wmv *.mpv *.mp4 *.avi)"))
    def browse_ad_additional_button_click_3(self):
        self.lineEdit_ad_plus_2.setText(QtGui.QFileDialog.getOpenFileName(None, "Open Ad Video" ,default_path,"Video (*.mpg *.flv *.wmv *.mpv *.mp4 *.avi)"))    
    
    def next_button(self,MainWindow,Date,Time,Client,Commercial,Station,Ad,Stream):
        Date_2 = Date.replace('/',',')
        Date_2 = [int(i) for i in Date.split(',')]
        Eth_date = str(conv(Date_2[2],Date_2[0],Date_2[1]))[1:-1]        
        Eth_date = Eth_date.replace('/',',')
        Eth_date = [int(i) for i in Eth_date.split(',')]
        Eth_date = str(Eth_date[1]) + str(',') + str(Eth_date[2]) + str(',') + str(Eth_date[0])
        Eth_date = QtCore.QString(Eth_date)
        entry_summary_page_ui = entry_summary_page.Ui_MainWindow()
        entry_summary_page_ui.setupUi(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream)
        MainWindow.show()
#from kimagefilepreview import KImageFilePreview
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    Date =" " 
    Time =" " 
    Client =" " 
    Commercial =" "
    Station =" " 
    Ad = " " 
    Stream = " "
    ui.setupUi(MainWindow,Date,Time,Client,Commercial,Station,Ad,Stream)
    MainWindow.show()
    sys.exit(app.exec_())

