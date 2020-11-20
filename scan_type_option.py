import os 
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import main_menu
# import fingerprint 
# import scanner 
# import stats_page
import scanner 

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(720, 400)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
   
        
 
        self.Easy_Scan = QtGui.QPushButton(self.centralwidget)
        self.Easy_Scan.setGeometry(QtCore.QRect(100,100,120,70))
        self.Easy_Scan.setText("Easy Scan")


        self.Normal_Scan = QtGui.QPushButton(self.centralwidget)
        self.Normal_Scan.setGeometry(QtCore.QRect(300,100,120,70))
        self.Normal_Scan.setText("Normal Scan \n \n (Recommended)")

        self.Advanced_Scan = QtGui.QPushButton(self.centralwidget)
        self.Advanced_Scan.setGeometry(QtCore.QRect(500,100,120,70))
        self.Advanced_Scan.setText("Advanced Scan")






        self.Easy_Scan.clicked.connect(lambda x: self.Easy_Scan_button_menu(MainWindow))
        self.Normal_Scan.clicked.connect(lambda x: self.Normal_Scan_button_menu(MainWindow))
        self.Advanced_Scan.clicked.connect(lambda x: self.Advanced_Scan_button_menu(MainWindow))
        MainWindow.setCentralWidget(self.centralwidget)

    def Easy_Scan_button_menu(self,MainWindow):
        easy_scan_menu_ui = easy_scanner.Ui_MainWindow()
        easy_scan_menu_ui.setupUi(MainWindow)
        MainWindow.show()
    def Normal_Scan_button_menu(self,MainWindow):
        normal_scan_menu_ui = scanner.Ui_MainWindow()
        normal_scan_menu_ui.setupUi(MainWindow)
        MainWindow.show()
    def Advanced_Scan_button_menu(self,MainWindow):
        advanced_scan_ui = advanced_scanner.Ui_MainWindow()
        advanced_scan_ui.setupUi(MainWindow)

        MainWindow.show()
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

