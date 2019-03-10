#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# app = QtWidgets.QApplication(sys.argv)
# win = QtWidgets.QWidget()
# win.resize(320, 240)
# win.setWindowTitle('Hello, World!')
# win.show()
# sys.exit(app.exec_())


app = QtWidgets.QApplication([])
button = QtWidgets.QPushButton('Exit')
button.clicked.connect(app.exit)
button.show()
app.exec_()