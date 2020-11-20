# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend_6.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import monthly_report_page
import yearly_report_page
import result_card_page
import main_menu
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
    #def setupUi(self, MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 120, 230, 190))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 120, 230, 190))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 510, 100, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 510, 100, 30))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.generate = QtGui.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(490, 510, 100, 30))
        self.generate.setObjectName(_fromUtf8("generate"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(lambda x: self.monthly_report(MainWindow))
        self.pushButton_2.clicked.connect(lambda x: self.yearly_report(MainWindow))
        self.pushButton_3.clicked.connect(lambda x: self.previous_button(MainWindow))
        self.pushButton_5.clicked.connect(lambda x: self.exit(MainWindow))
        self.generate.clicked.connect(self.generate_button_clicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Monthly Report", None))
        self.pushButton_2.setText(_translate("MainWindow", "Yearly Report", None))
        self.pushButton_3.setText(_translate("MainWindow", "Back", None))
        self.pushButton_5.setText(_translate("MainWindow", "Exit", None))
        self.generate.setText(_translate("MainWindow", "Generate", None))

    def generate_button_clicked(self):
        #generate excel report
        pass
    def monthly_report(self,MainWindow):
        monthly_report_ui = monthly_report_page.Ui_MainWindow()
        monthly_report_ui.setupUi(MainWindow)
        MainWindow.show()
    def yearly_report(self,MainWindow):
        yearly_report_ui = yearly_report_page.Ui_MainWindow()
        yearly_report_ui.setupUi(MainWindow)
        MainWindow.show()
    def previous_button(self,MainWindow):
        previous_button_ui = main_menu.Ui_MainWindow()
        previous_button_ui.setupUi(MainWindow)
        MainWindow.show()
    def exit(self,MainWindow):
        import sys
        sys.exit()


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow()
#     ui = Ui_MainWindow()
#     Date = str("12,05,12")
#     Eth_Date=str("15,01,07")
#     Time=str("3:45")
#     Client=str("Zeleman")
#     Commercial=str("Coca Cola")
#     Station=str("EBC")
#     Ad=str("/Coca_Cola")
#     Stream=str("/Stream_example")
#     broadcast_information=str("No")
#     Ad_dur=str("120sec")
#     Time_in_video = str("4:26")



#     ui.setupUi(MainWindow,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video)
#     MainWindow.show()
#     sys.exit(app.exec_())

