# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend_2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import browse_page
import load_page
from PyQt4 import QtCore, QtGui

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
    def setupUi(self, MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 560))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(690, 530, 100, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 530, 100, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 70, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(30, 80, 750, 250))
        self.widget.setObjectName(_fromUtf8("widget"))
        
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_17 = QtGui.QLabel(self.widget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_3.addWidget(self.label_17)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_7.addWidget(self.label_3)
        self.label_16 = QtGui.QLabel(self.widget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_7.addWidget(self.label_16)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_15 = QtGui.QLabel(self.widget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_2.addWidget(self.label_15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_6.addWidget(self.label_12)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.widget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.setText(_translate("MainWindow", "Next", None))
        self.pushButton_2.setText(_translate("MainWindow", "Previous", None))
        self.label_5.setText(_translate("MainWindow", "Summary", None))
        self.label_4.setText(_translate("MainWindow", "Time:", None))
        self.label_17.setText(_translate("MainWindow",Time, None))
        self.label_3.setText(_translate("MainWindow", "Date:", None))
        self.label_16.setText(_translate("MainWindow", Date, None))
        self.label_11.setText(_translate("MainWindow", "Eth Date:", None))
        self.label_15.setText(_translate("MainWindow", Eth_date, None))
        self.label_8.setText(_translate("MainWindow", "Client:", None))
        self.label_7.setText(_translate("MainWindow", Client, None))
        self.label_9.setText(_translate("MainWindow", "Commercial:", None))
        self.label_6.setText(_translate("MainWindow", Commercial, None))
        self.label_10.setText(_translate("MainWindow", "TV/Radio Channel:", None))
        self.label_12.setText(_translate("MainWindow", Station, None))
        self.label_2.setText(_translate("MainWindow", "Stream:", None))
        self.label.setText(_translate("MainWindow", "Ad:", None))
        self.label_13.setText(_translate("MainWindow", Ad, None))
        self.label_14.setText(_translate("MainWindow", Stream, None))

        self.pushButton.clicked.connect(lambda x: self.next_button(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream))

        self.pushButton_2.clicked.connect(lambda x: self.previous_button(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))

    def next_button(self,MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream):

        load_page_ui = load_page.Ui_MainWindow()
        load_page_ui.setupUi(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream)
        MainWindow.show()
    def previous_button(self,MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream):
        browse_page_ui = browse_page.Ui_MainWindow()
        browse_page_ui.setupUi(MainWindow,Date,Time,Client,Commercial,Station,Ad,Stream)
        MainWindow.show()
        

