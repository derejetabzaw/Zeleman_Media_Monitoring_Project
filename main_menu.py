import os 
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import main_menu
import fingerprint 
import stats_page
import scan_type_option

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
   
        
 
        self.fingerprint_button = QtGui.QPushButton(self.centralwidget)
        self.fingerprint_button.setGeometry(QtCore.QRect(100,100,120,70))
        self.fingerprint_button.setText("Fingerprint")


        self.scan_button = QtGui.QPushButton(self.centralwidget)
        self.scan_button.setGeometry(QtCore.QRect(300,100,120,70))
        self.scan_button.setText("Advertisment Scan")


        self.report_button = QtGui.QPushButton(self.centralwidget)
        self.report_button.setGeometry(QtCore.QRect(500,100,120,70))
        self.report_button.setText("Report and Stats")






        self.fingerprint_button.clicked.connect(lambda x: self.fingerprint_button_menu(MainWindow))
        self.scan_button.clicked.connect(lambda x: self.scan_button_menu(MainWindow))
        self.report_button.clicked.connect(lambda x: self.report_button_menu(MainWindow))
        MainWindow.setCentralWidget(self.centralwidget)

    def fingerprint_button_menu(self,MainWindow):
        fingerprint_menu_ui = fingerprint.Ui_MainWindow()
        fingerprint_menu_ui.setupUi(MainWindow)
        MainWindow.show()
    def scan_button_menu(self,MainWindow):
        scanner_menu_ui = scan_type_option.Ui_MainWindow()
        scanner_menu_ui.setupUi(MainWindow)
        MainWindow.show()
    def report_button_menu(self,MainWindow):
        stats_ui = stats_page.Ui_MainWindow()
        stats_ui.setupUi(MainWindow)

        MainWindow.show()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

