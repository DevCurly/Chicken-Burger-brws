
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import os
print("Welcome to Chicken Burger browser!")
Home =  str(input("Home page: "))
Final = Home
if Home.find("https://") == 0:
    Final = Home
else:
    Final = "https://"+Home
ver = ""
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
#        self.browser.setUrl(QUrl("/ver.js"))
        self.browser.setUrl(QUrl(Final))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar = QToolBar()
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        # navbar

        self.addToolBar(navbar)

        back_btn = QAction("🡸", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("🡺",self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        ver=""


        ver = QAction("A1.0",self)
        ver.triggered.connect(self.ripv)
        navbar.addAction(ver)

        reload_btn = QAction("⭮", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        # auto fill background btn (not used)
        #   dh = QAction("delete",self)
        #   dh.triggered.connect(self.browser.autoFillBackground)
        #  navbar.addAction(dh)
        home_btn = QAction("⌂", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        self.browser.urlChanged.connect(self.update_url)
    def ripv(self):
        self.ver =""
    def navigate_home(self):
        self.browser.setUrl(QUrl(Final))
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self, q):
        self.url_bar.setText(q.toString())






app = QApplication(sys.argv)
QApplication.setApplicationName("Chicken Burger")

window = MainWindow()
app.exec_()
print("Made by @zDevCurly")
print("---------------------------------------------------------------------------------")
