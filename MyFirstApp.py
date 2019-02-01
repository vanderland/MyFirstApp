#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    MyFirst app
"""
from PySide2 import QtCore, QtWidgets
from Idea01 import main
from Idea01 import about

import sqlite3


__author__ = "Van Der Fran"
__copyright__ = "Copyright 2019, VanDerLand Inc."
__credits__ = ["Van Der Fran"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Van Der Fran"
__email__ = "dev@vanderland.com"
__status__ = "Development"  # Production




class MyFirstApp(main.Ui_Main, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyFirstApp, self).__init__()
        self.setupUi(self)

        self.w_about = QtWidgets.QMainWindow()
        self.u_about = about.Ui_About()

        self.btnAdd.clicked.connect(self.me_add)
        self.btnClear.clicked.connect(self.me_clear)
        self.actAbout .triggered.connect(self.me_about)
        self.actExit.triggered.connect(self.me_close)
        self.actOpen.triggered.connect(self.me_open)
        self.lswMain.setAlternatingRowColors(True)
        self.lswMain.currentTextChanged()


        QtCore.QObject.connect(self.lswMain, QtCore.SIGNAL("itemSelectionChanged()"), self.btnClear.hide)

        db = sqlite3.connect('mydb')
        cursor = db.cursor()
        cursor.execute('''SELECT name, email, phone FROM users''')

        all_rows = cursor.fetchall()
        for row in all_rows:
            item = row[1]
            self.lswMain.addItem(item)




    def me_add(self):
        # item = QtWidgets.QListWidgetItem()
        item = self.ledLogin.text() + ' ' + self.ledPassword.text()
        self.lswMain.addItem(item)
        self.ledLogin.clear()
        self.ledPassword.clear()

    def me_clear(self):
        self.lswMain.clear()
        self.ledLogin.clear()


    def me_about(self):
        self.u_about.setupUi(self.w_about)
        self.w_about.show()

    def me_open(self):
        # TODO Open a file
        sys.exit()

    def me_close(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MyFirstApp()
    ui.show()
    sys.exit(app.exec_())

