# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Script\intersection_union\intersection.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_intersection_Dialog(object):
    def setupUi(self, intersection_Dialog):
        intersection_Dialog.setObjectName("intersection_Dialog")
        intersection_Dialog.resize(627, 445)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(intersection_Dialog.sizePolicy().hasHeightForWidth())
        intersection_Dialog.setSizePolicy(sizePolicy)
        intersection_Dialog.setToolTipDuration(-1)
        intersection_Dialog.setStyleSheet("font: 11pt \"黑体\";")
        intersection_Dialog.setSizeGripEnabled(True)
        self.File1_lineEdit = QtWidgets.QLineEdit(intersection_Dialog)
        self.File1_lineEdit.setGeometry(QtCore.QRect(170, 60, 251, 31))
        self.File1_lineEdit.setObjectName("File1_lineEdit")
        self.File1_label = QtWidgets.QLabel(intersection_Dialog)
        self.File1_label.setGeometry(QtCore.QRect(80, 70, 72, 15))
        self.File1_label.setStyleSheet("font: 11pt \"黑体\";")
        self.File1_label.setObjectName("File1_label")
        self.File1_toolButton = QtWidgets.QToolButton(intersection_Dialog)
        self.File1_toolButton.setGeometry(QtCore.QRect(440, 60, 51, 31))
        self.File1_toolButton.setObjectName("File1_toolButton")
        self.File2_label = QtWidgets.QLabel(intersection_Dialog)
        self.File2_label.setGeometry(QtCore.QRect(80, 130, 72, 15))
        self.File2_label.setStyleSheet("font: 11pt \"黑体\";")
        self.File2_label.setObjectName("File2_label")
        self.File2_toolButton = QtWidgets.QToolButton(intersection_Dialog)
        self.File2_toolButton.setGeometry(QtCore.QRect(440, 120, 51, 31))
        self.File2_toolButton.setObjectName("File2_toolButton")
        self.File2_lineEdit = QtWidgets.QLineEdit(intersection_Dialog)
        self.File2_lineEdit.setGeometry(QtCore.QRect(170, 120, 251, 31))
        self.File2_lineEdit.setObjectName("File2_lineEdit")
        self.File1_col_label = QtWidgets.QLabel(intersection_Dialog)
        self.File1_col_label.setGeometry(QtCore.QRect(80, 200, 72, 15))
        self.File1_col_label.setStyleSheet("font: 11pt \"黑体\";")
        self.File1_col_label.setObjectName("File1_col_label")
        self.File1_spinBox = QtWidgets.QSpinBox(intersection_Dialog)
        self.File1_spinBox.setGeometry(QtCore.QRect(170, 190, 81, 31))
        self.File1_spinBox.setObjectName("File1_spinBox")
        self.File1_spinBox.setRange(1,999)
        self.File2_col_label = QtWidgets.QLabel(intersection_Dialog)
        self.File2_col_label.setGeometry(QtCore.QRect(330, 200, 72, 15))
        self.File2_col_label.setStyleSheet("font: 11pt \"黑体\";")
        self.File2_col_label.setObjectName("File2_col_label")
        self.File2_spinBox = QtWidgets.QSpinBox(intersection_Dialog)
        self.File2_spinBox.setGeometry(QtCore.QRect(410, 190, 81, 31))
        self.File2_spinBox.setObjectName("File2_spinBox")
        self.File2_spinBox.setRange(1, 999)
        self.pushButton = QtWidgets.QPushButton(intersection_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 370, 93, 28))
        self.pushButton.setStyleSheet("font: 11pt \"黑体\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(intersection_Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 370, 93, 28))
        self.pushButton_2.setStyleSheet("font: 11pt \"黑体\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(intersection_Dialog)
        self.groupBox.setGeometry(QtCore.QRect(70, 260, 461, 80))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 471, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)

        self.retranslateUi(intersection_Dialog)
        QtCore.QMetaObject.connectSlotsByName(intersection_Dialog)

    def retranslateUi(self, intersection_Dialog):
        _translate = QtCore.QCoreApplication.translate
        intersection_Dialog.setWindowTitle(_translate("intersection_Dialog", "交集"))
        self.File1_label.setText(_translate("intersection_Dialog", "文件1："))
        self.File1_toolButton.setText(_translate("intersection_Dialog", "..."))
        self.File2_label.setText(_translate("intersection_Dialog", "文件2："))
        self.File2_toolButton.setText(_translate("intersection_Dialog", "..."))
        self.File1_col_label.setText(_translate("intersection_Dialog", "列1："))
        self.File2_col_label.setText(_translate("intersection_Dialog", "列2："))
        self.pushButton.setText(_translate("intersection_Dialog", "确定"))
        self.pushButton_2.setText(_translate("intersection_Dialog", "取消"))
        self.groupBox.setTitle(_translate("intersection_Dialog", "输出"))
        self.radioButton_2.setText(_translate("intersection_Dialog", "文件1"))
        self.radioButton_3.setText(_translate("intersection_Dialog", "文件2"))
        self.radioButton.setText(_translate("intersection_Dialog", "所有文件"))

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '提示',
                                     "是否退出?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    intersection_Dialog = QtWidgets.QDialog()
    ui = Ui_intersection_Dialog()
    ui.setupUi(intersection_Dialog)
    intersection_Dialog.show()
    sys.exit(app.exec_())
