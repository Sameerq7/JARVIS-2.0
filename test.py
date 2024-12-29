from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QProcess
import sys
import os
import time
import signal
import psutil



class Ui_MainWindow(object):
    def __init__(self):
        self.buffer = ''  # Buffer to accumulate characters until a space or newline is encountered

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # For the first label with the live wallpaper
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1440, 900))
        self.label.setText("")
        self.movie = QtGui.QMovie("features/images/live_wallpaper.gif")
        self.label.setMovie(self.movie)
        self.label.setScaledContents(True)
        self.movie.start()
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1180, 790, 101, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        # Add the Pause button
        self.pushButton_pause = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pause.setGeometry(QtCore.QRect(1060, 790, 101, 51))  # Positioned beside the Run button
        self.pushButton_pause.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                            "font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton_pause.setObjectName("pushButton_pause")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1310, 790, 101, 51))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 0, 0);\n"
                                        "font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 401, 91))
        self.label_2.setText("")
        self.movie2 = QtGui.QMovie("features/images/initiating.gif")
        self.label_2.setMovie(self.movie2)
        self.movie2.start()
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 550, 500, 350))
        self.label_3.setText("")
        self.movie3 = QtGui.QMovie("GIF/jarvisui2.gif")
        self.label_3.setMovie(self.movie3)
        self.movie3.start()
        self.label_3.setObjectName("label_3")
        self.label_3.setScaledContents(True)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(640, 30, 291, 61))
        self.textBrowser.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                       "background-color:transparent;\n"
                                       "border-radius:none;\n"
                                       "")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(930, 30, 291, 61))
        self.textBrowser_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                         "background-color:transparent;\n"
                                         "border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(1000, 100, 431, 441))
        self.textBrowser_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
                                         "background-color:white; color:black;")
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyRead.connect(self.dataReady)

        self.pushButton.clicked.connect(self.startJarvis)
        self.pushButton_2.clicked.connect(self.stopJarvis)
        self.pushButton_pause.clicked.connect(self.pauseJarvis)

        # Set up the QMediaPlayer for background music
        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(r"media/KGF_BGMI.wav")))
        self.mediaPlayer.setVolume(50)  # Set the volume (0-100)
        self.mediaPlayer.play()  # Start playing

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.pushButton_pause.setText(_translate("MainWindow", "Pause"))

    def startJarvis(self):
        self.process.start(".venv/Scripts/python.exe", ["myAI.py"])

    def stopJarvis(self):
        self.process.terminate()


    def pauseJarvis(self):
        try:
            pid = self.process.pid()  # Get the process ID of the running process
            if pid:
                pid_int = int(pid)  # Convert the pid to an integer if necessary
                p = psutil.Process(pid_int)
                p.suspend()  # Suspend the process
                self.textBrowser_3.append("Jarvis process paused.")
            else:
                self.textBrowser_3.append("No process found to pause.")
        except Exception as e:
             self.textBrowser_3.append(f"Error while pausing: {e}")  


    def dataReady(self):
        output = self.process.readAll().data().decode()
        # if output:
        #     if len(output) == 1:
        #         self.buffer += output
        #         if ' ' in self.buffer or '\n' in self.buffer:
        #             self.textBrowser_3.append(self.buffer.strip())
        #             self.buffer = ''
        #     else:
        self.textBrowser_3.append(output.strip())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
