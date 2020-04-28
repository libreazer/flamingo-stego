import os
import sys
import subprocess
import PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QColor, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QSpinBox
from PyQt5.QtWidgets import QPushButton, QRadioButton, QAction, QLineEdit, QMessageBox, QLabel


class Root(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setFixedSize(600, 800)
        self.title = "Stego Tool"
        self.top = 400
        self.left = 100
        self.width = 400
        self.height = 600

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('About')

        aboutButton = QAction('Details',self)
        aboutButton.setShortcut('Ctrl+i')
        aboutButton.setStatusTip('Application Information')
        aboutButton.triggered.connect(self.About)
        fileMenu.addAction(aboutButton)

        self.InitWindow()

    def InitWindow(self):

        self.setWindowIcon(QtGui.QIcon("flamingo.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.image1 = QLabel(self)
        self.image1.setPixmap(QtGui.QPixmap("flamingo.png"))
        self.image1.resize(100, 100)
        self.image1.move(50, 50)
        self.image1.show()

        self.image2 = QLabel(self)
        self.image2.setPixmap(QtGui.QPixmap("hide.png"))
        self.image2.resize(100, 100)
        self.image2.move(420, 220)
        self.image2.show()

        self.image3 = QLabel(self)
        self.image3.setPixmap(QtGui.QPixmap("file.png"))
        self.image3.resize(100, 100)
        self.image3.move(120, 210)
        self.image3.show()

        self.button1 = QPushButton('Cover File', self)
        self.button1.clicked.connect(self.Cover)
        self.button1.move(100, 310)
        self.button1.resize(100, 40)

        self.button2 = QPushButton('File to embed', self)
        self.button2.clicked.connect(self.Embed)
        self.button2.move(400, 310)
        self.button2.resize(100, 40)

        self.button3 = QPushButton('Launch', self)
        self.button3.clicked.connect(lambda:self.Launch(self.radio1.isChecked()))
        self.button3.move(250, 635)
        self.button3.resize(100, 40)

        self.radio1 = QRadioButton('None', self)
        self.radio1.setChecked(True)
        self.radio1.move(100, 480)
        self.radio1.resize(80, 20)

        self.radio2 = QRadioButton('AES', self)
        self.radio2.move(100, 505)
        self.radio2.resize(80, 20)

        self.radio3 = QRadioButton('DES', self)
        self.radio3.move(100, 530)
        self.radio3.resize(80, 20)

        self.radio4 = QRadioButton('Blowfish', self)
        self.radio4.move(100, 555)
        self.radio4.resize(80, 20)

        self.spinbox = QSpinBox(self)
        self.spinbox.move(390, 500)
        self.spinbox.resize(100, 50)
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(9)
        self.spinbox.valueChanged.connect(self.Compression)
        self.spinbox.show()


           
        self.font = QFont("SansSerif")
        self.font.setBold(True)

        self.label1 = QLabel(self)
        self.label1.setFont(self.font)
        self.label1.setText("User-friendly Steganography Tool")
        self.label1.move(220, 90)
        self.label1.resize(400, 20)

        self.label2 = QLabel(self)
        self.label2.setFont(self.font)
        self.label2.setText("Type of Encryption")
        self.label2.move(80, 450)
        self.label2.resize(140, 20)

        self.label3 = QLabel(self)
        self.label3.setFont(self.font)
        self.label3.setText("Quality of Compression")
        self.label3.move(370, 450)
        self.label3.resize(180, 20)

        self.label4 = QLabel(self)
        self.label4.setText("Version: 1.0")
        self.label4.move(50, 780)
        self.label4.resize(180, 20)

        self.label5 = QLabel(self)
        self.label5.setText("License: GPL 3.0")
        self.label5.move(430, 780)
        self.label5.resize(180, 20)

        self.label6 = QLabel(self)
        self.label6.setStyleSheet("color: red; ")
        self.label6.setText("")
        self.label6.move(175, 700)
        self.label6.resize(260, 20)

        self.label7 = QLabel(self)
        self.label7.setStyleSheet("color: green; ")
        self.label7.setText("")
        self.label7.move(195, 700)
        self.label7.resize(260, 20)

        self.show()

    def Cover(self):
        self.file1 = QFileDialog.getOpenFileName(self, "Select a File", "/home/", "Files (*.jpg *.jpeg *.au *.bmp *.wav)")[0]
        self.button1.setText(os.path.basename(self.file1))
        if self.button1.text() == '':
            self.label6.setText("Cover or Embed File has not been selected.")
            self.button1.setText("Cover File")
        try:
            if self.file1 and self.file2 != '':
                self.label6.setText("")
                self.label7.setText("Your file is ready to be concealed.")
            else:
                self.label7.setText("")
        except AttributeError:
                self.label6.setText("Cover or Embed File has not been selected.")


    def Embed(self):
        self.file2 = QFileDialog.getOpenFileName(self, "Select a File", "/home/", "All Files (*.*)")[0]
        self.button2.setText(os.path.basename(self.file2))
        if self.button2.text() == '':
            self.button2.setText("File to Embed")
            self.label6.setText("Cover or Embed File has not been selected.")
        try:
            if self.file1 and self.file2 != '':
                self.label6.setText("")
                self.label7.setText("Your file is ready to be concealed.")
            else:
                self.label7.setText("")
        except AttributeError:
                self.label6.setText("Cover or Embed File has not been selected.")

    def Compression(self):
        print(str(self.spinbox.value()))

    def Launch(self, check):
        if self.radio1.isChecked():
            try:
                if self.file1 and self.file2 != '':
                    subprocess.call(['bash', 'launch.sh', '-cf', self.file1, '-ef', self.file2, 'none', str(self.spinbox.value())])
                    self.label7.setText("Your file is ready to be concealed.")
                else:
                    self.label6.setText("Cover or Embed File has not been selected.")
            except AttributeError:
                self.label6.setText("Cover or Embed File has not been selected.")
        if self.radio2.isChecked():
            try:
                if self.file1 and self.file2 != '':
                    subprocess.call(['bash', 'launch.sh', '-cf', self.file1, '-ef', self.file2, 'rijndael-128', str(self.spinbox.value())])
                    self.label7.setText("Your file is ready to be concealed.")
                else:
                    self.label6.setText("Cover or Embed File has not been selected.")
            except AttributeError:
                self.label6.setText("Cover or Embed File has not been selected.")
        if self.radio3.isChecked():
            try:
                if self.file1 and self.file2 != '':
                    subprocess.call(['bash', 'launch.sh', '-cf', self.file1, '-ef', self.file2, 'des', str(self.spinbox.value())])
                    self.label7.setText("Your file is ready to be concealed.")
                else:
                    self.label6.setText("Cover or Embed File has not been selected.")
            except AttributeError:
                self.label6.setText("Cover or Embed File has not been selected.")
        if self.radio4.isChecked():
            try:
                if self.file1 and self.file2 != '':
                    subprocess.call(['bash', 'launch.sh', '-cf', self.file1, '-ef', self.file2, 'blowfish', str(self.spinbox.value())])
                    self.label7.setText("Your file is ready to be concealed.")
                else:
                    self.label6.setText("Cover or Embed File has not been selected.")
            except AttributeError:
                self.label6.setText("Cover or Embed File has not been selected.")

        self.answer = subprocess.call(['bash', 'out.sh'])
        if self.answer == 0:
            self.msg = QMessageBox()
            self.top3 = 600
            self.left3 = 200
            self.width3 = 400
            self.height3 = 600
            self.msg.setGeometry(self.top3, self.left3, self.width3, self.height3)
            self.msg.setText("Your file has been concealed     ")
            self.msg.show()
        else:
            self.msg = QMessageBox()
            self.top3 = 600
            self.left3 = 200
            self.width3 = 400
            self.height3 = 600
            self.msg.setGeometry(self.top3, self.left3, self.width3, self.height3)
            self.msg.setText("Something went Wrong      ")
            self.msg.show()

    def About(self):
        self.info = QMessageBox()
        self.top2 = 600
        self.left2 = 200
        self.width2 = 400
        self.height2 = 600
        self.info.setGeometry(self.top2, self.left2, self.width2, self.height2)
        self.info.setWindowTitle("Information")
        self.info.setText("\nThis tool is a free/open-source software \
that helps the user to hide a file inside another file in a user-friendly way. \
\n\n Version: 1.0 \n\n License: GPL v3.0")
        self.info.show()

App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())