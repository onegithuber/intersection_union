# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_intersection import Ui_intersection_Dialog
from Ui_main import Ui_MainWindow
from intersection import intersection_Dialog
from PyQt5.QtGui import QFont 


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_str=self.lineEdit.text()
        self.textBrowser.setText(my_str)
        
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    @pyqtSlot(str)
    def on_centralWidget_windowIconTextChanged(self, iconText):
        """
        Slot documentation goes here.
        
        @param iconText DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_save_file_action_triggered(self):
        """
        保存文件.
        """
        # TODO: not implemented yet
        print(u'保存文件')
        my_file = QtWidgets.QFileDialog.getSaveFileName()
        print(my_file)
        f = open(my_file[0], 'w')
        my_data = self.textBrowser.toPlainText()
        f.write(my_data)
        f.close()
        print(my_data)
    
    @pyqtSlot()
    def on_exit_action_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print(u'退出')
    
    @pyqtSlot()
    def on_author_action_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print(u'作者')
        QtWidgets.QMessageBox.about(self, u'作者', u'dunchen@capitalbiotech.com')
   
    @pyqtSlot()
    def on_copy_action_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print(u'复制')
    
    @pyqtSlot()
    def on_cut_action_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print(u'剪切')

    @pyqtSlot()
    def on_open_file_action_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print(u'打开文件')
        my_file = QtWidgets.QFileDialog.getOpenFileName(self, u'打开文件', '/')
        print(my_file)
        if my_file[0]:
            f = open(my_file[0])
            data = f.read()
            self.textBrowser.setText(data)
            f.close()
            
            
    @pyqtSlot()
    def on_about_action_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print(u'关于')
        QtWidgets.QMessageBox.about(self, u'关于', u'本软件是由博奥晶典生物技术有限公司研发，不收取任何费用！！！')
         
    @pyqtSlot()
    def on_help_action_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print(u'帮助')
    
    @pyqtSlot()
    def on_actionA_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print(u'咩有')
    
    @pyqtSlot()
    def on_paste_action_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print(u'粘贴')



    @pyqtSlot()
    def on_intersection_action_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_intersction = intersection_Dialog()
        QtWidgets.QToolTip.setFont(QFont('SansSerif', 10))
        my_intersction.radioButton_2.setToolTip(u'输出文件一的内容')
        my_intersction.radioButton_3.setToolTip(u'输出文件二的内容')
        my_intersction.radioButton.setToolTip(u'输出两个文件的内容')
        my_intersction.exec_()
    
    
    @pyqtSlot()
    def on_union_action_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
