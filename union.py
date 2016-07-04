#!/usr/bin/env python
# encoding: utf-8
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog
from Ui_union import Ui_union_Dialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets


def do_union(ffile, sfile, ffilecol, sfilecol):
    try:
        ff = open(ffile,'r')
    except:
        pass


class union_Dialog(QDialog, Ui_union_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(union_Dialog, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_File1_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        my_file = QtWidgets.QFileDialog.getOpenFileName(self, u'打开文件', '/')
        if my_file[0]:
            self.File1_lineEdit.setText(my_file[0])
        else:
            QtWidgets.QMessageBox.warning(self, u'警告', u'请选择输入文件')

    @pyqtSlot()
    def on_File2_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        my_file = QtWidgets.QFileDialog.getOpenFileName(self, u'打开文件', '/')
        if my_file[0]:
            self.File2_lineEdit.setText(my_file[0])
        else:
            QtWidgets.QMessageBox.warning(self, u'警告', u'请选择输入文件')

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        确定
        """
        my_file1 = self.File1_lineEdit.text()
        my_file2 = self.File2_lineEdit.text()
        print(type(self.File2_spinBox.value()))
        if my_file1 == '':
            # QtWidgets.QToolTip.setFont(QFont('SansSerif', 10))
            # self.File1_lineEdit.setToolTip(u'输出两个文件内容')
            QtWidgets.QMessageBox.warning(self, u'警告', u'请选择输入文件')
        elif my_file2 == '':
            # QtWidgets.QToolTip.setFont(QFont('SansSerif', 10))
            # self.File1_lineEdit.setToolTip(u'输出两个文件内容')
            QtWidgets.QMessageBox.warning(self, u'警告', u'请选择输入文件')
        else:
            if self.radioButton.isChecked():
                do_union()
            elif self.radioButton_2.isChecked():
                do_union()
            else:
                do_union()

    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # QtWidgets.QToolTip.setFont(QFont('SansSerif', 10))
        # self.radioButton_2.setToolTip(u'输出文件一的内容')
        print('xxx')

    @pyqtSlot()
    def on_radioButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # QtWidgets.QToolTip.setFont(QFont('SansSerif', 10))
        # self.radioButton_3.setToolTip(u'输出文件二的内容')
        print('xxx')

    @pyqtSlot()
    def on_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # QtWidgets.QToolTip.setFont(QFont('SansSerif', 10))
        # self.radioButton.setToolTip(u'输出两个文件内容')
        print('xxx')

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        退出
        """
        self.close()
