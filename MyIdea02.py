#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    MyFirst app
"""
#from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtSql import *
from Idea02 import gui

import sqlite3

__author__ = "Van Der Fran"
__copyright__ = "Copyright 2019, VanDerLand Inc."
__credits__ = ["Van Der Fran"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Van Der Fran"
__email__ = "dev@vanderland.com"
__status__ = "Development"  # Production


class MyIdea02App(gui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyIdea02App, self).__init__()
        self.setupUi(self)

        self.pbt_add.clicked.connect(self.me_add)
        self.pbt_delete.clicked.connect(self.me_dell)

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("Idea02/Idea02.dat")
        # self.db.setDatabaseName(":memory:")
        self.db.open()

        if self.db.open():
            print('open1')

            query = QSqlQuery()

            # query.exec_("SELECT sqlite_version()")
            # query.next()
            # print(query.value(0))
            #
            # query.exec_("""CREATE TABLE box(
            #                     ID      INTEGER PRIMARY KEY AUTOINCREMENT,
            #                     name    VARCHAR(30),
            #                     color   VARCHAR(30),
            #                     size    INT
            #                     )""")
            # query.exec_("INSERT INTO box VALUES ('Bela', 'blue', 1)")
            # query.prepare("INSERT INTO box (name, color, size) VALUES (:name, :color, :size)")
            # query.bindValue(":name", 'upper')
            # query.bindValue(":color", 'red')
            # query.bindValue(":size", 4)
            # query.exec_()

            query.exec_("SELECT id, name, color, size FROM box")

            while query.next():
                self.lsw_main.addItem(str(query.value(0)))
        else:
            print('nope')

        query.clear()

    def me_add(self):
        self.db.open()
        if self.db.open():
            print('open2')
            print(self.led_name.text())
            print(self.led_color.text())
            print(self.led_size.text())

            query = QSqlQuery()
            query.prepare("INSERT INTO box (name, color, size) VALUES (:name, :color, :size)")
            query.bindValue(":name", self.led_name.text())
            query.bindValue(":color", self.led_color.text())
            query.bindValue(":size", self.led_size.text())

            query.exec_()

            query.exec_("SELECT id, name, color, size FROM box")

            self.lsw_main.clear()
            while query.next():
                self.lsw_main.addItem(query.value(1))
            else:
                print('nope')
            query.clear()

    def me_dell(self):
        print(str(self.lsw_main.currentItem().text()))

        self.db.open()
        if self.db.open():

            query = QSqlQuery()
            query.prepare("DELETE FROM box WHERE ID = :id")
            query.bindValue(":id", self.lsw_main.currentItem().text())

            query.exec_()

            query.exec_("SELECT * FROM box")

            self.lsw_main.clear()
            while query.next():
                self.lsw_main.addItem(str(query.value(0)))
            else:
                print('nope')
            query.clear()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MyIdea02App()
    ui.show()
    sys.exit(app.exec_())

