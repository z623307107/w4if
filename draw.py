# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Draw(object):
    def setupUi(self, Draw):
        Draw.setObjectName("Draw")
        Draw.resize(800, 600)
        Draw.setMinimumSize(QtCore.QSize(800, 600))
        Draw.setMaximumSize(QtCore.QSize(800, 600))
        self.pushButton = QtWidgets.QPushButton(Draw)
        self.pushButton.setGeometry(QtCore.QRect(710, 14, 75, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Draw)
        self.label.setGeometry(QtCore.QRect(620, 20, 71, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Draw)
        self.pushButton_2.setGeometry(QtCore.QRect(707, 60, 75, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Draw)
        self.label_2.setGeometry(QtCore.QRect(620, 66, 71, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Draw)
        self.pushButton_3.setGeometry(QtCore.QRect(707, 110, 75, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Draw)
        self.label_3.setGeometry(QtCore.QRect(620, 110, 71, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalSlider = QtWidgets.QSlider(Draw)
        self.horizontalSlider.setGeometry(QtCore.QRect(620, 240, 160, 21))
        self.horizontalSlider.setMaximum(360)
        self.horizontalSlider.setProperty("value", 135)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.spinBox_2 = QtWidgets.QSpinBox(Draw)
        self.spinBox_2.setGeometry(QtCore.QRect(710, 160, 71, 31))
        self.spinBox_2.setMaximum(9999)
        self.spinBox_2.setProperty("value", 9)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_5 = QtWidgets.QLabel(Draw)
        self.label_5.setGeometry(QtCore.QRect(620, 160, 71, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Draw)
        self.lineEdit.setGeometry(QtCore.QRect(710, 270, 71, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(Draw)
        self.checkBox.setGeometry(QtCore.QRect(620, 350, 79, 31))
        self.checkBox.setObjectName("checkBox")
        self.horizontalSlider_2 = QtWidgets.QSlider(Draw)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(620, 320, 160, 21))
        self.horizontalSlider_2.setMaximum(360)
        self.horizontalSlider_2.setProperty("value", 0)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Draw)
        self.lineEdit_2.setGeometry(QtCore.QRect(710, 350, 71, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(Draw)
        self.label_7.setGeometry(QtCore.QRect(620, 270, 71, 31))
        self.label_7.setObjectName("label_7")
        self.spinBox_4 = QtWidgets.QSpinBox(Draw)
        self.spinBox_4.setGeometry(QtCore.QRect(710, 200, 71, 31))
        self.spinBox_4.setMaximum(9999)
        self.spinBox_4.setProperty("value", 9)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_8 = QtWidgets.QLabel(Draw)
        self.label_8.setGeometry(QtCore.QRect(620, 200, 71, 31))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Draw)
        QtCore.QMetaObject.connectSlotsByName(Draw)

    def retranslateUi(self, Draw):
        _translate = QtCore.QCoreApplication.translate
        Draw.setWindowTitle(_translate("Draw", "Draw"))
        self.pushButton.setText(_translate("Draw", "color1"))
        self.pushButton_2.setText(_translate("Draw", "color2"))
        self.pushButton_3.setText(_translate("Draw", "bgcolor"))
        self.label_5.setText(_translate("Draw", "width"))
        self.lineEdit.setText(_translate("Draw", "135"))
        self.checkBox.setText(_translate("Draw", "shake"))
        self.lineEdit_2.setText(_translate("Draw", "0"))
        self.label_7.setText(_translate("Draw", "angle"))
        self.label_8.setText(_translate("Draw", "size"))
