# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend_7_Yearly_Report.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import stats_page
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
import calendar 
import datetime


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        

        # Date = Internal Date
        # Time = Internal Time 
        # Client = User Defined 
        # Commercial = User Defined
        # Station = User Defined  
        
        Date = str("7,8,2020")
        # Client = str("Zeleman")
        # Commercial = str("Coca Cola")

        Date_2 = Date.replace('/',',')
        Date_2 = [int(i) for i in Date.split(',')]
        year = Date_2[2] 
        month_name = []
        number_of_days = []
        for i in range(1,13):
            month_name.append(calendar.month_name[i])
            number_of_days.append(calendar.monthrange(year,i)[1])


        year_date_button = {}

        month_name_button = {}
        for y in range(0,12):
            for x in range(0,number_of_days[y]):
                year_date_button[x,y] = QtGui.QPushButton(self.centralwidget)
                month_name_button[y] = QtGui.QPushButton(self.centralwidget)
                year_date_button[x,y].setGeometry(QtCore.QRect(90 + 22 * x, 40 + 40 * y, 25, 25))
                month_name_button[y].setGeometry(QtCore.QRect(10 , 30 + 40 * y, 70, 50))

                year_date_button[x,y].setText(_translate("MainWindow", str(x+1), None))
                month_name_button[y].setText(_translate("MainWindow", str(month_name[y]), None))
        label_year = QtGui.QLabel(self.centralwidget)
        label_year.setGeometry(QtCore.QRect(400, 500, 200, 100))
        label_year.setText(_translate("MainWindow", str(year) + str('-')+str("GC"), None))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        label_year.setFont(font)


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

    
        MainWindow.show()
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Media Monitoring Program", "Media Monitoring Program", None))
    
    def previous_button(self,MainWindow):
        stats_page_ui = stats_page.Ui_MainWindow()
        stats_page_ui.setupUi(MainWindow)    

# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

