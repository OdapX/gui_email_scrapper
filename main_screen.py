# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gui2 import Ui_MainWindow
from Emails_Bot import Bot
import threading


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 783)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, -10, 1111, 811))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
                                    "background-color:#597FF8\n"
                                    "}")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 311, 51))
        self.label.setStyleSheet("color:black;\n"
                                 "\n"
                                 "font: 25pt \"Arial\";\n"
                                 "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 161, 51))
        self.label_2.setStyleSheet("color:black;\n"
                                   "\n"
                                   "font: 22pt \"Arial\";\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.SiteInput = QtWidgets.QLineEdit(self.bgwidget)
        self.SiteInput.setGeometry(QtCore.QRect(170, 130, 441, 51))
        self.SiteInput.setStyleSheet("border-radius:14px;\n"
                                     "")
        self.SiteInput.setText("")
        self.SiteInput.setObjectName("SiteInput")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 141, 51))
        self.label_3.setStyleSheet("color:black;\n"
                                   "\n"
                                   "font: 24pt \"Arial\";\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.UploadNiche = QtWidgets.QPushButton(self.bgwidget)
        self.UploadNiche.setGeometry(QtCore.QRect(170, 230, 441, 51))
        self.UploadNiche.setStyleSheet("QWidget#UploadNiche{\n"
                                       "color:#122DAF;\n"
                                       "font: 20pt \"MS Shell Dlg 2\";\n"
                                       "background-color:#DDDDDD;\n"
                                       "border-radius:14px;\n"

                                       "}")
        self.UploadNiche.setObjectName("UploadNiche")
        self.label_4 = QtWidgets.QLabel(self.bgwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 141, 51))
        self.label_4.setStyleSheet("color:black;\n"
                                   "\n"
                                   "font: 24pt \"Arial\";\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.UploadProxies = QtWidgets.QPushButton(self.bgwidget)
        self.UploadProxies.setGeometry(QtCore.QRect(170, 340, 441, 51))
        self.UploadProxies.setStyleSheet("QWidget#UploadProxies{\n"
                                         "color:#122DAF;\n"
                                         "font: 20pt \"MS Shell Dlg 2\";\n"
                                         "background-color:#DDDDDD;\n"
                                         "border-radius:14px;\n"

                                         "}")
        self.UploadProxies.setObjectName("UploadProxies")
        self.startBtn = QtWidgets.QPushButton(self.bgwidget)
        self.startBtn.setGeometry(QtCore.QRect(90, 440, 201, 41))
        self.startBtn.setStyleSheet("background-color:#5CEBDF;\n"
                                    "border-radius:14px;\n"
                                    "color:#122DAF;\n"
                                    "font: 18pt \"MS Shell Dlg 2\";")

        self.startBtn.setObjectName("startBtn")
        self.Stopbtn = QtWidgets.QPushButton(self.bgwidget)
        self.Stopbtn.setGeometry(QtCore.QRect(360, 440, 201, 41))
        self.Stopbtn.setStyleSheet("background-color:#FF0400;\n"
                                   "border-radius:14px;\n"
                                   "color:#122DAF;\n"
                                   "font: 20pt \"MS Shell Dlg 2\";")
        self.Stopbtn.setObjectName("Stopbtn")
        self.label_5 = QtWidgets.QLabel(self.bgwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 590, 141, 51))
        self.label_5.setStyleSheet("color:black;\n"
                                   "\n"
                                   "font: 18pt \"Arial\";\n"
                                   "")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.bgwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 640, 231, 51))
        self.label_6.setStyleSheet("color:black;\n"
                                   "\n"
                                   "font: 18pt \"Arial\";\n"
                                   "")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.bgwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 730, 281, 51))
        self.label_8.setStyleSheet("color:black;\n"
                                   "\n"
                                   "font: 18pt \"Arial\";\n"
                                   "")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.bgwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 690, 231, 51))
        self.label_7.setStyleSheet("color:black;\n"
                                   "\n"
                                   "font: 18pt \"Arial\";\n"
                                   "")
        self.label_7.setObjectName("label_7")
        self.start_time = QtWidgets.QLabel(self.bgwidget)
        self.start_time.setGeometry(QtCore.QRect(150, 590, 201, 41))
        self.start_time.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                      "color:white\n"
                                      "")
        self.start_time.setObjectName("start_time")
        self.number_of_niches = QtWidgets.QLabel(self.bgwidget)
        self.number_of_niches.setGeometry(QtCore.QRect(240, 650, 191, 31))
        self.number_of_niches.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                            "color:white\n"
                                            "")
        self.number_of_niches.setObjectName("number_of_niches")
        self.number_of_proxies = QtWidgets.QLabel(self.bgwidget)
        self.number_of_proxies.setGeometry(QtCore.QRect(250, 700, 301, 31))
        self.number_of_proxies.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                             "color:white\n"
                                             "")
        self.number_of_proxies.setObjectName("number_of_proxies")
        self.total_emails_scrapped = QtWidgets.QLabel(self.bgwidget)
        self.total_emails_scrapped.setGeometry(QtCore.QRect(280, 740, 301, 31))
        self.total_emails_scrapped.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                                 "color:white\n"
                                                 "")
        self.total_emails_scrapped.setObjectName("total_emails_scrapped")
        self.label_9 = QtWidgets.QLabel(self.bgwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 530, 231, 51))
        self.label_9.setStyleSheet("color:black;\n"
                                   "\n"
                                   "font: 18pt \"Arial\";\n"
                                   "")
        self.label_9.setObjectName("label_9")
        self.current_Niche = QtWidgets.QLabel(self.bgwidget)
        self.current_Niche.setGeometry(QtCore.QRect(340, 530, 201, 41))
        self.current_Niche.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                         "color:white\n"
                                         "")
        self.current_Niche.setObjectName("current_Niche")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(630, 0, 691, 801))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
                                    "background-color:#122DAF;\n"
                                    "}")
        self.widget_2.setObjectName("widget_2")
        self.Emails_output = QtWidgets.QTextEdit(self.widget_2)
        self.Emails_output.setGeometry(QtCore.QRect(30, 20, 601, 521))
        self.Emails_output.setObjectName("Emails_output")
        self.copyBtn = QtWidgets.QPushButton(self.widget_2)
        self.copyBtn.setGeometry(QtCore.QRect(260, 570, 201, 41))
        self.copyBtn.setStyleSheet("background-color:#5CEBDF;\n"
                                   "border-radius:14px;\n"
                                   "color:#122DAF;\n"
                                   "font: 18pt \"MS Shell Dlg 2\";")
        self.copyBtn.setObjectName("copyBtn")

        # Buttons click Events
        self.startBtn.clicked.connect(self.Start)
        self.Stopbtn.clicked.connect(self.stop)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def Start(self):
        try:
            t.start()
        except:
            pass

    def stop(self):
        try:
            t.terminate()
        except:
            pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "DATA TO SEARCH"))
        self.label_2.setText(_translate("Dialog", "WEBSITES"))
        self.label_3.setText(_translate("Dialog", "NICHES"))
        self.UploadNiche.setText(_translate("Dialog", "UPLOAD"))
        self.label_4.setText(_translate("Dialog", "PROXIES"))
        self.UploadProxies.setText(_translate("Dialog", "UPLOAD"))
        self.startBtn.setText(_translate("Dialog", "SEARCH"))
        self.Stopbtn.setText(_translate("Dialog", "STOP"))
        self.label_5.setText(_translate("Dialog", "Start Time : "))
        self.label_6.setText(_translate("Dialog", "Number of Niches : "))
        self.label_8.setText(_translate("Dialog", "Total Emails Scrapped :"))
        self.label_7.setText(_translate("Dialog", "Number of Proxies  : "))
        self.start_time.setText(_translate("Dialog", "?"))
        self.number_of_niches.setText(_translate("Dialog", "?"))
        self.number_of_proxies.setText(_translate("Dialog", "?"))
        self.total_emails_scrapped.setText(_translate("Dialog", "?"))
        self.label_9.setText(_translate("Dialog", "Current Niche : "))
        self.current_Niche.setText(_translate("Dialog", "?"))
        self.copyBtn.setText(_translate("Dialog", "COPY"))

#     def newTab(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()
#         Dialog.close()


if __name__ == "__main__":
    import sys
    PROXY_LIST = [
        {
            'PROXY_HOST': '186.65.117.169',
            'PROXY_PORT': '9582',
            'PROXY_USER': '2c91Ug',
            'PROXY_PASS': '6MEc6s'

        },

        {
            'PROXY_HOST': '46.232.14.210',
            'PROXY_PORT': '8000',
            'PROXY_USER': 'jHmVb5',
            'PROXY_PASS': 'VaDjAG'

        },
        {
            'PROXY_HOST': '46.232.15.30',
            'PROXY_PORT': '8000',
            'PROXY_USER': 'jHmVb5',
            'PROXY_PASS': 'VaDjAG'

        },

    ]
    websites = ['instagram.com']
    niches = ['dogs', 'cats']
    bit = Bot(PROXY_LIST, websites, niches)

    t = threading.Thread(target=lambda: bit.All_Scrapper())
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())