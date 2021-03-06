# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from Emails_Bot import Bot
import threading
from datetime import datetime
from time import sleep
import sqlite3


class Ui_Dialog(object):
    Niche_file_dir = ""
    Proxy_file_dir = ""
    Websites = []
    Niches = []
    Proxies = []
    STOP = False
    bot = None

    def setupUi(self, Dialog):

        Dialog.setObjectName("BOT")
        Dialog.resize(1280, 783)
        Dialog.setFixedSize(1280, 783)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, -10, 1111, 811))
        self.bgwidget.setStyleSheet(
            "QWidget#bgwidget{\n" "background-color:#132E50\n" "}"
        )
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 311, 51))
        self.label.setStyleSheet(
            "color:white;\n" "\n" 'font: 25pt "Arial";\n' "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 161, 51))
        self.label_2.setStyleSheet(
            "color:white;\n" "\n" 'font: 22pt "Arial";\n' "")
        self.label_2.setObjectName("label_2")

        self.SiteInput = QtWidgets.QLineEdit(self.bgwidget)
        self.SiteInput.setGeometry(QtCore.QRect(170, 130, 441, 51))
        self.SiteInput.setStyleSheet("border-radius:14px;\n" "")
        self.SiteInput.setText("")
        self.SiteInput.setObjectName("SiteInput")
        self.SiteInput.setStyleSheet(
            "color:black;\n" "border-radius:14px;\n" 'font: 18pt "Arial";\n' ""
        )
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 141, 51))
        self.label_3.setStyleSheet(
            "color:white;\n" "\n" 'font: 24pt "Arial";\n' "")
        self.label_3.setObjectName("label_3")
        self.UploadNiche = QtWidgets.QPushButton(self.bgwidget)
        self.UploadNiche.setGeometry(QtCore.QRect(170, 230, 441, 51))
        self.UploadNiche.setStyleSheet(
            "QWidget#UploadNiche{\n"
            "color:#122DAF;\n"
            'font: 20pt "MS Shell Dlg 2";\n'
            "background-color:#DDDDDD;\n"
            "border-radius:14px;\n"
            "}"
        )
        self.UploadNiche.setObjectName("UploadNiche")
        self.label_4 = QtWidgets.QLabel(self.bgwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 141, 51))
        self.label_4.setStyleSheet(
            "color:white;\n" "\n" 'font: 24pt "Arial";\n' "")
        self.label_4.setObjectName("label_4")
        self.UploadProxies = QtWidgets.QPushButton(self.bgwidget)
        self.UploadProxies.setGeometry(QtCore.QRect(170, 340, 441, 51))
        self.UploadProxies.setStyleSheet(
            "QWidget#UploadProxies{\n"
            "color:#122DAF;\n"
            'font: 20pt "MS Shell Dlg 2";\n'
            "background-color:#DDDDDD;\n"
            "border-radius:14px;\n"
            "}"
        )

        self.UploadProxies.setObjectName("UploadProxies")
        self.startBtn = QtWidgets.QPushButton(self.bgwidget)
        self.startBtn.setGeometry(QtCore.QRect(20, 440, 301, 52))
        self.startBtn.setStyleSheet(
            """
QPushButton#startBtn {
    background-color:#838C95;
    color:white;
    border-radius: 14px;
    font: 20pt MS Shell Dlg 2;
}

QPushButton#startBtn:hover {
    background-color: #64b5f6;
    color: #fff;
}

"""
        )

        self.startBtn.setObjectName("startBtn")
        self.Stopbtn = QtWidgets.QPushButton(self.bgwidget)
        self.Stopbtn.setGeometry(QtCore.QRect(330, 440, 301, 52))
        self.Stopbtn.setStyleSheet(
            """
QPushButton#Stopbtn {
    background-color: #838C95 ;
    color:white;
    border-radius: 14px;
    font: 20pt MS Shell Dlg 2;
}

QPushButton#Stopbtn:hover {
    background-color: #64b5f6;
    color: #fff;
}

"""
        )
        self.Stopbtn.setObjectName("Stopbtn")
        self.label_5 = QtWidgets.QLabel(self.bgwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 590, 141, 51))
        self.label_5.setStyleSheet(
            "color:white;\n" "\n" 'font: 18pt "Arial";\n' "")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.bgwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 640, 231, 51))
        self.label_6.setStyleSheet(
            "color:white;\n" "\n" 'font: 18pt "Arial";\n' "")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.bgwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 730, 281, 51))
        self.label_8.setStyleSheet(
            "color:white;\n" "\n" 'font: 18pt "Arial";\n' "")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.bgwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 690, 231, 51))
        self.label_7.setStyleSheet(
            "color:white;\n" "\n" 'font: 18pt "Arial";\n' "")
        self.label_7.setObjectName("label_7")
        self.start_time = QtWidgets.QLabel(self.bgwidget)
        self.start_time.setGeometry(QtCore.QRect(150, 590, 201, 41))
        self.start_time.setStyleSheet(
            'font: 16pt "MS Shell Dlg 2";\n' "color:white\n" ""
        )
        self.start_time.setObjectName("start_time")
        self.number_of_niches = QtWidgets.QLabel(self.bgwidget)
        self.number_of_niches.setGeometry(QtCore.QRect(280, 650, 191, 31))
        self.number_of_niches.setStyleSheet(
            'font: 16pt "MS Shell Dlg 2";\n' "color:white\n" ""
        )
        self.number_of_niches.setObjectName("number_of_niches")
        self.number_of_proxies = QtWidgets.QLabel(self.bgwidget)
        self.number_of_proxies.setGeometry(QtCore.QRect(280, 700, 301, 31))
        self.number_of_proxies.setStyleSheet(
            'font: 16pt "MS Shell Dlg 2";\n' "color:white\n" ""
        )
        self.number_of_proxies.setObjectName("number_of_proxies")
        self.total_emails_scrapped = QtWidgets.QLabel(self.bgwidget)
        self.total_emails_scrapped.setGeometry(QtCore.QRect(280, 740, 301, 31))
        self.total_emails_scrapped.setStyleSheet(
            'font: 16pt "MS Shell Dlg 2";\n' "color:white\n" ""
        )
        self.total_emails_scrapped.setObjectName("total_emails_scrapped")
        self.label_9 = QtWidgets.QLabel(self.bgwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 530, 231, 51))
        self.label_9.setStyleSheet(
            "color:white;\n" "\n" 'font: 18pt "Arial";\n' "")
        self.label_9.setObjectName("label_9")

        self.current_Niche = QtWidgets.QLabel(self.bgwidget)
        self.current_Niche.setGeometry(QtCore.QRect(300, 535, 201, 41))
        self.current_Niche.setStyleSheet(
            'font: 16pt "MS Shell Dlg 2";\n' "color:white\n" ""
        )

        self.Alert = QtWidgets.QLabel(self.bgwidget)
        self.Alert.setGeometry(QtCore.QRect(240, 490, 301, 51))
        self.Alert.setStyleSheet(
            "color:red;\n" "\n" 'font: 16pt "Arial";\n' "")
        self.Alert.setObjectName("Alert")

        self.current_Niche.setObjectName("current_Niche")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(630, 0, 691, 801))
        self.widget_2.setStyleSheet(
            "QWidget#widget_2{\n" "background-color:#132E50;\n" "}"
        )
        self.widget_2.setObjectName("widget_2")
        self.Emails_output = QtWidgets.QTextEdit(self.widget_2)
        self.Emails_output.setGeometry(QtCore.QRect(30, 20, 601, 521))
        self.Emails_output.setObjectName("Emails_output")
        self.Emails_output.setStyleSheet(
            """         
                       top:10px;
                       font:20px;
        
        """
        )

        self.copyBtn = QtWidgets.QPushButton(self.widget_2)
        self.copyBtn.setGeometry(QtCore.QRect(200, 570, 330, 48))
        self.copyBtn.setStyleSheet(
            """
QPushButton#copyBtn {
    background-color: #838C95;
    color:white;
    border-radius: 14px;
    font: 20pt MS Shell Dlg 2;

}

QPushButton#copyBtn:hover {

    background-color: #64b5f6;
    color: #fff;
}

"""
        )
        self.copyBtn.setObjectName("copyBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # __________________________________________
        #
        #
        #   Buttons EVENTS AND CLICKS
        #
        # ____________________________________________

        self.startBtn.clicked.connect(self.Start)
        self.Stopbtn.clicked.connect(self.stop)
        self.UploadNiche.clicked.connect(self.Upload_Niche_FILE)
        self.UploadProxies.clicked.connect(self.Upload_Proxies_FILE)
        # self.copyBtn.clicked.connect()

    # __________________________________________
    #
    #
    #   FILES UPLOAD AND PREREQUISITE DATA
    #
    # ____________________________________________

    def Get_Emails(self):
        Start_RowId = 0
        while not self.STOP or self.bot.Error:
            con = sqlite3.connect(os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "lightDatabase", "Emails.db"))
            cur = con.cursor()
            cur.execute(
                """
                        SELECT rowid,email,niche,website
                        FROM Emails where rowid > %d;

                                """
                % Start_RowId
            )

            emails = cur.fetchall()
            cur.execute(
                """
                        SELECT max(rowid)
                        FROM Emails ;

                                """
            )
            Start_RowId = cur.fetchone()[0]
            con.commit()
            con.close()
            for e in emails:
                self.Emails_output.append(f"\n{e[0]} \t{e[1]}\t{e[2]} ")
            self.total_emails_scrapped.setText(str(Start_RowId))
            sleep(5)

    def Upload_Niche_FILE(self):

        dir = "./"
        self.Niche_file_dir = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select a file...", dir, filter="*.txt"
        )[0]

        if self.Niche_file_dir:
            self.UploadNiche.setStyleSheet(
                "QWidget#UploadNiche{\n"
                "color:white;\n"
                'font: 20pt "MS Shell Dlg 2";\n'
                "background-color:#1DA1F2;\n"
                "border-radius:14px;\n"
                "}"
            )
            self.UploadNiche.setText("Uploaded")

    def Upload_Proxies_FILE(self):

        dir = "./"
        self.Proxy_file_dir = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select a file...", dir, filter="*.txt"
        )[0]

        if self.Proxy_file_dir:
            self.UploadProxies.setStyleSheet(
                "QWidget#UploadProxies{\n"
                "color:white;\n"
                'font: 20pt "MS Shell Dlg 2";\n'
                "background-color:#1DA1F2;\n"
                "border-radius:14px;\n"
                "}"
            )
            self.UploadProxies.setText("Uploaded")

    def Fill_PreScrapping_Fields(self):

        try:
            self.start_time.setText(datetime.now().strftime("%H:%M:%S"))
        except:
            pass

        try:
            count_Niches = 0
            with open(self.Niche_file_dir) as Niche_File:

                Lines = Niche_File.readlines()
                for line in Lines:
                    if line != "\n":
                        count_Niches += 1

            self.number_of_niches.setText(str(count_Niches))
        except:
            pass

        try:
            count_Proxies = 0
            with open(self.Proxy_file_dir) as Proxy_File:

                Lines = Proxy_File.readlines()
                for line in Lines:
                    if line != "\n":
                        count_Proxies += 1

            self.number_of_proxies.setText(str(count_Proxies))
        except:
            pass

    def Get_Scrapping_Update(self):
        old_niche = ""
        emails_number = 0
        sleep(5)

        # only keep getting updates if the scrapping is not finished
        # and no error was occurred from the bot side
        try:
            while not self.bot.Finished_Scrapping and not self.bot.Error:
                con = sqlite3.connect(os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), "lightDatabase", "Emails.db"))
                cur = con.cursor()
                total_rows = cur.execute(
                    "SELECT rowid from Emails order by ROWID DESC limit 1"
                )
                con.close()
                if emails_number != total_rows:
                    try:
                        self.current_Niche.setText(self.bot.Current_Niche)
                        self.total_emails_scrapped.setText(total_rows)
                        old_niche = self.bot.Current_Niche
                        emails_number = self.bot.Total_Emails
                    except:
                        pass
                else:
                    sleep(5)
        except Exception as e:
            print(e)
            pass

    # ___________________________
    #
    # Store data into the class variables
    #
    # ____________________________

    def Store_Inputs(self):
        try:
            self.Websites = self.SiteInput.text().split(",")

            with open(self.Niche_file_dir) as Niche_File:
                for Line in Niche_File:

                    self.Niches.append(Line.split("\n")[0])

            with open(self.Proxy_file_dir) as Proxy_File:
                for Line in Proxy_File:
                    proxy = {
                        "PROXY_HOST": "",
                        "PROXY_PORT": "",
                        "PROXY_USER": "",
                        "PROXY_PASS": "",
                    }
                    Proxy_Details = Line.split("\n")[0].split(":")
                    proxy["PROXY_HOST"] = Proxy_Details[0]
                    proxy["PROXY_PORT"] = Proxy_Details[1]
                    proxy["PROXY_USER"] = Proxy_Details[2]
                    proxy["PROXY_PASS"] = Proxy_Details[3]

                    self.Proxies.append(proxy)
        except:
            pass

    # __________________________________________
    #
    # Handlers
    #
    # __________________________________________

    def Start(self):
        self.Store_Inputs()

        if (
            self.Niche_file_dir
            and self.Proxy_file_dir
            and self.Websites
            and self.Niches
            and self.Proxies
        ):
            try:
                self.bot = Bot(self.Proxies, self.Websites, self.Niches)
                self.Fill_PreScrapping_Fields()
                t = threading.Thread(target=lambda: self.bot.All_Scrapper())
                t.start()

                t1 = threading.Thread(
                    target=lambda: self.Get_Scrapping_Update())
                t1.start()

                t2 = threading.Thread(target=lambda: self.Get_Emails())
                t2.start()

            except:
                print("eroor")
                pass
        else:
            self.Alert.setText("*All the fields are required")

    def stop(self):
        try:
            self.bot.Exit = True
            self.STOP = True
        except:
            pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BOT SCRAPPER "))
        Dialog.setWindowIcon(QtGui.QIcon("./public/Icon.png"))
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
        self.number_of_niches.setText(_translate("Dialog", "0"))
        self.number_of_proxies.setText(_translate("Dialog", "0"))
        self.total_emails_scrapped.setText(_translate("Dialog", "0"))
        self.label_9.setText(_translate("Dialog", "Current Niche : "))
        self.Alert.setText(_translate("Dialog", ""))
        self.current_Niche.setText(_translate("Dialog", "?"))
        self.copyBtn.setText(_translate("Dialog", "COPY"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
