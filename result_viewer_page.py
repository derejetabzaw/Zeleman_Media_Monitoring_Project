# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend_4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
import load_page 
import os
import result_card_page
import browse_page
#import watch_in_time as wit
from functools import partial
program = str("mplayer")

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,Date,Eth_Date,Time,Client,commercial,Commercial_Length,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))


        grid = QtGui.QGridLayout(self.centralwidget)
        groupBox = []      
        groupBoxLayout = []
        status_information = []
        Agent = []
        Commercial = []
        Total_Seconds_Broadcasted = []
        Broadcast_Status = []
        watch_in_time_video = []
        
        groupBox_horizontal = QtGui.QGroupBox(self.centralwidget)
        groupBox_horizontalLayout=QtGui.QHBoxLayout()
        groupBox_horizontalLayout.addStretch(1)
        groupBox_horizontal.setLayout(groupBox_horizontalLayout)
        groupBox_horizontal.resize(100,100)

        self.next = QtGui.QPushButton()
        self.previous = QtGui.QPushButton()
        self.next.setText(_translate("MainWindow", "Next", None))
        self.previous.setText(_translate("MainWindow", "Previous", None))


        groupBox_horizontalLayout.addWidget(self.previous)
        groupBox_horizontalLayout.addWidget(self.next)
        
        for i in range (Commercial_Length):
            groupBox.append(QtGui.QGroupBox(self.centralwidget))
            groupBoxLayout.append(QtGui.QVBoxLayout())
            groupBox[i].setLayout(groupBoxLayout[i])
            groupBox[i].resize(100,100)

            
            status_information.append(QtGui.QLabel())
            status_information[i].setGeometry(QtCore.QRect(250, 100, 150, 100))
            Agent.append(QtGui.QLabel())
            Agent[i].setText(_translate("MainWindow", "Agent: " + str(Client[i]), None))
            Agent[i].setGeometry(QtCore.QRect(50, 30, 150, 100))

            Commercial.append(QtGui.QLabel())
            Commercial[i].setText(_translate("MainWindow", "Commercial: " + str(commercial[i]), None))
            Commercial[i].setGeometry(QtCore.QRect(50, 50, 150, 100))


            Total_Seconds_Broadcasted.append(QtGui.QLabel())
            Total_Seconds_Broadcasted[i].setText(_translate("MainWindow", "Total Broadcasted Seconds: " + str(Ad_dur[i]), None))
            Total_Seconds_Broadcasted[i].setGeometry(QtCore.QRect(50, 70, 150, 100))

            
            watch_in_time_video.append(QtGui.QPushButton())
            watch_in_time_video[i].setText(_translate("MainWindow", "Watch in Time", None))
            watch_in_time_video[i].setGeometry(QtCore.QRect(50,140, 100, 30))
            watch_in_time_video[i].clicked.connect(lambda x, i=i : self.watch_in_time_button(Time_in_video[i],str(Stream)))
            


            Broadcast_Status.append(QtGui.QLabel())
            
            Broadcast_Status[i].setText(_translate("MainWindow", "Broadcast-Status: " + str(broadcast_information[i]), None))
            if (broadcast_information[i] == "Yes"):
                Broadcast_Status[i].setStyleSheet("background-color : #1900dd")

            else:
                watch_in_time_video[i].setEnabled(False)
                Broadcast_Status[i].setStyleSheet("background-color : #ee001b")
            Broadcast_Status[i].setGeometry(QtCore.QRect(50, 70, 150, 100))
            



            groupBoxLayout[i].addWidget(Agent[i])
            groupBoxLayout[i].addWidget(Commercial[i])
            groupBoxLayout[i].addWidget(Total_Seconds_Broadcasted[i])
            groupBoxLayout[i].addWidget(Broadcast_Status[i])
            groupBoxLayout[i].addWidget(watch_in_time_video[i])
            
            grid.addWidget(groupBox[i],i,0)
        horizontal_widget_size = int(Commercial_Length + 1)
        grid.addWidget(groupBox_horizontal,horizontal_widget_size,0,5,2)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        if broadcast_information =='':
            self.watch_in_time_video.setEnabled(False)
        self.next.clicked.connect(lambda x: self.next_button(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video))
        self.previous.clicked.connect(lambda x: self.previous_button(MainWindow,Date,Time,Client,Commercial,Station,Ad,Stream))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))


    def watch_in_time_button(self,Time_in_video,Stream):
        cmd = program + str(" ") + str(Stream) + " -ss " + str(Time_in_video)
        os.system(cmd)

    def next_button(self,MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,Was_Broadcasted,Time_BS,Time_in_video):
        result_card_page_ui = result_card_page.Ui_MainWindow()
        result_card_page_ui.setupUi(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,Was_Broadcasted,Time_BS,Time_in_video)
        MainWindow.show()

    def previous_button(self,MainWindow,Date,Time,Client,Commercial,Station,Ad,Stream):
        browse_page_ui = browse_page.Ui_MainWindow()
        browse_page_ui.setupUi(MainWindow,Date,Time,Client,Commercial,Station,Ad,Stream)
        MainWindow.show()
