# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    #######################################################
    ##            CODIGO ADICIONADO POR MIM              ##
    #######################################################

    firstOperand = 0
    operation = 0
    mustClearText = False

    def insert_number(self, number):
        if self.mustClearText:
             self.textBrowser.setText(str(number))
             self.mustClearText = False
        else:
            self.textBrowser.setText(self.textBrowser.toPlainText() + str(number))

    def set_operand(self, operation):
        if self.operation != 0:
            return
        self.operation = operation
        if self.textBrowser.toPlainText() == '':
            self.firstOperand = 0
        else:
            self.firstOperand = int(self.textBrowser.toPlainText())
        self.mustClearText = True

    def calc(self):
        if self.textBrowser.toPlainText() == '':
            secondOperand = 0
        else:
            secondOperand = int(self.textBrowser.toPlainText())

        if self.operation == 1:
            self.textBrowser.setText(str(self.firstOperand + secondOperand))
        elif self.operation == 2:
            self.textBrowser.setText(str(self.firstOperand - secondOperand))
        elif self.operation == 3:
            self.textBrowser.setText(str(self.firstOperand * secondOperand))
        elif self.operation == 4:
            self.textBrowser.setText(str(self.firstOperand / secondOperand))

        self.operation = 0
        if self.textBrowser.toPlainText() == '':
            self.firstOperand = 0
        else:
            self.firstOperand = int(self.textBrowser.toPlainText())
        self.mustClearText = True
    #######################################################
    ##          FIM DO CODIGO ADICIONADO POR MIM         ##
    #######################################################

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(167, 275)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(166)
        sizePolicy.setVerticalStretch(26)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(167, 275))
        Dialog.setMaximumSize(QtCore.QSize(167, 275))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 146, 258))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(144, 20))
        self.textBrowser.setMaximumSize(QtCore.QSize(144, 25))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_11.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_11.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_12.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_7.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_16.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_16.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_14.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_14.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_9.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_10.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 3, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_15.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_15.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout.addWidget(self.pushButton_15)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_13.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_13.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        #######################################################
        ##            CODIGO ADICIONADO POR MIM              ##
        #######################################################

        self.pushButton_12.clicked.connect(lambda: self.insert_number(3))
        self.pushButton_16.clicked.connect(lambda: self.insert_number(2))
        self.pushButton_14.clicked.connect(lambda: self.insert_number(1))
        self.pushButton_7.clicked.connect(lambda: self.insert_number(6))
        self.pushButton_8.clicked.connect(lambda: self.insert_number(5))
        self.pushButton_5.clicked.connect(lambda: self.insert_number(4))
        self.pushButton.clicked.connect(lambda: self.insert_number(9))
        self.pushButton_2.clicked.connect(lambda: self.insert_number(8))
        self.pushButton_3.clicked.connect(lambda: self.insert_number(7))
        self.pushButton_11.clicked.connect(lambda: self.insert_number(0))

        self.pushButton_6.clicked.connect(lambda: self.set_operand(1))
        self.pushButton_15.clicked.connect(lambda: self.set_operand(2))
        self.pushButton_13.clicked.connect(lambda: self.set_operand(3))
        self.pushButton_4.clicked.connect(lambda: self.set_operand(4))

        self.pushButton_10.clicked.connect(self.calc)

        self.pushButton_9.clicked.connect(lambda: self.textBrowser.setText(''))

        #######################################################
        ##          FIM DO CODIGO ADICIONADO POR MIM         ##
        #######################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculadora"))
        self.pushButton_5.setText(_translate("Dialog", "4"))
        self.pushButton_11.setText(_translate("Dialog", "0"))
        self.pushButton.setText(_translate("Dialog", "9"))
        self.pushButton_12.setText(_translate("Dialog", "3"))
        self.pushButton_7.setText(_translate("Dialog", "6"))
        self.pushButton_16.setText(_translate("Dialog", "2"))
        self.pushButton_8.setText(_translate("Dialog", "5"))
        self.pushButton_14.setText(_translate("Dialog", "1"))
        self.pushButton_9.setText(_translate("Dialog", "C"))
        self.pushButton_2.setText(_translate("Dialog", "8"))
        self.pushButton_10.setText(_translate("Dialog", "="))
        self.pushButton_3.setText(_translate("Dialog", "7"))
        self.pushButton_6.setText(_translate("Dialog", "+"))
        self.pushButton_15.setText(_translate("Dialog", "-"))
        self.pushButton_13.setText(_translate("Dialog", "*"))
        self.pushButton_4.setText(_translate("Dialog", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowTitleHint)
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

