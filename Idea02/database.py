#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description
"""

import sys
from PySide2.QtSql import *
from PySide2.QtWidgets import QApplication




__author__ = "Van Der Fran"
__copyright__ = "Copyright 2019, VanDerLand Inc."
__credits__ = ["Van Der Fran"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Van Der Fran"
__email__ = "dev@vanderland.com"
__status__ = "Development"  # Production

class DBAOPS():
    def __init__(self):
        super(DBAOPS, self).__init__()

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("Idea02/Idea02.dat")
    # self.db.setDatabaseName(":memory:")
    db.open()

    if db.open():
        print('open')

        query = QSqlQuery()

        query.exec_("SELECT sqlite_version()")
        query.next()
        print(query.value(0))

        query.exec_("""CREATE TABLE box(
                            id      INT PRIMARY KEY,
                            name    VARCHAR(30),
                            color   VARCHAR(30),
                            size    INT
                            )""")
        query.exec_("INSERT INTO box VALUES (1,'Bela', 'blue', 1)")
        query.prepare("INSERT INTO box (id, name, color, size) VALUES (:id, :name, :color, :size)")
        query.bindValue(":id", 2)
        query.bindValue(":name", 'upper')
        query.bindValue(":color", 'red')
        query.bindValue(":size", 4)
        query.exec_()

        query.exec_("SELECT * FROM box")
        query.next()
        print(query.value(1))
        query.next()
        print(query.value(1))

        while query.next():
            print(query.value(1))

        query.clear()
    else:
        print('nope')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.exit(app.exec_())


# query.exec_("""CREATE TABLE box(
#                     id      INT PRIMARY KEY,
#                     name    VARCHAR(30),
#                     color   VARCHAR(30),
#                     size    int
#
#                 )""")
# query.exec_("INSERT INTO box VALUES (1,'Bela', 'blue', 1)")
# query.prepare("INSERT INTO box (id, name, color, size) VALUES (:id, :name, :color, :size)")
# query.bindValue(":id", 2)
# query.bindValue(":name", 'upper')
# query.bindValue(":color", 'red')
# query.bindValue(":size", 4)
# query.exec_()
#

# query = QSqlQuery()
# query.prepare("EXEC [dot].[Servers_GetAll]")
# query.exec_()




