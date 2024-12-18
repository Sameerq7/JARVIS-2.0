from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QProcess
import sys
import os
import time

def print_slow(text, delay=0.1):
    output = ''
    for char in text:
        output += char
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    return output  # Return the accumulated string


# Add the 'features' directory to the system path
sys.path.append(r'C:\Users\hp\Desktop\JARVIS2.0\features')


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
        self.label.setMovie(self.movie)  # Set the QMovie to the label
        self.label.setScaledContents(True)
        self.movie.start()  # Start the GIF animation
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1180, 790, 101, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1310, 790, 101, 51))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 0, 0);\n"
                                        "font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")

        # For the second label with the initiating GIF
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 401, 91))
        self.label_2.setText("")
        self.movie2 = QtGui.QMovie("features/images/initiating.gif")
        self.label_2.setMovie(self.movie2)  # Set the QMovie to the label
        self.movie2.start()  # Start the GIF animation
        self.label_2.setObjectName("label_2")

        # For the new GIF at the bottom-left corner
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 550, 500, 350))  
        # Position at bottom-left corner
        self.label_3.setText("")
        self.movie3 = QtGui.QMovie("GIF/jarvisui2.gif")
        self.label_3.setMovie(self.movie3)  # Set the QMovie to the label
        self.movie3.start()  # Start the GIF animation
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

        # Create a QProcess to manage the myAI.py script
        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyRead.connect(self.dataReady)

        # Connect the buttons to start and stop the process
        self.pushButton.clicked.connect(self.startJarvis)
        self.pushButton_2.clicked.connect(self.stopJarvis)

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

    def startJarvis(self):
        # Use the virtual environment's Python interpreter
        self.process.start("C:/Users/hp/Desktop/JARVIS2.0/.venv/Scripts/python.exe", ["myAI.py"])

    def stopJarvis(self):
        # Kill the process to stop Jarvis
        self.process.terminate()

    def dataReady(self):
        output = self.process.readAll().data().decode()
        print("Output received:", repr(output))  # Log the raw output

        if output:
            if len(output) == 1:  # Single character received
                self.buffer += output  # Accumulate character
                print("Accumulated buffer:", repr(self.buffer))  # Log buffer state
                if ' ' in self.buffer or '\n' in self.buffer:  # Finalize word on space/newline
                    self.textBrowser_3.append(self.buffer.strip())  # Append word to GUI
                    print("Appended word:", repr(self.buffer.strip()))  # Log appended word
                    self.buffer = ''  # Clear buffer after appending
            else:
                # Handle cases where the output is a full word/sentence
                self.textBrowser_3.append(output.strip())
                print("Directly appended:", repr(output.strip()))  # Log direct output
        else:
            print("No output received.")  # Log when no output is received


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
