# Chicken Burger browser
# PL: Python
# Packages: PyQt5 and PyQtWebEngine
# Author: DevCurly
# https://www.github.com/DevCurly/Chicken-Burger-brws





import os
import sys
os.system("pip install PyQt5")
from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *

import time


print("Welcome to Chicken Burger browser!")


#Settings

std = [
    
    "duckduckgo.com", # home page (0)
    # You can add more settings here
    # Example:
    "Dark mode", # Change to dark mode (1)
]

# Home Page



Home = std[0] or str(input("Enter your homepage: "))

for settin in std:
    print(settin)



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

        ver = QAction("A2",self)

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

        # Extensions button

        # new Tab button
        newTab = QAction("New Tab",self)
        
        newTab.triggered.connect(self.newTab)
        
        navbar.addAction(newTab)

        # Home button

        home_btn = QAction("⌂", self)

        home_btn.triggered.connect(self.navigate_home)

        navbar.addAction(home_btn)

        # Update URL
        
        self.browser.urlChanged.connect(self.update_url)


        # Dark mode
        if std[1] == "Dark mode":
            self.browser.setStyleSheet("background-color: black; color: white;")
            self.browser.setAutoFillBackground(True)
            print(self.browser.styleSheet())
            navbar.setStyleSheet("background-color: black; color: white;")
            
        self.navbar= navbar
            
    # self.functions
    # ripv
    # navigate_home
    # navigate_to_url
    # update_url

        

    def ripv(self): 
        print("A2")

    
    #new tab
    def newTab(self):
        
       
        newTab = MainWindow()
        
        newTab.__init__()
        
        
        
        newTab.browser.setUrl(QUrl(self.url_bar.text()))
        
        # Fix url bar
        
        
        newTab.url_bar.returnPressed.connect(newTab.navigate_to_url)
        
        #Set Tab 
        newTab.browser.setTabOrder(newTab,self.browser)
        
        # Set theme
        newTab.browser.setStyleSheet(self.browser.styleSheet())
        newTab.browser.setAutoFillBackground(self.browser.autoFillBackground())
        newTab.navbar.setStyleSheet(self.navbar.styleSheet())
        
        
        
        # Beta Warning
        print("Beta Warning: This is a beta feature, it can have bugs, if you find a bug report it please")
        os.system("echo beta warning: this is a beta feature, it can have bugs, if you find a bug report it please")
        
        
        
    
    # Go to home

    def navigate_home(self):

        self.browser.setUrl(QUrl(Final))

    # Go to URL

    def navigate_to_url(self):

        # Set Window title
    

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

QApplication.setApplicationName("Chicken Burger Browser")
QApplication.setApplicationVersion("A2")
QApplication.setOrganizationName("DevCurly")
QApplication.setOrganizationDomain("https://www.github.com/DevCurly/Chicken-Burger-brws")

window = MainWindow()

app.exec_()

print("Made by @DevCurly")

print("https://www.github.com/DevCurly/Chicken-Burger-brws")

print("---------------------------------------------------------------------------------")

