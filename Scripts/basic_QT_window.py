#!/usr/bin/env python3

import sys
import pyautogui

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui, QtCore

screen_width, screen_height = pyautogui.size()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width = 600
        self.height = 400
        self.title = "My App"
        self.left = int((screen_width / 2) - (self.width / 2))
        self.top = int((screen_height / 2) - (self.height / 2))
        self.label = QLabel("Hello World!")
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: white;")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
