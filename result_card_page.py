# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend_5.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import stats_page
import result_viewer_page
import create_database_file as cdf
import create_database as cd 
import insert_data as idata 
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
database = str(os.getcwd() + "/" + str("fingerprint_database.db")).replace("\\","/")

#create database file 
cdf.create_connection(database_file)
#create database and add tables
cd.create_database_and_tables(database_file)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video):
        #MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(550, 520, 250, 50))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(70, 30, 520, 360))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout = QtGui.QGridLayout(self.widget1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_7 = QtGui.QLabel(self.widget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.widget1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_10 = QtGui.QLabel(self.widget1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_9 = QtGui.QLabel(self.widget1)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_4 = QtGui.QLabel(self.widget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.label_10.setText(_translate("MainWindow", str(Date), None))
        self.label_9.setText(_translate("MainWindow", str(Eth_Date), None))
        self.label_4.setText(_translate("MainWindow", str(broadcast_information), None))
        self.label_6.setText(_translate("MainWindow", str(Ad_dur), None))

        self.pushButton.clicked.connect(lambda x: self.see_stats(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video))
        self.pushButton_3.clicked.connect(lambda x: self.previous_button(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video))
        self.pushButton_2.clicked.connect(lambda x: self.exit(MainWindow))
        #self.pushButton_3.clicked.connect(lambda x: self.previous_button())

        #add information to database
        idata.insert_information_to_database(database_file,str(Date),str(Eth_Date),str(Time),str(Client),str(Commercial),str(Station),str(Ad),str(Stream),str(broadcast_information),str(Ad_dur),str(Time_in_video))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))
        self.pushButton.setText(_translate("MainWindow", "See Stats", None))
        self.pushButton_3.setText(_translate("MainWindow", "Previous", None))
        self.pushButton_2.setText(_translate("MainWindow", "Exit", None))
        self.label_7.setText(_translate("MainWindow", "Date:", None))
        self.label_8.setText(_translate("MainWindow", "Eth Date:", None))
        self.label.setText(_translate("MainWindow", "Was Broadcasted:", None))
        self.label_3.setText(_translate("MainWindow", "Total Seconds Broadcasted:", None))
        
    def setupUi_mod(self,number,MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(550, 520, 250, 50))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(70, 30, 520, 360))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout = QtGui.QGridLayout(self.widget1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_7 = QtGui.QLabel(self.widget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.widget1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_10 = QtGui.QLabel(self.widget1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_2.addWidget(self.label_10)
        #self.label_9 = QtGui.QLabel(self.widget1)
        #self.label_9.setObjectName(_fromUtf8("label_9"))
        #self.verticalLayout_2.addWidget(self.label_9)
        self.label_4 = QtGui.QLabel(self.widget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        Date[0]==number
        self.label_10.setText(_translate("MainWindow", str(Date), None))
        #self.label_9.setText(_translate("MainWindow", str(Eth_Date), None))
        self.label_4.setText(_translate("MainWindow", str(broadcast_information), None))
        self.label_6.setText(_translate("MainWindow", str(Ad_dur), None))

        self.pushButton.clicked.connect(lambda x: self.see_stats(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video))
        self.pushButton_3.clicked.connect(lambda x: self.previous_button(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video))
        self.pushButton_2.clicked.connect(lambda x: self.exit(MainWindow))
        #self.pushButton_3.clicked.connect(lambda x: self.previous_button())

        #add information to database
        #idata.insert_information_to_database(database_file,str(Date),str(Eth_Date),str(Time),str(Client),str(Commercial),str(Station),str(Ad),str(Stream),str(broadcast_information),str(Ad_dur),str(Time_in_video))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def see_stats(self,MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video):
        stats_page_ui = stats_page.Ui_MainWindow()
        stats_page_ui.setupUi(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video)
        MainWindow.show()
    def previous_button(self,MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video):
        result_viewer_page_ui = result_viewer_page.Ui_MainWindow()
        result_viewer_page_ui.setupUi(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video)
        MainWindow.show()
    #def previous_button(self,MainWindow):
        #stats_page_ui = stats_page.Ui_MainWindow()
        #stats_page_ui.setupUi(MainWindow)
        #MainWindow.show()
    def exit(self,MainWindow):
        import sys
        sys.exit()

# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

