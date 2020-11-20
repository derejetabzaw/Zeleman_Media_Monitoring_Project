# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend_3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from proprocess import get_sec,getLength,trimmer
from time import sleep
import subprocess
import os
import sys
import result_viewer_page
sys.path.insert(1, os.path.join(os.getcwd(),'matching'))
import sqed_dir as sqd
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
    def setupUi(self,MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(795, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        
        self.pushButton.setGeometry(QtCore.QRect(690, 530, 100, 30))

        self.pushButton.setObjectName(_fromUtf8("pushButton"))
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
        self.myLongTask = TaskThread(Ad = Ad,Stream = Stream)
        self.myLongTask.start()
        

        self.myLongTask.valueChanged.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.progressBar.setValue)
        self.myLongTask.taskFinished.connect(self.pushButton.setEnabled)
        

        self.myLongTask.connect(self.myLongTask, QtCore.SIGNAL('labeltext(QString)'), self.label.setText)
        self.pushButton.clicked.connect(lambda x: self.next_button(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))
        self.pushButton.setText(_translate("MainWindow", "Next", None))
        self.pushButton.setEnabled(False)
        self.label.setText(_translate("MainWindow", "This may take few minutes...", None))

    def next_button(self,MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream):
        broadcast_information, additional_information = sqd.matching(str(os.path.join(os.getcwd(),'output'))) 
        print broadcast_information
        Ad_dur = get_sec(getLength(str(Ad))[0:8])
        Time_in_video = Ad_dur * (int(additional_information[1]) - 1)
        result_viewer_page_ui = result_viewer_page.Ui_MainWindow()
        result_viewer_page_ui.setupUi(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video)
        MainWindow.show()

class TaskThread(QThread):
    taskFinished = QtCore.pyqtSignal(int,bool)
    valueChanged = QtCore.pyqtSignal(int)
    

    def __init__(self,Ad,Stream):
        super(QThread, self).__init__()
        self.Ad = Ad
        self.Stream = Stream
        print self.Ad
        print self.Stream
    def run(self):
        self.Ad = str(self.Ad)
        self.Stream = str(self.Stream)
        
        sleep(1)
        '''Getting Duration'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Getting Duration..."))
        Ad_dur = get_sec(getLength(self.Ad)[0:8])
        St_dur = get_sec(getLength(self.Stream)[0:8])
        for i in xrange(15,2):
            self.valueChanged.emit(i) 
            sleep(0.5)
        
        '''Indexing'''    
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Indexing..."))
        segment_index = int(round(St_dur / Ad_dur))
        for i in range(15,26,2):
            self.valueChanged.emit(i)
            sleep(0.5)
        
        '''Trimming'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Trimming..."))
        #trimmer(Ad_dur,St_dur,segment_index,self.Stream,self.Ad)
        for i in range(26,41,2):
            self.valueChanged.emit(i)
            sleep(0.5) 
        
        '''Centroid of Gradient Orientation'''
        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Fingerprinting..."))
        fingerprint="ruby dupe.rb"                                                                                  
        #os.system(fingerprint) 
        for i in range(41,98,4):
            self.valueChanged.emit(i)
            sleep(0.5)

        self.emit(QtCore.SIGNAL('labeltext(QString)'), QtCore.QString("Done"))
        self.taskFinished.emit(100,True)  
        
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow,Date,Eth_date,Time,Client,Commercial,Station,Ad,Stream)
#     MainWindow.show()
#     sys.exit(app.exec_())

