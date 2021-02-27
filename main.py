import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))  # set the url for seearch engine
        self.setCentralWidget(self.browser)  # set the central widget
        self.showMaximized()  # to show a maximized window

        navbar = QToolBar()
        self.addToolBar(navbar)
        back = QAction("Back", self)
        back.triggered.connect(self.browser.back)
        navbar.addAction(back)
        forward = QAction("forward", self)
        back.triggered.connect(self.browser.forward)
        navbar.addAction(forward)
        reload = QAction("Reload", self)
        reload.triggered.connect(self.browser.reload)
        navbar.addAction(reload)
        home = QAction("Home", self)
        home.triggered.connect(self.navigate_home)
        navbar.addAction(home)
    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))


app = QApplication(sys.argv)
QApplication.setApplicationName("cyspace")  # name the browser
window = mainwindow()
app.exec_()
