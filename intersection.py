# -*- coding: utf-8 -*-

"""
Module implementing intersection_Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import QtWidgets
from Ui_intersection import Ui_intersection_Dialog
from PyQt5.QtGui import QFont 


'''
处理文件，取交集
'''
def do_intersection():
    pass

class intersection_Dialog(QDialog, Ui_intersection_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(intersection_Dialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_File1_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'打开文件')
        my_file = QtWidgets.QFileDialog.getOpenFileName(self, u'打开文件', '/')
        print(my_file)
        if my_file[0]:
            self.File1_lineEdit.setText(my_file[0])
        else:
            QtWidgets.QMessageBox.warning(self, u'警告',u'请选择输入文件')
    
    @pyqtSlot()
    def on_File2_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'打开文件')
        my_file = QtWidgets.QFileDialog.getOpenFileName(self, u'打开文件', '/')
        print(my_file)
        if my_file[0]:
            self.File2_lineEdit.setText(my_file[0])
        else:
            QtWidgets.QMessageBox.warning(self, u'警告',u'请选择输入文件')
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        确定
        """
        
    
    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        #QtWidgets.QToolTip.setFont(QFont('SansSerif', 10))
        #self.radioButton_2.setToolTip(u'输出文件一的内容')
        print('xxx')
    @pyqtSlot()
    def on_radioButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        #QtWidgets.QToolTip.setFont(QFont('SansSerif', 10))
        #self.radioButton_3.setToolTip(u'输出文件二的内容')
        print('xxx')
    
    @pyqtSlot()
    def on_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        #QtWidgets.QToolTip.setFont(QFont('SansSerif', 10))
        #self.radioButton.setToolTip(u'输出两个文件内容')
        print('xxx')
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        退出
        """
        self.close()
