
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_kalkulator(object):
    def setupUi(self, kalkulator):
        kalkulator.setObjectName("kalkr")
        kalkulator.resize(676, 529)
        self.tableView = QtWidgets.QTableView(kalkulator)
        self.tableView.setGeometry(QtCore.QRect(180, 20, 331, 411))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(kalkulator)
        self.pushButton.setGeometry(QtCore.QRect(290, 30, 119, 61))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(kalkulator)
        self.checkBox.setGeometry(QtCore.QRect(320, 120, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(kalkulator)
        self.checkBox_2.setGeometry(QtCore.QRect(320, 160, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi(kalkulator)
        QtCore.QMetaObject.connectSlotsByName(kalkulator)

    def retranslateUi(self, kalkulator):
        _translate = QtCore.QCoreApplication.translate
        kalkulator.setWindowTitle(_translate("kalkulator", "kalkulator"))

        self.pushButton.setText(_translate("kalkulator", "PushButton"))
        self.checkBox.setText(_translate("kalkulator", "CheckBox"))
        self.checkBox_2.setText(_translate("kalkulator", "CheckBox"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kalkulator = QtWidgets.kalkulator()
    ui = kalkulator()
    ui.setupUi(kalkulator)
    kalkulator.show()
    sys.exit(app.exec_())




