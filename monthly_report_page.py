# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend_8_Monthly_Report.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np
import functools
import os
import stats_page
import calendar 
import datetime
import result_card_page as rcp
import database_query as db_query
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

#month_number , year = 2 , 2011 
#month_start_date,number_of_days = calendar.monthrange(year,month_number)[0],calendar.monthrange(year,month_number)[1]
#month_name = calendar.month_name[month_number]
#database = r"C:/Users/dereje/Desktop/Media_Monitoring_Project/Frontend/frontend_codes/information_database.db"
database = str(os.getcwd() + "/" + str("fingerprint_database.db")).replace("\\","/")

conn = db_query.create_connection(database)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)

        # Date = Internal Date
        # Time = Internal Time 
        # Client = User Defined 
        # Commercial = User Defined
        # Station = User Defined  
        

        Date = str("7,8,2020")
        Client = str("Zeleman")
        Commercial = str("Coca Cola")

        Date_2 = Date.replace('/',',')
        Date_2 = [int(i) for i in Date.split(',')]
        month_number , year = Date_2[0] , Date_2[2] 
        month_start_date,number_of_days = calendar.monthrange(year,month_number)[0],calendar.monthrange(year,month_number)[1]
        month_name = calendar.month_name[month_number]
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        # self.comboBox = QtGui.QComboBox(self.centralwidget)
        # for i in range(1,13):
        #     self.comboBox.addItem(calendar.month_name[i])
        # self.comboBox.setItemText (-1,str(month_name))
        
        #month_number , year = int(self.comboBox.currentIndex()) + 1 , Date_2[2]
        #month_start_date,number_of_days = calendar.monthrange(year,month_number)[0],calendar.monthrange(year,month_number)[1]
        #month_name = calendar.month_name[month_number]
        
        count = 1
        '''week 1'''
        day_button = {}
        if (month_start_date == 6):
            for x in range(6 - month_start_date,7):
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 30, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count+= 1 
        else:
            for x in range(month_start_date + 1,7):
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 30, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count+= 1 
        # '''week 2-4,21days'''
        for y in range(1,4):
            for x in range(0,7):
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x,  30 + 70 * y, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count+= 1 
        # '''week 5'''
        remaining_days = number_of_days - (count - 1)

        if (remaining_days <=6):
            for x in range(remaining_days):    
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 310, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count += 1 
        # '''week 6'''
        else: 
            for x in range(0,7):    
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 310, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count += 1 
            remaining_days_2 = remaining_days -7 
            for x in range(remaining_days_2):    
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 380, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count += 1  
        
        
        db_information = db_query.select_some_video_information(conn,str(Client),str(Commercial))
        db_informations = db_query.select_all_video_information(conn)
        #print db_informations
        Date_3 = []       
        for y in range(len(db_information)):  
            Date_3.append(db_information[y][0].replace('/',','))
            Date_3[y] = [int(i) for i in Date_3[y].split(',')]
            if db_information[y][1] == 'Yes' and Date_3[y][0] ==Date_2[0]:
                day_button[Date_3[y][1]].setStyleSheet("background-color: blue")
            if db_information[y][1] == 'No'and Date_3[y][0] ==Date_2[0]:
                day_button[Date_3[y][1]].setStyleSheet("background-color: red")

   

    
        for i in range(1,count):
            day_button[i].clicked.connect(functools.partial(self.day_buttons_clicked,i))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 435, 80, 20))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 435, 80, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 435, 80, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 435, 80, 20))
        self.label_8.setObjectName(_fromUtf8("label_3"))
        
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 435, 80, 20))
        self.label_9.setObjectName(_fromUtf8("label_3"))
        
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 435, 80, 20))
        self.label_10.setObjectName(_fromUtf8("label_3"))
        
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(550, 435, 80, 20))
        self.label_11.setObjectName(_fromUtf8("label_3"))

        label_month_name = QtGui.QLabel(self.centralwidget)
        label_month_name.setGeometry(QtCore.QRect(340, 450, 200, 100))
        label_month_name.setText(_translate("MainWindow", str(month_name) + str('  ') + str(year), None))


        self.next_month_button = QtGui.QPushButton(self.centralwidget)
        self.next_month_button.setGeometry(QtCore.QRect(510, 490, 50, 20))
        self.next_month_button.setText(" >> ")
        self.previous_month_button = QtGui.QPushButton(self.centralwidget)
        self.previous_month_button.setGeometry(QtCore.QRect(250, 490, 50, 20))
        self.previous_month_button.setText(" << ")

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        label_month_name.setFont(font)


        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 100, 420))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)

        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_12)
        
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_13)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 550, 100, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 550, 100, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit", None))
        self.pushButton_2.setText(_translate("MainWindow", "Previous", None))

        self.pushButton_2.clicked.connect(lambda x: self.previous_button(MainWindow))
        # self.comboBox.currentIndexChanged.connect(lambda x: self.month_selection_changed(MainWindow,Date_2))
        #print month_number
        
        self.next_month_button.clicked.connect(lambda x: self.next_month_button_method(MainWindow,month_number,year,label_month_name))
        self.previous_month_button.clicked.connect(lambda x: self.previous_month_button_method(MainWindow,month_number,year,label_month_name))
        
        self.client_label_query = QtGui.QLabel(self.centralwidget)
        self.client_label_query.setGeometry(QtCore.QRect(600, 50, 80, 20))
        self.client_label_query.setObjectName(_fromUtf8("client_label"))
        self.commercial_label_query = QtGui.QLabel(self.centralwidget)
        self.commercial_label_query.setGeometry(QtCore.QRect(600, 80, 80, 20))
        self.commercial_label_query.setObjectName(_fromUtf8("commercial_label_query"))
        self.client_label_query.setText("Client:")
        self.commercial_label_query.setText("Commercial:")  
        self.client_entry_query = QtGui.QLineEdit(self.centralwidget)
        self.client_entry_query.setGeometry(QtCore.QRect(670, 50, 100, 20))
        self.client_entry_query.setObjectName(_fromUtf8("client_entry"))
        self.commercial_entry_query = QtGui.QLineEdit(self.centralwidget)
        self.commercial_entry_query.setGeometry(QtCore.QRect(670, 80, 100, 20))
        self.commercial_entry_query.setObjectName(_fromUtf8("commercial_entry"))
        self.search_button = QtGui.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(635, 120, 80 , 20))
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.search_button.setText("Search")

        self.search_button.clicked.connect(lambda x: self.search_button_clicked(self.client_entry_query.text(),self.commercial_entry_query.text()))


      

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Monthly Report", "Monthly Report", None))
        
        self.label_2.setText(_translate("MainWindow", "Mon", None))
        self.label_3.setText(_translate("MainWindow", "Tue", None))
        self.label_8.setText(_translate("MainWindow", "Wed", None))
        self.label_9.setText(_translate("MainWindow", "Thu", None))
        self.label_10.setText(_translate("MainWindow", "Fri", None))
        self.label_11.setText(_translate("MainWindow", "Sat", None))
        self.label.setText(_translate("MainWindow", "Sun", None))
        
        self.label_5.setText(_translate("MainWindow", "Week 1", None))
        self.label_7.setText(_translate("MainWindow", "Week 2 ", None))
        self.label_6.setText(_translate("MainWindow", "Week 3", None))
        self.label_4.setText(_translate("MainWindow", "Week 4", None))
        self.label_12.setText(_translate("MainWindow", "Week 5", None))
        self.label_13.setText(_translate("MainWindow", "Week 6", None))
    def search_button_clicked(self,client,commercial):
        with conn:
            client_query = db_query.select_video_information_client(conn, str(client))
            commercial_query = db_query.select_video_information_commercial(conn, str(commercial))
        #print client_query
        #print commercial_query

    def day_buttons_clicked(self,number,MainWindow):
        pass
        #result_card_page_ui = rcp.Ui_MainWindow()
        #result_card_page_ui.setupUi_mod(number,MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video)
    def previous_button(self,MainWindow):
        stats_page_ui = stats_page.Ui_MainWindow()
        stats_page_ui.setupUi(MainWindow)    

    def next_month_button_method(self,MainWindow,month_number,year,label_month_name):
        #label_month_name.setGeometry(QtCore.QRect(340, 450, 200, 100))
        #print month_number
        #month_name = calendar.month_name[month_number + 1]
        #label_month_name.setText(str(month_name) + str('  ') + str(year))
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)

        #Date_2 = Date.replace('/',',')
        #Date_2 = [int(i) for i in Date.split(',')]
        # Next/Previous Button should start from here
        month_number = month_number + 1
        #print month_number
        #month_number , year = Date_2[0] , Date_2[2] 
        month_start_date,number_of_days = calendar.monthrange(year,month_number)[0],calendar.monthrange(year,month_number)[1]
        month_name = calendar.month_name[month_number]
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        # self.comboBox = QtGui.QComboBox(self.centralwidget)
        # for i in range(1,13):
        #     self.comboBox.addItem(calendar.month_name[i])
        # self.comboBox.setItemText (-1,str(month_name))
        
        #month_number , year = int(self.comboBox.currentIndex()) + 1 , Date_2[2]
        #month_start_date,number_of_days = calendar.monthrange(year,month_number)[0],calendar.monthrange(year,month_number)[1]
        #month_name = calendar.month_name[month_number]
        
        count = 1
        '''week 1'''
        day_button = {}
        if (month_start_date == 6):
            for x in range(6 - month_start_date,7):
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 30, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count+= 1 
        else:
            for x in range(month_start_date + 1,7):
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 30, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count+= 1 
        # '''week 2-4,21days'''
        for y in range(1,4):
            for x in range(0,7):
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x,  30 + 70 * y, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count+= 1 
        # '''week 5'''
        remaining_days = number_of_days - (count - 1)

        if (remaining_days <=6):
            for x in range(remaining_days):    
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 310, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count += 1 
        # '''week 6'''
        else: 
            for x in range(0,7):    
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 310, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count += 1 
            remaining_days_2 = remaining_days -7 
            for x in range(remaining_days_2):    
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 380, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count += 1  
        for i in range(1,count):
            day_button[i].clicked.connect(functools.partial(self.day_buttons_clicked,i))

        #db_information = db_query.select_some_video_information(conn,str(Client),str(Commercial))
        
        #Date_3 = []    

        # for y in range(len(db_information)):  
        #     Date_3.append(db_information[y][0].replace('/',','))
        #     Date_3[y] = [int(i) for i in Date_3[y].split(',')]
        #     if db_information[y][1] == 'Yes' and Date_3[y][0] ==month_number + 1:
        #         day_button[Date_3[y][1]].setStyleSheet("background-color: blue")
        #     if db_information[y][1] == 'No'and Date_3[y][0] ==Date_2[0]:
        #         day_button[Date_3[y][1]].setStyleSheet("background-color: red")

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 435, 80, 20))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 435, 80, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 435, 80, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 435, 80, 20))
        self.label_8.setObjectName(_fromUtf8("label_3"))
        
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 435, 80, 20))
        self.label_9.setObjectName(_fromUtf8("label_3"))
        
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 435, 80, 20))
        self.label_10.setObjectName(_fromUtf8("label_3"))
        
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(550, 435, 80, 20))
        self.label_11.setObjectName(_fromUtf8("label_3"))

        label_month_name = QtGui.QLabel(self.centralwidget)
        label_month_name.setGeometry(QtCore.QRect(340, 450, 200, 100))
        label_month_name.setText(_translate("MainWindow", str(month_name) + str('  ') + str(year), None))


        self.next_month_button = QtGui.QPushButton(self.centralwidget)
        self.next_month_button.setGeometry(QtCore.QRect(510, 490, 50, 20))
        self.next_month_button.setText(" >> ")
        self.previous_month_button = QtGui.QPushButton(self.centralwidget)
        self.previous_month_button.setGeometry(QtCore.QRect(250, 490, 50, 20))
        self.previous_month_button.setText(" << ")

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        label_month_name.setFont(font)


        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 100, 420))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)

        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_12)
        
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_13)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 550, 100, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 550, 100, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit", None))
        self.pushButton_2.setText(_translate("MainWindow", "Previous", None))
        if month_number ==12:
            self.next_month_button.setEnabled(False)
        
        self.pushButton_2.clicked.connect(lambda x: self.previous_button(MainWindow))
        # self.comboBox.currentIndexChanged.connect(lambda x: self.month_selection_changed(MainWindow,Date_2))
        self.next_month_button.clicked.connect(lambda x: self.next_month_button_method(MainWindow,month_number,year,label_month_name))
        self.previous_month_button.clicked.connect(lambda x: self.previous_month_button_method(MainWindow,month_number,year,label_month_name))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    


    def previous_month_button_method(self,MainWindow,month_number,year,label_month_name):
        #label_month_name.setGeometry(QtCore.QRect(340, 450, 200, 100))
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)

        #Date_2 = Date.replace('/',',')
        #Date_2 = [int(i) for i in Date.split(',')]
        # Next/Previous Button should start from here
        month_number = month_number - 1
        print month_number
        #month_number , year = Date_2[0] , Date_2[2] 
        month_start_date,number_of_days = calendar.monthrange(year,month_number)[0],calendar.monthrange(year,month_number)[1]
        month_name = calendar.month_name[month_number]
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        # self.comboBox = QtGui.QComboBox(self.centralwidget)
        # for i in range(1,13):
        #     self.comboBox.addItem(calendar.month_name[i])
        # self.comboBox.setItemText (-1,str(month_name))
        
        #month_number , year = int(self.comboBox.currentIndex()) + 1 , Date_2[2]
        #month_start_date,number_of_days = calendar.monthrange(year,month_number)[0],calendar.monthrange(year,month_number)[1]
        #month_name = calendar.month_name[month_number]
        
        count = 1
        '''week 1'''
        day_button = {}
        if (month_start_date == 6):
            for x in range(6 - month_start_date,7):
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 30, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count+= 1 
        else:
            for x in range(month_start_date + 1,7):
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 30, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count+= 1 
        # '''week 2-4,21days'''
        for y in range(1,4):
            for x in range(0,7):
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x,  30 + 70 * y, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count+= 1 
        # '''week 5'''
        remaining_days = number_of_days - (count - 1)

        if (remaining_days <=6):
            for x in range(remaining_days):    
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 310, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count += 1 
        # '''week 6'''
        else: 
            for x in range(0,7):    
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 310, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count += 1 
            remaining_days_2 = remaining_days -7 
            for x in range(remaining_days_2):    
                day_button[count] = QtGui.QPushButton(self.centralwidget)
                day_button[count].setGeometry(QtCore.QRect(120 + 70 * x, 380, 40, 40))
                day_button[count].setText(_translate("MainWindow", str(count), None))
                count += 1  
        for i in range(1,count):
            day_button[i].clicked.connect(functools.partial(self.day_buttons_clicked,i))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 435, 80, 20))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 435, 80, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 435, 80, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 435, 80, 20))
        self.label_8.setObjectName(_fromUtf8("label_3"))
        
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 435, 80, 20))
        self.label_9.setObjectName(_fromUtf8("label_3"))
        
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 435, 80, 20))
        self.label_10.setObjectName(_fromUtf8("label_3"))
        
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(550, 435, 80, 20))
        self.label_11.setObjectName(_fromUtf8("label_3"))

        label_month_name = QtGui.QLabel(self.centralwidget)
        label_month_name.setGeometry(QtCore.QRect(340, 450, 200, 100))
        label_month_name.setText(_translate("MainWindow", str(month_name) + str('  ') + str(year), None))


        self.next_month_button = QtGui.QPushButton(self.centralwidget)
        self.next_month_button.setGeometry(QtCore.QRect(510, 490, 50, 20))
        self.next_month_button.setText(" >> ")
        self.previous_month_button = QtGui.QPushButton(self.centralwidget)
        self.previous_month_button.setGeometry(QtCore.QRect(250, 490, 50, 20))
        self.previous_month_button.setText(" << ")

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        label_month_name.setFont(font)


        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 100, 420))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)

        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_12)
        
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_13)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 550, 100, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 550, 100, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit", None))
        self.pushButton_2.setText(_translate("MainWindow", "Previous", None))

        self.pushButton_2.clicked.connect(lambda x: self.previous_button(MainWindow))
        # self.comboBox.currentIndexChanged.connect(lambda x: self.month_selection_changed(MainWindow,Date_2))
        if month_number ==1:
            self.previous_month_button.setEnabled(False)
        self.next_month_button.clicked.connect(lambda x: self.next_month_button_method(MainWindow,month_number,year,label_month_name))
        self.previous_month_button.clicked.connect(lambda x: self.previous_month_button_method(MainWindow,month_number,year,label_month_name))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

         
        

# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow()
#     ui = Ui_MainWindow()
    
#     Date = str("1,27,2020")
#     Eth_Date = str('07/08/2010')
#     Time = str("6:06"),
#     Client = str(" Zeleman")
#     Commercial = str("Coca Cola")
#     Station = str("EBC")
#     Ad = str("/Users/Ad.mpg") 
#     Stream = str("Users/Stream.mpg")
#     broadcast_information = str("Yes")
#     Ad_dur = str("120")
#     Time_in_video = str("360")
#     ui.setupUi(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video)
#     MainWindow.show()
#     sys.exit(app.exec_())

