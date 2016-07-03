# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Script\intersection_union\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 534)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(116, 0))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menuBar/icon/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMouseTracking(False)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setAcceptDrops(True)
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 648, 26))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.menuBar.setFont(font)
        self.menuBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setObjectName("menuBar")
        self.flie_menu = QtWidgets.QMenu(self.menuBar)
        self.flie_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.flie_menu.setObjectName("flie_menu")
        self.tools_menu = QtWidgets.QMenu(self.menuBar)
        self.tools_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tools_menu.setObjectName("tools_menu")
        self.help_menu = QtWidgets.QMenu(self.menuBar)
        self.help_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help_menu.setObjectName("help_menu")
        MainWindow.setMenuBar(self.menuBar)
        self.open_file_action = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menuBar/textprocess.qrc"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_action.setIcon(icon1)
        self.open_file_action.setObjectName("open_file_action")
        self.save_file_action = QtWidgets.QAction(MainWindow)
        self.save_file_action.setObjectName("save_file_action")
        self.exit_action = QtWidgets.QAction(MainWindow)
        self.exit_action.setObjectName("exit_action")
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.help_action = QtWidgets.QAction(MainWindow)
        self.help_action.setObjectName("help_action")
        self.author_action = QtWidgets.QAction(MainWindow)
        self.author_action.setObjectName("author_action")
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.copy_action = QtWidgets.QAction(MainWindow)
        self.copy_action.setObjectName("copy_action")
        self.cut_action = QtWidgets.QAction(MainWindow)
        self.cut_action.setObjectName("cut_action")
        self.paste_action = QtWidgets.QAction(MainWindow)
        self.paste_action.setObjectName("paste_action")
        self.actionA_4 = QtWidgets.QAction(MainWindow)
        self.actionA_4.setObjectName("actionA_4")
        self.intersection_action = QtWidgets.QAction(MainWindow)
        self.intersection_action.setObjectName("intersection_action")
        self.union_action = QtWidgets.QAction(MainWindow)
        self.union_action.setObjectName("union_action")
        self.flie_menu.addAction(self.open_file_action)
        self.flie_menu.addAction(self.save_file_action)
        self.flie_menu.addAction(self.exit_action)
        self.tools_menu.addAction(self.copy_action)
        self.tools_menu.addAction(self.cut_action)
        self.tools_menu.addAction(self.paste_action)
        self.tools_menu.addAction(self.intersection_action)
        self.tools_menu.addAction(self.union_action)
        self.help_menu.addAction(self.about_action)
        self.help_menu.addAction(self.help_action)
        self.help_menu.addAction(self.author_action)
        self.menuBar.addAction(self.flie_menu.menuAction())
        self.menuBar.addAction(self.tools_menu.menuAction())
        self.menuBar.addAction(self.help_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文本处理"))
        self.flie_menu.setTitle(_translate("MainWindow", "文件"))
        self.tools_menu.setTitle(_translate("MainWindow", "工具"))
        self.help_menu.setTitle(_translate("MainWindow", "帮助"))
        self.open_file_action.setText(_translate("MainWindow", "打开"))
        self.save_file_action.setText(_translate("MainWindow", "保存"))
        self.exit_action.setText(_translate("MainWindow", "退出"))
        self.about_action.setText(_translate("MainWindow", "关于"))
        self.help_action.setText(_translate("MainWindow", "使用说明"))
        self.author_action.setText(_translate("MainWindow", "作者"))
        self.actionA.setText(_translate("MainWindow", "复制"))
        self.copy_action.setText(_translate("MainWindow", "复制"))
        self.cut_action.setText(_translate("MainWindow", "剪切"))
        self.paste_action.setText(_translate("MainWindow", "粘贴"))
        self.actionA_4.setText(_translate("MainWindow", "a"))
        self.intersection_action.setText(_translate("MainWindow", "交集"))
        self.union_action.setText(_translate("MainWindow", "并集"))


    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, '提示',
            "是否退出?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

import textprocess_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

