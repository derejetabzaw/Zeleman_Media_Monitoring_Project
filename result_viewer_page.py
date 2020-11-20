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
    def setupUi(self, MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 80, 480, 150))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.setText(_translate("MainWindow", broadcast_information, None))
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.setText(_translate("MainWindow",str(Time_in_video), None))
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 2)
        
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 560))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        

        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setGeometry(QtCore.QRect(490, 530, 100, 30))
        
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 530, 100, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 530, 100, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        #self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_6.setText(_translate("MainWindow",str(Ad_dur), None))
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        if broadcast_information =='No':
            self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(lambda x: self.watch_in_time_button(str(Time_in_video),str(Stream)))
        #self.pushButton_2.clicked.connect(lambda x: self.previous_button(str(Time_in_video),str(Stream)))
        self.pushButton_3.clicked.connect(lambda x: self.next_button(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video))
        self.pushButton_2.clicked.connect(lambda x: self.previous_button(MainWindow,Date,Time,Client,Commercial,Station,Ad,Stream))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Was Broadcasted:", None))
        #self.label_4.setText(_translate("MainWindow", broadcast_information, None))
        self.label_2.setText(_translate("MainWindow", "Time in Video:", None))
        self.pushButton.setText(_translate("MainWindow", "Watch in Time", None))
        self.label_3.setText(_translate("MainWindow", "Total Seconds Broadcasted:", None))
        #self.label_6.setText(_translate("MainWindow",Ad_dur, None))
        self.pushButton_3.setText(_translate("MainWindow", "Next", None))
        self.pushButton_2.setText(_translate("MainWindow", "Previous", None))

    def watch_in_time_button(self,Time_in_video,Stream):
        cmd = program + str(" ") + str(Stream) + " -ss " + str(Time_in_video)
        os.system(cmd)
    #def previous_button():

    def next_button(self,MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,Was_Broadcasted,Time_BS,Time_in_video):
        #MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video
        result_card_page_ui = result_card_page.Ui_MainWindow()
        result_card_page_ui.setupUi(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,Was_Broadcasted,Time_BS,Time_in_video)
        MainWindow.show()

    def previous_button(self,MainWindow,Date,Time,Client,Commercial,Station,Ad,Stream):
        browse_page_ui = browse_page.Ui_MainWindow()
        browse_page_ui.setupUi(MainWindow,Date,Time,Client,Commercial,Station,Ad,Stream)
        MainWindow.show()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

