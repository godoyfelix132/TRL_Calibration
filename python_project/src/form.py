# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(649, 682)
        MainWindow.setBaseSize(QSize(0, 0))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(16)
        font.setUnderline(False)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.widget_8 = QWidget(self.centralwidget)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox = QGroupBox(self.widget_8)
        self.groupBox.setObjectName(u"groupBox")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.groupBox.setPalette(palette1)
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.groupBox.setFont(font1)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_7 = QWidget(self.groupBox)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.horizontalLayout_4.addWidget(self.widget_7)

        self.top = QWidget(self.groupBox)
        self.top.setObjectName(u"top")
        self.verticalLayout_5 = QVBoxLayout(self.top)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_5 = QWidget(self.top)
        self.widget_5.setObjectName(u"widget_5")
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        self.widget_5.setFont(font2)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_dut = QLineEdit(self.widget_5)
        self.lineEdit_dut.setObjectName(u"lineEdit_dut")
        self.lineEdit_dut.setEnabled(False)
        self.lineEdit_dut.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_dut)

        self.pushButton_open_dut = QPushButton(self.widget_5)
        self.pushButton_open_dut.setObjectName(u"pushButton_open_dut")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush6 = QBrush(QColor(239, 239, 239, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush6)
        brush7 = QBrush(QColor(236, 236, 236, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        brush8 = QBrush(QColor(54, 154, 141, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        brush9 = QBrush(QColor(255, 0, 0, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.pushButton_open_dut.setPalette(palette2)

        self.horizontalLayout_5.addWidget(self.pushButton_open_dut)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.top)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setFont(font2)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_thru = QLineEdit(self.widget_3)
        self.lineEdit_thru.setObjectName(u"lineEdit_thru")
        self.lineEdit_thru.setEnabled(False)
        self.lineEdit_thru.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_thru)

        self.pushButton_open_thru = QPushButton(self.widget_3)
        self.pushButton_open_thru.setObjectName(u"pushButton_open_thru")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        self.pushButton_open_thru.setPalette(palette3)

        self.horizontalLayout_3.addWidget(self.pushButton_open_thru)


        self.verticalLayout_5.addWidget(self.widget_3)


        self.horizontalLayout_4.addWidget(self.top)

        self.widget_4 = QWidget(self.groupBox)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font2)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_line = QLineEdit(self.widget)
        self.lineEdit_line.setObjectName(u"lineEdit_line")
        self.lineEdit_line.setEnabled(False)
        self.lineEdit_line.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_line)

        self.pushButton_open_line = QPushButton(self.widget)
        self.pushButton_open_line.setObjectName(u"pushButton_open_line")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        self.pushButton_open_line.setPalette(palette4)

        self.horizontalLayout.addWidget(self.pushButton_open_line)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setFont(font2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_open = QLineEdit(self.widget_2)
        self.lineEdit_open.setObjectName(u"lineEdit_open")
        self.lineEdit_open.setEnabled(False)
        self.lineEdit_open.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_open)

        self.pushButton_open_open = QPushButton(self.widget_2)
        self.pushButton_open_open.setObjectName(u"pushButton_open_open")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        self.pushButton_open_open.setPalette(palette5)

        self.horizontalLayout_2.addWidget(self.pushButton_open_open)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout_4.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.groupBox)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setFont(font2)
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.horizontalLayout_4.addWidget(self.widget_6)


        self.horizontalLayout_7.addWidget(self.groupBox)

        self.label_image = QLabel(self.widget_8)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setMinimumSize(QSize(90, 90))

        self.horizontalLayout_7.addWidget(self.label_image)


        self.verticalLayout.addWidget(self.widget_8)

        self.groupBox_info = QGroupBox(self.centralwidget)
        self.groupBox_info.setObjectName(u"groupBox_info")
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setBold(True)
        font3.setWeight(75)
        self.groupBox_info.setFont(font3)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_9 = QWidget(self.groupBox_info)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(38, 16777215))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setBold(False)
        font4.setWeight(50)
        self.label_7.setFont(font4)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.comboBox_file = QComboBox(self.widget_9)
        self.comboBox_file.setObjectName(u"comboBox_file")
        self.comboBox_file.setMinimumSize(QSize(150, 0))
        self.comboBox_file.setMaximumSize(QSize(200, 16777215))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setBold(False)
        font5.setWeight(50)
        self.comboBox_file.setFont(font5)

        self.horizontalLayout_8.addWidget(self.comboBox_file)

        self.horizontalSpacer = QSpacerItem(400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_file = QLabel(self.widget_9)
        self.label_file.setObjectName(u"label_file")

        self.horizontalLayout_8.addWidget(self.label_file)

        self.horizontalSpacer_2 = QSpacerItem(400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.widget_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.pushButton_correct_dut = QPushButton(self.widget_9)
        self.pushButton_correct_dut.setObjectName(u"pushButton_correct_dut")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        self.pushButton_correct_dut.setPalette(palette6)
        self.pushButton_correct_dut.setFont(font5)

        self.horizontalLayout_8.addWidget(self.pushButton_correct_dut)


        self.verticalLayout_2.addWidget(self.widget_9)

        self.tableView_temp = QTableView(self.groupBox_info)
        self.tableView_temp.setObjectName(u"tableView_temp")
        self.tableView_temp.setFont(font5)

        self.verticalLayout_2.addWidget(self.tableView_temp)


        self.verticalLayout.addWidget(self.groupBox_info)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RF Calibration", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CALIBRATION", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DUT", None))
        self.pushButton_open_dut.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Thru", None))
        self.pushButton_open_thru.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.pushButton_open_line.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushButton_open_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_image.setText("")
        self.groupBox_info.setTitle(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_file.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Create correct DUT", None))
        self.pushButton_correct_dut.setText(QCoreApplication.translate("MainWindow", u"Create", None))
    # retranslateUi

