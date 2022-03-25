# Chicken Burger browser
# PL: Python
# Packages: PyQt5 and PyQtWebEngine
# https://www.github.com/DevCurly/Chicken-Burger-brws


import sys

from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *

import time

print("Welcome to Chicken Burger browser!")

Home =  str(input("Home page (Example: url.com): "))

print("""
The browser automatically completes links like
    asd.com = https://www.asd.com
To dont use this do this:
    nh:///asd.com = asd.com
To open a file do this:
    file:///exampledir = file:///exampledir
""")

Final = Home

if Home.find("https://") == 0:

    Final = Home

else:

    Final = "https://"+Home

ver = ""

class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        # browser main
        self.browser = QWebEngineView()

        self.browser.setUrl(QUrl(Final))

        self.setCentralWidget(self.browser)

        self.showMaximized()

        navbar = QToolBar()

        self.url_bar = QLineEdit()

        self.url_bar.returnPressed.connect(self.navigate_to_url)

        navbar.addWidget(self.url_bar)

        # navbar

        self.addToolBar(navbar)

        # Back button

        back_btn = QAction("🡸", self)

        back_btn.triggered.connect(self.browser.back)

        navbar.addAction(back_btn)

        # Forward button

        forward_btn = QAction("🡺",self)

        forward_btn.triggered.connect(self.browser.forward)

        navbar.addAction(forward_btn)

        # Version  button

        ver=""

        ver = QAction("A1.1.01",self)

        ver.triggered.connect(self.ripv)

        navbar.addAction(ver)

        # Reload page button

        reload_btn = QAction("⭮", self)

        reload_btn.triggered.connect(self.browser.reload)

        navbar.addAction(reload_btn)

        # Auto fill background btn (not used)

        #   dh = QAction("delete",self)
        #   dh.triggered.connect(self.browser.autoFillBackground)
        #   navbar.addAction(dh)

        # Home button

        home_btn = QAction("⌂", self)

        home_btn.triggered.connect(self.navigate_home)

        navbar.addAction(home_btn)

        # Update URL
        
        self.browser.urlChanged.connect(self.update_url)

    # self.functions

    # Do nothing lol
    def ripv(self):

        self.ver =QAction("A1.1.01")

    # Go to home

    def navigate_home(self):

        self.browser.setUrl(QUrl(Final))

    # Go to URL

    def navigate_to_url(self):

        url = self.url_bar.text()

        __final__ = ""

        # Https

        if url.find("https://") == 0:

            __final__ = url

        else:

            __final__ = "https://"+url

        # Files  (to open a file you need put file:/// at the start to work)

        if url.find("file:///") == 0:

            __final__ = url

        # no https

        if url.find("nh:///") == 0:

            __final__ = url.replace("nh:///","")

        self.browser.setUrl(QUrl(__final__))

    # Update URL func

    def update_url(self, q):

        self.url_bar.setText(q.toString())






# App set-up

app = QApplication(sys.argv)

QApplication.setApplicationName("Chicken Burger")

window = MainWindow()

app.exec_()

print("Made by DevCurly")

print("https://www.github.com/DevCurly/Chicken-Burger-brws")

print("---------------------------------------------------------------------------------")
